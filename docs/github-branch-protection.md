# Branch Protection Rules

Branch protection rulesets applied to repositories in **metapercept-metr**.

**Example repository:** `metR-Converter-FrameMaker`  
**Last updated:** June 2026

---

## Ruleset overview

| Ruleset | ID (example) | Target branches |
|---|---|---|
| **Secure Branch Protection Ruleset** | 17217760 | `dev`, `devops-testing` |
| **metR-Phase2-Core-Governance** | 14869601 | `main`, `develop`, `staging`, `release/v*`, `feature/**`, `xslt/**`, `customer/**` |

Both rulesets are **active** and apply at the repository level. Organization admins can bypass in emergencies.

---

## Ruleset 1 — Secure Branch Protection (`dev`, `devops-testing`)

### Branch patterns

| Include | Exclude |
|---|---|
| `refs/heads/dev` | — |
| `refs/heads/devops-testing` | — |

### Rules

| Rule | Effect |
|---|---|
| **creation** | Branch cannot be created outside allowed workflow |
| **update** | Direct pushes to branch are blocked |
| **deletion** | Branch cannot be deleted |
| **required_signatures** | All commits must be **cryptographically signed and verified** |
| **required_linear_history** | No merge commits — use squash or rebase |
| **non_fast_forward** | Force-push to protected branch blocked |
| **pull_request** | All changes must go through a PR |

### Pull request parameters

| Setting | Value |
|---|---|
| Required approving reviews | **2** |
| Dismiss stale reviews on push | **Yes** |
| Require CODEOWNER review | **Yes** |
| Require approval of most recent push | **Yes** |
| Require resolved review threads | **Yes** |
| Allowed merge methods | merge, squash, rebase |

### Bypass

| Actor | Mode |
|---|---|
| Organization Admin | Always |

---

## Ruleset 2 — metR-Phase2-Core-Governance

### Branch patterns

| Include | Exclude |
|---|---|
| `refs/heads/main` | `refs/heads/dependabot/**` |
| `refs/heads/develop` | |
| `refs/heads/staging` | |
| `refs/heads/release/v*` | |
| `refs/heads/feature/**` | |
| `refs/heads/xslt/**` | |
| `refs/heads/customer/**` | |

### Rules

| Rule | Effect |
|---|---|
| **deletion** | Branch cannot be deleted |
| **non_fast_forward** | Force-push blocked |
| **required_linear_history** | Squash or rebase merge only |
| **pull_request** | All changes via PR |
| **required_status_checks** | CI must pass (see below) |

### Pull request parameters

| Setting | Value |
|---|---|
| Required approving reviews | **2** |
| Dismiss stale reviews on push | **Yes** |
| Require CODEOWNER review | **Yes** |
| Require approval of most recent push | **Yes** |
| Require resolved review threads | **No** |
| Allowed merge methods | merge, squash, rebase |

### Required status checks (strict)

All checks must pass before merge. Branch must be up to date with base branch.

| Check context | Purpose |
|---|---|
| `unit-tests-pytest` | Python unit tests |
| `xslt-validation` | XSLT transformation validation |
| `dita-ot-schema-check` | DITA Open Toolkit schema validation |
| `security-scan` | Security / dependency scan |

### Bypass

| Actor | Mode |
|---|---|
| Organization Admin | Always |

---

## Comparison matrix

| Requirement | `dev` / `devops-testing` | `main` / `feature/**` |
|---|---|---|
| Signed commits | **Required** | Not in this ruleset |
| 2 approving reviews | Yes | Yes |
| CODEOWNER review | Yes | Yes |
| Re-approve after push | Yes | Yes |
| Resolve review threads | **Yes** | No |
| Required CI checks | No | **Yes** (4 checks) |
| Linear history | Yes | Yes |
| Direct push | Blocked | Blocked |

---

## Common merge blockers

| Error message | Ruleset cause | Fix |
|---|---|---|
| Commits must have verified signatures | `required_signatures` on `dev` | Developer signs commits — see [Signed Commits](github-signed-commits.md) |
| Cannot update this protected ref | `update` rule + unmet requirements | Satisfy all PR rules first |
| Review required | < 2 approvals or missing CODEOWNER | Get 2 approvals incl. CODEOWNER |
| Changes must be made through a pull request | `update` / `pull_request` rules | Do not push directly to protected branch |
| Required status check expected | Core Governance CI checks | Fix failing CI on `main` / feature branches |
| Review threads must be resolved | `required_review_thread_resolution` on `dev` | Resolve all conversations on PR |

---

## Recommended merge method

| Target branch | Recommended method | Reason |
|---|---|---|
| `dev` | **Squash and merge** | Linear history + single signed commit |
| `devops-testing` | **Squash and merge** | Same as dev |
| `main` | **Squash and merge** | Clean history; passes linear history rule |

---

## Applying rulesets to a new repository

1. Go to **Repository → Settings → Rules → Rulesets**
2. Verify both rulesets are inherited or assigned:
   - Secure Branch Protection Ruleset
   - metR-Phase2-Core-Governance
3. Confirm branch patterns match your repo's branch naming
4. Test with a sample PR before team rollout

---

## Related documents

- [GitHub Org Governance](github-org-governance.md)
- [PR Merge Guide](github-pr-merge-guide.md)
- [Signed Commits Setup](github-signed-commits.md)
