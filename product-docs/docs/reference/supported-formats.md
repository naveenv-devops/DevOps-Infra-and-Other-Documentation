# Supported formats

Input and output format matrix for Met-R converters.

---

## Input formats

| Format | Extensions | Converter service |
|---|---|---|
| Adobe FrameMaker | `.fm`, `.book` | metR-Converter-FrameMaker |
| DITA | `.dita`, `.ditamap` | Native / cross-converter |
| DocBook | `.xml` | metR-Converter-DocBook |
| Markdown | `.md` | metR-Converter-Markdown |
| Microsoft Word | `.docx` | metR-Converter-DOCX |
| HTML | `.html`, `.htm` | metR-Converter-HTML |
| PDF | `.pdf` | metR-Converter-PDF |
| Sitecore XML | `.xml` | metR-Converter-SitecoreXML |
| PropDITA | `.dita` | metR-Converter-PropDITA |

---

## Output formats

| Format | Service | Use case |
|---|---|---|
| DITA 1.2 / 1.3 | Converters | Structured authoring |
| HTML5 | metR-Output-HTML5-CMS | Web delivery |
| PDF | metR-Output-PDF | Print distribution |
| XML / JSON | metR-Output-XML-JSON-AI | AI / RAG pipelines |
| CMS package | metR-Output-HTML5-CMS | CMS import |

---

## Conversion matrix (selected)

| From → To | DITA | HTML5 | PDF | Markdown |
|---|---|---|---|---|
| FrameMaker | ✅ | ✅ | — | — |
| DOCX | ✅ | ✅ | — | — |
| Markdown | ✅ | ✅ | — | ✅ |
| DocBook | ✅ | ✅ | — | — |
| HTML | ✅ | ✅ | — | ✅ |

---

## Related

- [Converters](../product/converters/README.md)
- [Key concepts](../get-started/key-concepts.md)
