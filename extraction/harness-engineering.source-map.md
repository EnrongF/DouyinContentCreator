# Harness Engineering Source Map

## Core Thesis
Harness engineering is agent harness engineering for software delivery. The model supplies intelligence, but the harness supplies control: memory, live context, governed tools, permissions, verification, evidence, and execution boundaries.

## Central Framing
- Inner loop: software development, where coding agents help one developer write, edit, test, and review code.
- Outer loop: software delivery, where code is built, tested, secured, deployed, verified, operated, rolled back, and audited.
- Harness argues these two loops need different harnesses because delivery crosses teams, production systems, secrets, policies, and compliance evidence.

## What A Delivery Agent Needs
| Element | Harness Interpretation |
|---|---|
| Memory | Software Delivery Knowledge Graph: services, teams, pipelines, deployments, incidents, policies, scorecards, artifacts. |
| Context | Live state: scans, incidents, change freezes, recent deployments, chaos experiments, dependencies, on-call state. |
| Tools | Governed execution actions: deploy, run migrations, apply feature flags, trigger scans, run chaos experiments, open incidents. |
| Verification | Scorecards, policy gates, approvals, evidence, rollback, signed proof that policy conditions were met. |

## Key Architecture Claims
- A delivery agent cannot be just a coding assistant with API access.
- The delivery harness decides whether a request is allowed, how it executes, and what evidence is retained.
- Execution should happen inside the enterprise perimeter through a Delegate, not by moving production credentials into a model provider.
- Secrets are decrypted inside the Delegate, not in the model context, provider memory, or audit logs.
- Pipelines are not agents; pipelines are the harness where agent actions are evaluated, constrained, and executed under policy.

## Harness MCP Server
- Official repo describes Harness MCP Server 2.0 as giving AI agents access to the Harness platform.
- Design choice: 11 consolidated tools instead of one tool per endpoint.
- Coverage: 168 resource types in the GitHub README, spanning 31 toolsets.
- Architecture: registry-based dispatch routes operations such as list/get/create/update/delete/execute to many Harness resources.
- Transport: stdio for local clients like Claude Desktop, Cursor, Windsurf; HTTP for remote/shared deployments.
- Supports dynamic org/project discovery so agents can navigate account hierarchy.
- Includes prompt templates for workflows such as build/deploy, pipeline debugging, DORA review, vulnerability triage, cloud cost optimization, access audit, feature flag rollout, PR review, and approval handling.

## Harness Skills
- Skills are structured instruction files layered on top of MCP tools.
- They let coding assistants operate Harness workflows through natural language.
- The official repo describes skills for creating, operating, debugging, and governing Harness CI/CD workflows.
- Design pattern: do not force the user to know Harness internals; map user intent to correct Harness tool calls.

## Software Delivery Knowledge Graph
- Knowledge graph is the memory layer for AI-first software delivery.
- It models relationships between services, pipelines, environments, policies, scorecards, incidents, dependencies, and operational signals.
- It addresses the "context gap": a coding assistant knows the repo, but not whether a checkout service is safe to deploy tonight.
- RAG alone can retrieve text, but graph context can represent relationships, dependencies, ownership, blast radius, and state.

## Failure Modes Without A Harness
- Prompt injection through PR descriptions, poisoned dependencies, or malicious issue comments can redirect agent behavior.
- Broad agent access becomes a privileged insider-threat path.
- Agents can skip policy gates, approvals, and audit trails if they use a parallel path.
- Partial context produces locally plausible but globally unsafe decisions.
- AI-specific failures include hallucinated actions, loops, wrong Kubernetes manifests, repeated rollback/redeploy cycles, or confident fixes that break production.
- Autonomous errors compound in parallel; speed becomes a damage multiplier.

## Quantitative / Artifact Details
- Harness MCP Server README: 11 tools, 168 resource types, 31 toolsets, 30 prompt templates.
- Earlier product update referenced MCP v2 with 10 unified tools, 119+ resource types, and 26 prompt templates; the GitHub repo appears newer and broader.
- Harness article states pipelines execute hundreds of millions of runs a year across enterprise production systems.
- Harness frames release control as one delivery control plane, one policy set, one audit trail, and one evidence source.

## Reusable Ideas
- Agent harness = model + memory + context + tools + permissions + verification + audit.
- Coding-agent harness and delivery-agent harness are separate categories.
- Model provider can be the brain, but the enterprise delivery harness owns credentials, live state, execution, and accountability.
- Skills are a translation layer between human intent and platform-specific tool calls.
- Consolidated MCP tools reduce tool-selection burden compared with one tool per endpoint.
