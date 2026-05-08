# SDD Agent SDK v1 — Components

## SDK Package Structure

The SDK package contains:

```text
sdd-agent-sdk/
  README.md
  init-sdd.py
  schemas/
  examples/
  core/
  adapters/
  extensions/
  docs/
```

This is the SDK distribution structure. It is not exactly the same as the structure installed into a project.

---

## Installed Workspace Structure

A workspace initialized by the SDK contains:

```text
AGENTS.md
SDD_INDEX.md
.sdd/
  CONTEXT_LOADING.md
  WORKSPACE_STATE.md
  steering/
  specs/
  decisions/
  operations/
  templates/
```

Optional adapters may add:

```text
CLAUDE.md
.cursor/rules/sdd-workflow.mdc
.kiro/steering/sdd-workflow.md
opencode.json
.sdd/adapters/codex.md
```

---

## `AGENTS.md`

Main repository instruction file.

Purpose:

- define safe defaults;
- point agents to `.sdd/`;
- define the mandatory SDD flow;
- define stop conditions;
- state that implementation must come from specs.

It should be a router, not a giant manual.

---

## `SDD_INDEX.md`

The map of the SDD workspace.

Purpose:

- list specs;
- track macro statuses;
- show workstreams;
- record dependencies;
- link policies and compatibility docs.

It should not contain detailed implementation notes.

---

## `.sdd/CONTEXT_LOADING.md`

Policy for token-efficient agent behavior.

Purpose:

- prevent agents from reading the full tree;
- define what to read by action;
- define what not to read by default;
- describe escalation rules.

---

## `.sdd/WORKSPACE_STATE.md`

Short living macro-state.

Purpose:

- summarize active workstreams;
- show current phase;
- show recommended next actions;
- list open macro risks.

It must not become a detailed log.

---

## `.sdd/steering/`

Current stable context.

Default files:

```text
README.md
product.md
architecture.md
tech.md
principles.md
agent-workflow.md
```

Steering should remain small and curated.

---

## `.sdd/specs/`

Specs are contracts for work.

Each spec should contain:

```text
context.md
requirements.md
design.md
tasks.md
notes.md
```

Agents should usually read only the active spec.

---

## `.sdd/decisions/`

Historical rationale.

Default files:

```text
README.md
decision-template.md
```

Use decisions when changing stable context such as architecture, stack, workflow, primary agent, issue tracker or Git policy.

---

## `.sdd/operations/`

Operational workflows and policies.

Examples:

```text
action-rules.md
git-workflow.md
memory-policy.md
tooling-and-mcp-policy.md
new-spec-workflow.md
split-issue-workflow.md
daily-workflow.md
pre-implementation-checklist.md
pr-checklist.md
```

Agents should not read all operations files by default.

---

## `.sdd/templates/`

Reusable templates.

The default spec template contains:

```text
context.md
requirements.md
design.md
tasks.md
notes.md
```

Templates should not be edited for one-off work.

---

## `schemas/`

Contains the schema for workspace context files.

Current main schema:

```text
schemas/workspace-context.schema.json
```

---

## `examples/`

Contains sample context files for different workspace types.

Examples:

```text
workspace-context.example.json
workspace-context.functional-document.json
```

---

## `adapters/`

Agent-specific or tool-specific bridges.

Adapters must point to the `.sdd/` core and avoid duplicating the methodology.

---

## `extensions/`

Reserved for optional future capabilities:

- Skills;
- MCP workflows;
- SDD CLI;
- stack detectors;
- advanced validators;
- external tool adapters.
