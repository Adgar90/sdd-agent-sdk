# SDD Agent SDK v1 — Operating Model

## 1. Initialize Workspace

Create a workspace context file and run:

```bash
python init-sdd.py --context workspace-context.json --output . --agents codex,claude-code,cursor
```

Commit the generated structure separately.

---

## 2. Create First Spec

Ask:

```text
Create an SDD spec for this source context.
```

The agent should create a spec, not implement.

---

## 3. Review Spec

Human reviews:

- context;
- requirements;
- design;
- tasks;
- risks;
- validation plan;
- out of scope.

---

## 4. Implement One Task

Ask:

```text
Implement the next task of <SPEC>.
```

The agent implements only one task.

---

## 5. Update Living Memory

After each task:

- update `tasks.md`;
- update `notes.md`;
- run tests or document why not.

Update `WORKSPACE_STATE.md` only when macro state changes.

---

## 6. Review Diff

Ask:

```text
Review the current diff against <SPEC>.
```

Check:

- scope;
- tests;
- unrelated changes;
- architecture;
- notes;
- secrets;
- tool writes.

---

## 7. Commit and Push

Commit and push only when approved.

The default is no commit and no push.

---

## 8. Sync External Tools

After review/commit, prepare external updates:

```text
Prepare issue tracker sync for <SPEC>. Do not write yet.
```

Approve writes explicitly.

---

## Working With Several Workstreams

A workspace may have several streams:

```text
refactor-roadmap
features
bugfixes
documentation
discovery
operations
```

When new work arrives, classify it first.

Do not force unrelated work into the current roadmap.

---

## Existing Codebase Workflow

Use this when there is already a repository.

Recommended first specs:

- audit current state;
- create functional baseline;
- add regression validation;
- implement small changes.

---

## Functional Document Workflow

Use this when there is no code yet.

Recommended first specs:

- discovery scope;
- domain model;
- architecture decision;
- API or interface design;
- implementation plan.

Do not generate production code until architecture and requirements are approved.

---

## Migration Workflow

Use this when moving from one state to another.

Recommended specs:

- current state audit;
- target architecture decision;
- migration phases;
- compatibility strategy;
- rollback plan;
- validation plan.
