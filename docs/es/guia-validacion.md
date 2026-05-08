# SDD Agent SDK v1 — Guía de validación

Usa esta guía para confirmar que SDK v1 es funcional.

## 1. Validación del paquete

Comprueba que el SDK contiene:

```text
README.md
init-sdd.py
schemas/
examples/
core/
adapters/
extensions/
docs/
```

## 2. Validación de instalación

Ejecuta:

```bash
python init-sdd.py --context examples/workspace-context.example.json --output ./tmp-sdd-test --agents codex,claude-code,cursor,kiro,opencode
```

Ficheros esperados:

```text
AGENTS.md
SDD_INDEX.md
.sdd/CONTEXT_LOADING.md
.sdd/WORKSPACE_STATE.md
.sdd/steering/
.sdd/specs/
.sdd/decisions/
.sdd/operations/
.sdd/templates/
CLAUDE.md
.cursor/rules/sdd-workflow.mdc
.kiro/steering/sdd-workflow.md
opencode.json
```

## 3. Validación del script

Ejecuta:

```bash
python init-sdd.py --validate ./tmp-sdd-test
```

Resultado esperado:

```text
SDD validation passed.
```

## 4. Validación de carga de contexto

Confirma que `.sdd/CONTEXT_LOADING.md` indica:

- qué leer por acción;
- qué no leer por defecto;
- cuándo escalar contexto.

## 5. Validación de memoria viva

Confirma que existen y explican su rol:

```text
.sdd/WORKSPACE_STATE.md
.sdd/operations/memory-policy.md
.sdd/decisions/
.sdd/specs/<spec>/notes.md
```

## 6. Validación de adaptadores

Confirma que los adaptadores apuntan a `.sdd/` y no duplican toda la metodología.

## 7. Dry-run humano con agente

Pide a un agente:

```text
Lee las instrucciones SDD y prepara la primera spec.
No modifiques archivos.
No hagas commit.
No hagas push.
Indica qué has leído y qué harías a continuación.
```

Resultado esperado:

- el agente lee ficheros de entrada;
- no modifica archivos;
- identifica la siguiente acción segura;
- no implementa.

## 8. Condiciones de fallo

SDK v1 no debería considerarse listo si:

- la instalación sobrescribe ficheros existentes sin advertir;
- la validación no detecta ficheros requeridos;
- la documentación generada depende de un agente o stack específico;
- los adaptadores duplican la metodología en vez de apuntar a `.sdd/`;
- el agente lee todo `.sdd/` por defecto;
- la memoria vive solo en chat;
- las escrituras externas no requieren aprobación clara.
