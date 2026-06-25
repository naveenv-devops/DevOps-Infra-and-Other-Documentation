# Platform Licensing

Software licenses for platform components, open source compliance, and third-party dependencies.

---

## Platform software licenses

| Component | License | Commercial? | Notes |
|---|---|---|---|
| **Met-R platform** | Proprietary | Yes | MetaPercept IP |
| **DITA Open Toolkit** | Apache 2.0 | No | Core conversion engine |
| **Python** | PSF License | No | Runtime for services |
| **Node.js** | MIT | No | Frontend runtime |
| **Kubernetes** | Apache 2.0 | No | Orchestration |
| **MkDocs Material** | MIT | No | Documentation sites |

---

## Customer-facing product licensing

Met-R SaaS subscription plans (Starter, Professional, Enterprise) are documented in:

**[Product licensing](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/reference/licensing.md)**

---

## Engineering tooling licenses

GitHub, Copilot, and DevOps tool licenses:

**[DevOps licensing](../devops/licensing.md)**

---

## Open source compliance

### SBOM

A Software Bill of Materials is maintained per service repository. Enterprise customers may request a consolidated SBOM.

### License policy

| License type | Allowed | Action |
|---|---|---|
| MIT, Apache 2.0, BSD | Yes | No approval needed |
| LGPL | Case-by-case | Legal review |
| GPL (copyleft) | Restricted | Legal approval required |
| Commercial / proprietary | Case-by-case | Purchase + legal review |

### Attribution

Open source attributions are included in platform release packages for Enterprise deployments.

---

## Third-party API licenses

| API / Service | Used by | License model |
|---|---|---|
| Anthropic Claude API | AI agents | Pay-per-token (enterprise contract) |
| OpenAI API | AI features (if enabled) | Pay-per-token |
| Azure OpenAI | AI features (if enabled) | Azure enterprise agreement |
| Adobe FrameMaker | Customer source files | Customer-owned license |
| Cloud provider APIs | Infrastructure | PAYG or enterprise agreement |

---

## DITA-OT licensing

| Item | Detail |
|---|---|
| License | Apache License 2.0 |
| Cost | Free |
| Usage | Server-side only; bundled in Met-R |
| Attribution | Included in platform SBOM |
| Version | Pinned per service; updated via CI |

---

## Container base image licenses

| Base image | License | Scanning |
|---|---|---|
| `python:3.11-slim` | PSF (Python) + Debian | Scanned on build |
| `node:20-alpine` | MIT (Node) + Alpine | Scanned on build |
| Custom images | Per Dockerfile | `security-scan` CI check |

---

## Enterprise compliance packages

Available for Enterprise customers:

| Package | Includes |
|---|---|
| **SOC 2 report** | On request under NDA |
| **HIPAA BAA** | Business Associate Agreement |
| **Data residency** | Region-locked deployment |
| **Custom SLA** | 99.9% uptime guarantee |
| **SBOM export** | Full dependency list per release |

Contact MetaPercept sales for compliance documentation.

---

## License audit schedule

| Activity | Frequency | Owner |
|---|---|---|
| GitHub seat audit | Quarterly | DevOps |
| Copilot license review | Monthly | DevOps |
| Open source dependency scan | Every PR (`security-scan`) | CI/CD |
| Cloud cost / license review | Monthly | DevOps lead |
| Customer seat compliance | Quarterly | Client Admin |

---

## Related

- [Product licensing](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/reference/licensing.md)
- [DevOps licensing](../devops/licensing.md)
- [Security & compliance](security-compliance.md)
- [Prerequisites](prerequisites.md)
