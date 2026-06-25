# Runbook: Rollback

Revert a failed deployment on the Met-R platform.

---

## When to rollback

- P1/P2 incident caused by recent deployment
- Smoke tests fail after production deploy
- Customer-reported regression tied to release

---

## Rollback steps

### Option A — Redeploy previous tag

1. Identify last known good tag: `git tag --sort=-version:refname`
2. Trigger deploy workflow with previous tag via `workflow_dispatch`
3. Verify health checks
4. Notify team

### Option B — Revert merge commit on `main`

```bash
git checkout main
git pull origin main
git revert -m 1 <merge-commit-sha>
git push origin main
```

5. CI runs on revert PR — ensure all checks pass
6. Merge revert PR
7. Verify production

### Option C — Hotfix branch

For targeted fix without full revert:

```bash
git checkout -b hotfix/MDP-XXX-fix main
# Apply minimal fix
git commit -S -m "hotfix: description"
# PR to main with expedited review
```

---

## Post-rollback

- [ ] Confirm incident resolved
- [ ] Document root cause
- [ ] Fix forward on `dev` before next release

---

## Related

- [Deployment runbook](deployment.md)
- [Incident response](incident-response.md)
