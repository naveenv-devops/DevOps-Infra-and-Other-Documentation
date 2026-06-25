# GitHub Organization Governance

Standards that apply to **all repositories** in the **metapercept-metr** GitHub organization.

**Organization:** [metapercept-metr](https://github.com/metapercept-metr)  
**DevOps owners:** `@naveenv-devops`, `@nilesh-sk`  
**Last updated:** June 2026

---

## Overview

Every repository in the org follows a common governance model:

| Area | Standard |
|---|---|
| **Protected branches** | `dev`, `devops-testing`, `main` (+ feature/release branches per ruleset) |
| **CODEOWNERS** | `.github/CODEOWNERS` on all existing target branches |
| **Reviews** | Minimum 2 approvals; CODEOWNER review required |
| **Signed commits** | Required on `dev` and `devops-testing` |
| **Merge method** | Squash or rebase (linear history required) |
| **Direct pushes** | Blocked on protected branches — merge via PR only |

---

## Standard branches

| Branch | Purpose | Protection level |
|---|---|---|
| `main` | Production / stable release | High (Core Governance ruleset) |
| `dev` | Active development integration | High (Secure Branch Protection) |
| `devops-testing` | DevOps / pipeline validation | High (Secure Branch Protection) |
| `develop`, `staging` | Environment promotion (where used) | Core Governance ruleset |
| `feature/**`, `release/v*` | Feature and release work | Core Governance ruleset |

> Not every repository has all three branches (`dev`, `devops-testing`, `main`). Branches are created as needed per project lifecycle.

---

## Repository categories

### Category A — Full metR application repos

Examples: `metR-Frontend`, `metR-API-Gateway`, `metR-Converter-FrameMaker`, `metR-Converter-DOCX`

- Branches: `dev`, `devops-testing`, `main`
- CODEOWNERS: **Standard** (`@nilesh-sk` + `@naveenv-devops`)
- Branch protection rulesets applied
- CI status checks on governance branches (where configured)

### Category B — Infrastructure / tooling repos

Examples: `metR-Core-Infrastructure`, `metR-Phase2-shared-pipelines`, `github-org-mcp-server`, `KUBERNETES`

- Branches: typically `main` only
- CODEOWNERS: **Standard** or **Restricted** depending on collaborator access
- DevOps-managed

### Category C — Website / admin panel repos

Examples: `blog-metapercept`, `careers-metapercept`, `portfolio-metapercept`, `*-adminpanel-metapercept`

- Branches: `main` (some may lack `dev` / `devops-testing`)
- CODEOWNERS: per-repo based on team access

### Category D — Test / demo repos

Examples: `Asish_Test_Repo`, `Kajal_Test_Repo`, `demo-repository`

- Minimal governance; `main` branch only in most cases

---

## CODEOWNERS policy

Two approved templates — see [CODEOWNERS Standard](github-codeowners.md).

| Template | Owners | When to use |
|---|---|---|
| **Standard** | `@nilesh-sk` `@naveenv-devops` | Default for all metR repos |
| **Restricted** | `@naveenv-devops` only | Repo where `@nilesh-sk` is not a collaborator |

**Rule:** Every user listed in CODEOWNERS **must have write access** to that repository. GitHub rejects invalid owner entries.

**File location:** `.github/CODEOWNERS`  
**Target branches:** `dev`, `devops-testing`, `main` (where branch exists)

---

## Roles & responsibilities

| Role | Person(s) | Responsibilities |
|---|---|---|
| **Org admin** | DevOps lead | Rulesets, bypass (emergency), org settings |
| **CODEOWNER** | `@naveenv-devops`, `@nilesh-sk` | Approve PRs; ensure governance compliance |
| **Developer** | Feature branch author | Signed commits, PR hygiene, resolve review threads |
| **Reviewer** | Any write-access member | Code review; 2nd approval when required |
| **Merger** | CODEOWNER or admin | Final merge after all rules pass |

---

## Pull request workflow (summary)

```
Developer                    Reviewers / CODEOWNER           Merger
    │                              │                          │
    ├─ Create feature branch       │                          │
    ├─ Signed commits              │                          │
    ├─ Open PR → dev               │                          │
    │                              ├─ Review code             │
    │                              ├─ CODEOWNER approve       │
    │                              ├─ 2nd approval           │
    │                              ├─ Resolve all threads     │
    ├─ Fix & push (re-approval)    │                          │
    │                              │                          ├─ Squash/rebase merge
    │                              │                          └─ Into dev
```

Full guide: [PR Merge Guide](github-pr-merge-guide.md)

---

## Branch protection rulesets

Two org-level rulesets are applied per repository. Details: [Branch Protection Rules](github-branch-protection.md).

| Ruleset | Branches | Key rules |
|---|---|---|
| **Secure Branch Protection** | `dev`, `devops-testing` | Signed commits, 2 reviews, CODEOWNER, linear history |
| **metR-Phase2-Core-Governance** | `main`, `feature/**`, `release/v*`, etc. | 2 reviews, CODEOWNER, required CI checks |

---

## Validation & compliance

Run read-only validation after any CODEOWNERS change:

```powershell
py -3 scripts/validate_codeowners_org.py
```

| Result | Meaning |
|---|---|
| `valid` | CODEOWNERS present, correct template, GitHub accepts owners |
| `invalid` | Missing file, wrong template, or owner lacks repo access |
| `skipped` | Branch does not exist in that repository |

Reports are written to `reports/codeowners-validation-latest.csv`.

---

## New repository checklist

When creating a new repository in **metapercept-metr**:

- [ ] Add `.github/CODEOWNERS` (standard or restricted template)
- [ ] Create `dev`, `devops-testing`, `main` branches as needed
- [ ] Apply **Secure Branch Protection** ruleset to `dev` / `devops-testing`
- [ ] Apply **metR-Phase2-Core-Governance** ruleset to `main` / feature branches
- [ ] Add required collaborators before listing them in CODEOWNERS
- [ ] Run `validate_codeowners_org.py` to confirm
- [ ] Document repo in team wiki / project board

---

## Related documents

- [Branch Protection Rules](github-branch-protection.md)
- [CODEOWNERS Standard](github-codeowners.md)
- [PR Merge Guide](github-pr-merge-guide.md)
- [Signed Commits Setup](github-signed-commits.md)
- [Templates](../templates/.github/)

---

*Questions? Contact `@naveenv-devops` (DevOps lead).*
