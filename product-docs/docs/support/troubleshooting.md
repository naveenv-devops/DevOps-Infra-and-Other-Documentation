# Troubleshooting

Common issues and resolutions.

---

## Conversion failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Job stuck in **Queued** | Service unavailable | Retry; contact admin if persists |
| **Validation failed** | Schema or XSLT error | Review validation report; fix source content |
| **Unsupported format** | Wrong format selected at upload | Re-upload with correct source format |
| **Timeout** | Large file or complex book | Split into smaller files; contact admin |

---

## Access issues

| Symptom | Fix |
|---|---|
| Cannot sign in | Verify credentials; contact workspace admin |
| Permission denied on action | Request role upgrade from Client Admin |
| API 401 Unauthorized | Regenerate API key; check token expiry |

---

## Output issues

| Symptom | Fix |
|---|---|
| PDF missing images | Check source image references and paths |
| HTML broken layout | Review XSLT profile; check CSS configuration |
| DITA validation errors | Fix source structure; see validation log |

---

## PR / development (internal)

For GitHub merge blockers on Met-R repositories, see internal docs:

- [PR merge guide](../../docs/github-pr-merge-guide.md)
- [Signed commits](../../docs/github-signed-commits.md)

---

## Related

- [Contact support](contact.md)
- [FAQ](../reference/faq.md)
