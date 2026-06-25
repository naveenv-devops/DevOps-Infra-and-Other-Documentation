# Infrastructure

Cloud, Kubernetes, and core infrastructure for the Met-R platform.

---

## Core infrastructure repository

**Repository:** `metR-Core-Infrastructure`  
**Purpose:** Shared IaC, networking, and platform foundation

---

## Technology stack

| Layer | Technology | Notes |
|---|---|---|
| **Cloud** | Azure / AWS (TBD per deployment) | Multi-cloud capable |
| **Orchestration** | Kubernetes | `KUBERNETES` repository |
| **CI/CD** | GitHub Actions | Per-service + shared pipelines |
| **Container registry** | Cloud-native registry | Per environment |
| **Secrets** | Azure Key Vault / GitHub Secrets | No secrets in code |
| **IaC** | Terraform / Bicep (TBD) | Document in POC-003 |

---

## Kubernetes layout (conceptual)

```
Namespace: metr-platform
├── api-gateway
├── frontend
├── converters/          (one deployment per converter)
│   ├── framemaker
│   ├── html
│   └── ...
├── doc-services/
│   ├── docmanager
│   ├── doceditor
│   └── ...
├── output/
│   ├── pdf
│   ├── html5-cms
│   └── ...
└── ai/
    ├── determinacy-engine
    └── master-ai-agent
```

---

## Networking

| Zone | Access |
|---|---|
| Public | API Gateway, Frontend (HTTPS) |
| Internal | Service-to-service (cluster network) |
| Data | Database / storage (private endpoint) |

---

## Scaling

| Service type | Scaling strategy |
|---|---|
| API Gateway | Horizontal (HPA on CPU/requests) |
| Converters | Horizontal (queue depth trigger) |
| Output | Horizontal (job queue) |
| DocManager | Vertical + read replicas |

---

## Related

- [Architecture](architecture.md)
- [Services catalog](services-catalog.md)
- [Observability](observability.md)
- [KUBERNETES repo](https://github.com/metapercept-metr/KUBERNETES)
