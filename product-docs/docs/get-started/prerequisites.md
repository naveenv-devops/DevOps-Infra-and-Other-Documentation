# Prerequisites

Everything required before using Met-R — accounts, tooling, network, and third-party licenses.

---

## Before you begin

| Prerequisite | Required for | How to obtain |
|---|---|---|
| Met-R workspace account | All users | Invited by workspace admin or MetaPercept |
| Supported web browser | Web UI | Install latest Chrome, Edge, or Firefox |
| Network access to `*.met-r.io` | Web UI, API | IT firewall allowlist |
| Source authoring tool (if applicable) | Upload & convert | See [Authoring tool licenses](#authoring-tool-licenses) |
| API credentials (optional) | Integrations | Issued by workspace admin |

---

## Account prerequisites

### Workspace access

1. Your organization must have an active **Met-R subscription** (see [Licensing](licensing.md))
2. A **Client Admin** creates your user account and assigns a role:
   - Viewer, Author, Reviewer, Client Admin, or Server Admin
3. You receive an invitation email with sign-in instructions

### Role minimums by task

| Task | Minimum role |
|---|---|
| View published content | Viewer |
| Upload and convert documents | Author |
| Approve for publish | Reviewer |
| Manage users and pipelines | Client Admin |
| Server / infrastructure config | Server Admin |

---

## Technical prerequisites

### Web browser

| Browser | Minimum |
|---|---|
| Google Chrome | Latest 2 major versions |
| Microsoft Edge | Latest 2 major versions |
| Mozilla Firefox | Latest 2 major versions |
| Safari | Latest 2 major versions (macOS) |

Requirements: JavaScript enabled, cookies allowed, TLS 1.2+.

### Network

| Requirement | Detail |
|---|---|
| Protocol | HTTPS (TLS 1.2 or higher) |
| Outbound URLs | `*.met-r.io`, your workspace URL |
| Ports | 443 (HTTPS) |
| Proxy | Standard HTTPS proxy supported; contact admin for config |
| Upload bandwidth | Minimum 5 Mbps recommended for large book files |

### Hardware (author workstation)

| Component | Minimum | Recommended |
|---|---|---|
| CPU | 4 cores | 8+ cores |
| RAM | 8 GB | 16 GB |
| Disk | 10 GB free | SSD with 50 GB+ for local authoring tools |
| Display | 1280 × 720 | 1920 × 1080 |

---

## Authoring tool licenses

Met-R converts content **from** your existing authoring tools. You may need valid licenses for source tools depending on your workflow.

| Tool | Required when | License type | Notes |
|---|---|---|---|
| **Adobe FrameMaker** | Uploading `.fm` / `.book` files | Commercial (Adobe) | Met-R converts FM → DITA; FM not required to *view* output |
| **Microsoft Word** | Uploading `.docx` | Microsoft 365 or standalone | DOCX conversion only |
| **Oxygen XML Editor** | Optional — editing DITA locally | Commercial (Oxygen) | Not required for Met-R web UI |
| **DITA Open Toolkit** | N/A for authors | Included in platform | Used server-side by Met-R |
| **Markdown editor** | Optional | Any (VS Code, etc.) | Free options available |

!!! note "Server-side processing"
    DITA-OT, XSLT engines, and conversion pipelines run on Met-R infrastructure. Authors do not need to install DITA-OT locally unless doing offline development.

---

## API integration prerequisites

For REST API access via [API Gateway](../developers/api-gateway.md):

| Requirement | Detail |
|---|---|
| API key or OAuth token | Issued by Client Admin |
| HTTPS client | TLS 1.2+ |
| JSON support | Request and response bodies |
| Rate limit awareness | Standard: 60 req/min (see [API overview](../developers/api-overview.md)) |

---

## On-premises / dedicated deployment

Additional prerequisites for private or dedicated deployments:

| Requirement | Detail |
|---|---|
| Kubernetes cluster | 1.27+ (see [Platform prerequisites](../../docs/platform/prerequisites.md)) |
| Container registry | Accessible from cluster |
| DNS & TLS certificate | Custom domain for workspace |
| Identity provider | SAML/OIDC for SSO (enterprise) |
| Storage | Object storage for document files |

Contact MetaPercept sales for the full infrastructure checklist.

---

## Pre-flight checklist

```
☐ Workspace account created and invitation accepted
☐ Browser updated and JavaScript enabled
☐ Network access to met-r.io confirmed
☐ Source files prepared in supported format
☐ Authoring tool license valid (if using FM, Word, etc.)
☐ Role assigned (Author or above for conversions)
☐ API key obtained (if integrating programmatically)
```

---

## Related

- [Licensing](licensing.md)
- [System requirements](system-requirements.md)
- [Quick start](quick-start.md)
- [Platform prerequisites (internal)](../../docs/platform/prerequisites.md)
