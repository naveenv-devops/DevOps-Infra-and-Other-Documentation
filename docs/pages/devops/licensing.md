# DevOps & Engineering Tool Licensing

Licenses for development tooling used by the MetaPercept engineering team and `metapercept-metr` GitHub organization.

**Last updated:** June 2026

---

## Current license inventory

| Tool | Plan | Seats | Cost (monthly) | Owner |
|---|---|---|---|---|
| **GitHub Team** | Team | 15 users | $60 ($4/user) | DevOps |
| **GitHub Copilot** | Business | 4 licenses | $76 ($19/user) | DevOps |
| **Met-R platform** | Enterprise (internal) | — | Internal | Platform |
| **Cursor IDE** | Teams (if adopted) | TBD | TBD | DevOps |
| **Cloud (Azure/AWS)** | Pay-as-you-go | — | Variable | DevOps |

**Fixed tooling baseline:** ~$136/month (GitHub Team + Copilot) + variable AI overages

---

## GitHub Team

| Item | Detail |
|---|---|
| **Plan** | GitHub Team |
| **Organization** | `metapercept-metr` |
| **Users** | 15 |
| **Cost** | $4/user/month = **$60/month** |
| **Includes** | Private repos, GitHub Actions (2,000 min/month), branch protection, CODEOWNERS |
| **Billing** | [github.com/pricing](https://github.com/pricing) |

### Entitlements used

- 52 repositories
- Organization rulesets (branch protection)
- GitHub Actions CI/CD
- CODEOWNERS across all repos

---

## GitHub Copilot Business

| Item | Detail |
|---|---|
| **Plan** | Copilot Business |
| **Licenses** | 4 (assigned to power users) |
| **Cost** | $19/user/month = **$76/month** |
| **Billing model** | Per-seat + usage-based AI credits (from Jun 2026) |

### Included AI credits

| Period | Credits per license | Pooled (4 licenses) |
|---|---|---|
| Standard | 1,900/month (~$19) | 7,600/month |
| Promo (Jun–Aug 2026) | 3,000/month (~$30) | 12,000/month |
| Overage | $0.01/credit | Budget controls per user |

### Unlimited (no credits)

- Code completions
- Next-edit suggestions

### Metered (consumes credits)

- Copilot Chat, Agent mode, CLI, cloud agents, code review

Evaluation reference: [POC-001 Copilot comparison](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/poc/github-gitlab-bitbucket-ai-pricing-comparison.md)

---

## AI tooling alternatives (under evaluation)

| Tool | Plan | Cost/user | Status |
|---|---|---|---|
| Claude Team Standard | $20/seat | Under POC | |
| Cursor Teams Standard | $40/seat | Under POC | |
| Rovo Dev | $20/seat | Under POC | |
| Copilot Enterprise | $39/seat | For heavy users | |

---

## CI/CD & cloud

| Service | Licensing | Notes |
|---|---|---|
| **GitHub Actions** | Included in Team (2,000 min) | Overage: $0.008/min |
| **Azure / AWS** | Enterprise agreement or PAYG | Per environment |
| **Container registry** | Cloud-native | Per storage/transfer |
| **Kubernetes** | Open source (CNCF) | No license fee |

---

## Open source (no license cost)

| Component | License | Used in |
|---|---|---|
| DITA Open Toolkit | Apache 2.0 | Converter services |
| Python | PSF | All Python services |
| MkDocs Material | MIT | Documentation sites |
| pytest | MIT | Testing |

---

## Third-party commercial (platform dependencies)

| Software | License type | Who pays | Notes |
|---|---|---|---|
| DITA-OT | Apache 2.0 (free) | — | Bundled server-side |
| Adobe FrameMaker | Commercial | Customer | Source authoring only |
| Security scanning tools | Per CI vendor | MetaPercept | `security-scan` check |

---

## License compliance rules

| Rule | Action |
|---|---|
| Copilot seats | Assign only to active users; remove on offboarding |
| GitHub seats | Remove departed employees within 24 hours |
| No shared accounts | One GitHub account per person |
| No secrets in repos | Use GitHub Secrets / Key Vault |
| Annual review | DevOps audits seat count quarterly |

---

## Requesting new licenses

1. Submit request to `@naveenv-devops` with justification
2. For AI tools: reference POC evaluation criteria
3. DevOps lead approves and provisions
4. Document in this file on approval

---

## Related

- [DevOps prerequisites](prerequisites.md)
- [POC-001 AI pricing comparison](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/poc/github-gitlab-bitbucket-ai-pricing-comparison.md)
- [Product licensing](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/reference/licensing.md)
