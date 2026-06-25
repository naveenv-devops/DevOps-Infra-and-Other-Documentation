# Security & Compliance

Platform-level security controls for Met-R.

---

## Security layers

| Layer | Control |
|---|---|
| **Transport** | TLS 1.2+ on all external traffic |
| **Authentication** | API keys, OAuth, workspace SSO (enterprise) |
| **Authorization** | RBAC per workspace; CODEOWNERS on repos |
| **Secrets** | Key Vault / GitHub Secrets; never in source code |
| **Supply chain** | `security-scan` on every PR to governance branches |
| **Branch protection** | Signed commits, required reviews, no direct push |

---

## Repository security

| Control | Implementation |
|---|---|
| CODEOWNERS | `.github/CODEOWNERS` on all protected branches |
| Branch rulesets | Secure Branch Protection + Core Governance |
| Signed commits | Required on `dev` / `devops-testing` |
| Dependency scanning | `security-scan` CI check |
| Org admin bypass | Emergency only; logged |

Details: [GitHub org governance](../github-org-governance.md)

---

## Data security

| Data type | Protection |
|---|---|
| Customer documents | Workspace isolation; encrypted at rest |
| API tokens | Scoped per workspace; rotatable |
| Audit logs | Admin actions logged in Client/Server Admin |
| PII | Minimize collection; configurable retention |

---

## Compliance readiness

| Area | Status |
|---|---|
| Access control | RBAC + CODEOWNERS |
| Change management | PR + review + CI gates |
| Audit trail | GitHub audit log + platform logs |
| Vulnerability management | security-scan CI check |
| Formal certifications | Contact MetaPercept for SOC/ISO docs |

---

## Security incident process

1. Report to `@naveenv-devops`
2. Follow [Incident response runbook](../devops/runbooks/incident-response.md)
3. Assess data exposure
4. Remediate and document

---

## Related

- [Governance (product)](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/admin/governance.md)
- [Branch protection](../github-branch-protection.md)
