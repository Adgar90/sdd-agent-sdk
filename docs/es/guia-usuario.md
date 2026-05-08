# SDD Agent SDK v1 — Guía de usuario

## 1. Qué es este SDK

**SDD Agent SDK** ayuda a inicializar un workspace estructurado para trabajar con agentes de IA usando **Spec-Driven Development**.

Proporciona:

- instrucciones persistentes para agentes;
- un core metodológico neutral bajo `.sdd/`;
- plantillas para specs;
- reglas operativas para Git, herramientas y MCPs;
- un modelo de memoria para trabajos largos;
- adaptadores para diferentes agentes de IA;
- documentación para personas.

El SDK está diseñado para funcionar con distintas herramientas, stacks y formas de trabajo.

No está limitado a Codex, Claude Code, Kiro, Cursor, OpenCode, Jira, Python, .NET, Streamlit ni ningún stack concreto.

---

## 2. Qué problema resuelve

Sin SDD, un agente suele recibir instrucciones como:

```text
Implementa este ticket de Jira.
```

Eso es arriesgado porque el texto de un issue normalmente no contiene suficiente detalle para guiar una implementación segura.

El SDK promueve este patrón:

```text
Crear o localizar una spec.
Revisar requisitos y diseño.
Implementar una task.
Actualizar notas.
Validar.
Parar para revisión.
```

Esto reduce:

- cambios fuera de alcance;
- refactors accidentales;
- supuestos no documentados;
- pérdida de contexto;
- diffs difíciles de revisar;
- commits, pushes o escrituras externas inesperadas.

---

## 3. Para quién es

Usa este SDK si quieres:

- introducir desarrollo asistido por IA en un proyecto real;
- gestionar refactors largos de forma segura;
- convertir briefs funcionales en specs técnicas;
- evitar que los agentes implementen directamente desde el issue tracker;
- soportar agentes como Codex, Claude Code, Cursor, Kiro u OpenCode;
- mantener la memoria del proyecto versionada en el repositorio;
- hacer que el trabajo con IA sea revisable y repetible.

---

## 4. Flujo básico

El flujo recomendado de SDD es:

```text
Contexto fuente
→ Spec
→ Task
→ Implementación o análisis
→ Validación
→ Revisión humana
→ Sincronización externa
```

Donde:

- **Contexto fuente** puede ser un ticket, issue, documento funcional, auditoría, chat, página de documentación o repositorio.
- **Spec** es el contrato de trabajo.
- **Task** es la unidad ejecutable más pequeña.
- **Validación** prueba o documenta el resultado.
- **Revisión humana** evita automatización insegura.
- **Sincronización externa** actualiza herramientas solo cuando se aprueba.

---

## 5. Instalar el SDK en un workspace

Prepara un fichero de contexto:

```bash
cp examples/workspace-context.example.json workspace-context.json
```

Edita el fichero para tu workspace.

Después ejecuta:

```bash
python init-sdd.py --context workspace-context.json --output . --agents codex,claude-code,cursor
```

Valida:

```bash
python init-sdd.py --validate .
```

Haz commit de la estructura SDD generada separado de cualquier cambio de implementación.

---

## 6. Qué pedir primero al agente

Después de instalar el SDK, empieza con un dry-run:

```text
Lee las instrucciones SDD y prepara la primera spec.
No modifiques archivos.
No hagas commit.
No hagas push.
Indica qué has leído y qué harías a continuación.
```

Esto valida que el agente entiende:

- la estructura SDD;
- la carga progresiva de contexto;
- las reglas seguras por defecto;
- el trabajo basado en specs;
- las restricciones de Git.

---

## 7. Crear una spec

Cuando llegue un nuevo trabajo, pide:

```text
Crea una spec SDD para <issue, brief o petición>.
```

El agente debería:

1. leer el contexto fuente relevante;
2. clasificar el workstream;
3. crear una spec bajo `.sdd/specs/`;
4. rellenar `context.md`, `requirements.md`, `design.md`, `tasks.md`, `notes.md`;
5. actualizar `SDD_INDEX.md`;
6. parar para revisión humana.

No debería implementar código mientras crea la spec.

---

## 8. Implementar trabajo

Para implementar de forma segura:

```text
Implementa la siguiente task de <SPEC>.
```

El agente debería:

1. leer solo el contexto necesario;
2. comprobar estado de Git;
3. implementar exactamente una task de `tasks.md`;
4. actualizar `tasks.md`;
5. actualizar `notes.md`;
6. ejecutar tests o documentar por qué no;
7. parar.

No pidas al agente implementar una spec completa salvo que sea deliberadamente muy pequeña.

---

## 9. Revisar trabajo

Pide:

```text
Revisa el diff actual contra <SPEC>.
```

El agente debería comparar el diff contra:

- `requirements.md`;
- `design.md`;
- `tasks.md`;
- `notes.md`;
- `.sdd/operations/pr-checklist.md`.

Debería detectar:

- cambios no relacionados;
- tests ausentes;
- documentación sin actualizar;
- cambios de comportamiento no autorizados;
- violaciones de scope;
- uso inseguro de herramientas.

---

## 10. Sincronizar herramientas externas

Después de revisar y commitear, puedes pedir al agente que prepare actualizaciones externas:

```text
Prepara la sincronización del issue tracker para <SPEC>. No escribas todavía.
```

Las escrituras en herramientas externas requieren aprobación explícita.

El agente debería mostrar primero:

- recurso objetivo;
- comentario o actualización propuesta;
- cambio de estado propuesto;
- riesgos;
- si necesita aprobación.

---

## 11. Trabajos largos

Para trabajos largos, usa:

- `SDD_INDEX.md` para catálogo de specs y estado macro;
- `.sdd/WORKSPACE_STATE.md` para estado corto multi-workstream;
- `.sdd/specs/<spec>/notes.md` para memoria de una spec;
- `.sdd/decisions/` para decisiones históricas.

No dependas del historial del chat como única memoria.

---

## 12. Cuándo no usar modo implementación

No pidas implementación si:

- la spec no existe;
- los criterios de aceptación no están claros;
- el trabajo afecta varias capas no relacionadas;
- hay dependencias sin resolver;
- el cambio solicitado es un refactor amplio;
- el workspace está en discovery;
- stack o arquitectura no están decididos;
- se necesitan escrituras externas no aprobadas.

Usa primero workflows de discovery, diseño o división.
