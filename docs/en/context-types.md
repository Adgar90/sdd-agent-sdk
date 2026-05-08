# Context Types

The SDK supports different workspace origins:

- `existing-codebase`
- `functional-document`
- `new-product`
- `technical-audit`
- `migration-plan`
- `integration-request`
- `discovery`

A workspace may evolve over time.

Example:

```text
functional-document → new-product → existing-codebase → maintenance
```

When this happens, update steering through a decision record.
