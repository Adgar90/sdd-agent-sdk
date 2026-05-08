# SDD Agent SDK v1 — Modelo operativo

## 1. Inicializar workspace

Crea un fichero de contexto y ejecuta:

```bash
python init-sdd.py --context workspace-context.json --output . --agents codex,claude-code,cursor
```

Haz commit de la estructura generada por separado.

---

## 2. Crear la primera spec

Pide:

```text
Crea una spec SDD para este contexto fuente.
```

El agente debe crear una spec, no implementar.

---

## 3. Revisar la spec

La persona revisa:

- contexto;
- requisitos;
- diseño;
- tasks;
- riesgos;
- plan de validación;
- fuera de alcance.

---

## 4. Implementar una task

Pide:

```text
Implementa la siguiente task de <SPEC>.
```

El agente implementa solo una task.

---

## 5. Actualizar memoria viva

Después de cada task:

- actualizar `tasks.md`;
- actualizar `notes.md`;
- ejecutar tests o documentar por qué no.

Actualizar `WORKSPACE_STATE.md` solo cuando cambie el estado macro.

---

## 6. Revisar diff

Pide:

```text
Revisa el diff actual contra <SPEC>.
```

Comprueba:

- scope;
- tests;
- cambios no relacionados;
- arquitectura;
- notes;
- secretos;
- escrituras externas.

---

## 7. Commit y push

Commit y push solo cuando se apruebe.

Por defecto: no commit, no push.

---

## 8. Sincronizar herramientas externas

Después de revisar/commitear, prepara actualizaciones externas:

```text
Prepara la sincronización del issue tracker para <SPEC>. No escribas todavía.
```

Aprueba escrituras explícitamente.

---

## Trabajar con varios workstreams

Un workspace puede tener varios frentes:

```text
roadmap-refactor
features
bugfixes
documentacion
discovery
operaciones
```

Cuando llega nuevo trabajo, clasifícalo primero.

No fuerces trabajo no relacionado dentro del roadmap actual.

---

## Workflow para codebase existente

Úsalo cuando ya existe un repositorio.

Specs iniciales recomendadas:

- auditar estado actual;
- crear baseline funcional;
- añadir validación de regresión;
- implementar cambios pequeños.

---

## Workflow para documento funcional

Úsalo cuando aún no hay código.

Specs iniciales recomendadas:

- discovery de alcance;
- modelo de dominio;
- decisión de arquitectura;
- diseño de API o interfaz;
- plan de implementación.

No generar código productivo hasta aprobar arquitectura y requisitos.

---

## Workflow de migración

Úsalo al pasar de un estado a otro.

Specs recomendadas:

- auditoría de estado actual;
- decisión de arquitectura objetivo;
- fases de migración;
- estrategia de compatibilidad;
- plan de rollback;
- plan de validación.
