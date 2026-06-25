# Pull Request Merge Guide

Step-by-step guide for opening, reviewing, and merging pull requests in **metapercept-metr** repositories.

**Last updated:** June 2026

---

## Roles

| Role | Who | Responsibility |
|---|---|---|
| **PR author** | Developer (e.g. `vaibhavsp-spec`) | Write code, sign commits, address review feedback |
| **CODEOWNER** | `@naveenv-devops` or `@nilesh-sk` | Governance approval; required on every protected PR |
| **Reviewer** | Any team member with write access | Code quality review; provides 2nd approval |
| **Merger** | CODEOWNER or org admin | Final merge after all rules pass |

> The PR author fixes their own commits. The CODEOWNER approves and merges. An admin's SSH key does not sign another developer's commits.

---

## PR lifecycle — merging into `dev`

### Step 1 — Author prepares branch

```bash
git checkout dev
git pull origin dev
git checkout -b feature/MDP-244-description

# Make changes with SIGNED commits
git commit -S -m "MDP-244: description of change"
git push -u origin feature/MDP-244-description
```

Signed commits are **mandatory** for `dev` and `devops-testing`. See [Signed Commits Setup](github-signed-commits.md).

---

### Step 2 — Open pull request

| Field | Value |
|---|---|
| **Base branch** | `dev` |
| **Compare branch** | `feature/MDP-244-description` |
| **Reviewers** | Request `@naveenv-devops` and one other reviewer |
| **Linked issue** | Jira / GitHub issue if applicable |

---

### Step 3 — Review phase

Reviewers check:

- [ ] Code quality and correctness
- [ ] Tests pass locally / in CI
- [ ] No secrets or credentials committed
- [ ] Signed commits show **Verified** badge on GitHub

CODEOWNER checks:

- [ ] CODEOWNERS compliance
- [ ] Branch protection rules will be satisfied at merge time

---

### Step 4 — Merge requirements checklist (`dev` branch)

All items must be green before the merge button is enabled:

| # | Requirement | Rule source |
|---|---|---|
| 1 | All commits **verified signed** | `required_signatures` |
| 2 | **2 approving reviews** | `required_approving_review_count: 2` |
| 3 | At least **1 CODEOWNER** approval | `require_code_owner_review: true` |
| 4 | Approvals are **after the latest push** | `require_last_push_approval: true` |
| 5 | All review **threads resolved** | `required_review_thread_resolution: true` |
| 6 | Branch is **up to date** with `dev` | Best practice |
| 7 | Merge via **Squash** or **Rebase** | `required_linear_history` |

---

### Step 5 — Author fixes feedback

If changes are requested:

```bash
git add .
git commit -S -m "MDP-244: address review feedback"
git push
```

> **Important:** Any new push **dismisses existing approvals**. Two fresh approvals are required after every push.

---

### Step 6 — Merge

Merger (`@naveenv-devops` or admin):

1. Confirm all checklist items are green
2. Click **Squash and merge** (recommended)
3. Confirm commit message
4. Delete feature branch (optional, recommended)

---

## Example — blocked PR resolution

**Scenario:** PR #14 on `metR-Converter-FrameMaker` — 2 approvals but merge blocked.

| Blocker | Owner | Action |
|---|---|---|
| Unsigned commits | `vaibhavsp-spec` | Set up signing → squash → signed force-push |
| Approvals dismissed after push | Reviewers | 2 fresh approvals (incl. CODEOWNER) |
| Unresolved threads | Author + reviewers | Resolve all conversations |
| Merge | `@naveenv-devops` | Squash and merge into `dev` |

---

## Merging into `main` / `feature/**` branches

Governed by **metR-Phase2-Core-Governance** ruleset. Additional requirements:

| # | Requirement |
|---|---|
| 1 | 2 approving reviews (incl. CODEOWNER) |
| 2 | All 4 CI checks pass: `unit-tests-pytest`, `xslt-validation`, `dita-ot-schema-check`, `security-scan` |
| 3 | Branch up to date with base (strict policy) |
| 4 | Signed commits not required by this ruleset (but recommended) |

---

## Emergency bypass (org admin only)

Organization admins can check **"Merge without waiting for requirements to be met"** to bypass rulesets.

Use only when:

- Production incident requires immediate merge
- Policy explicitly allows bypass
- Bypass is logged and reviewed post-incident

---

## PR checklist card (copy for PR description)

```markdown
## PR Checklist
- [ ] Commits are signed and show Verified on GitHub
- [ ] Branch is up to date with base branch
- [ ] Self-reviewed code changes
- [ ] Tests pass locally
- [ ] CODEOWNER reviewer requested
- [ ] All review threads resolved
```

---

## Related documents

- [Branch Protection Rules](github-branch-protection.md)
- [CODEOWNERS Standard](github-codeowners.md)
- [Signed Commits Setup](github-signed-commits.md)
- [GitHub Org Governance](github-org-governance.md)
