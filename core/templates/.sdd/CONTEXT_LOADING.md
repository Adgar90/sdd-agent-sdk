# Context Loading Policy

## Purpose

Avoid unnecessary token usage by loading only the context required for the current action.

## Default Rule

Do not read the entire `.sdd/` tree by default.

Read progressively:

1. Entry point.
2. Action workflow.
3. Relevant steering.
4. Active spec.
5. Additional references only if needed.

## Always Read

- `AGENTS.md`
- `SDD_INDEX.md`

## Read by Action

| Action | Required Files | Optional Files |
|---|---|---|
| prepare-spec | `action-rules.md`, `pre-implementation-checklist.md`, `git-workflow.md`, active spec | `WORKSPACE_STATE.md`, related decisions |
| create-spec | `new-spec-workflow.md`, templates, relevant steering | related specs |
| implement-task | `action-rules.md`, `git-workflow.md`, active spec, relevant steering | code/docs referenced by spec |
| review-diff | `pr-checklist.md`, active spec, diff | decisions if architecture changed |
| sync-tracker | `issue-workflow.md`, active spec, `notes.md`, `tooling-and-mcp-policy.md` | external tracker context |
| resume-work | `WORKSPACE_STATE.md`, `SDD_INDEX.md`, active spec | related decisions |

## Do Not Read by Default

All specs, all docs, all decisions, all audits, all adapters or all source code.
