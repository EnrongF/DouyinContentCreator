#!/usr/bin/env python3
"""Build the Open Douyin authorization URL and extract the returned code.

This is a browser authorization flow. The script cannot fetch the code directly
from Douyin; it opens the authorization page, then parses the callback URL or
raw code you paste after approving the QR/native authorization page.
"""

from __future__ import annotations

import argparse
import os
import secrets
import sys
import urllib.parse
import webbrowser
from pathlib import Path


AUTH_URL = "https://open.douyin.com/platform/oauth/connect/"
REPO_ROOT = Path(__file__).resolve().parents[1]


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
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        values[key] = value
    return values


def env_value(values: dict[str, str], *keys: str, default: str | None = None) -> str | None:
    for key in keys:
        value = os.environ.get(key) or values.get(key)
        if value:
            return value
    return default


def build_authorization_url(
    *,
    client_key: str,
    redirect_uri: str,
    scope: str,
    state: str,
    optional_scope: str | None,
) -> str:
    params = {
        "client_key": client_key,
        "response_type": "code",
        "scope": scope,
        "redirect_uri": redirect_uri,
        "state": state,
    }
    if optional_scope:
        params["optionalScope"] = optional_scope
    return f"{AUTH_URL}?{urllib.parse.urlencode(params)}"


def extract_code(callback_or_code: str) -> str | None:
    value = callback_or_code.strip()
    if not value:
        return None
    if value.startswith("code="):
        return value.split("=", 1)[1]
    if "://" not in value and "code=" not in value:
        return value

    parsed = urllib.parse.urlparse(value)
    candidates = []
    candidates.extend(urllib.parse.parse_qs(parsed.query).get("code", []))
    candidates.extend(urllib.parse.parse_qs(parsed.fragment).get("code", []))
    return candidates[0] if candidates else None


def write_env_value(path: Path, key: str, value: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    replacement = f"{key}={value}"
    for index, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[index] = replacement
            break
    else:
        lines.append(replacement)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Open the Douyin OAuth page and parse the returned authorization code."
    )
    parser.add_argument(
        "--env-file",
        default=None,
        help="Env file to read and optionally update. Defaults to .env in the current directory, then repo root.",
    )
    parser.add_argument("--no-open", action="store_true", help="Print the URL without opening a browser.")
    parser.add_argument("--save", action="store_true", help="Save the parsed code as DOUYIN_CODE in the env file.")
    parser.add_argument("--code-or-url", help="Callback URL or raw code to parse without prompting.")
    args = parser.parse_args()

    if args.env_file:
        env_path = Path(args.env_file)
    else:
        cwd_env = Path.cwd() / ".env"
        repo_env = REPO_ROOT / ".env"
        env_path = cwd_env if cwd_env.exists() else repo_env
    env = load_env(env_path)

    client_key = env_value(env, "DOUYIN_CLIENT_KEY", "CLIENT_KEY", "client_key")
    redirect_uri = env_value(env, "DOUYIN_REDIRECT_URI", "REDIRECT_URI", "redirect_uri")
    scope = env_value(env, "DOUYIN_SCOPE", "SCOPE", "scope", default="user_info")
    optional_scope = env_value(env, "DOUYIN_OPTIONAL_SCOPE", "OPTIONAL_SCOPE", "optionalScope", "optional_scope")
    state = env_value(env, "DOUYIN_STATE", "STATE", default=f"codex-{secrets.token_urlsafe(12)}")

    missing = [
        name
        for name, value in (
            ("DOUYIN_CLIENT_KEY", client_key),
            ("DOUYIN_REDIRECT_URI", redirect_uri),
            ("DOUYIN_SCOPE", scope),
        )
        if not value
    ]
    if missing:
        print(f"Missing required env value(s): {', '.join(missing)}", file=sys.stderr)
        print(f"Checked env file: {env_path}", file=sys.stderr)
        return 2

    assert client_key is not None
    assert redirect_uri is not None
    assert scope is not None
    assert state is not None

    url = build_authorization_url(
        client_key=client_key,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        optional_scope=optional_scope,
    )

    print("Authorization URL:")
    print(url)
    print()
    print("State:")
    print(state)
    print()

    if not args.no_open:
        webbrowser.open(url)

    callback_or_code = args.code_or_url
    if callback_or_code is None:
        print("After authorization, paste the final redirect URL or raw code.")
        callback_or_code = input("> ")

    code = extract_code(callback_or_code)
    if not code:
        print("Could not find a code in that value.", file=sys.stderr)
        return 1

    print()
    print("DOUYIN_CODE:")
    print(code)

    if args.save:
        write_env_value(env_path, "DOUYIN_CODE", code)
        print()
        print(f"Saved DOUYIN_CODE to {env_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
