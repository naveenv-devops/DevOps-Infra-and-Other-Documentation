# POC Documentation Index

Proof of Concept documents for DevOps infrastructure evaluations. Each POC follows a standard structure so comparisons are consistent and decisions are auditable.

[← Back to repository README](../README.md)

---

## POC Catalog

| ID | Document | Domain | Status |
|---|---|---|---|
| POC-001 | [Git hosting + AI coding agents](github-gitlab-bitbucket-ai-pricing-comparison.md) | Source control · AI productivity | In progress |

---

## POC Document Template

Copy the block below when starting a new POC. Save as `poc/<domain>-<short-description>.md`.

```markdown
# POC: <Title>

**POC ID:** POC-00X  
**Prepared for:** <team / audience>  
**Date:** <YYYY-MM-DD>  
**Owner:** <name>  
**Status:** Planned | In progress | Review | Adopted | Deferred | Rejected  
**Context:** <1–2 sentences on why this POC exists>

---

## Executive Summary

| Current state | Monthly cost (est.) |
|---|---|
| <item> | $<amount> |
| **Total baseline** | **$<amount>** |

**Key finding:** <one-sentence recommendation>

---

## Problem Statement

- What pain point or decision triggered this POC?
- What happens if we do nothing?
- What is in scope / out of scope?

---

## Success Criteria

| KPI | Baseline | Target | How measured |
|---|---|---|---|
| <metric> | <value> | <value> | <dashboard / export> |

---

## Candidates

| Candidate | Tier / plan | $/user or $/month | Notes |
|---|---|---|---|
| A (current) | | | |
| B | | | |
| C | | | |

---

## Feature Comparison

| Feature | A | B | C |
|---|---|---|---|
| <feature> | | | |

---

## Cost Scenarios

| Scenario | Fixed monthly | Variable (est.) | 12-month TCO |
|---|---|---|---|
| Status quo | | | |
| Option B | | | |
| Option C | | | |

---

## POC Test Plan

### Phase 1 — Baseline (Week 1)
- [ ] Export current usage / billing data
- [ ] Document pain points from team survey
- [ ] Set budget cap for trial if applicable

### Phase 2 — Parallel trial (Weeks 2–3)

| Arm | Users | Tool | Success metrics |
|---|---|---|---|
| Control | 2 | <current> | |
| Trial B | 2 | <candidate> | |

### Phase 3 — Decision matrix (Week 4)

| Criterion | Weight | A | B | C |
|---|---|---|---|---|
| Total cost (12-month TCO) | 25% | | | |
| Feature fit | 25% | | | |
| Stack integration | 20% | | | |
| Admin / security | 15% | | | |
| Team preference | 15% | | | |
| **Weighted total** | 100% | | | |

---

## Risks & Migration Effort

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| | | | |

**Estimated migration effort:** <person-days / weeks>

---

## Decision Tree

\`\`\`
<ASCII or bullet decision flow>
\`\`\`

---

## Recommendation Summary

| Priority | Action | Expected outcome |
|---|---|---|
| 1 | | |
| 2 | | |

---

## Decision (fill on completion)

| Field | Value |
|---|---|
| **Outcome** | Adopt / Defer / Reject |
| **Date** | |
| **Approved by** | |
| **Revisit trigger** | (if Deferred) |
| **Next steps** | |

---

## References

- <official pricing / docs links with access date>

---

*Document version: 1.0*
```

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| POC ID | `POC-001`, `POC-002`, … | POC-001 |
| Filename | `<domain>-<short-description>.md` | `ci-cd-github-actions-vs-azure-devops.md` |
| Domain prefixes | `git-`, `ci-cd-`, `cloud-`, `iac-`, `k8s-`, `monitoring-`, `security-`, `ai-` | `ai-copilot-vs-claude-code.md` |

---

## Planned POC Topics

Use this backlog to prioritize future evaluations. Move to the catalog when a charter is written.

| Priority | Topic | Domain | Trigger |
|---|---|---|---|
| High | CI/CD platform (GitHub Actions vs alternatives) | CI/CD | Pipeline complexity or minute overages |
| High | Copilot usage optimization | AI productivity | Post–Jun 2026 overage spike |
| Medium | IaC tool standardization | Infrastructure as Code | Multi-tool drift |
| Medium | Observability stack | Monitoring | Alert fatigue / cost |
| Low | Secrets management consolidation | Security | Audit or rotation policy |
| Low | Self-hosted vs cloud runners | CI/CD | Build minute cost at scale |

---

## Trial Guidelines

1. **Time box:** 2–4 weeks maximum unless extended with DevOps lead approval
2. **Participants:** 2–4 users per trial arm; same role/seniority where possible
3. **Tasks:** Use identical stories or tickets across arms (e.g., same bug fix, same feature branch)
4. **Budget:** Set vendor trial limits or spend caps before starting
5. **Feedback:** Short survey at end (1–5 scale: quality, speed, friction, would use daily)
6. **No production impact:** Trials run on non-prod repos or feature branches unless explicitly approved

---

## Related Documents

- [Repository README — DevOps Infrastructure POC Hub](../README.md)
- [POC-001: Git hosting + AI agent comparison](github-gitlab-bitbucket-ai-pricing-comparison.md)
