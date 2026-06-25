# Licensing

Met-R subscription plans, entitlements, and third-party license requirements.

---

## Met-R product plans

| Feature | **Starter** | **Professional** | **Enterprise** |
|---|---|---|---|
| **Users** | Up to 5 | Up to 25 | Unlimited |
| **Workspaces** | 1 | 3 | Unlimited |
| **Converters** | Core (HTML, MD, DOCX) | All converters | All + custom |
| **Output channels** | PDF, HTML5 | + CMS, XML/JSON AI | + Infinity DocSite, custom |
| **AI features** | — | Determinacy Engine | Full AI agent suite |
| **API access** | — | Standard API | Full API + webhooks |
| **SSO / SAML** | — | — | Included |
| **Dedicated instance** | — | — | Optional |
| **Support** | Email (P4) | Email (P3) | Priority + SLA |
| **Billing** | Monthly | Annual | Custom contract |

!!! note "Pricing"
    Contact [MetaPercept sales](https://metapercept.com) or your account manager for current pricing. Plans and limits are subject to change.

---

## What is included in every plan

| Included | Description |
|---|---|
| Platform hosting | SaaS at met-r.io (unless dedicated) |
| TLS encryption | In transit for all traffic |
| DITA-OT processing | Server-side — no separate DITA-OT license needed |
| XSLT transforms | Platform XSLT library usage |
| Workspace isolation | Data separated per workspace |
| Standard CI validation | Schema and XSLT checks on conversions |
| Platform updates | Security patches and feature releases |

---

## Usage limits (typical)

| Resource | Starter | Professional | Enterprise |
|---|---|---|---|
| Conversion jobs / month | 500 | 5,000 | Custom |
| Storage | 10 GB | 100 GB | Custom |
| API requests / min | — | 60 | Custom |
| Infinity DocSite sites | — | 1 | Unlimited |
| Concurrent conversion jobs | 2 | 10 | Custom |

Overage billing or upgrade required when limits are exceeded. Admins receive usage alerts at 80% and 100%.

---

## User license types

| License | Assigned to | Counted as |
|---|---|---|
| **Viewer** | Read-only users | 1 seat |
| **Author** | Content creators | 1 seat |
| **Reviewer** | Approvers | 1 seat |
| **Admin** | Client / Server Admin | 1 seat |

A user with multiple roles counts as **one seat**.

---

## Third-party licenses (customer responsibility)

Met-R does not include licenses for third-party authoring tools. Customers must maintain:

| Software | License owner | Required for |
|---|---|---|
| Adobe FrameMaker | Customer | FM source file authoring |
| Microsoft Word / 365 | Customer | DOCX authoring |
| Oxygen XML Author | Customer (optional) | Advanced DITA editing offline |
| Sitecore | Customer | CMS source content |
| Atlassian (Jira/Confluence) | Customer (optional) | Integration only |

**Included in Met-R subscription** (no separate customer license):

- DITA Open Toolkit (server-side)
- Platform XSLT library
- PDF generation engine (server-side)
- AI model usage (within plan limits)

---

## AI usage licensing

| Plan | AI entitlement |
|---|---|
| Starter | Not included |
| Professional | Determinacy Engine; limited agent calls/month |
| Enterprise | Full Master AI Agent; custom usage pool |

AI usage beyond plan limits is billed per consumption unit or requires plan upgrade. See your workspace admin for current quotas.

---

## Enterprise add-ons

| Add-on | Description |
|---|---|
| Dedicated instance | Single-tenant cloud deployment |
| Private cloud / on-prem | Customer-managed Kubernetes |
| Custom converter | Bespoke format support |
| Premium SLA | 99.9% uptime, 1-hour P1 response |
| HIPAA / compliance package | BAA, enhanced audit, data residency |
| Training & onboarding | Admin and author training sessions |

---

## License compliance

| Rule | Detail |
|---|---|
| Seat count | Must not exceed subscribed user limit |
| Workspace count | Per plan tier |
| Sharing credentials | Prohibited — one account per person |
| API keys | Scoped to workspace; not transferable |
| Audit | MetaPercept may audit usage for compliance |

Violations may result in service suspension. Contact your account manager to upgrade.

---

## Open source components

Met-R platform services use open source software. Key components:

| Component | License | Usage |
|---|---|---|
| DITA Open Toolkit | Apache 2.0 | DITA processing |
| Python runtime | PSF | Converter services |
| Various JS/TS libs | MIT / Apache | Frontend |

A full SBOM (Software Bill of Materials) is available for Enterprise customers on request.

---

## Engineering tooling (internal)

MetaPercept engineering team tooling is documented in the repository under `docs/pages/` (engineering audience only).

---

## Related

- [Prerequisites](../get-started/prerequisites.md)
- [Contact support](../support/contact.md)
- [Admin — workspace setup](../admin/workspace-setup.md)
- [Governance](../admin/governance.md)
