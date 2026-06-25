# Maintainers Guide

This folder documents automation and generated artifacts — **not for end-users**.

---

## Scripts

| Script | Purpose | Mode |
|---|---|---|
| `scripts/validate_codeowners_org.py` | Validate CODEOWNERS across GitHub org | Read-only |
| `scripts/add_codeowners_to_org.py` | Roll out CODEOWNERS to org repos | Write |
| `scripts/generate_org_scan_xlsx.py` | Generate org scan spreadsheet | Read-only |

Requires `gh` CLI authenticated with `repo` and `read:org` scopes.

---

## Reports

Generated output in `reports/` — safe to regenerate. Not published to GitHub Pages.

| File | Description |
|---|---|
| `codeowners-validation-latest.csv` | Latest CODEOWNERS validation |
| `codeowners-rollout.csv` | Rollout log |
| `github-org-scan.xlsx` | Org branch/CODEOWNERS scan |

---

## Templates

| File | Use |
|---|---|
| `templates/.github/CODEOWNERS` | Standard CODEOWNERS |
| `templates/.github/CODEOWNERS.restricted` | Single-owner variant |

---

## Who maintains this

MetaPercept DevOps team. See [engineering docs](../docs/pages/README.md).
