# Platform Prerequisites

Infrastructure and technical requirements for deploying and operating the Met-R platform.

---

## Deployment model prerequisites

| Model | Prerequisites |
|---|---|
| **SaaS (multi-tenant)** | MetaPercept-managed; customers need browser + account only |
| **Dedicated cloud** | Customer contract; MetaPercept provisions isolated instance |
| **Private / on-prem** | Customer provides infrastructure below |

---

## Kubernetes cluster

| Requirement | Minimum | Recommended |
|---|---|---|
| Kubernetes version | 1.27+ | 1.29+ |
| Worker nodes | 3 | 5+ (across AZs) |
| Node CPU | 4 vCPU per node | 8 vCPU |
| Node RAM | 16 GB per node | 32 GB |
| Storage class | SSD-backed PV | NVMe / premium SSD |
| Ingress controller | NGINX or cloud LB | With TLS termination |
| DNS | Managed zone for `*.met-r.io` | |

**Repository:** `KUBERNETES` — manifests and Helm charts

---

## Cloud provider

| Resource | Specification |
|---|---|
| **Compute** | Managed Kubernetes (AKS, EKS, or GKE) |
| **Object storage** | S3-compatible or Azure Blob for document files |
| **Container registry** | ACR, ECR, or GHCR |
| **Secrets** | Azure Key Vault or AWS Secrets Manager |
| **Load balancer** | Cloud-native L7 LB with TLS |
| **DNS** | Route53, Azure DNS, or Cloudflare |

---

## Core infrastructure repository

**Repository:** `metR-Core-Infrastructure`

Deploy order:
1. Networking (VNet/VPC, subnets, NSGs)
2. Kubernetes cluster
3. Container registry
4. Key Vault / secrets
5. Storage accounts
6. Ingress and TLS certificates
7. Platform namespaces and services

---

## Per-service resource guidelines

| Service type | CPU request | Memory request | Replicas (min) |
|---|---|---|---|
| API Gateway | 500m | 512 Mi | 2 |
| Frontend | 250m | 256 Mi | 2 |
| Converter service | 1000m | 1 Gi | 2 |
| DocManager | 500m | 512 Mi | 2 |
| Output service | 1000m | 1 Gi | 2 |
| AI Agent | 2000m | 2 Gi | 1 |

Scale horizontally based on queue depth and CPU (HPA configured per service).

---

## Network prerequisites

| Rule | Detail |
|---|---|
| Ingress | HTTPS 443 from internet to API Gateway + Frontend |
| Internal | Service mesh / cluster DNS for inter-service calls |
| Egress | Outbound HTTPS for AI APIs, package registries |
| Firewall | Deny all except required ports |
| TLS | Valid certificate for custom domain |

---

## Database & storage

| Component | Requirement |
|---|---|
| Document metadata DB | PostgreSQL 14+ (managed) |
| Job queue | Redis or cloud message queue |
| File storage | Object storage; min 500 GB (production) |
| Backup | Daily automated backup; 30-day retention |

---

## Identity & SSO (enterprise)

| Requirement | Detail |
|---|---|
| IdP | SAML 2.0 or OIDC (Okta, Entra ID, etc.) |
| SCIM | Optional — automated user provisioning |
| MFA | Enforced on IdP for admin accounts |

---

## Monitoring prerequisites

| Component | Requirement |
|---|---|
| Metrics | Prometheus-compatible or cloud monitor |
| Logs | Centralized aggregation (90-day retention) |
| Alerts | Pager / Teams integration for P1/P2 |
| Health endpoints | `/health` on all services |

See [Observability](observability.md).

---

## CI/CD prerequisites

| Component | Requirement |
|---|---|
| GitHub Actions | Org-level runners or self-hosted runners |
| Shared pipelines | `metR-Phase2-shared-pipelines` access |
| Container build | Docker buildx; push to registry |
| Secrets in CI | GitHub Secrets per environment |

---

## Security prerequisites

| Control | Requirement |
|---|---|
| Pod security | Non-root containers, read-only filesystem where possible |
| Network policies | Namespace isolation |
| Image scanning | Scan on push to registry |
| Secrets | Never in code; Key Vault / GH Secrets only |
| Branch protection | Active on all service repos |

See [Security & compliance](security-compliance.md).

---

## Pre-deployment checklist

```
☐ Kubernetes cluster provisioned (1.27+)
☐ Container registry accessible from cluster
☐ Key Vault / secrets manager configured
☐ Object storage bucket created
☐ PostgreSQL instance provisioned
☐ TLS certificate issued for domain
☐ DNS records configured
☐ Ingress controller deployed
☐ Monitoring and alerting connected
☐ GitHub Actions deploy workflow tested
☐ metR-Core-Infrastructure applied
☐ Smoke test passed on staging
```

---

## Related

- [Infrastructure](infrastructure.md)
- [Deployment environments](deployment-environments.md)
- [Product prerequisites](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/get-started/prerequisites.md)
- [DevOps prerequisites](../devops/prerequisites.md)
