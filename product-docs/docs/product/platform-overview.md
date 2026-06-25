# Platform overview

Met-R is a modular documentation orchestration platform. Each capability is delivered as an independent service, enabling scalable conversion, management, and publishing workflows.

---

## Architecture

```
                    ┌──────────────────┐
                    │   met-r.io UI    │
                    │  (metR-Frontend) │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │   API Gateway    │
                    │ (metR-API-Gateway)│
                    └────────┬─────────┘
         ┌───────────────────┼───────────────────┐
         │                   │                   │
  ┌──────▼──────┐    ┌───────▼───────┐   ┌──────▼──────┐
  │  Converters │    │  Doc Services │   │   Output    │
  │  (8+ svcs)  │    │  Manager/Edit │   │  PDF/HTML/  │
  └──────┬──────┘    └───────┬───────┘   │  CMS/XML    │
         │                   │           └──────┬──────┘
  ┌──────▼──────┐    ┌───────▼───────┐   ┌──────▼──────┐
  │ XSLT Library│    │  AI Services  │   │ Infinity    │
  │ Validation  │    │  Agents       │   │ DocSite     │
  └─────────────┘    └───────────────┘   └─────────────┘
```

---

## Core services

| Service | Repository | Purpose |
|---|---|---|
| **Frontend** | `metR-Frontend` | Web UI for authors and admins |
| **API Gateway** | `metR-API-Gateway` | API routing, auth, rate limiting |
| **Client Admin** | `metR-Client-Admin` | Workspace and client configuration |
| **Server Admin** | `metR-Server-Admin` | Server and infrastructure administration |
| **Core Infrastructure** | `metR-Core-Infrastructure` | Shared platform infrastructure |

---

## Converter services

See [Converters](converters/README.md) for full details.

| Service | Input | Output |
|---|---|---|
| FrameMaker | `.fm` | DITA, HTML |
| HTML | HTML | DITA, Markdown |
| Markdown | `.md` | HTML, DITA |
| DOCX | `.docx` | DITA, HTML |
| DocBook | DocBook XML | DITA, HTML |
| PropDITA | Proprietary DITA | Standard DITA |
| Sitecore XML | Sitecore | DITA, HTML |
| PDF | `.pdf` | Structured content |

---

## Document services

| Service | Purpose |
|---|---|
| **DocManager** | Document inventory, versioning, metadata |
| **DocEditor** | In-browser and integrated editing |
| **DocMigrate** | Bulk migration from legacy systems |
| **DocPublisher** | Publication orchestration and scheduling |
| **DedUp** | Content deduplication |

---

## Output services

| Service | Output type |
|---|---|
| **Output PDF** | Print-ready PDF |
| **Output HTML5-CMS** | HTML5 for web and CMS delivery |
| **Output XML-JSON-AI** | Structured output for AI/ML pipelines |
| **Infinity DocSite** | Dynamic searchable documentation portal |

---

## AI & intelligence

| Service | Purpose |
|---|---|
| **Determinacy Engine** | Rule-based content decision engine |
| **Master AI Agent** | Multi-step AI orchestration |
| **AI Agent flows** | FM-to-DITA and similar agentic conversions |

See [AI capabilities](ai/README.md).

---

## Shared platform

| Component | Purpose |
|---|---|
| **XSLT Library** | Reusable transformation stylesheets |
| **Phase2 Shared Pipelines** | CI/CD pipeline templates |
| **DITA validation** | Schema and content validation |

---

## Deployment model

| Model | Description |
|---|---|
| **SaaS (cloud)** | Hosted by MetaPercept at met-r.io |
| **Dedicated** | Single-tenant cloud instance |
| **Private / on-prem** | Customer-managed infrastructure |

---

## Related

- [Key concepts](../get-started/key-concepts.md)
- [Repository map](../reference/repository-map.md)
- [API overview](../developers/api-overview.md)
