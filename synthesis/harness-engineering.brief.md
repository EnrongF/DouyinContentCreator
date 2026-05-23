# Harness Engineering Brief

## Short Version
Harness engineering is the engineering of the control system around software delivery agents. The important claim is not that AI can write code. It is that autonomous agents need a governed delivery harness before they can safely act on production systems.

## Core Mental Model
Harness separates two loops:
- Inner loop: coding agents help developers write and edit code.
- Outer loop: delivery agents build, test, secure, deploy, verify, operate, and roll back software.

The outer loop has higher blast radius. It touches production, secrets, policy, compliance, and audit evidence. That is why Harness argues a delivery agent cannot simply be a coding assistant with API access.

## The Harness Pattern
The model is the brain. The harness is the control plane.

The harness provides:
- Memory: software delivery knowledge graph.
- Context: live delivery state.
- Tools: governed execution through Harness platform modules and Delegates.
- Verification: scorecards, policy gates, approvals, evidence, rollback.
- Accountability: audit trails and evidence retained by the enterprise.

## Why MCP And Skills Matter
Harness MCP Server exposes a broad delivery platform to AI agents through a smaller set of consolidated tools and resource types. Harness Skills add task-specific instructions so assistants can create, operate, debug, and govern CI/CD workflows without users needing to know Harness internals.

## Why Knowledge Graphs Matter
RAG can retrieve text, but delivery decisions depend on relationships: which services depend on checkout, who owns them, which policies apply, whether there is a change freeze, which incidents are open, and what recent scans found. The Software Delivery Knowledge Graph is the memory layer that lets an agent reason over those relationships.

## Main Takeaway
Harness engineering is about making agentic software delivery fast without making it ungoverned. The platform has to constrain what agents can do, execute actions inside the enterprise boundary, keep secrets out of model context, and produce evidence when actions are allowed.
