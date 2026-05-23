#!/usr/bin/env python3
"""Small Open Douyin API helper for token and video-share-result calls."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ACCESS_TOKEN_URL = "https://open.douyin.com/oauth/access_token/"
CLIENT_TOKEN_URL = "https://open.douyin.com/oauth/client_token/"
SHARE_ID_URL = "https://open.douyin.com/share-id/"
USERINFO_URL = "https://open.douyin.com/oauth/userinfo/"
VIDEO_LIST_URL = "https://open.douyin.com/video/list/"
USER_DATA_ENDPOINTS = {
    "item": "https://open.douyin.com/data/external/user/item/",
    "fans": "https://open.douyin.com/data/external/user/fans/",
    "like": "https://open.douyin.com/data/external/user/like/",
    "comment": "https://open.douyin.com/data/external/user/comment/",
    "share": "https://open.douyin.com/data/external/user/share/",
    "profile": "https://open.douyin.com/data/external/user/profile/",
}


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line.removeprefix("export ").strip()
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def write_env_values(path: Path, updates: dict[str, str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    seen: set[str] = set()
    for index, line in enumerate(lines):
        stripped = line.strip()
        candidate = stripped.removeprefix("export ").strip()
        if "=" not in candidate:
            continue
        key = candidate.split("=", 1)[0].strip()
        if key in updates:
            lines[index] = f"{key}={updates[key]}"
            seen.add(key)
    for key, value in updates.items():
        if key not in seen:
            lines.append(f"{key}={value}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def env_value(env: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = os.environ.get(key) or env.get(key)
        if value:
            return value
    return None


def request_json(url: str, *, method: str = "POST", headers: dict[str, str], data: bytes | None) -> dict[str, Any]:
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
    return json.loads(body)


def get_access_token(client_key: str, client_secret: str, code: str) -> dict[str, Any]:
    data = urllib.parse.urlencode(
        {
            "client_key": client_key,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
        }
    ).encode("utf-8")
    return request_json(
        ACCESS_TOKEN_URL,
        headers={"content-type": "application/x-www-form-urlencoded"},
        data=data,
    )


def get_client_token(client_key: str, client_secret: str) -> dict[str, Any]:
    data = json.dumps(
        {
            "grant_type": "client_credential",
            "client_key": client_key,
            "client_secret": client_secret,
        }
    ).encode("utf-8")
    return request_json(
        CLIENT_TOKEN_URL,
        headers={"content-type": "application/json"},
        data=data,
    )


def get_user_info(access_token: str, open_id: str) -> dict[str, Any]:
    data = urllib.parse.urlencode(
        {
            "access_token": access_token,
            "open_id": open_id,
        }
    ).encode("utf-8")
    return request_json(
        USERINFO_URL,
        headers={"content-type": "application/x-www-form-urlencoded"},
        data=data,
    )


def list_videos(access_token: str, open_id: str, *, cursor: int, count: int) -> dict[str, Any]:
    query = urllib.parse.urlencode(
        {
            "open_id": open_id,
            "cursor": cursor,
            "count": count,
        }
    )
    return request_json(
        f"{VIDEO_LIST_URL}?{query}",
        method="GET",
        headers={"access-token": access_token, "content-type": "application/json"},
        data=None,
    )


def get_account_metric(access_token: str, open_id: str, *, metric: str, date_type: int) -> dict[str, Any]:
    query = urllib.parse.urlencode({"open_id": open_id, "date_type": date_type})
    return request_json(
        f"{USER_DATA_ENDPOINTS[metric]}?{query}",
        method="GET",
        headers={"access-token": access_token, "content-type": "application/json"},
        data=None,
    )


def create_share_id(
    client_token: str,
    *,
    need_callback: bool,
    default_hashtag: str | None,
    source_style_id: str | None,
    link_param: str | None,
) -> dict[str, Any]:
    query = {
        "need_callback": str(need_callback).lower(),
        "default_hashtag": default_hashtag or "",
        "source_style_id": source_style_id or "",
        "link_param": link_param or "",
    }
    url = f"{SHARE_ID_URL}?{urllib.parse.urlencode(query)}"
    return request_json(
        url,
        method="GET",
        headers={"access-token": client_token, "content-type": "application/json"},
        data=None,
    )


def print_response(label: str, response: dict[str, Any]) -> None:
    response = redact_sensitive(response)
    print(label)
    print(json.dumps(response, ensure_ascii=False, indent=2))


def redact_sensitive(value: Any) -> Any:
    if isinstance(value, dict):
        redacted: dict[str, Any] = {}
        for key, item in value.items():
            if key in {"access_token", "refresh_token"} and isinstance(item, str):
                redacted[key] = f"{item[:8]}...{item[-6:]}" if len(item) > 18 else "***"
            else:
                redacted[key] = redact_sensitive(item)
        return redacted
    if isinstance(value, list):
        return [redact_sensitive(item) for item in value]
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Call selected Open Douyin APIs.")
    parser.add_argument("--env-file", default=".env")
    parser.add_argument("--save", action="store_true", help="Save returned tokens/share_id to the env file.")
    parser.add_argument("--get-access-token", action="store_true")
    parser.add_argument("--get-client-token", action="store_true")
    parser.add_argument("--get-user-info", action="store_true")
    parser.add_argument("--list-videos", action="store_true")
    parser.add_argument("--account-performance", action="store_true")
    parser.add_argument("--date-type", type=int, default=7, choices=(7, 15))
    parser.add_argument("--cursor", type=int, default=0)
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--create-share-id", action="store_true")
    parser.add_argument("--default-hashtag")
    parser.add_argument("--source-style-id")
    parser.add_argument("--link-param")
    parser.add_argument("--no-callback", action="store_true")
    args = parser.parse_args()

    env_path = Path(args.env_file)
    env = load_env(env_path)
    client_key = env_value(env, "DOUYIN_CLIENT_KEY", "CLIENT_KEY", "client_key")
    client_secret = env_value(
        env,
        "DOUYIN_CLIENT_SECRET",
        "DOUYIN_CLIENT_SECRECT",
        "CLIENT_SECRET",
        "CLIENT_SECRECT",
        "client_secret",
    )
    code = env_value(env, "DOUYIN_CODE")
    access_token = env_value(env, "DOUYIN_ACCESS_TOKEN")
    open_id = env_value(env, "DOUYIN_OPEN_ID")
    client_token = env_value(env, "DOUYIN_CLIENT_TOKEN")

    if not client_key or not client_secret:
        print("Missing DOUYIN_CLIENT_KEY or DOUYIN_CLIENT_SECRET/DOUYIN_CLIENT_SECRECT.", file=sys.stderr)
        return 2

    updates: dict[str, str] = {}

    if args.get_access_token:
        if not code:
            print("Missing DOUYIN_CODE.", file=sys.stderr)
            return 2
        response = get_access_token(client_key, client_secret, code)
        print_response("access_token response:", response)
        data = response.get("data") or {}
        if data.get("error_code") == 0:
            for source, target in (
                ("access_token", "DOUYIN_ACCESS_TOKEN"),
                ("refresh_token", "DOUYIN_REFRESH_TOKEN"),
                ("open_id", "DOUYIN_OPEN_ID"),
            ):
                if data.get(source):
                    updates[target] = str(data[source])
            access_token = updates.get("DOUYIN_ACCESS_TOKEN", access_token)
            open_id = updates.get("DOUYIN_OPEN_ID", open_id)

    if args.get_client_token:
        response = get_client_token(client_key, client_secret)
        print_response("client_token response:", response)
        data = response.get("data") or {}
        if data.get("error_code") == 0 and data.get("access_token"):
            client_token = str(data["access_token"])
            updates["DOUYIN_CLIENT_TOKEN"] = client_token

    if args.get_user_info:
        if not access_token or not open_id:
            print("Missing DOUYIN_ACCESS_TOKEN or DOUYIN_OPEN_ID.", file=sys.stderr)
            return 2
        response = get_user_info(access_token, open_id)
        print_response("user_info response:", response)

    if args.list_videos:
        if not access_token or not open_id:
            print("Missing DOUYIN_ACCESS_TOKEN or DOUYIN_OPEN_ID.", file=sys.stderr)
            return 2
        response = list_videos(access_token, open_id, cursor=args.cursor, count=args.count)
        print_response("video_list response:", response)

    if args.account_performance:
        if not access_token or not open_id:
            print("Missing DOUYIN_ACCESS_TOKEN or DOUYIN_OPEN_ID.", file=sys.stderr)
            return 2
        for metric in USER_DATA_ENDPOINTS:
            response = get_account_metric(
                access_token,
                open_id,
                metric=metric,
                date_type=args.date_type,
            )
            print_response(f"account_{metric} response:", response)

    if args.create_share_id:
        if not client_token:
            print("Missing DOUYIN_CLIENT_TOKEN. Run --get-client-token first or combine both flags.", file=sys.stderr)
            return 2
        response = create_share_id(
            client_token,
            need_callback=not args.no_callback,
            default_hashtag=args.default_hashtag,
            source_style_id=args.source_style_id,
            link_param=args.link_param,
        )
        print_response("share_id response:", response)
        data = response.get("data") or {}
        if data.get("error_code") == 0 and data.get("share_id"):
            updates["DOUYIN_SHARE_ID"] = str(data["share_id"])

    if args.save and updates:
        write_env_values(env_path, updates)
        print(f"Saved: {', '.join(sorted(updates))}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
