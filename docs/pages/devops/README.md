# DevOps Documentation

Engineering operations standards for the **metapercept-metr** organization — CI/CD, GitHub governance, environments, and runbooks.

[← Documentation hub](README.md)

---

## DevOps areas

| Area | Description |
|---|---|
| [Prerequisites](prerequisites.md) | Tools, access, workstation setup |
| [Licensing](licensing.md) | GitHub, Copilot, tooling licenses |
| [CI/CD overview](ci-cd-overview.md) | Pipelines, status checks, and deployment flow |
| [Shared pipelines](shared-pipelines.md) | `metR-Phase2-shared-pipelines` templates |
| [Environments](environments.md) | dev, devops-testing, staging, production |
| [Engineer onboarding](onboarding.md) | New developer setup checklist |
| [Runbooks](runbooks/README.md) | Operational procedures |

---

## GitHub governance

| Document | Description |
|---|---|
| [Org governance](github-org-governance.md) | Org-wide standards for all 52 repositories |
| [Branch protection](github-branch-protection.md) | Rulesets for `dev` and `main` |
| [CODEOWNERS](github-codeowners.md) | Standard vs restricted templates |
| [PR merge guide](github-pr-merge-guide.md) | Review and merge workflow |
| [Signed commits](github-signed-commits.md) | Required for `dev` / `devops-testing` |

---

## Automation scripts

| Script | Command | Mode |
|---|---|---|
| Validate CODEOWNERS | `py -3 scripts/validate_codeowners_org.py` | Read-only |
| Rollout CODEOWNERS | `py -3 scripts/add_codeowners_to_org.py` | Write |
| Org scan → XLSX | `py -3 scripts/generate_org_scan_xlsx.py` | Read-only |

Reports: [`../reports/`](../reports/)

---

## Standard CI status checks

Required on **metR-Phase2-Core-Governance** branches (`main`, `feature/**`, etc.):

| Context | Purpose |
|---|---|
| `unit-tests-pytest` | Python unit tests |
| `xslt-validation` | XSLT transform validation |
| `dita-ot-schema-check` | DITA schema compliance |
| `security-scan` | Security / dependency scan |

---

## Roles

| Role | Responsibility |
|---|---|
| **DevOps lead** (`@naveenv-devops`) | Pipelines, infra, org governance, releases |
| **CODEOWNER** (`@nilesh-sk`) | Technical review and approval |
| **Developers** | Signed commits, PR hygiene, CI green |
| **Org admin** | Ruleset bypass (emergency only) |

---

*Maintained by DevOps. Last updated: June 2026.*
