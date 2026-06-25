# Pipeline configuration

Configure conversion pipelines and CI/CD integration.

---

## Pipeline components

| Component | Repository | Purpose |
|---|---|---|
| Shared pipelines | `metR-Phase2-shared-pipelines` | Reusable CI/CD templates |
| XSLT Library | `metR-XSLT-Library` | Custom transforms |
| DITA validation | `dita2-validation-transformation` | Schema validation rules |

---

## Configure a pipeline

1. Open **Client Admin** → **Pipelines**
2. Select or create a pipeline profile
3. Add conversion steps (converter service + target format)
4. Add validation steps (XSLT, DITA-OT schema, security scan)
5. Set output channel (PDF, HTML5, DocSite)
6. Save and assign to workspace or project

---

## CI/CD integration

Pipelines integrate with GitHub Actions. Required status checks for governance branches:

- `unit-tests-pytest`
- `xslt-validation`
- `dita-ot-schema-check`
- `security-scan`

---

## Related

- [Conversion workflows](../guides/conversion-workflows.md)
- [API Gateway](../developers/api-gateway.md)
