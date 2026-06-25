# AI capabilities

Met-R integrates AI across conversion, validation, and orchestration workflows.

---

## AI services

| Service | Repository | Purpose |
|---|---|---|
| **Determinacy Engine** | `metR_Determinacy_Engine` | Rule-based content decisions |
| **Master AI Agent** | `MetR-Master-AI-Agent` | Multi-step task orchestration |
| **Output XML/JSON AI** | `metR-Output-XML-JSON-AI` | AI-ready structured output |

---

## Use cases

| Use case | Description |
|---|---|
| **FM → DITA agent** | AI-assisted FrameMaker to DITA conversion |
| **Content enrichment** | Metadata extraction, tagging, summarization |
| **Validation assistance** | Intelligent error detection and fix suggestions |
| **Search & RAG** | Prepare content for retrieval-augmented generation |

---

## AI agent workflows

```
Trigger (upload / schedule / API)
    → Master AI Agent plans steps
    → Converter + Determinacy Engine execute
    → Validation + human review gate
    → Publish to output channel
```

---

## Governance

AI features respect workspace access controls. Sensitive content stays within your workspace boundary. Contact your admin for data residency and model usage policies.

---

## Related

- [FrameMaker converter](../converters/framemaker.md)
- [Platform overview](../platform-overview.md)
