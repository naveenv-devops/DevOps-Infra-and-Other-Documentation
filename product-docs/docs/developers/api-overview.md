# API overview

Programmatic access to Met-R via REST API through the API Gateway.

**Repository:** `metR-API-Gateway`

---

## Base URL

```
https://api.met-r.io/v1
```

Your workspace may use a custom API endpoint — check with your administrator.

---

## Authentication

| Method | Use case |
|---|---|
| **API key** | Server-to-server integrations |
| **Bearer token** | User-scoped operations |
| **OAuth 2.0** | Enterprise SSO integrations |

Include the token in the `Authorization` header:

```http
Authorization: Bearer YOUR_API_TOKEN
```

---

## Common endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/documents` | GET, POST | List and upload documents |
| `/documents/{id}` | GET, PUT, DELETE | Document CRUD |
| `/conversions` | POST | Start a conversion job |
| `/conversions/{id}` | GET | Job status and output |
| `/publish` | POST | Publish to output channel |

!!! note "Full API reference"
    OpenAPI specification coming soon. Contact DevOps for early access.

---

## Rate limits

| Tier | Requests / minute |
|---|---|
| Standard | 60 |
| Enterprise | Custom |

---

## Related

- [API Gateway](api-gateway.md)
- [Integrations](integrations.md)
