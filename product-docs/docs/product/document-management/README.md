# Document management

Services for storing, editing, versioning, and migrating documentation content.

---

## Services

| Service | Repository | Purpose |
|---|---|---|
| **DocManager** | `metR-DocManager` | Document inventory, metadata, versioning |
| **DocEditor** | `metR-DocEditor` | Authoring and in-place editing |
| **DocMigrate** | `metR-DocMigrate` | Bulk migration from legacy systems |
| **DedUp** | `metR-DedUp` | Duplicate content detection and merge |

---

## Document lifecycle

```
Create / Upload → Edit → Version → Review → Archive / Publish
```

| Stage | Service | Actions |
|---|---|---|
| Ingest | DocManager | Upload, classify, tag |
| Author | DocEditor | Edit content, apply styles |
| Migrate | DocMigrate | Bulk import from FM, Word, CMS |
| Deduplicate | DedUp | Find and resolve duplicate topics |
| Publish | DocPublisher | Route to output channels |

---

## Related

- [Author workflows](../../guides/author-workflows.md)
- [User guide](../../guides/user-guide/README.md)
