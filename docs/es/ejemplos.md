# SDD Agent SDK v1 — Ejemplos

## Ejemplo 1: Codebase existente

Tienes un repositorio de API y quieres introducir SDD.

Contexto:

```json
{
  "workspace": {
    "type": "existing-codebase",
    "lifecycle_stage": "implementation"
  }
}
```

Primer prompt:

```text
Lee las instrucciones SDD y prepara la primera spec de discovery.
No modifiques archivos.
```

---

## Ejemplo 2: Brief funcional

Tienes un documento funcional pero aún no hay código.

Contexto:

```json
{
  "workspace": {
    "type": "functional-document",
    "lifecycle_stage": "discovery"
  }
}
```

Primer prompt:

```text
Crea una spec SDD de discovery a partir de este brief funcional.
No propongas implementación todavía.
```

Specs iniciales recomendadas:

```text
discovery-functional-scope
define-domain-model
select-technical-stack
define-api-contract
```

---

## Extracción asistida de contexto desde codebase existente

Un agente puede analizar un repositorio existente para generar `workspace-context.json`. Solo debe preparar el fichero de contexto para revisión y no debe ejecutar `init-sdd.py` todavía.

```text
Analiza este repositorio para preparar la instalación de SDD Agent SDK.

Objetivo:
Generar un workspace-context.json compatible con schemas/workspace-context.schema.json.

No modifiques archivos.
No ejecutes init-sdd.py.
No hagas commit.
No hagas push.

Extrae:
- workspace.type
- workspace.lifecycle_stage
- source_context
- project.name
- project.description
- project.domain
- project.primary_language
- project.frameworks
- project.test_framework
- project.package_manager
- architecture.current_summary
- architecture.target_summary
- architecture.layers
- architecture.risks
- workflow.issue_tracker
- workflow.docs_platform
- workflow.git_provider
- workflow.base_branch
- workflow.branch_strategy
- agents.primary
- agents.supported
- sdd.language
- sdd.require_human_review
- sdd.allow_agent_commits
- sdd.allow_agent_push

Reglas:
- Si algo no está confirmado, usa "unknown".
- No inventes herramientas ni stack.
- Distingue hechos observados de inferencias.
- Devuélveme el JSON final y una breve lista de supuestos.
```

---

## Extracción asistida de contexto desde brief funcional

Un agente puede analizar un brief funcional para generar `workspace-context.json`. No debe elegir stack técnico salvo que el brief lo indique explícitamente.

```text
Analiza este brief funcional para preparar la instalación de SDD Agent SDK.

Objetivo:
Generar un workspace-context.json compatible con schemas/workspace-context.schema.json.

No propongas implementación todavía.
No elijas stack técnico salvo que el brief lo indique explícitamente.
No ejecutes init-sdd.py.

Reglas:
- workspace.type debería ser "functional-document".
- lifecycle_stage normalmente será "discovery".
- Si stack, arquitectura o repositorio son desconocidos, usa "unknown".
- Distingue requisitos confirmados, supuestos y preguntas abiertas.
- Devuélveme el JSON final y una breve lista de supuestos/preguntas abiertas.
```

---

## Ejemplo 3: Roadmap largo de refactor más feature nueva

Tienes un roadmap largo de refactor, pero entra una feature nueva.

Incorrecto:

```text
Añade esta feature dentro de la spec actual de refactor.
```

Correcto:

```text
Clasifica esta nueva petición.
Si es independiente, crea una spec separada de tipo feature-change.
Si bloquea o depende del roadmap de refactor, documenta la relación.
```

---

## Ejemplo 4: Bugfix durante refactor

Prompt:

```text
Crea una spec bugfix para este issue y determina si bloquea el workstream de refactor actual.
```

Resultado esperado:

- spec bugfix separada;
- relación con roadmap;
- plan de validación pequeño;
- sin refactor no relacionado.

---

## Ejemplo 5: Cambiar de agente

Empiezas con Codex y luego pasas a Claude Code.

Pasos:

1. Mantener `.sdd/`.
2. Añadir `CLAUDE.md`.
3. Apuntar Claude hacia `.sdd/`.
4. Ejecutar dry-run.
5. No reescribir specs.

Prompt:

```text
Lee el workspace SDD y prepara la spec activa.
No modifiques archivos.
Indica qué ficheros has leído.
```

---

## Ejemplo 6: Sincronización externa

Prompt:

```text
Prepara la sincronización de Jira para SPEC-123.
No escribas todavía.
```

Comportamiento esperado:

- leer spec y notes;
- preparar propuesta de comentario/estado;
- pedir aprobación antes de escribir.
