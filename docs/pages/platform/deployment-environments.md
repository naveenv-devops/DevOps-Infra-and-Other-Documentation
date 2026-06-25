# Deployment & Environments

How Met-R platform services are deployed across environments.

---

## Deployment models

| Model | Description | Customers |
|---|---|---|
| **SaaS (multi-tenant)** | Shared cloud at met-r.io | Standard |
| **Dedicated** | Single-tenant cloud instance | Enterprise |
| **Private / on-prem** | Customer-managed K8s | Regulated industries |

---

## Environment topology

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Development │    │   Staging   │    │ Production  │
│  (dev branch)│ →  │  (staging)  │ →  │   (main)    │
└─────────────┘    └─────────────┘    └─────────────┘
       ↑                    ↑                  ↑
  Engineers            QA / UAT           Customers
```

---

## Service deployment unit

Each microservice deploys as an independent unit:

| Artifact | Registry | Orchestration |
|---|---|---|
| Container image | Container registry | Kubernetes |
| Configuration | Key Vault / GH Secrets | Per environment |
| Pipeline | GitHub Actions | Per repository |

---

## Release process

| Step | Action | Owner |
|---|---|---|
| 1 | Feature PR merged to `dev` | Developer |
| 2 | Auto-deploy to development | CI/CD |
| 3 | Validation on `devops-testing` | DevOps |
| 4 | Release PR `dev` → `main` | DevOps lead |
| 5 | Tag `vX.Y.Z` on `main` | DevOps lead |
| 6 | Deploy to production | CI/CD |
| 7 | Smoke test + announce | DevOps |

---

## Rollback

See [Rollback runbook](../devops/runbooks/rollback.md).

---

## Related

- [DevOps environments](../devops/environments.md)
- [Infrastructure](infrastructure.md)
- [Deployment runbook](../devops/runbooks/deployment.md)
