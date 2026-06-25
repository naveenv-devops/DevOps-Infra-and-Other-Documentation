# API Gateway

The Met-R API Gateway (`metR-API-Gateway`) is the single entry point for all API traffic.

---

## Responsibilities

| Function | Description |
|---|---|
| **Routing** | Direct requests to converter, doc, and output services |
| **Authentication** | Validate API keys and tokens |
| **Rate limiting** | Protect services from abuse |
| **Logging** | Request/response audit trail |

---

## Architecture

```
Client → API Gateway → Converter / DocManager / Output services
```

---

## Related

- [API overview](api-overview.md)
- [Platform overview](../product/platform-overview.md)
