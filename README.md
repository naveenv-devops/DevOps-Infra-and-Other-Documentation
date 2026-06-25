# DevOps Infrastructure & Met-R Documentation Hub

Central documentation for **MetaPercept DevOps** (internal governance) and **met-r.io** (product documentation).

**Organization:** [metapercept-metr](https://github.com/metapercept-metr) · **Product:** [met-r.io](https://met-r.io)  
**Last updated:** June 2026

---

## Documentation tracks

| Track | Audience | Location | Site |
|---|---|---|---|
| **Product docs** | Customers, authors, admins | [`product-docs/docs/`](product-docs/docs/README.md) | [docs.met-r.io](https://docs.met-r.io) |
| **DevOps docs** | Engineers, CI/CD, GitHub | [`docs/pages/devops/`](docs/pages/devops/README.md) | platform-docs.met-r.io |
| **Platform docs** | Architects, SRE, leads | [`docs/pages/platform/`](docs/pages/platform/README.md) | platform-docs.met-r.io |
| **Internal hub** | All engineering | [`docs/pages/`](docs/pages/README.md) | Combined index |
| **POC evaluations** | Infrastructure decisions | [`poc/`](poc/README.md) | — |

---

## Quick start — internal docs (DevOps + Platform)

```bash
pip install mkdocs-material
cd docs
mkdocs serve
# Open http://127.0.0.1:8000
```

---

## Quick start — product documentation

```bash
pip install -r product-docs/requirements.txt
cd product-docs
mkdocs serve
# Open http://127.0.0.1:8000
```

Hub page: [`product-docs/README.md`](product-docs/README.md) (structured like [GitHub Docs](https://docs.github.com/en))

---

## Repository Structure

```
cursor-documentation/
├── README.md                          ← You are here
├── product-docs/                      ← met-r.io product docs (public-facing)
│   ├── README.md                      ← Docs hub (like docs.github.com/en)
│   ├── mkdocs.yml                     ← Site config → docs.met-r.io
│   ├── get-started/                   ← Onboarding
│   ├── product/                       ← Platform, converters, AI, publishing
│   ├── guides/                        ← User how-to guides
│   ├── admin/                         ← Administration
│   ├── developers/                    ← API & integrations
│   ├── reference/                     ← Formats, glossary, FAQ
│   └── support/                       ← Troubleshooting, contact
├── docs/                              ← Internal DevOps + Platform docs
│   ├── README.md                      ← Internal docs hub
│   ├── mkdocs.yml                     ← → platform-docs.met-r.io
│   ├── devops/                        ← CI/CD, GitHub, runbooks
│   ├── platform/                      ← Architecture, services, infra
│   └── github-*.md                    ← GitHub governance (linked from devops/)
├── poc/                               ← Infrastructure POC records
├── scripts/                           ← Org automation scripts
├── templates/.github/                 ← CODEOWNERS templates
└── reports/                           ← Scan & validation reports
```

---

## Active & Completed POCs

| ID | Topic | Status | Document | Owner |
|---|---|---|---|---|
| POC-001 | Git hosting + AI coding agents (GitHub vs GitLab vs Bitbucket vs Claude vs Cursor) | **In progress** | [poc/github-gitlab-bitbucket-ai-pricing-comparison.md](poc/github-gitlab-bitbucket-ai-pricing-comparison.md) | DevOps |
| POC-002 | CI/CD platform evaluation | Planned | — | — |
| POC-003 | Infrastructure as Code (Terraform vs Pulumi vs Bicep) | Planned | — | — |
| POC-004 | Container orchestration (AKS vs EKS vs self-managed) | Planned | — | — |
| POC-005 | Observability stack (Datadog vs Grafana vs Azure Monitor) | Planned | — | — |
| POC-006 | Secrets management (Vault vs Azure Key Vault vs GitHub Secrets) | Planned | — | — |

---

## Current Infrastructure Baseline

| Layer | Current choice | Plan / tier | Monthly cost (est.) | Notes |
|---|---|---|---|---|
| **Source control** | GitHub | Team ($4/user × 15) | $60 | Primary git host |
| **AI coding assistant** | GitHub Copilot | Business ($19 × 4 licenses) | $76 | Usage-based billing from Jun 2026 |
| **CI/CD** | _TBD_ | — | — | Document in POC-002 |
| **Cloud provider** | _TBD_ | — | — | |
| **IaC** | _TBD_ | — | — | |
| **Monitoring** | _TBD_ | — | — | |
| **Secrets** | _TBD_ | — | — | |
| **Artifact registry** | _TBD_ | — | — | |

**Fixed baseline (known):** ~$136/month (GitHub Team + Copilot) + variable AI overages

---

## DevOps Infrastructure POC Domains

POCs in this repo are grouped by infrastructure domain:

| Domain | Example evaluations | Typical decision drivers |
|---|---|---|
| **Source control & collaboration** | GitHub, GitLab, Bitbucket | Cost, AI tooling, CI integration, compliance |
| **CI/CD & automation** | GitHub Actions, GitLab CI, Azure DevOps, Jenkins | Build minutes, pipeline complexity, secrets, self-hosted runners |
| **Cloud & compute** | Azure, AWS, GCP | Existing contracts, region, compliance, team skills |
| **Infrastructure as Code** | Terraform, Bicep, Pulumi, Ansible | State management, drift detection, module ecosystem |
| **Containers & orchestration** | Docker, Kubernetes, managed K8s | Scale, cost, operational overhead |
| **Monitoring & observability** | Metrics, logs, traces, alerting | SLO coverage, cost per host, retention |
| **Security & compliance** | SAST, DAST, secret scanning, IAM | Regulatory requirements, integration with git host |
| **AI / developer productivity** | Copilot, Claude Code, Cursor, Rovo Dev | Per-seat vs usage-based cost, agent quality |

---

## POC Process

Every POC in this repo follows the same lifecycle:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. Charter │ →  │  2. Baseline│ →  │  3. Trial   │ →  │  4. Score   │ →  │  5. Decision│
│  & scope    │    │  & metrics  │    │  (parallel) │    │  & compare  │    │  record     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Phase 1 — Charter (Week 0)

- Define the problem and success criteria
- List candidates (max 3–4 to keep scope manageable)
- Assign owner and trial participants
- Set budget and time box (typically 2–4 weeks)

### Phase 2 — Baseline (Week 1)

- Document current state (cost, usage, pain points)
- Export metrics from existing tools (billing, usage dashboards)
- Establish measurable KPIs (e.g., credits/user, build minutes, MTTR)

### Phase 3 — Parallel trial (Weeks 2–3)

- Run controlled trials with a small user group (2–4 people per arm)
- Use the same tasks across candidates where possible
- Capture qualitative feedback (developer survey, friction log)

### Phase 4 — Score & compare (Week 4)

- Fill the decision matrix (see [POC template](poc/README.md#poc-document-template))
- Calculate total cost of ownership (fixed + variable)
- Identify risks, migration effort, and vendor lock-in

### Phase 5 — Decision record

- **Adopt** — proceed with rollout plan
- **Defer** — revisit when triggers are met (cost threshold, feature GA, contract renewal)
- **Reject** — document why; archive POC

---

## Decision Matrix (Standard Weights)

Use these default weights unless the POC charter specifies otherwise:

| Criterion | Weight | What to measure |
|---|---|---|
| **Total cost (12-month TCO)** | 25% | Fixed seats + variable usage + migration cost |
| **Feature fit** | 25% | Does it solve the stated problem completely? |
| **Integration with existing stack** | 20% | GitHub, cloud, IdP, ticketing, monitoring |
| **Admin / security / compliance** | 15% | SSO, audit logs, RBAC, data residency |
| **Team preference & adoption risk** | 15% | Developer survey, learning curve, IDE/tooling fit |

**Scoring:** 1 (poor) → 5 (excellent) per criterion per candidate. Weighted total determines recommendation.

---

## Quick Links

### Met-R product documentation

- [Product docs hub](product-docs/README.md)
- [Prerequisites](product-docs/get-started/prerequisites.md) · [Licensing](product-docs/reference/licensing.md)
- [Introduction to Met-R](product-docs/get-started/introduction.md)

### DevOps & Platform (internal)

- [Internal docs hub](docs/README.md)
- [DevOps prerequisites](docs/devops/prerequisites.md) · [DevOps licensing](docs/devops/licensing.md)
- [Platform prerequisites](docs/platform/prerequisites.md) · [Platform licensing](docs/platform/licensing.md)
- [DevOps — CI/CD](docs/devops/ci-cd-overview.md) · [Runbooks](docs/devops/runbooks/README.md)
- [Platform — Architecture](docs/platform/architecture.md) · [Services catalog](docs/platform/services-catalog.md)
- [GitHub governance](docs/github-org-governance.md) · [Branch protection](docs/github-branch-protection.md) · [Signed commits](docs/github-signed-commits.md)
- Preview: `cd docs && mkdocs serve`

### Completed / in-progress POC documents

- [Git hosting + AI agent pricing comparison](poc/github-gitlab-bitbucket-ai-pricing-comparison.md) — GitHub vs GitLab vs Bitbucket; Copilot vs Claude vs Cursor vs Rovo Dev

### POC program

- [POC index, templates, and naming conventions](poc/README.md)

### External references

| Topic | Link |
|---|---|
| GitHub pricing | https://github.com/pricing |
| GitHub Copilot billing | https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises |
| GitLab pricing | https://about.gitlab.com/pricing/ |
| Bitbucket pricing | https://www.atlassian.com/software/bitbucket/pricing |
| Claude pricing | https://claude.com/pricing |
| Cursor Teams pricing | https://cursor.com/docs/account/teams/pricing |

---

## How to Add a New POC

1. Copy the [POC document template](poc/README.md#poc-document-template) into `poc/<topic-slug>.md`
2. Assign the next `POC-00X` ID and add a row to the [Active & Completed POCs](#active--completed-pocs) table above
3. Fill in charter, baseline, comparison tables, test plan, and decision tree
4. Run the trial; update status and scores
5. On conclusion, add a **Decision** section (Adopt / Defer / Reject) with date and approver

**Naming convention:** `poc/<domain>-<short-description>.md`  
Examples: `poc/ci-cd-github-actions-vs-gitlab.md`, `poc/monitoring-grafana-vs-datadog.md`

---

## Contributing

| Role | Responsibility |
|---|---|
| **POC owner** | Writes charter, runs trial, delivers scored recommendation |
| **DevOps lead** | Approves scope, budget, and final decision |
| **Trial participants** | Execute test tasks, submit feedback survey |
| **Finance / procurement** | Validates pricing and contract terms when applicable |

- Keep documents factual; cite official vendor pricing pages with access date
- Mark estimates clearly when vendor pricing is custom or negotiated
- Do not commit secrets, credentials, or internal account IDs

### Git commit conventions

Use concise messages that explain **why**, not just what changed.

| Change type | Prefix | Example |
|---|---|---|
| New POC document | `docs(poc):` | `docs(poc): add CI/CD platform comparison for POC-002` |
| POC hub / README | `docs:` | `docs: add DevOps infrastructure POC hub and index` |
| Update existing POC | `docs(poc):` | `docs(poc): update POC-001 Copilot credit estimates` |
| Template or process | `chore(docs):` | `chore(docs): add POC decision matrix template` |

**Format:** `<prefix> <short summary>` (imperative mood, ≤72 characters)

```
docs: add DevOps infrastructure POC hub and index

Introduce root README and poc/README with POC catalog, process,
decision matrix weights, and copy-paste template for future evaluations.
```

---

## Document Status Legend

| Status | Meaning |
|---|---|
| **Planned** | Charter not yet written |
| **In progress** | Trial running or document being drafted |
| **Review** | POC complete; awaiting DevOps lead sign-off |
| **Adopted** | Decision made; rollout in progress or complete |
| **Deferred** | Paused; revisit trigger documented |
| **Rejected** | Not proceeding; rationale recorded |

---

*Repository maintained by the DevOps team. For questions or new POC requests, contact the DevOps lead.*
