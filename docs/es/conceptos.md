# SDD Agent SDK v1 — Conceptos

## Spec-Driven Development

Spec-Driven Development es una forma de trabajar donde la implementación está guiada por una spec estructurada.

Una spec responde:

- ¿Cuál es el contexto?
- ¿Qué problema resolvemos?
- ¿Cuáles son los requisitos?
- ¿Cuál es el diseño propuesto?
- ¿Qué tareas están permitidas?
- ¿Qué queda fuera de alcance?
- ¿Cómo se validará?
- ¿Qué ocurrió durante la implementación?

## Por qué un issue tracker no basta

Los issue trackers son útiles para:

- priorización;
- ownership;
- estado de workflow;
- coordinación del equipo.

Pero normalmente no contienen suficiente información para guiar de forma segura a un agente de IA.

Una spec añade:

- scope;
- dependencias;
- diseño;
- criterios de aceptación;
- riesgos;
- límites de task;
- reglas de validación.

## Contexto fuente vs Spec

El contexto fuente puede ser:

- item de issue tracker;
- brief funcional;
- página de documentación;
- auditoría técnica;
- transcripción de chat;
- análisis de repositorio.

La spec es el contrato curado derivado de ese contexto.

## Steering

Steering contiene el contexto estable actual del workspace.

Ejemplos:

- contexto de producto;
- dirección arquitectónica;
- decisiones tecnológicas;
- principios;
- workflow del agente.

Steering debe ser pequeño y curado. No debe convertirse en una wiki.

## Decisions

Las decisions explican por qué cambió el contexto estable.

Ejemplos:

- seleccionar un stack;
- cambiar arquitectura;
- cambiar de un agente a otro;
- adoptar un nuevo issue tracker;
- cambiar política de Git.

Steering dice qué es verdad ahora. Decisions explica por qué cambió.

## Specs

Las specs definen trabajo.

Cada spec contiene:

```text
context.md       por qué existe y qué toca
requirements.md  qué debe cumplirse
design.md        cómo debe abordarse
tasks.md         pasos ejecutables
notes.md         memoria viva de esta spec
```

## Memoria viva

El SDK usa varios niveles de memoria:

| Nivel | Fichero/Carpeta | Finalidad |
|---|---|---|
| Estado macro | `.sdd/WORKSPACE_STATE.md` | Estado corto actual por workstreams. |
| Memoria de spec | `notes.md` | Memoria detallada de una spec. |
| Decisiones | `.sdd/decisions/` | Razonamiento histórico. |
| Índice | `SDD_INDEX.md` | Catálogo de specs y estados. |

## Workstreams

Un workspace puede tener varios frentes activos.

Ejemplo:

```text
roadmap-refactor
cambios-producto
bugfixes
documentacion
discovery
operaciones
```

El agente no debe asumir que toda nueva tarea pertenece al roadmap principal.

## Carga de contexto

Los agentes no deben leerlo todo.

Deben cargar contexto progresivamente:

```text
AGENTS.md
SDD_INDEX.md
CONTEXT_LOADING.md
ficheros de operación necesarios
steering relevante
spec activa
archivos adicionales solo si hace falta
```

Esto controla el consumo de tokens.

## Adaptadores de agentes

Distintos agentes usan distintos ficheros de instrucciones.

| Agente | Adaptador |
|---|---|
| Codex | `AGENTS.md` |
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/sdd-workflow.mdc` |
| Kiro | `.kiro/steering/sdd-workflow.md` |
| OpenCode | `opencode.json` |

Los adaptadores apuntan a `.sdd/`. No sustituyen `.sdd/`.

## Herramientas, MCPs y plugins

Las herramientas externas pueden ayudar a leer o sincronizar contexto. No sustituyen las specs.

Las escrituras requieren aprobación explícita.

## Skills

Las Skills son capacidades reutilizables opcionales para asistentes.

Una futura SDD Operator Skill podría ayudar a inicializar, validar y operar el SDK.

El `.sdd/` del repositorio sigue siendo la fuente de verdad del proyecto.
