# Contributing to Met-R Documentation

Guidelines for writing and publishing documentation for **met-r.io**, modeled after professional doc sites such as [GitHub Docs](https://docs.github.com/en).

---

## Documentation principles

| Principle | Guideline |
|---|---|
| **Audience-first** | Write for the reader's job (author, admin, developer) — not internal jargon |
| **Task-oriented** | Lead with *how to accomplish something*, not system internals |
| **Accurate** | Verify against the running product; mark unreleased features as `Beta` |
| **Scannable** | Short paragraphs, tables, numbered steps, clear headings |
| **Maintainable** | One topic per file; cross-link instead of duplicating |

---

## Folder structure

```
product-docs/
├── README.md                 ← Hub page (like docs.github.com/en)
├── CONTRIBUTING.md           ← This file
├── mkdocs.yml                ← Site config for docs.met-r.io
├── get-started/              ← Onboarding
├── product/                  ← What Met-R is and does
├── guides/                   ← How-to guides for users
├── admin/                    ← Administration
├── developers/               ← API and integrations
├── reference/                ← Lookup tables, glossary, FAQ
└── support/                  ← Troubleshooting, contact, releases
```

### Section naming rules

| Folder | Use for | Avoid |
|---|---|---|
| `get-started/` | First-time setup, concepts | Deep technical reference |
| `product/` | Feature descriptions, capabilities | Step-by-step procedures |
| `guides/` | Task procedures ("How to…") | Marketing copy |
| `admin/` | Org settings, security, pipelines | End-user authoring tasks |
| `developers/` | API, SDK, webhooks | User-facing UI help |
| `reference/` | Tables, glossary, enums | Narrative tutorials |
| `support/` | Errors, contact, changelog | Feature specs |

---

## File naming

- Lowercase with hyphens: `conversion-workflows.md`
- `README.md` in each folder = section index
- Keep filenames short and descriptive

---

## Page template

```markdown
# Page title

One-sentence summary of what this page covers.

---

## Prerequisites

- Item 1
- Item 2

---

## Steps (or sections)

### Step 1 — Do something

Explanation and commands.

---

## Related articles

- [Link to related page](../path/page.md)
```

---

## Writing style

| Do | Don't |
|---|---|
| Use active voice: "Click **Publish**" | Passive: "The publish button should be clicked" |
| Use exact UI labels in **bold** | Paraphrase button names |
| Include screenshots for complex UI | Walls of text without visuals |
| Note version availability: `Available in Met-R 2.x` | Assume all readers are on latest |
| Link to [GitHub Docs](https://docs.github.com/en) patterns when helpful | Copy GitHub content verbatim |

---

## Publishing to docs.met-r.io

Documentation is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

### Local preview

```bash
pip install mkdocs-material
cd product-docs
mkdocs serve
# Open http://127.0.0.1:8000
```

### Build static site

```bash
mkdocs build
# Output in product-docs/site/
```

### Deploy

Deploy `site/` to your hosting target (GitHub Pages, Azure Static Web Apps, S3 + CloudFront, etc.) with custom domain `docs.met-r.io`.

---

## Review process

1. Create a branch from `dev`
2. Add or edit markdown under `product-docs/`
3. Run `mkdocs serve` locally and verify links
4. Open a pull request with label `documentation`
5. Maintainer review and merge to `main`
6. GitHub Pages workflow publishes the site automatically

---

## Status labels

Use in page front matter or opening paragraph:

| Label | Meaning |
|---|---|
| **GA** | Generally available, production-ready |
| **Beta** | Available but may change |
| **Preview** | Early access, not for production |
| **Deprecated** | Scheduled for removal; link to replacement |

---

## Questions

Contact MetaPercept via [admin@metapercept.com](mailto:admin@metapercept.com) or open a GitHub issue in this repository.
