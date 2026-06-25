# POC: Git Hosting + AI Coding Agent — Pricing & Feature Comparison

**Prepared for:** 15-user team evaluation  
**Date:** June 25, 2026  
**Context:** GitHub Team + Copilot Business usage spike after June 1, 2026 (usage-based billing rollout)

---

## Executive Summary

| Current state | Monthly base cost |
|---|---|
| GitHub Team (15 users × $4) | **$60** |
| Copilot Business (4 licenses × $19) | **$76** |
| **Total fixed baseline** | **$136/month** |

From **June 1, 2026**, GitHub moved Copilot Business to **usage-based billing** (AI credits). Completions remain unlimited, but **agentic features** (Chat, CLI, cloud agents, code review) consume pooled credits. Existing customers get a **3-month promo** (3,000 credits/user/month vs standard 1,900), then drop to 1,900. Overages cost **$0.01 per AI credit**.

**Key finding:** Staying on GitHub is still the lowest-cost *platform* option at your scale. The cost pressure is almost entirely from **AI agent consumption**, not Git hosting. Alternatives fall into three buckets:

1. **Optimize on GitHub** — budget controls, Copilot Enterprise for heavy users, or mixed licensing
2. **Add/replace AI tooling** — Claude Team Premium, Cursor Teams, Rovo Dev (works with GitHub)
3. **Migrate platform** — GitLab or Bitbucket only makes sense if you also want DevOps consolidation or Atlassian integration; both are **more expensive** for 15 users at base tier

---

## What Changed on GitHub (June 1, 2026)

| Item | Before | After (June 2026) |
|---|---|---|
| Copilot Business seat price | $19/user/month | **Unchanged** — $19/user/month |
| Billing model | Mostly flat per-seat | **Usage-based** for agentic AI features |
| Included credits (standard) | N/A | **1,900 AI credits/user/month** (pooled org-wide) |
| Promo credits (Jun–Aug 2026) | N/A | **3,000 AI credits/user/month** |
| Overages | N/A | **$0.01/credit** ($10 = 1,000 credits) |
| Unlimited features | Completions | **Still unlimited:** code completions + next-edit suggestions |
| Metered features | — | Chat, CLI, cloud agent, Spaces, Spark, third-party agents, code review |

**Your 4-license pool (promo period):** 4 × 3,000 = **12,000 credits/month** (~$120 value)  
**After promo:** 4 × 1,900 = **7,600 credits/month** (~$76 value)

> Heavy agent users (multi-file edits, cloud agents, PR review bots) routinely exceed included credits. GitHub explicitly recommends budgeting for overages or upgrading heavy users to Copilot Enterprise ($39/seat, 3,900 credits standard / 7,000 promo).

