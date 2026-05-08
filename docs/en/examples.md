# SDD Agent SDK v1 — Examples

## Example 1: Existing Codebase

You have an API repository and want to introduce SDD.

Context:

```json
{
  "workspace": {
    "type": "existing-codebase",
    "lifecycle_stage": "implementation"
  }
}
```

First prompt:

```text
Read the SDD instructions and prepare the first discovery spec.
Do not modify files.
```

---

## Example 2: Functional Brief

You have a functional document but no code yet.

Context:

```json
{
  "workspace": {
    "type": "functional-document",
    "lifecycle_stage": "discovery"
  }
}
```

First prompt:

```text
Create an SDD discovery spec from this functional brief.
Do not propose implementation yet.
```

Recommended initial specs:

```text
discovery-functional-scope
define-domain-model
select-technical-stack
define-api-contract
```

---

## Example 3: Long Refactor Roadmap Plus New Feature

You have a long refactor roadmap, but a new feature arrives.

Wrong:

```text
Add this feature inside the current refactor spec.
```

Correct:

```text
Classify this new request.
If independent, create a separate feature-change spec.
If it blocks or depends on the refactor roadmap, document the relationship.
```

---

## Example 4: Bugfix During Refactor

Prompt:

```text
Create a bugfix spec for this issue and determine whether it blocks the current refactor workstream.
```

Expected output:

- separate bugfix spec;
- relationship with roadmap;
- small validation plan;
- no unrelated refactor.

---

## Example 5: Switching Agents

You start with Codex and later move to Claude Code.

Steps:

1. Keep `.sdd/`.
2. Add `CLAUDE.md`.
3. Point Claude back to `.sdd/`.
4. Run a dry-run.
5. Do not rewrite specs.

Prompt:

```text
Read the SDD workspace and prepare the active spec.
Do not modify files.
Report which files you read.
```

---

## Example 6: External Sync

Prompt:

```text
Prepare Jira sync for SPEC-123.
Do not write yet.
```

Expected behavior:

- read spec and notes;
- prepare comment/status proposal;
- ask for approval before writing.
