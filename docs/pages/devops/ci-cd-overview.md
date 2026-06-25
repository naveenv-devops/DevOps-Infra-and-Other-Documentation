# CI/CD Overview

Continuous integration and delivery practices for Met-R platform repositories.

---

## Pipeline model

```
Feature branch → PR → dev → devops-testing → main → Production
```

| Stage | Branch | Gate |
|---|---|---|
| Development | `feature/**` | CI checks + 2 reviews + CODEOWNER |
| Integration | `dev` | Signed commits + 2 reviews + CODEOWNER + threads resolved |
| DevOps validation | `devops-testing` | Same as `dev` |
| Release | `main` | CI checks + 2 reviews + CODEOWNER |

---

## GitHub Actions workflow

Each Met-R service repository includes workflows triggered on:

| Event | Action |
|---|---|
| `pull_request` | Run CI checks |
| `push` to `dev` / `main` | Run CI + deploy (per repo config) |
| `workflow_dispatch` | Manual deploy / validation |

---

## Required status checks

On **metR-Phase2-Core-Governance** branches:

| Check | Description | Failure action |
|---|---|---|
| `unit-tests-pytest` | Python unit test suite | Fix tests before merge |
| `xslt-validation` | XSLT stylesheet validation | Fix transform errors |
| `dita-ot-schema-check` | DITA OT schema validation | Fix DITA structure |
| `security-scan` | Dependency / security scan | Resolve vulnerabilities |

Strict policy: branch must be **up to date** with base before merge.

---

## Shared pipelines

Reusable workflow templates live in `metR-Phase2-shared-pipelines`. See [Shared pipelines](shared-pipelines.md).

---

## Branch protection summary

| Branch | Signed commits | CI checks | CODEOWNER |
|---|---|---|---|
| `dev` | **Required** | Optional | Required |
| `devops-testing` | **Required** | Optional | Required |
| `main` | No | **Required** | Required |
| `feature/**` | No | **Required** | Required |

Details: [Branch protection](../github-branch-protection.md)

---

## Deployment triggers

| Environment | Trigger | Approved by |
|---|---|---|
| Development | Merge to `dev` | CODEOWNER |
| DevOps testing | Merge to `devops-testing` | DevOps |
| Production | Merge to `main` + release tag | DevOps lead |

---

## Related

- [Shared pipelines](shared-pipelines.md)
- [Environments](environments.md)
- [PR merge guide](../github-pr-merge-guide.md)
