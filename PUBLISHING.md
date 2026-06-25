# Publishing Guide

Checklist before making this repository **public** on GitHub and enabling documentation for end-users.

---

## 1. Make the repository public on GitHub

1. Open **Settings → General → Danger Zone**
2. Click **Change repository visibility**
3. Select **Public**
4. Confirm repository name: `DevOps-Infra-and-Other-Documentation`

> Private repos return **404** to users without access — even for valid file paths.

---

## 2. Enable GitHub Pages (product docs)

1. Push the workflow in `.github/workflows/publish-product-docs.yml`
2. Go to **Settings → Pages**
3. Source: **GitHub Actions**
4. After first successful run, docs will be at:

```
https://naveenv-devops.github.io/DevOps-Infra-and-Other-Documentation/
```

5. (Optional) Add custom domain `docs.met-r.io` in Pages settings

---

## 3. What end-users should read

| Document | Purpose |
|---|---|
| [Product hub](product-docs/docs/README.md) | Main entry point |
| [Introduction](product-docs/docs/get-started/introduction.md) | What Met-R is |
| [Prerequisites](product-docs/docs/get-started/prerequisites.md) | Before you start |
| [Licensing](product-docs/docs/reference/licensing.md) | Plans and entitlements |
| [Quick start](product-docs/docs/get-started/quick-start.md) | First conversion |
| [FAQ](product-docs/docs/reference/faq.md) | Common questions |
| [Troubleshooting](product-docs/docs/support/troubleshooting.md) | Error resolution |
| [Contact](product-docs/docs/support/contact.md) | Support channels |

---

## 4. What is internal (not for end-users)

| Folder | Content | Note |
|---|---|---|
| `docs/pages/` | DevOps, platform architecture, GitHub governance | Engineering team |
| `poc/` | Vendor pricing comparisons, POC records | May contain internal cost data |
| `scripts/` | Org automation (CODEOWNERS rollout) | Maintainer tools |
| `reports/` | Generated CSV/XLSX audit reports | Regenerate; do not treat as docs |

Internal pages are labeled **"MetaPercept engineering"** where applicable.

---

## 5. Pre-publish content checklist

- [ ] Product docs use **support@metapercept.com** (not personal GitHub handles) for customer contact
- [ ] No API keys, tokens, or credentials in any file
- [ ] `reports/` contains no customer data (org scan data is OK for internal use — consider `.gitignore` if needed)
- [ ] Links in `product-docs/docs/` resolve correctly (run `py -m mkdocs build` in `product-docs/`)
- [ ] `product-docs/README.md` redirect exists for old URLs
- [ ] Root README clearly separates public vs internal sections

---

## 6. Verify build before publish

```bash
# Product docs — must succeed with zero errors
cd product-docs
py -m mkdocs build

# Engineering docs
cd ../docs
py -m mkdocs build
```

---

## 7. After going public

| Task | Action |
|---|---|
| Share product docs URL | GitHub Pages link or `docs.met-r.io` |
| Update met-r.io website | Link to published docs |
| Team onboarding | Point engineers to `docs/pages/` only |
| Customer onboarding | Point to product docs hub only |

----

## Related

- [Product CONTRIBUTING](product-docs/docs/CONTRIBUTING.md)
- [Maintainers guide](internal/MAINTAINERS.md)
