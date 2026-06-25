# Observability

Monitoring, logging, and alerting for the Met-R platform.

---

## Observability pillars

| Pillar | Purpose | Tools (TBD) |
|---|---|---|
| **Metrics** | Service health, latency, throughput | Azure Monitor / Grafana |
| **Logs** | Request traces, conversion job logs | Centralized log aggregation |
| **Traces** | Distributed request tracing | OpenTelemetry |
| **Alerts** | Incident detection | Pager / Teams notification |

> Tooling selection documented in POC-005 (Observability stack evaluation).

---

## Key metrics

| Metric | Service | Alert threshold |
|---|---|---|
| API latency p95 | API Gateway | > 2s |
| Error rate | All services | > 1% over 5 min |
| Conversion job queue depth | Converters | > 100 pending |
| Conversion job failure rate | Converters | > 5% over 15 min |
| Pod restarts | Kubernetes | > 3 in 10 min |

---

## Health checks

| Service | Endpoint | Expected |
|---|---|---|
| API Gateway | `/health` | 200 OK |
| Converters | `/health` | 200 OK |
| Frontend | `/` | 200 OK |

---

## Log retention

| Log type | Retention | Access |
|---|---|---|
| Application logs | 90 days | DevOps, on-call |
| Audit logs | 1 year | Admin only |
| CI/CD logs | 90 days (GitHub) | Engineering |

---

## On-call escalation

| Level | Contact | When |
|---|---|---|
| L1 | DevOps on-call | Alert fires |
| L2 | `@naveenv-devops` | L1 cannot resolve in 30 min |
| L3 | `@nilesh-sk` | Platform architecture issue |

---

## Related

- [Incident response runbook](../devops/runbooks/incident-response.md)
- [Infrastructure](infrastructure.md)
