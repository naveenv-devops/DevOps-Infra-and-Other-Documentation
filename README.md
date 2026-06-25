# Met-R & MetaPercept Documentation

Official documentation for **[met-r.io](https://met-r.io)** — the intelligent documentation orchestration platform by MetaPercept.

This repository is **public**. Content is organized by audience so end-users, administrators, and engineers each find the right material without confusion.

---

## Start here (end-users & customers)

| I want to… | Go to |
|---|---|
| **Learn what Met-R is** | [Introduction](product-docs/docs/get-started/introduction.md) |
| **Check prerequisites & licensing** | [Prerequisites](product-docs/docs/get-started/prerequisites.md) · [Licensing](product-docs/docs/reference/licensing.md) |
| **Run my first conversion** | [Quick start](product-docs/docs/get-started/quick-start.md) |
| **Browse all product docs** | [Product documentation hub](product-docs/docs/README.md) |
| **Get help** | [FAQ](product-docs/docs/reference/faq.md) · [Troubleshooting](product-docs/docs/support/troubleshooting.md) · [Contact](product-docs/docs/support/contact.md) |

**Published site (after GitHub Pages enabled):**  
`https://<your-username>.github.io/DevOps-Infra-and-Other-Documentation/`

---

## Documentation map

| Section | Audience | Folder |
|---|---|---|
| **Product documentation** | Customers, authors, admins, integrators | [`product-docs/docs/`](product-docs/docs/README.md) |
| **Engineering & DevOps** | MetaPercept engineers only | [`docs/pages/`](docs/pages/README.md) |
| **POC evaluations** | Internal architecture decisions | [`poc/`](poc/README.md) |
| **Automation scripts** | Maintainers | [`scripts/`](internal/MAINTAINERS.md) |

---

## Preview documentation locally

### Product docs (customer-facing)

```bash
pip install -r product-docs/requirements.txt
cd product-docs
py -m mkdocs serve
# Open http://127.0.0.1:8000
```

### Engineering docs (internal)

```bash
pip install mkdocs-material
cd docs
py -m mkdocs serve
# Open http://127.0.0.1:8000
```

---

## Repository structure

```
├── product-docs/           # PUBLIC — met-r.io product documentation
│   ├── docs/               # MkDocs content (publish this)
│   ├── mkdocs.yml
│   └── README.md           # Redirect to docs/
├── docs/pages/             # INTERNAL — DevOps & platform engineering
├── poc/                    # INTERNAL — infrastructure evaluations
├── scripts/                # Maintainer automation
├── templates/              # CODEOWNERS templates
└── reports/                # Generated audit reports (not for end-users)
```

---

## Making this repository public

See **[PUBLISHING.md](PUBLISHING.md)** for the checklist before setting the repo to public on GitHub.

---

## Contributing

- Product docs: [product-docs/docs/CONTRIBUTING.md](product-docs/docs/CONTRIBUTING.md)
- Engineering docs: for MetaPercept team members via pull request

---

*Maintained by MetaPercept · [met-r.io](https://met-r.io) · [metapercept.com](https://metapercept.com)*
