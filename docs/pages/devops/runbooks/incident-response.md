# Runbook: Incident Response

Respond to production incidents on the Met-R platform.

---

## Immediate actions (first 15 minutes)

1. **Acknowledge** — confirm incident in team channel
2. **Assess severity** — P1 / P2 / P3 / P4
3. **Assign incident lead** — typically DevOps on-call
4. **Check status** — API Gateway, Frontend, affected converter service
5. **Communicate** — notify stakeholders if P1/P2

---

## Investigation checklist

- [ ] Recent deployments (last 2 hours)?
- [ ] GitHub Actions failures?
- [ ] Cloud provider status page?
- [ ] Error rate spike in logs / monitoring?
- [ ] Single service or platform-wide?

---

## Common failure points

| Symptom | Likely cause | Action |
|---|---|---|
| API 502/503 | Service pod down | Restart / redeploy service |
| Conversion jobs stuck | Converter service unavailable | Check converter pod logs |
| Auth failures | API Gateway / token issue | Check gateway config |
| CI pipeline red | Test or validation failure | Fix and redeploy |

---

## Resolution

1. Apply fix or rollback (see [Rollback](rollback.md))
2. Verify health checks green
3. Monitor for 30 minutes
4. Post-incident: document root cause and preventive action

---

## Post-incident

- [ ] Update incident log
- [ ] Schedule post-mortem if P1/P2
- [ ] Create follow-up tickets

---

## Related

- [Observability](../../platform/observability.md)
- [Deployment runbook](deployment.md)
