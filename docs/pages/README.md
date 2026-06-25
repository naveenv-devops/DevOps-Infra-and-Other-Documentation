# Documentation Hub

> **Audience:** MetaPercept engineering and DevOps only — not for Met-R end-users.  
> **Customers:** see [product documentation](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/README.md).

Internal engineering documentation for **MetaPercept** — DevOps operations and Met-R platform engineering.

[← Repository README](../README.md)

---

## Documentation tracks

| Track | Audience | Path |
|---|---|---|
| **[DevOps](devops/README.md)** | Engineers, CI/CD, GitHub governance | `docs/devops/` |
| **[Platform](platform/README.md)** | Architects, SRE, DevOps leads | `docs/platform/` |
| **[Product](../product-docs/README.md)** | Customers, authors (public) | `product-docs/` → docs.met-r.io |
| **[POC](../poc/README.md)** | Infrastructure evaluations | `poc/` |

---

## DevOps — quick links

| Topic | Document |
|---|---|
| CI/CD pipelines | [CI/CD overview](devops/ci-cd-overview.md) |
| Prerequisites & licensing | [DevOps prerequisites](devops/prerequisites.md) · [DevOps licensing](devops/licensing.md) |
| Shared pipeline templates | [Shared pipelines](devops/shared-pipelines.md) |
| Branch environments | [Environments](devops/environments.md) |
| New engineer setup | [Onboarding](devops/onboarding.md) |
| Operational runbooks | [Runbooks](devops/runbooks/README.md) |
| GitHub org governance | [Org governance](github-org-governance.md) |
| Branch protection | [Branch protection](github-branch-protection.md) |
| CODEOWNERS | [CODEOWNERS standard](github-codeowners.md) |
| PR workflow | [PR merge guide](github-pr-merge-guide.md) |
| Commit signing | [Signed commits](github-signed-commits.md) |

---

## Platform — quick links

| Topic | Document |
|---|---|
| System architecture | [Architecture](platform/architecture.md) |
| Prerequisites & licensing | [Platform prerequisites](platform/prerequisites.md) · [Platform licensing](platform/licensing.md) |
| All services & repos | [Services catalog](platform/services-catalog.md) |
| Deployment model | [Deployment & environments](platform/deployment-environments.md) |
| Cloud & K8s | [Infrastructure](platform/infrastructure.md) |
| Security | [Security & compliance](platform/security-compliance.md) |
| Monitoring | [Observability](platform/observability.md) |

---

## Preview internal docs site

```bash
pip install mkdocs-material
cd docs
mkdocs serve
# Open http://127.0.0.1:8000
```

Config: [`mkdocs.yml`](mkdocs.yml) → target: `platform-docs.met-r.io` or internal wiki

---

## Scripts & reports

| Item | Path |
|---|---|
| CODEOWNERS validation | `scripts/validate_codeowners_org.py` |
| Org scan report | `reports/github-org-scan.xlsx` |
| Validation CSV | `reports/codeowners-validation-latest.csv` |

---

*Maintained by DevOps & Platform Engineering. Last updated: June 2026.*
