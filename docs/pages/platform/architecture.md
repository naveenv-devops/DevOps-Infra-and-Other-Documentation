# Platform Architecture

System design for the Met-R documentation orchestration platform.

---

## Design principles

| Principle | Implementation |
|---|---|
| **Microservices** | Each converter/output service is independently deployable |
| **API-first** | All capabilities exposed via API Gateway |
| **Pipeline-driven** | Conversion and validation as automated pipelines |
| **Multi-tenant** | Workspace isolation per customer |
| **AI-augmented** | Optional AI agents layered on conversion workflows |

---

## High-level architecture

```
                         ┌─────────────────┐
                         │   Users / API   │
                         │    Clients      │
                         └────────┬────────┘
                                  │ HTTPS
                         ┌────────▼────────┐
                         │  metR-Frontend  │
                         │   (Web UI)      │
                         └────────┬────────┘
                                  │
                         ┌────────▼────────┐
                         │ metR-API-Gateway│
                         │  Auth · Routing │
                         └───┬─────────┬───┘
              ┌──────────────┼─────────┼──────────────┐
              │              │         │              │
       ┌──────▼─────┐ ┌──────▼───┐ ┌───▼────┐ ┌──────▼──────┐
       │ Converters │ │   Doc    │ │ Output │ │  AI Agents  │
       │  (8+ svcs) │ │ Services │ │  Svcs  │ │  Engine     │
       └──────┬─────┘ └──────┬───┘ └───┬────┘ └──────┬──────┘
              │              │         │              │
              └──────────────┼─────────┼──────────────┘
                             │         │
                    ┌────────▼─────────▼────────┐
                    │   Shared Platform Layer   │
                    │  XSLT · Validation · CI   │
                    │  Core Infrastructure      │
                    └───────────────────────────┘
```

---

## Request flow — document conversion

```
1. Client uploads document (UI or API)
2. API Gateway authenticates and routes to DocManager
3. DocManager stores metadata + file reference
4. Conversion job queued → appropriate Converter service
5. Converter runs transform + XSLT post-processing
6. Validation: xslt-validation, dita-ot-schema-check
7. Output service generates deliverable (PDF/HTML/XML)
8. DocPublisher routes to channel (DocSite, CMS, download)
9. Client notified (webhook / UI status update)
```

---

## Service communication

| Pattern | Use case |
|---|---|
| **Synchronous REST** | API Gateway → service calls |
| **Async job queue** | Long-running conversions |
| **Shared storage** | Document files between services |
| **Event notification** | Job complete webhooks |

---

## Admin planes

| Plane | Component | Scope |
|---|---|---|
| **Client** | `metR-Client-Admin` | Workspace users, pipelines, client config |
| **Server** | `metR-Server-Admin` | Infrastructure, service config, scaling |

---

## Data boundaries

| Data type | Isolation | Retention |
|---|---|---|
| Customer documents | Per workspace | Configurable |
| Conversion logs | Per workspace | 90 days default |
| Platform metrics | Aggregated | Per observability policy |
| Secrets | Key Vault / GH Secrets | Rotated per policy |

---

## Related

- [Services catalog](services-catalog.md)
- [Infrastructure](infrastructure.md)
- [Product platform overview](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/product/platform-overview.md)
