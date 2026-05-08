# SDD Agent SDK v1 — Componentes

## Estructura del paquete SDK

El paquete SDK contiene:

```text
sdd-agent-sdk/
  README.md
  init-sdd.py
  schemas/
  examples/
  core/
  adapters/
  extensions/
  docs/
```

Esta es la estructura de distribución del SDK. No es exactamente igual que la estructura instalada en un proyecto.

---

## Estructura instalada en un workspace

Un workspace inicializado por el SDK contiene:

```text
AGENTS.md
SDD_INDEX.md
.sdd/
  CONTEXT_LOADING.md
  WORKSPACE_STATE.md
  steering/
  specs/
  decisions/
  operations/
  templates/
```

Los adaptadores opcionales pueden añadir:

```text
CLAUDE.md
.cursor/rules/sdd-workflow.mdc
.kiro/steering/sdd-workflow.md
opencode.json
.sdd/adapters/codex.md
```

---

## `AGENTS.md`

Fichero principal de instrucciones del repositorio.

Finalidad:

- definir reglas seguras por defecto;
- apuntar a `.sdd/`;
- definir el flujo SDD obligatorio;
- definir condiciones de parada;
- indicar que la implementación debe venir desde specs.

Debe ser un router, no un manual gigante.

---

## `SDD_INDEX.md`

Mapa del workspace SDD.

Finalidad:

- listar specs;
- seguir estados macro;
- mostrar workstreams;
- registrar dependencias;
- enlazar políticas y documentación de compatibilidad.

No debe contener notas detalladas de implementación.

---

## `.sdd/CONTEXT_LOADING.md`

Política para uso eficiente de tokens.

Finalidad:

- evitar que los agentes lean todo el árbol;
- definir qué leer según la acción;
- definir qué no leer por defecto;
- describir reglas de escalado.

---

## `.sdd/WORKSPACE_STATE.md`

Estado macro vivo y corto.

Finalidad:

- resumir workstreams activos;
- mostrar fase actual;
- mostrar próximas acciones recomendadas;
- listar riesgos macro abiertos.

No debe convertirse en un log detallado.

---

## `.sdd/steering/`

Contexto estable actual.

Ficheros por defecto:

```text
README.md
product.md
architecture.md
tech.md
principles.md
agent-workflow.md
```

Steering debe mantenerse pequeño y curado.

---

## `.sdd/specs/`

Las specs son contratos de trabajo.

Cada spec debería contener:

```text
context.md
requirements.md
design.md
tasks.md
notes.md
```

Los agentes normalmente deberían leer solo la spec activa.

---

## `.sdd/decisions/`

Razonamiento histórico.

Ficheros por defecto:

```text
README.md
decision-template.md
```

Usa decisions cuando cambie contexto estable como arquitectura, stack, workflow, agente principal, issue tracker o política Git.

---

## `.sdd/operations/`

Workflows y políticas operativas.

Ejemplos:

```text
action-rules.md
git-workflow.md
memory-policy.md
tooling-and-mcp-policy.md
new-spec-workflow.md
split-issue-workflow.md
daily-workflow.md
pre-implementation-checklist.md
pr-checklist.md
```

Los agentes no deberían leer todos los ficheros de operations por defecto.

---

## `.sdd/templates/`

Plantillas reutilizables.

La plantilla de spec contiene:

```text
context.md
requirements.md
design.md
tasks.md
notes.md
```

No se deben editar plantillas para trabajos puntuales.

---

## `schemas/`

Contiene el schema de los ficheros de contexto del workspace.

Schema principal actual:

```text
schemas/workspace-context.schema.json
```

---

## `examples/`

Contiene ejemplos de contexto para diferentes tipos de workspace.

Ejemplos:

```text
workspace-context.example.json
workspace-context.functional-document.json
```

---

## `adapters/`

Puentes específicos de agentes o herramientas.

Los adaptadores deben apuntar al core `.sdd/` y evitar duplicar la metodología.

---

## `extensions/`

Reservado para capacidades futuras opcionales:

- Skills;
- workflows MCP;
- CLI SDD;
- detectores de stack;
- validadores avanzados;
- adaptadores de herramientas externas.
