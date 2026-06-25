# System requirements

Hardware, software, and network requirements for using Met-R.

---

## Prerequisites

Before using Met-R, ensure you have:

- Active workspace account (see [Prerequisites](prerequisites.md))
- Supported browser and network access
- Valid subscription plan (see [Licensing](../reference/licensing.md))
- Source authoring tool license if uploading FrameMaker, Word, etc.

---

## Browser requirements

| Browser | Minimum version |
|---|---|
| Google Chrome | Latest 2 major versions |
| Microsoft Edge | Latest 2 major versions |
| Mozilla Firefox | Latest 2 major versions |
| Safari | Latest 2 major versions (macOS) |

JavaScript must be enabled. Pop-up blockers may interfere with file downloads.

---

## Network

| Requirement | Detail |
|---|---|
| HTTPS | All traffic over TLS 1.2+ |
| Outbound access | `*.met-r.io` and your workspace URL |
| File upload size | Configurable per workspace (default: contact admin) |
| API access | REST over HTTPS via API Gateway |

---

## Supported source formats

| Format | Extensions | Notes |
|---|---|---|
| Adobe FrameMaker | `.fm`, `.book` | FM → DITA conversion |
| DITA | `.dita`, `.ditamap` | DITA 1.2 / 1.3 |
| DocBook | `.xml` | DocBook 5.x |
| Markdown | `.md` | CommonMark / GFM |
| Microsoft Word | `.docx` | DOCX conversion |
| HTML | `.html`, `.htm` | Structured HTML |
| PDF | `.pdf` | Extraction workflows |

Full matrix: [Supported formats](../reference/supported-formats.md).

---

## API client requirements

For programmatic access via [API Gateway](../developers/api-gateway.md):

- HTTPS client with TLS 1.2+
- API key or OAuth token (issued by workspace admin)
- JSON request/response support

---

## On-premises / private cloud

For self-hosted or dedicated deployments, contact MetaPercept for infrastructure requirements (Kubernetes, storage, compute minimums).

---

## Related

- [Prerequisites](prerequisites.md)
- [Licensing](../reference/licensing.md)
- [Quick start](quick-start.md)
- [Troubleshooting](../support/troubleshooting.md)
