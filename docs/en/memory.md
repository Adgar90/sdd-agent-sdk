# Living Memory

Project memory must be versioned in the repository, not only kept in chat or in an agent's private memory.

Levels:

| Level | Location |
|---|---|
| Macro state | `.sdd/WORKSPACE_STATE.md` |
| Spec memory | `.sdd/specs/<spec>/notes.md` |
| Decisions | `.sdd/decisions/` |
| Catalog/status | `SDD_INDEX.md` |

Rule:

```text
WORKSPACE_STATE.md = short summary
notes.md = detail for one spec
decisions/ = why stable context changed
SDD_INDEX.md = specs and status map
```
