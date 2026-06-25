# Runbooks

Operational procedures for DevOps and platform engineering.

---

## Runbook index

| Runbook | When to use |
|---|---|
| [Deployment](deployment.md) | Deploy a service to dev / production |
| [Incident response](incident-response.md) | Production outage or degradation |
| [CODEOWNERS validation](codeowners-validation.md) | Audit CODEOWNERS across org |
| [Rollback](rollback.md) | Revert a bad deployment |

---

## Severity definitions

| Level | Description | Response |
|---|---|---|
| **P1** | Production down | Immediate — all hands |
| **P2** | Major feature broken | < 4 hours |
| **P3** | Degraded / workaround exists | < 1 business day |
| **P4** | Minor / planned maintenance | Scheduled |

---

## On-call contacts

| Role | Handle |
|---|---|
| DevOps lead | `@naveenv-devops` |
| CODEOWNER | `@nilesh-sk` |

---

*Expand runbooks as operational procedures mature.*
