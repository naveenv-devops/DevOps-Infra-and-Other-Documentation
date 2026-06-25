# Shared Pipelines

Reusable CI/CD workflow templates for Met-R services.

**Repository:** `metR-Phase2-shared-pipelines`  
**Branch:** `main` (CODEOWNERS: standard template)

---

## Purpose

Centralize pipeline logic so all converter, output, and platform services use consistent:

- Test execution (`unit-tests-pytest`)
- XSLT validation (`xslt-validation`)
- DITA schema checks (`dita-ot-schema-check`)
- Security scanning (`security-scan`)

---

## Consumption pattern

Service repositories reference shared workflows:

```yaml
# .github/workflows/ci.yml (example pattern)
jobs:
  test:
    uses: metapercept-metr/metR-Phase2-shared-pipelines/.github/workflows/unit-tests.yml@main
```

---

## Available workflow templates

| Workflow | Check context | Services |
|---|---|---|
| Unit tests | `unit-tests-pytest` | All Python services |
| XSLT validation | `xslt-validation` | Converter services |
| DITA schema | `dita-ot-schema-check` | DITA-related services |
| Security scan | `security-scan` | All services |

---

## Adding a new service to shared pipelines

1. Add service repo name to pipeline configuration in `metR-Phase2-shared-pipelines`
2. Create `.github/workflows/ci.yml` in the new service referencing shared templates
3. Enable required status checks in branch protection ruleset
4. Verify checks appear on a test PR

---

## Related

- [CI/CD overview](ci-cd-overview.md)
- [Platform — Infrastructure](../platform/infrastructure.md)
