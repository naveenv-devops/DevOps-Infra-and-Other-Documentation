# Runbook: CODEOWNERS Validation

Audit CODEOWNERS compliance across the metapercept-metr organization.

---

## When to run

- After CODEOWNERS rollout or manual changes
- Monthly compliance check
- Before enabling new branch protection rules
- After adding/removing collaborators

---

## Run validation (read-only)

```powershell
py -3 scripts/validate_codeowners_org.py
```

---

## Interpret results

| Status | Action |
|---|---|
| `valid` + `standard` | No action needed |
| `valid` + `restricted` | Expected for repos without `@nilesh-sk` access |
| `invalid` | Fix owner access or update CODEOWNERS template |
| `skipped` | Branch does not exist — no action unless branch planned |

Report: `reports/codeowners-validation-latest.csv`

---

## Fix invalid entries

| Issue | Fix |
|---|---|
| Unknown owner `@nilesh-sk` | Add collaborator OR switch to restricted template |
| Missing file | Run `add_codeowners_to_org.py` or add manually |
| Wrong template | Copy from `templates/.github/CODEOWNERS` |

---

## Related

- [CODEOWNERS standard](../../github-codeowners.md)
- [Org governance](../../github-org-governance.md)
