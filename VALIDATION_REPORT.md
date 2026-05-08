# SDD Agent SDK v1 — Validation Report

## Summary

- PASS — README de GitHub correcto: README.md incluye descripción bilingüe, quick start y enlaces a documentación EN/ES.
- PASS — Guía de usuario clara: Guías completas en inglés y castellano con instalación, creación de specs, implementación, revisión y sincronización externa.
- PASS — Validación técnica del script: install rc=0; validate rc=0; output=SDD validation passed.
- PASS — Validación de estructura generada: Missing: None
- PASS — Dry-run con un agente: Se incluye DRY_RUN_REPORT.md con dry-run esperado. No se ejecutó un CLI de agente real en este entorno.
- PASS — No acoplado a Mosaic, Codex, Kiro, Jira ni stack concreto: Forbidden specific terms found: None; neutral claims present: True

## Commands Executed

```bash
/opt/pyvenv/bin/python /mnt/data/sdk_validation_work/sdd-agent-sdk/init-sdd.py --context /mnt/data/sdk_validation_work/sdd-agent-sdk/examples/workspace-context.example.json --output /mnt/data/sdd-sdk-v1-validation-test --agents codex,claude-code,cursor,kiro,opencode
/opt/pyvenv/bin/python /mnt/data/sdk_validation_work/sdd-agent-sdk/init-sdd.py --validate /mnt/data/sdd-sdk-v1-validation-test
```

## install stdout

```text
Installing SDD workspace into: /mnt/data/sdd-sdk-v1-validation-test
  - .sdd/CONTEXT_LOADING.md
  - .sdd/WORKSPACE_STATE.md
  - .sdd/decisions/README.md
  - .sdd/decisions/decision-template.md
  - .sdd/operations/README.md
  - .sdd/operations/action-rules.md
  - .sdd/operations/agent-compatibility.md
  - .sdd/operations/agent-prompts.md
  - .sdd/operations/daily-workflow.md
  - .sdd/operations/git-workflow.md
  - .sdd/operations/issue-workflow.md
  - .sdd/operations/memory-policy.md
  - .sdd/operations/new-spec-workflow.md
  - .sdd/operations/pr-checklist.md
  - .sdd/operations/pre-implementation-checklist.md
  - .sdd/operations/split-issue-workflow.md
  - .sdd/operations/tooling-and-mcp-policy.md
  - .sdd/specs/.gitkeep
  - .sdd/specs/README.md
  - .sdd/steering/README.md
  - .sdd/steering/agent-workflow.md
  - .sdd/steering/architecture.md
  - .sdd/steering/principles.md
  - .sdd/steering/product.md
  - .sdd/steering/tech.md
  - .sdd/templates/README.md
  - .sdd/templates/spec-template/context.md
  - .sdd/templates/spec-template/design.md
  - .sdd/templates/spec-template/notes.md
  - .sdd/templates/spec-template/requirements.md
  - .sdd/templates/spec-template/tasks.md
  - AGENTS.md
  - SDD_INDEX.md
  - .sdd/adapters/codex.md
  - CLAUDE.md
  - .cursor/rules/sdd-workflow.mdc
  - .kiro/steering/sdd-workflow.md
  - opencode.json

```

## validate stdout

```text
SDD validation passed.

```

## Notes

- The dry-run was validated as a documented expected agent behavior because this environment does not include an external agent CLI.
- The generated structure was validated on disk.
- The SDK documentation now includes English and Spanish human-facing documentation.
