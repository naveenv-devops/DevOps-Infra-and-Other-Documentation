# CODEOWNERS Standard

How CODEOWNERS files are managed across all **metapercept-metr** repositories.

**Last updated:** June 2026

---

## Purpose

The CODEOWNERS file automatically requests reviews from designated owners when a pull request changes files they own. Combined with branch protection (`require_code_owner_review: true`), at least one CODEOWNER approval is mandatory before merge.

---

## File location

```
.github/CODEOWNERS
```

Must exist on each protected branch: `dev`, `devops-testing`, `main` (where the branch exists).

---

## Approved templates

### Standard (default)

Use for all metR repos where both owners have **write access**.

**File:** `templates/.github/CODEOWNERS`

```text
# This is a basic CODEOWNERS file.
# See https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners for details on how to specify code owners.

*  @nilesh-sk @naveenv-devops
```

| Owner | GitHub handle | Role |
|---|---|---|
| Nilesh | `@nilesh-sk` | Technical lead / CODEOWNER |
| Naveen | `@naveenv-devops` | DevOps lead / CODEOWNER |

The `*` pattern means both owners review **all files** in the repository.

---

### Restricted

Use when `@nilesh-sk` does **not** have collaborator write access on that repo.

**File:** `templates/.github/CODEOWNERS.restricted`

```text
# This is a basic CODEOWNERS file.
# See https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners for details on how to specify code owners.

*  @naveenv-devops
```

---

## Validation rules

GitHub enforces these rules — our validation script checks them too.

| Rule | Description |
|---|---|
| **Write access required** | Every `@user` in CODEOWNERS must be a collaborator with write access |
| **Valid syntax** | File must parse without errors (GitHub API: `codeowners/errors`) |
| **Template match** | Content must match standard or restricted template exactly |
| **Correct path** | File must be at `.github/CODEOWNERS` |

### Run validation (read-only)

```powershell
py -3 scripts/validate_codeowners_org.py
```

| Status | Meaning |
|---|---|
| `valid` + `standard` | Both owners, GitHub accepts |
| `valid` + `restricted` | DevOps only, GitHub accepts |
| `invalid` | Fix before relying on CODEOWNER reviews |
| `skipped` | Branch does not exist |

---

## Repositories using restricted template

Use restricted template when `@nilesh-sk` is intentionally not a collaborator:

| Repository | Reason |
|---|---|
| KUBERNETES | DevOps-only access |
| oxygen-web-author | DevOps-only access |
| _(others as decided by DevOps)_ | No write access for `@nilesh-sk` |

> If you add `@nilesh-sk` as a collaborator later, upgrade to the **standard** template.

---

## How CODEOWNERS interacts with PR reviews

```
PR opened → dev branch
    │
    ├─ GitHub reads .github/CODEOWNERS on base branch (dev)
    ├─ Requests review from @nilesh-sk and @naveenv-devops
    │
    ├─ Branch protection requires:
    │     • 2 approving reviews total
    │     • At least 1 from a CODEOWNER
    │
    └─ Merge allowed when both conditions met (+ other rules)
```

---

## Adding CODEOWNERS to a new branch or repo

### Manual (single repo)

1. Create `.github/CODEOWNERS` with the correct template
2. Commit to `dev`, `devops-testing`, and/or `main`
3. Run validation script

### Bulk rollout (org-wide)

```powershell
py -3 scripts/add_codeowners_to_org.py
```

> Write operation — requires `gh` CLI authenticated with `repo` scope.

---

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| `Unknown owner: @nilesh-sk` | User not a collaborator | Add collaborator OR use restricted template |
| CODEOWNER review not requested | File missing on base branch | Add `.github/CODEOWNERS` to target branch |
| Approval doesn't count as CODEOWNER | Approver not in CODEOWNERS file | Only listed owners count |
| `content does not match template` | Extra whitespace or different owners | Copy exact content from `templates/` |

---

## Related documents

- [GitHub Org Governance](github-org-governance.md)
- [Branch Protection Rules](github-branch-protection.md)
- [PR Merge Guide](github-pr-merge-guide.md)
