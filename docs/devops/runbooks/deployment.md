# Runbook: Deployment

Deploy a Met-R service to a target environment.

---

## Prerequisites

- [ ] PR merged to target branch with all checks green
- [ ] CODEOWNER approval recorded
- [ ] Signed commits (if merging to `dev`)
- [ ] Deployment window approved (production only)

---

## Deploy to development (`dev`)

1. Confirm PR merged to `dev`
2. GitHub Actions deploy workflow triggers automatically
3. Monitor workflow in **Actions** tab
4. Verify service health endpoint
5. Notify team in channel if breaking change

---

## Deploy to production (`main`)

1. Confirm PR merged to `main` with all 4 CI checks green
2. Create release tag: `vX.Y.Z`
3. Monitor deploy workflow
4. Run smoke tests against production endpoints
5. Update [release notes](../../product-docs/support/release-notes.md)
6. Announce in team channel

---

## Verify deployment

| Check | Command / action |
|---|---|
| Service health | Hit `/health` endpoint |
| Logs | Check observability dashboard |
| API Gateway | Test routed endpoint |
| Frontend | Load met-r.io UI |

---

## Rollback

If deployment fails, see [Rollback runbook](rollback.md).

---

## Related

- [Environments](../environments.md)
- [CI/CD overview](../ci-cd-overview.md)
