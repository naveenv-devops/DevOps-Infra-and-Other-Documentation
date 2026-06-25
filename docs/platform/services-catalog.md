# Services Catalog

Complete catalog of Met-R platform microservices and GitHub repositories.

**Organization:** [metapercept-metr](https://github.com/metapercept-metr)  
**Total repositories:** 52

---

## Tier 1 — Core platform

| Service | Repository | Branches | Owner |
|---|---|---|---|
| Frontend | `metR-Frontend` | dev, devops-testing, main | Platform |
| API Gateway | `metR-API-Gateway` | dev, devops-testing, main | Platform |
| Client Admin | `metR-Client-Admin` | main | Platform |
| Server Admin | `metR-Server-Admin` | dev, devops-testing | Platform |
| Core Infrastructure | `metR-Core-Infrastructure` | main | DevOps |
| Phase 2 Platform | `metR-Phase2` | main | Platform |
| Shared Pipelines | `metR-Phase2-shared-pipelines` | main | DevOps |

---

## Tier 2 — Converter services

| Service | Repository | Primary transform |
|---|---|---|
| FrameMaker | `metR-Converter-FrameMaker` | FM → DITA |
| HTML | `metR-Converter-HTML` | HTML ↔ structured |
| Markdown | `metR-Converter-Markdown` | MD ↔ structured |
| DOCX | `metR-Converter-DOCX` | Word → DITA/HTML |
| DocBook | `metR-Converter-DocBook` | DocBook ↔ DITA |
| PropDITA | `metR-Converter-PropDITA` | PropDITA → DITA |
| Sitecore XML | `metR-Converter-SitecoreXML` | Sitecore → DITA |
| PDF | `metR-Converter-PDF` | PDF extraction |

All converter repos: branches `dev`, `devops-testing`, `main` (where provisioned).

---

## Tier 3 — Document services

| Service | Repository | Function |
|---|---|---|
| DocManager | `metR-DocManager` | Inventory, versioning |
| DocEditor | `metR-DocEditor` | Authoring |
| DocMigrate | `metR-DocMigrate` | Bulk migration |
| DocPublisher | `metR-DocPublisher` | Publication orchestration |
| DedUp | `metR-DedUp` | Deduplication |

---

## Tier 4 — Output services

| Service | Repository | Output |
|---|---|---|
| PDF | `metR-Output-PDF` | Print PDF |
| HTML5/CMS | `metR-Output-HTML5-CMS` | Web + CMS |
| XML/JSON AI | `metR-Output-XML-JSON-AI` | AI-ready structured |
| Infinity DocSite | `metR-InfinityDocSite` | Documentation portal |

---

## Tier 5 — AI & intelligence

| Service | Repository | Function |
|---|---|---|
| Determinacy Engine | `metR_Determinacy_Engine` | Rule-based decisions |
| Master AI Agent | `MetR-Master-AI-Agent` | Multi-step orchestration |

---

## Tier 6 — Shared libraries & validation

| Component | Repository | Function |
|---|---|---|
| XSLT Library | `metR-XSLT-Library` | Shared transforms |
| DITA validation | `dita2-validation-transformation` | Schema validation |

---

## Tier 7 — Tooling & internal

| Component | Repository | Function |
|---|---|---|
| GitHub org MCP | `github-org-mcp-server` | GitHub automation |
| AI DevOps teammate | `ai-devops-teammate` | DevOps AI assistant |
| RuleSet Branches Secure | `RuleSet-Branches-Secure` | Branch rules reference |
| Kubernetes | `KUBERNETES` | K8s manifests / config |

---

## Governance status (June 2026)

| Metric | Value |
|---|---|
| Repos with CODEOWNERS | 58 branches across 52 repos |
| Branch protection active | `dev`, `devops-testing`, `main` (per ruleset) |
| Valid CODEOWNERS | 55 branches |
| Invalid (pending fix) | 3 branches |

Report: `reports/codeowners-validation-latest.csv`

---

## Related

- [Architecture](architecture.md)
- [Product repository map](../../product-docs/reference/repository-map.md)
