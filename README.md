# SDD Agent SDK

**SDD Agent SDK** is a generic SDK for initializing and operating **Spec-Driven Development workspaces** with AI coding agents.

## What It Provides

- a neutral `.sdd/` core;
- workspace context schemas;
- initialization and validation tooling;
- spec templates;
- agent adapters;
- memory and decision policies;
- context loading guidance;
- operational workflows for Git, tools and MCPs.

---

## Quick Start

```bash
python init-sdd.py --context examples/workspace-context.example.json --output ./my-workspace --agents codex,claude-code,cursor
```

Validate:

```bash
python init-sdd.py --validate ./my-workspace
```

---

## Documentation

- [English](docs/en/README.md)
- [Castellano](docs/es/README.md)

---

## Repository Layout

- [core](core/) - neutral SDD workspace core.
- [schemas](schemas/) - workspace context schemas.
- [adapters](adapters/) - AI agent adapters.
- [extensions](extensions/) - optional extension assets.
- [examples](examples/) - example workspace context files.
- [docs](docs/README.md) - human-facing documentation by language.

---

## Core Flow

```text
Source context
→ SDD Spec
→ Task
→ Controlled implementation or analysis
→ Validation
→ Human review
→ External sync
```

---

## Package Validation

- [Validation report](VALIDATION_REPORT.md)
