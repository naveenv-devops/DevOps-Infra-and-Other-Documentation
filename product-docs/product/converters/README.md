# Converters

Met-R converter services transform content between authoring formats. Each converter runs as an independent microservice with dedicated validation and CI pipelines.

---

## Converter catalog

| Converter | Repository | Primary use case |
|---|---|---|
| [FrameMaker](framemaker.md) | `metR-Converter-FrameMaker` | Legacy FM books → DITA |
| [HTML](html.md) | `metR-Converter-HTML` | HTML normalization and transformation |
| [Markdown](markdown.md) | `metR-Converter-Markdown` | MD ↔ structured formats |
| [DOCX](docx.md) | `metR-Converter-DOCX` | Microsoft Word → DITA/HTML |
| [DocBook](docbook.md) | `metR-Converter-DocBook` | DocBook ↔ DITA |
| [PropDITA](propdita.md) | `metR-Converter-PropDITA` | Proprietary DITA dialect normalization |
| [Sitecore XML](sitecore-xml.md) | `metR-Converter-SitecoreXML` | Sitecore CMS export conversion |
| [PDF](pdf.md) | `metR-Converter-PDF` | PDF content extraction |

---

## Common conversion flow

```
Source file → Upload → Converter service → XSLT / validation → Target output
```

1. Author uploads source file via UI or API
2. API Gateway routes to the appropriate converter
3. Converter applies transformation rules
4. XSLT Library post-processing (if configured)
5. Schema validation (DITA-OT, custom rules)
6. Output delivered to publishing channel

---

## Validation

All converters run through standard CI checks:

| Check | Context |
|---|---|
| Unit tests | `unit-tests-pytest` |
| XSLT validation | `xslt-validation` |
| DITA schema | `dita-ot-schema-check` |
| Security scan | `security-scan` |

---

## Related

- [Conversion workflows](../../guides/conversion-workflows.md)
- [Supported formats](../../reference/supported-formats.md)
- [XSLT library](../../developers/xslt-library.md)
