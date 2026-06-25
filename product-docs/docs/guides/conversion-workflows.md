# Conversion workflows

End-to-end procedures for converting content between formats.

---

## Standard conversion

1. Upload source file with correct format selected
2. Choose target format and pipeline profile
3. Run conversion — monitor job status
4. Review validation report
5. Download or publish output

---

## FrameMaker → DITA

1. Upload `.fm` or `.book` file
2. Select **FrameMaker** source, **DITA** target
3. Choose FM→DITA pipeline (standard or AI-assisted)
4. Review DITA topic structure in output preview
5. Fix validation errors and re-run if needed

See [FrameMaker converter](../product/converters/framemaker.md).

---

## Bulk migration

For large-scale legacy migration:

1. Admin configures DocMigrate job
2. Batch upload source files
3. Pipeline runs conversions in parallel
4. Review aggregate validation report
5. Publish to target channel

---

## Pipeline validation

Every conversion runs these checks (where applicable):

| Check | Description |
|---|---|
| `unit-tests-pytest` | Service unit tests |
| `xslt-validation` | XSLT transform validation |
| `dita-ot-schema-check` | DITA schema compliance |
| `security-scan` | Dependency and content security |

---

## Related

- [Converters](../product/converters/README.md)
- [Supported formats](../reference/supported-formats.md)
