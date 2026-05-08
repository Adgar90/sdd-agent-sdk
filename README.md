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

1. Prepare or generate `workspace-context.json`.

   You can create it manually from [the example](examples/workspace-context.example.json), or ask an agent to generate it from a repository, brief, issue, audit, documentation or conversation. Review the file before running the script.

2. Run `init-sdd.py`.

```bash
python init-sdd.py --context workspace-context.json --output ./my-workspace --agents codex,claude-code,cursor
```

3. Validate the generated SDD structure.

```bash
python init-sdd.py --validate ./my-workspace
```

For the full flow, see the [English user guide](docs/en/user-guide.md) or [guia de usuario en castellano](docs/es/guia-usuario.md).

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
