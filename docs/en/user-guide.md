# SDD Agent SDK v1 — User Guide

## 1. What This SDK Is

The **SDD Agent SDK** helps you initialize a structured workspace for working with AI coding agents using **Spec-Driven Development**.

It provides:

- persistent agent instructions;
- a neutral `.sdd/` methodology core;
- templates for specs;
- operational rules for Git, tools and MCPs;
- a memory model for long-running work;
- adapters for different AI agents;
- documentation for human users.

The SDK is designed to work across different tools, stacks and delivery workflows.

It is not limited to Codex, Claude Code, Kiro, Cursor, OpenCode, Jira, Python, .NET, Streamlit or any specific stack.

---

## 2. What Problem It Solves

Without SDD, an agent often receives instructions like:

```text
Implement this Jira ticket.
```

That is risky because issue tracker text rarely contains enough detail to safely guide implementation.

The SDK promotes this pattern instead:

```text
Create or find a spec.
Review requirements and design.
Implement one task.
Update notes.
Validate.
Stop for review.
```

This reduces:

- scope creep;
- accidental refactors;
- undocumented assumptions;
- lost context;
- unreviewable diffs;
- unexpected commits, pushes or external writes.

---

## 3. Who This Is For

Use this SDK if you want to:

- introduce AI-assisted development into a real project;
- manage long-running refactors safely;
- turn functional briefs into technical specs;
- avoid agents implementing directly from issue tracker text;
- support several agents such as Codex, Claude Code, Cursor, Kiro or OpenCode;
- keep project memory versioned in the repository;
- make AI work reviewable and repeatable.

---

## 4. Basic Workflow

The recommended SDD workflow is:

```text
Source context
→ Spec
→ Task
→ Implementation or analysis
→ Validation
→ Human review
→ External sync
```

Where:

- **Source context** can be a ticket, issue, functional document, audit, chat, documentation page or repository.
- **Spec** is the contract for the work.
- **Task** is the smallest executable unit.
- **Validation** proves or documents the result.
- **Human review** prevents unsafe automation.
- **External sync** updates tools only when approved.

---

## Prepare workspace context

Before running `init-sdd.py`, create a `workspace-context.json`.

In SDK v1, `init-sdd.py` is deterministic. It does not analyze the project by itself. It receives `workspace-context.json`, renders the SDD structure and validates it. Context extraction and interpretation must happen before running the script, either by a person or by an agent.

It can be prepared in two ways:

### Option A — Manual

Copy the example:

```bash
cp examples/workspace-context.example.json workspace-context.json
```

Then edit it manually and review it before running the script.

### Option B — Agent-assisted

Ask an agent such as Codex, Claude Code, Cursor, Kiro or another tool to analyze the source context and generate `workspace-context.json`.

The source context can be:

- existing repository;
- functional brief;
- epic or issue;
- technical audit;
- documentation;
- conversation;
- mixed sources.

Prompt example:

```text
Analyze this repository/context and generate a workspace-context.json compatible with SDD Agent SDK.

Do not modify files.
Do not run init-sdd.py yet.
Do not commit.
Do not push.

If a value is not confirmed, use "unknown" or document the assumption.
Distinguish observed facts from inferences.

Return the final JSON and a short list of assumptions.
```

Review the generated file before running the script.

---

## Initialize SDD structure

Command:

```bash
python init-sdd.py --context workspace-context.json --output . --agents codex,claude-code,cursor
```

---

## Validate

Command:

```bash
python init-sdd.py --validate .
```

---

## Commit generated structure

Commit the generated SDD structure separately from implementation work. This keeps workspace initialization reviewable and prevents setup changes from being mixed with feature, fix or refactor changes.

---

## 6. What to Ask the Agent First

After installing the SDK, start with a dry run:

```text
Read the SDD instructions and prepare the first spec.
Do not modify files.
Do not commit.
Do not push.
Report what you read and what you would do next.
```

This verifies that the agent understands:

- the SDD structure;
- context loading;
- safe defaults;
- spec-based work;
- Git restrictions.

---

## 7. Creating a Spec

When a new piece of work arrives, ask:

```text
Create an SDD spec for <issue, brief or request>.
```

The agent should:

1. read the relevant source context;
2. classify the workstream;
3. create a spec under `.sdd/specs/`;
4. fill `context.md`, `requirements.md`, `design.md`, `tasks.md`, `notes.md`;
5. update `SDD_INDEX.md`;
6. stop for human review.

It should not implement code while creating the spec.

---

## 8. Implementing Work

To implement safely:

```text
Implement the next task of <SPEC>.
```

The agent should:

1. read only the required context;
2. check Git status;
3. implement exactly one task from `tasks.md`;
4. update `tasks.md`;
5. update `notes.md`;
6. run tests or document why not;
7. stop.

Do not ask the agent to implement a whole spec at once unless the spec is deliberately tiny.

---

## 9. Reviewing Work

Ask:

```text
Review the current diff against <SPEC>.
```

The agent should compare the diff against:

- `requirements.md`;
- `design.md`;
- `tasks.md`;
- `notes.md`;
- `.sdd/operations/pr-checklist.md`.

It should detect:

- unrelated changes;
- missing tests;
- missing documentation updates;
- behavior changes not authorized by the spec;
- scope violations;
- unsafe tool usage.

---

## 10. Syncing External Tools

After review and commit, you can ask the agent to prepare external updates:

```text
Prepare issue tracker sync for <SPEC>. Do not write yet.
```

Writes to external tools require explicit approval.

The agent should first show:

- target resource;
- proposed comment or update;
- proposed status change;
- risks;
- whether approval is needed.

---

## 11. Long-Running Work

For long-running work, use:

- `SDD_INDEX.md` for spec catalog and macro status;
- `.sdd/WORKSPACE_STATE.md` for short multi-workstream state;
- `.sdd/specs/<spec>/notes.md` for spec-level memory;
- `.sdd/decisions/` for historical rationale.

Do not rely on chat history as the only memory.

---

## 12. When Not to Use Implementation Mode

Do not ask for implementation if:

- the spec does not exist;
- acceptance criteria are unclear;
- the work affects several unrelated layers;
- dependencies are unresolved;
- the requested change is a broad refactor;
- the workspace is still in discovery;
- stack or architecture is not decided;
- external writes are needed but not approved.

Use discovery, design or split workflows first.
