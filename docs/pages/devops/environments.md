# Environments

Branch-to-environment mapping for Met-R platform services.

---

## Environment matrix

| Environment | Git branch | Purpose | Access |
|---|---|---|---|
| **Local** | Feature branch | Developer workstation | Developer |
| **Development** | `dev` | Active integration | Engineering team |
| **DevOps testing** | `devops-testing` | Pipeline / infra validation | DevOps |
| **Staging** | `staging` / `develop` | Pre-production validation | QA + leads |
| **Production** | `main` | Live customer workloads | Restricted |

> Not all repositories maintain every branch. See org scan report for branch availability per repo.

---

## Promotion flow

```
feature/MDP-XXX  →  dev  →  devops-testing  →  main
     (PR)           (PR)        (PR)            (release)
```

### Development (`dev`)

- Signed commits required
- 2 approvals + CODEOWNER
- All review threads resolved
- Primary integration branch for feature work

### DevOps testing (`devops-testing`)

- Same protection as `dev`
- Used for pipeline changes, infra validation, release candidates
- DevOps-owned merges

### Production (`main`)

- 4 CI status checks required
- 2 approvals + CODEOWNER
- No signed commit requirement (by current ruleset)
- Tagged releases from `main`

---

## Environment-specific configuration

| Config type | Storage | Managed by |
|---|---|---|
| App settings | Environment variables / Key Vault | DevOps |
| Secrets | GitHub Secrets / Azure Key Vault | DevOps |
| Feature flags | Server Admin / config service | Platform team |
| Pipeline vars | GitHub Actions vars per environment | DevOps |

---

## Related

- [CI/CD overview](ci-cd-overview.md)
- [Platform deployment](../platform/deployment-environments.md)
- [Branch protection](../github-branch-protection.md)