**References:**  
- [GitHub Copilot usage-based billing](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)  
- [GitHub blog: Copilot moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

---

## Current Baseline Cost Model (15 Users)

### Scenario A — Status quo (your setup)

| Line item | Calculation | Monthly |
|---|---|---|
| GitHub Team | 15 × $4 | $60 |
| Copilot Business | 4 × $19 | $76 |
| **Subtotal (fixed)** | | **$136** |
| AI overages (variable) | Depends on agent usage | $0 – $500+ |

**Annual fixed:** ~$1,632 + overages

### Scenario B — Copilot for all 15 devs

| Line item | Calculation | Monthly |
|---|---|---|
| GitHub Team | 15 × $4 | $60 |
| Copilot Business | 15 × $19 | $285 |
| Included credits (post-promo) | 15 × 1,900 pooled | 28,500 credits (~$285 value) |
| **Subtotal (fixed)** | | **$345** |

---

## Platform Comparison: GitHub vs GitLab vs Bitbucket

*Based on [Marker.io comparison](https://marker.io/blog/github-vs-gitlab-vs-bitbucket) and official pricing pages (June 2026).*

### Git hosting — 15 users

| Feature | GitHub Team | GitLab Premium | Bitbucket Standard | Bitbucket Premium |
|---|---|---|---|---|
| **Price/user/month** | $4 | $29 | $3.65 | $7.25 |
| **15-user monthly** | **$60** | **$435** | **$54.75** | **$108.75** |
| **15-user annual** | ~$720 | ~$5,220 | ~$657 | ~$1,305 |
| CI/CD | GitHub Actions (2,000 min/mo Team) | 10,000 compute min/mo | Pipelines (50 min free tier) | Same + merge checks |
| DevSecOps depth | Good (GHAS add-on) | **Best** (built-in scanning) | Moderate | Moderate + compliance |
| Ecosystem | Largest OSS community | All-in-one DevOps | **Best if using Jira/Confluence** |
| Self-hosted option | Enterprise Server | Self-Managed | Data Center (legacy) |

### Platform feature matrix

| Capability | GitHub | GitLab | Bitbucket |
|---|---|---|---|
| Code repository | ✅ | ✅ | ✅ |
| Pull/Merge requests | ✅ | ✅ | ✅ |
| Issue tracking | ✅ GitHub Issues | ✅ | ✅ (+ Jira native) |
| CI/CD | ✅ Actions | ✅ Built-in | ✅ Pipelines |
| Container registry | ✅ | ✅ | ❌ |
| Security scanning | ✅ (Advanced Security add-on) | ✅ Built-in (Ultimate) | ✅ Limited |
| Social / OSS community | ✅ **Largest** | ✅ Medium | ❌ Smaller |
| AI in platform (base) | Copilot (paid add-on) | Duo Core included (limited) | AI PR descriptions (Premium) |

**Verdict for 15-user team:**  
- **Cheapest hosting:** Bitbucket Standard ($54.75) ≈ GitHub Team ($60)  
- **Most expensive hosting:** GitLab Premium ($435) — 7× GitHub Team  
- **Migration cost** (repos, CI, integrations, retraining) typically outweighs hosting savings unless you have a strategic DevOps or Atlassian driver

---

## AI Coding Agent Comparison

### Pricing overview (per developer/month)

| Product | Seat price | Included usage | Overage | Best for |
|---|---|---|---|---|
| **GitHub Copilot Business** | $19 | 1,900 credits (~$19); promo 3,000 | $0.01/credit | Teams already on GitHub; IDE-integrated |
| **GitHub Copilot Enterprise** | $39 | 3,900 credits (~$39); promo 7,000 | $0.01/credit | Heavy agent users on GHE Cloud |
| **GitLab Duo Pro** | $19 (add-on) | Unlimited suggestions + chat (seat-based) | N/A for classic Duo | GitLab Premium/Ultimate shops |
| **GitLab Duo Agent Platform** | No per-AI seat | $12/user promo credits (Premium) | $1/credit on-demand | Agentic flows inside GitLab |
| **Bitbucket AI (built-in)** | Included in Premium | PR descriptions, comment assist | N/A | Light generative AI only |
| **Atlassian Rovo Dev** | $20 | 2,000 credits/dev | $0.01/credit | Agentic AI; works with **GitHub or Bitbucket** |
| **Claude Team Standard** | $20 (min 5 seats) | Bundled usage allowance | API rates beyond cap | Claude Code terminal/IDE agent |
| **Claude Team Premium** | $100 | Higher bundled allowance | API rates beyond cap | Power users, Claude-native workflows |
| **Cursor Teams Standard** | $40 ($32 annual) | Composer + third-party pools | Public API + token rate | Full IDE replacement, multi-model |
| **Cursor Teams Premium** | $120 ($96 annual) | 5× Standard pools | Public API + token rate | All-day agent users |

### AI feature depth

| Feature | Copilot Business | GitLab Duo Agent | Rovo Dev | Claude Code | Cursor Teams |
|---|---|---|---|---|---|
| Inline completions | ✅ Unlimited | ✅ (Core: 2K req/mo) | ❌ | ✅ via IDE plugins | ✅ Tab |
| Chat / agent mode | ✅ Metered | ✅ Metered (credits) | ✅ | ✅ **Core strength** | ✅ **Core strength** |
| Cloud / background agents | ✅ Metered | ✅ Flows (MR, CI fix) | ✅ | ✅ | ✅ |
| PR / code review AI | ✅ Metered | ✅ $0.25/review or credits | ✅ | ✅ | Limited |
| CLI agent | ✅ Copilot CLI | ❌ | ✅ Terminal | ✅ **Native** | ✅ |
| Model choice | Multi-model catalog | Claude, GPT, etc. | Atlassian models | **Anthropic only** | Claude, GPT, Gemini, Composer |
| Works with GitHub repos | ✅ Native | ❌ (GitLab only) | ✅ | ✅ | ✅ |
| SSO / enterprise admin | Business: basic | Premium+ | Atlassian admin | Team: Google/MS; Enterprise: SAML | SAML/OIDC on Teams |
| Pooled org usage | ✅ Credits pooled | ✅ Credits pooled | Per-dev credits | Team: per-seat; Enterprise: pooled | Per-seat pools (Enterprise: pooled) |

---

## Total Cost Scenarios (15 Users)

*Assumes all 15 developers need AI tooling. Adjust if only a subset does.*

| Scenario | Platform | AI layer | Fixed monthly | Notes |
|---|---|---|---|---|
| **Current** | GitHub Team $60 | Copilot ×4 $76 | **$136** | + overages for 4 power users |
| **GitHub + Copilot all** | $60 | 15 × $19 = $285 | **$345** | 28,500 pooled credits post-promo |
| **GitHub + Copilot Enterprise (4 heavy)** | $60 | 4×$39 + 11×$19 = $365 | **$425** | More credits for power users |
| **GitHub + Rovo Dev all** | $60 | 15 × $20 = $300 | **$360** | Keep GitHub; swap/add AI agent |
| **GitHub + Claude Team Standard all** | $60 | 15 × $20 = $300 | **$360** | Strong terminal agent; separate from IDE |
| **GitHub + Claude Team Premium (4 heavy)** | $60 | 4×$100 + 11×$20 = $620 | **$680** | Premium for power users only |
| **GitHub + Cursor Standard all** | $60 | 15 × $40 = $600 | **$660** | Full IDE; highest IDE-native agent UX |
| **Bitbucket Premium + Rovo Dev** | $108.75 | $300 | **$408.75** | Only if Jira-centric |
| **GitLab Premium + Duo Agent** | $435 | Promo credits included ($180 value) | **$435** + overages | 7× platform cost vs GitHub |
| **GitLab Premium + Duo Pro all** | $435 | 15 × $19 = $285 | **$720** | Full AI seat licensing |

### Variable / overage sensitivity

| If monthly overage is… | Added to current ($136) | Added to all-Copilot ($345) |
|---|---|---|
| $50 | $186 | $395 |
| $150 | $286 | $495 |
| $300 | $436 | $645 |

---

## Alternative Plan Recommendations

### Option 1 — Stay on GitHub, optimize Copilot (lowest disruption) ⭐ Recommended first step

**Actions:**
1. Enable **budget controls** per user in GitHub org settings
2. Identify the 4 Copilot users' consumption in **Copilot usage dashboard**
3. For users exceeding ~3,000 credits/month consistently → upgrade to **Copilot Enterprise** ($39) or set a **$20–50/user overage cap**
4. Keep completions-only users off Copilot licenses (completions are not useful without a license anyway, but casual Chat users can use fewer licenses)

**Pros:** No migration; best ecosystem; cheapest platform  
**Cons:** Ongoing variable billing for agent-heavy workflows  
**Est. cost:** $136–$425/month depending on license mix + overages

---

### Option 2 — GitHub + Rovo Dev for agent workloads

Use **GitHub Team** for repos + **Rovo Dev** ($20/user) for planning, generation, terminal, and code review.

| | Copilot Business | Rovo Dev Standard |
|---|---|---|
| Price | $19/user | $20/user |
| Credits | 1,900/user (pooled) | 2,000/user |
| Overage | $0.01/credit | $0.01/credit |
| GitHub native | ✅ | ✅ (supports GitHub + Bitbucket) |

**Pros:** Comparable pricing; works with existing GitHub; strong Atlassian agent if you use Jira  
**Cons:** Two vendors; feature overlap with Copilot; team learns new tool  
**POC scope:** 2-week trial with 2 developers on Rovo Dev vs 2 on Copilot; compare credits consumed per story point

---

### Option 3 — Claude Team (Standard / Premium mix)

| Tier | Price | When to use |
|---|---|---|
| Team Standard | $20/seat | Developers using Claude Code in terminal/VS Code for agent tasks |
| Team Premium | $100/seat | 3–5 heaviest agent users needing 5× usage headroom |

**Example mix (15 users):** 4 Premium + 11 Standard = $400 + $60 GitHub = **$460/month**

**Pros:** Best-in-class reasoning agent (Claude Code); predictable seat tiers; includes Claude Code on every seat  
**Cons:** Does not replace GitHub; no native PR integration like Copilot; Team plan lacks full SAML/audit (Enterprise required); usage beyond allowance bills at API rates  
**POC scope:** 5-seat minimum already met; run Claude Code on 3 repos for 2 sprints

---

### Option 4 — Cursor Teams (IDE replacement)

| Seat | Price | Profile |
|---|---|---|
| Standard | $40/mo ($32 annual) | Moderate agent usage |
| Premium | $120/mo ($96 annual) | All-day agent users (5× usage) |

**Example:** 15 Standard = $600 + $60 GitHub = **$660/month**

**Pros:** Unified IDE + agent; multi-model; strong for greenfield and refactors  
**Cons:** Highest per-seat cost; developers must switch IDE; usage pools are per-seat (not pooled on Teams)  
**POC scope:** 30-day trial with 3 devs on Standard, 1 on Premium

---

### Option 5 — Migrate to GitLab Premium

**Cost:** $435/month base (no GitHub) + GitLab Credits for agent overages

**Pros:** Single platform for repo + CI + security + AI agents; Duo Agent Platform promo credits ($12/user)  
**Cons:** **7× hosting cost**; migration effort; loses GitHub Actions marketplace and community; AI credit model ($1/credit) is expensive on-demand  
**When it makes sense:** You want to consolidate DevSecOps and are already considering leaving GitHub for operational reasons—not purely for AI cost savings

---

### Option 6 — Migrate to Bitbucket Premium

**Cost:** $108.75/month + optional Rovo Dev ($300) = **$408.75**

**Pros:** Cheaper than GitLab; excellent Jira/Confluence integration; built-in AI for PRs on Premium  
**Cons:** Smaller ecosystem; agentic AI requires separate Rovo Dev purchase; migration cost  
**When it makes sense:** Already on Atlassian stack (Jira, Confluence, JSM)

---

## Feature Comparison — Agentic / Code Agent Capabilities

| Capability | GitHub Copilot | GitLab Duo Agent | Rovo Dev | Claude Code | Cursor |
|---|---|---|---|---|---|
| **Autonomous multi-file edits** | ✅ Agent mode | ✅ Developer Flow | ✅ | ✅ | ✅ Composer |
| **Issue → PR automation** | ✅ Cloud agent | ✅ Developer Flow | ✅ | ✅ | Partial |
| **CI/CD failure auto-fix** | Limited | ✅ Fix CI/CD Flow | ✅ | ✅ | Limited |
| **Automated code review** | ✅ Metered | ✅ $0.25/review | ✅ | ✅ | Limited |
| **Custom team agents** | ✅ Copilot Spaces | ✅ Custom agents | ✅ | ✅ MCP | ✅ Rules |
| **Background async agents** | ✅ Copilot coding agent | ✅ External agents | ✅ | ✅ | ✅ |
| **Third-party tool integration** | MCP support | ✅ External agents | Atlassian ecosystem | ✅ MCP | ✅ MCP |
| **Works in JetBrains** | ✅ Plugin | ✅ | ❌ | ✅ Plugin | ❌ (VS Code fork) |
| **Works in Visual Studio** | ✅ Native | ❌ | ❌ | Plugin | ❌ |
| **Data residency / compliance** | Enterprise + GHAS | Dedicated / Self-Managed | Atlassian Cloud | Enterprise | Enterprise |

---

## POC Test Plan (4-Week)

### Phase 1 — Baseline measurement (Week 1)

- [ ] Export GitHub Copilot usage report (credits per user, feature breakdown)
- [ ] Document which features drive consumption: Chat vs Agent vs CLI vs Code Review
- [ ] Calculate actual $ overage for June (promo period)
- [ ] Project September cost at 1,900 credits/user (post-promo)

### Phase 2 — Parallel trials (Weeks 2–3)

| Trial arm | Users | Tool | Success metrics |
|---|---|---|---|
| A (control) | 2 | Copilot Business + budget cap $30 | Credits used, PRs merged, dev satisfaction |
| B | 2 | Rovo Dev Standard | Same metrics + GitHub integration friction |
| C | 2 | Claude Team Standard (Claude Code) | Terminal agent tasks, multi-file refactor time |
| D (optional) | 1 | Cursor Teams Standard | IDE switch tolerance, agent task completion |

### Phase 3 — Decision matrix (Week 4)

| Criterion | Weight | Copilot | Rovo Dev | Claude | Cursor |
|---|---|---|---|---|---|
| Monthly cost (15 users) | 25% | | | | |
| Agent quality / task completion | 25% | | | | |
| GitHub integration | 20% | | | | |
| Admin / SSO / compliance | 15% | | | | |
| Developer preference (survey) | 15% | | | | |

**Scoring:** 1–5 per criterion; weighted total → recommendation

---

## Decision Tree

```
Are you primarily trying to reduce AI overage costs?
├── YES → Optimize Copilot budgets first
│         ├── Heavy users >3K credits/mo? → Copilot Enterprise for those users
│         ├── Still over budget? → Trial Rovo Dev or Claude Team for agent tasks
│         └── Keep GitHub Team (cheapest platform)
│
└── NO — strategic platform change?
    ├── Need Jira/Confluence native? → Bitbucket Premium + Rovo Dev
    ├── Need all-in-one DevSecOps? → GitLab Premium + Duo Agent Platform
    └── Need best agent IDE experience? → GitHub + Cursor Teams
```

---

## Quick Reference — Official Pricing Links

| Vendor | Pricing page |
|---|---|
| GitHub | https://github.com/pricing |
| GitHub Copilot billing | https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises |
| GitLab | https://about.gitlab.com/pricing/ |
| GitLab Credits | https://docs.gitlab.com/subscriptions/gitlab_credits/ |
| Bitbucket | https://www.atlassian.com/software/bitbucket/pricing |
| Rovo Dev | https://www.atlassian.com/software/rovo-dev/pricing |
| Claude | https://claude.com/pricing |
| Cursor Teams | https://cursor.com/docs/account/teams/pricing |

---

## Recommendation Summary

| Priority | Action | Expected outcome |
|---|---|---|
| **1 (immediate)** | Configure Copilot user budgets + usage alerts | Stop surprise overages |
| **2 (30 days)** | Profile 4 Copilot users; upgrade 1–2 to Enterprise if >5K credits/mo | Better credit pool for power users |
| **3 (POC)** | 2-week Rovo Dev or Claude Team trial on 2 devs | Validate if alternate agent is cheaper per task |
| **4 (avoid unless strategic)** | GitLab migration for cost reasons alone | Likely **increases** total cost 3–5× |
| **5 (consider)** | Cursor for 2–3 agent-heavy devs only | Targeted spend vs all-seat rollout |

**Bottom line:** Your June consumption increase is an industry-wide shift to usage-based AI billing, not a GitHub Team plan problem. At 15 users, **GitHub Team ($60) remains the best-value host**. Focus the POC on **which AI agent layer** delivers the best credits-per-delivered-feature ratio—not on replacing GitHub unless you have separate DevOps or Atlassian drivers.

---

*Document version: 1.0 | Sources verified June 2026. Pricing subject to vendor changes; confirm with sales for enterprise quotes.*
