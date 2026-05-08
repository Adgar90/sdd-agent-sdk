# Tipos de contexto

El SDK soporta distintos orígenes:

- `existing-codebase`
- `functional-document`
- `new-product`
- `technical-audit`
- `migration-plan`
- `integration-request`
- `discovery`

Un workspace puede evolucionar.

Ejemplo:

```text
functional-document → new-product → existing-codebase → maintenance
```

Cuando esto ocurra, actualiza steering mediante una decision record.
