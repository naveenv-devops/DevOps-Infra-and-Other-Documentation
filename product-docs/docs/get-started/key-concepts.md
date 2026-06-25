# Key concepts

Core terminology and concepts used across the Met-R platform.

---

## Workspace

A **workspace** is your organization's isolated environment on Met-R. It contains users, documents, pipelines, and output channels. Each customer typically has one or more workspaces.

---

## Source format vs target format

| Term | Definition | Examples |
|---|---|---|
| **Source format** | The authoring format you upload | FrameMaker, DITA, DocBook, Markdown, DOCX, PDF |
| **Target format** | The output Met-R produces | HTML5, PDF, DITA, CMS package, XML/JSON |

See the full matrix in [Supported formats](../reference/supported-formats.md).

---

## Converter

A **converter** is a microservice that transforms content between formats. Each converter is maintained as an independent service in the Met-R platform.

| Converter | Repository | Source → Target |
|---|---|---|
| FrameMaker | `metR-Converter-FrameMaker` | FM → DITA |
| HTML | `metR-Converter-HTML` | HTML ↔ structured formats |
| Markdown | `metR-Converter-Markdown` | MD ↔ structured formats |
| DOCX | `metR-Converter-DOCX` | Word → structured formats |
| DocBook | `metR-Converter-DocBook` | DocBook ↔ DITA/HTML |
| PropDITA | `metR-Converter-PropDITA` | Proprietary DITA variants |
| Sitecore XML | `metR-Converter-SitecoreXML` | Sitecore → standard formats |
| PDF | `metR-Converter-PDF` | PDF extraction / conversion |

---

## Pipeline

A **pipeline** defines the sequence of conversion, validation, and publishing steps applied to a document. Pipelines can include:

- Format conversion
- XSLT transformation (`metR-XSLT-Library`)
- DITA-OT schema validation
- Security scan
- Output to PDF, HTML5, or CMS

Pipelines are configured in **Client Admin** or via CI/CD (`metR-Phase2-shared-pipelines`).

---

## Document lifecycle

```
Upload → Convert → Validate → Review → Publish → Deliver
```

| Stage | Component |
|---|---|
| Upload | DocManager |
| Edit | DocEditor |
| Migrate | DocMigrate |
| Publish | DocPublisher |
| Deliver | Infinity DocSite, HTML5/CMS output |

---

## Output channels

| Channel | Description |
|---|---|
| **PDF** | Print-ready output (`metR-Output-PDF`) |
| **HTML5** | Web-ready HTML (`metR-Output-HTML5-CMS`) |
| **XML/JSON AI** | Structured output for AI consumption (`metR-Output-XML-JSON-AI`) |
| **Infinity DocSite** | Dynamic documentation portal (`metR-InfinityDocSite`) |

---

## AI capabilities

Met-R includes AI-powered features for intelligent documentation workflows:

| Feature | Description |
|---|---|
| **Determinacy Engine** | Structured decision logic for content processing |
| **Master AI Agent** | Orchestrates multi-step documentation tasks |
| **AI-assisted conversion** | FrameMaker-to-DITA and similar agent-driven flows |

See [AI capabilities](../product/ai/README.md).

---

## Administration roles

| Role | Access |
|---|---|
| **Author** | Upload, edit, convert, request publish |
| **Reviewer** | Approve content before publication |
| **Client Admin** | Workspace users, pipelines, client settings |
| **Server Admin** | Infrastructure, services, server-level config |

---

## Related

- [Glossary](../reference/glossary.md)
- [Platform overview](../product/platform-overview.md)
