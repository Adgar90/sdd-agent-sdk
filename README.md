# SDD Agent SDK

**SDD Agent SDK** is a generic SDK for initializing and operating **Spec-Driven Development workspaces** with AI coding agents.

**SDD Agent SDK** es un SDK genérico para inicializar y operar workspaces de **Spec-Driven Development** con agentes de IA.

---

## English

The SDK provides:

- a neutral `.sdd/` core;
- workspace context schemas;
- initialization and validation tooling;
- spec templates;
- agent adapters;
- memory and decision policies;
- context loading guidance;
- operational workflows for Git, tools and MCPs.

Start with:

[English user guide](docs/en/user-guide.md)

---

## Español

El SDK proporciona:

- un core neutral `.sdd/`;
- schemas de contexto de workspace;
- herramientas de inicialización y validación;
- plantillas de specs;
- adaptadores de agentes;
- políticas de memoria y decisiones;
- guía de carga de contexto;
- workflows operativos para Git, herramientas y MCPs.

Empieza por:

[Guía de usuario en castellano](docs/es/guia-usuario.md)

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

## Documentation

English:

[English documentation](docs/en/README.md)

Español:

[Documentación en castellano](docs/es/README.md)

Validation report for this package:

```text
VALIDATION_REPORT.md
```


## Documentation layout

Human documentation is organized by language:

- [English documentation](docs/en/README.md)
- [Documentación en castellano](docs/es/README.md)
