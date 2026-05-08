# SDD Agent SDK v1 — Validation Guide

Use this guide to confirm that SDK v1 is functional.

## 1. Package Validation

Check that the SDK contains:

```text
README.md
init-sdd.py
schemas/
examples/
core/
adapters/
extensions/
docs/
```

## Workspace Context Validation

Confirm before running `init-sdd.py`:

- `workspace-context.json` exists before running `init-sdd.py`.
- `workspace-context.json` was reviewed by a human.
- Unknown values are represented as `"unknown"` instead of invented values.
- Assumptions are documented.
- The agent did not run `init-sdd.py` before context review.
- The agent did not modify files while extracting context unless explicitly requested.
- The generated context matches `schemas/workspace-context.schema.json`.

## 2. Install Validation

Run:

```bash
python init-sdd.py --context examples/workspace-context.example.json --output ./tmp-sdd-test --agents codex,claude-code,cursor,kiro,opencode
```

Expected generated files:

```text
AGENTS.md
SDD_INDEX.md
.sdd/CONTEXT_LOADING.md
.sdd/WORKSPACE_STATE.md
.sdd/steering/
.sdd/specs/
.sdd/decisions/
.sdd/operations/
.sdd/templates/
CLAUDE.md
.cursor/rules/sdd-workflow.mdc
.kiro/steering/sdd-workflow.md
opencode.json
```

## 3. Script Validation

Run:

```bash
python init-sdd.py --validate ./tmp-sdd-test
```

Expected:

```text
SDD validation passed.
```

## 4. Context Loading Validation

Confirm `.sdd/CONTEXT_LOADING.md` tells agents:

- what to read by action;
- what not to read by default;
- when to escalate context.

## 5. Memory Validation

Confirm:

```text
.sdd/WORKSPACE_STATE.md
.sdd/operations/memory-policy.md
.sdd/decisions/
.sdd/specs/<spec>/notes.md
```

are present and explain their roles.

## 6. Agent Adapter Validation

Confirm adapters point back to `.sdd/` and do not duplicate the full methodology.

## 7. Human Dry Run

Ask an agent:

```text
Read the SDD instructions and prepare the first spec.
Do not modify files.
Do not commit.
Do not push.
Report what you read and what you would do next.
```

Expected:

- agent reads entrypoint files;
- does not modify files;
- identifies next safe action;
- does not implement.

## 8. Failure Conditions

SDK v1 should be considered not ready if:

- install overwrites existing files without warning;
- validation misses required files;
- generated docs are tied to a specific agent or stack;
- adapters duplicate the methodology instead of pointing to `.sdd/`;
- the agent reads the entire `.sdd/` tree by default;
- memory is stored only in chat;
- external writes are not clearly approval-gated.
