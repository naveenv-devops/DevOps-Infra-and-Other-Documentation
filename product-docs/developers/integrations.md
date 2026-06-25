# Integrations

Connect Met-R with CMS, CCMS, ticketing, and CI/CD tools.

---

## Supported integration patterns

| Pattern | Description |
|---|---|
| **REST API** | Push/pull documents and trigger conversions |
| **Webhooks** | Receive events on conversion complete, publish |
| **CMS export** | Sitecore XML converter for CMS content |
| **CI/CD** | GitHub Actions pipelines for automated validation |

---

## CMS / CCMS

| System | Integration |
|---|---|
| Sitecore | `metR-Converter-SitecoreXML` |
| Custom CMS | HTML5/CMS output channel |
| DITA CCMS | Native DITA import/export |

---

## CI/CD

Use `metR-Phase2-shared-pipelines` templates to integrate Met-R validation into your GitHub workflow.

---

## Related

- [API overview](api-overview.md)
- [Pipeline configuration](../admin/pipeline-configuration.md)
