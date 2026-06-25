# Platform Documentation

Internal platform architecture and operations documentation for the **Met-R** platform (`met-r.io`).

[← Documentation hub](../README.md)

---

## Platform areas

| Area | Description |
|---|---|
| [Prerequisites](prerequisites.md) | K8s, cloud, infra requirements |
| [Licensing](licensing.md) | Open source, third-party, compliance |
| [Architecture](architecture.md) | System design, service mesh, data flow |
| [Services catalog](services-catalog.md) | All microservices and repositories |
| [Deployment & environments](deployment-environments.md) | SaaS, dedicated, and environment promotion |
| [Infrastructure](infrastructure.md) | Cloud, Kubernetes, core infra repo |
| [Security & compliance](security-compliance.md) | Platform security controls |
| [Observability](observability.md) | Monitoring, logging, alerting |

---

## Platform vs product docs

| Documentation | Audience | Location |
|---|---|---|
| **Platform (this section)** | DevOps, SRE, architects, leads | `docs/platform/` |
| **DevOps operations** | Engineers, CI/CD, GitHub | `docs/devops/` |
| **Product (customer)** | Customers, authors, admins | `product-docs/` |

---

## Platform components at a glance

```
┌─────────────────────────────────────────────────────────────┐
│                     met-r.io Platform                        │
├──────────────┬──────────────┬──────────────┬────────────────┤
│   Edge       │   Services   │   Data       │   Delivery     │
│  API Gateway │  Converters  │  DocManager  │  Output svcs   │
│  Frontend    │  AI Agents   │  DocEditor   │  Infinity Site │
├──────────────┴──────────────┴──────────────┴────────────────┤
│  Core Infrastructure · Shared Pipelines · XSLT Library       │
└─────────────────────────────────────────────────────────────┘
```

---

## Key repositories

| Layer | Repository |
|---|---|
| Core | `metR-Core-Infrastructure`, `metR-Phase2` |
| Gateway | `metR-API-Gateway` |
| UI | `metR-Frontend` |
| Admin | `metR-Client-Admin`, `metR-Server-Admin` |
| Pipelines | `metR-Phase2-shared-pipelines` |

Full map: [Services catalog](services-catalog.md)

---

*Maintained by Platform Engineering & DevOps. Last updated: June 2026.*
