# XSLT library

Reusable XSLT stylesheets for custom content transformations.

**Repository:** `metR-XSLT-Library`

---

## Overview

The XSLT Library provides shared transformation rules used across converter and output services. Extend or override stylesheets for customer-specific formatting requirements.

---

## Usage

1. Admin uploads custom XSLT to workspace
2. Pipeline references stylesheet by name
3. Converter applies transform after base conversion
4. `xslt-validation` CI check validates stylesheet

---

## Related

- [Pipeline configuration](../admin/pipeline-configuration.md)
- [Converters](../product/converters/README.md)
