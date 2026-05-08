# SDD Agent SDK v1 — Concepts

## Spec-Driven Development

Spec-Driven Development is a way of working where implementation is guided by a structured spec.

A spec answers:

- What is the context?
- What problem are we solving?
- What are the requirements?
- What is the proposed design?
- What tasks are allowed?
- What is out of scope?
- How will we validate it?
- What happened during implementation?

## Why Issue Trackers Are Not Enough

Issue trackers are useful for:

- prioritization;
- ownership;
- workflow status;
- team coordination.

But they usually do not contain enough information to safely guide an AI agent.

A spec adds:

- scope;
- dependencies;
- design;
- acceptance criteria;
- risks;
- task boundaries;
- validation rules.

## Source Context vs Spec

Source context can be:

- issue tracker item;
- functional brief;
- documentation page;
- technical audit;
- chat transcript;
- repository analysis.

The spec is the curated contract derived from that context.

## Steering

Steering contains current stable guidance for the workspace.

Examples:

- product context;
- architecture direction;
- technology choices;
- principles;
- agent workflow.

Steering should stay small and curated. It should not become a wiki.

## Decisions

Decisions explain why stable context changed.

Examples:

- selecting a stack;
- changing architecture;
- switching from one agent to another;
- adopting a new issue tracker;
- changing Git policy.

Steering says what is true now. Decisions explain why it changed.

## Specs

Specs define work.

Each spec contains:

```text
context.md       why this exists and what it touches
requirements.md  what must be true
design.md        how it should be approached
tasks.md         executable steps
notes.md         living memory for this spec
```

## Living Memory

The SDK uses several memory levels:

| Level | File/Folder | Purpose |
|---|---|---|
| Macro state | `.sdd/WORKSPACE_STATE.md` | Short current state across workstreams. |
| Spec memory | `notes.md` | Detailed memory for one spec. |
| Decisions | `.sdd/decisions/` | Historical rationale. |
| Index | `SDD_INDEX.md` | Spec catalog and statuses. |

## Workstreams

A workspace can have several active streams of work.

Example:

```text
refactor-roadmap
product-changes
bugfixes
documentation
discovery
operations
```

The agent must not assume every new task belongs to the current main roadmap.

## Context Loading

Agents should not read everything.

They should load context progressively:

```text
AGENTS.md
SDD_INDEX.md
CONTEXT_LOADING.md
required operation files
relevant steering
active spec
additional files only if needed
```

This keeps token usage under control.

## Agent Adapters

Different agents use different instruction files.

| Agent | Adapter |
|---|---|
| Codex | `AGENTS.md` |
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/sdd-workflow.mdc` |
| Kiro | `.kiro/steering/sdd-workflow.md` |
| OpenCode | `opencode.json` |

Adapters point to `.sdd/`. They do not replace `.sdd/`.

## Tools, MCPs and Plugins

External tools may help read or sync context. They must not replace specs.

Writes require explicit approval.

## Skills

Skills are optional reusable assistant capabilities.

A future SDD Operator Skill could help initialize, validate and operate the SDK.

The repository `.sdd/` remains the project source of truth.
