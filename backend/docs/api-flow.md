# API Usage Flow

Every client interaction follows this sequence. Use this as the reference for frontend integration.

---

## Response Contract

Every endpoint returns the same envelope:

```json
{ "success": true,  "message": "...", "data": {...}, "error": null }
{ "success": false, "message": "...", "data": null,  "error": {"code": "...", "detail": "..."} }
```

SSE (`/jobs/:id/stream`) is the only exception — it is a raw event stream.

---

## 1. New User Registration

```
POST /api/v1/auth/register
Body: { name, email, password }
```

**What happens:**
1. Email uniqueness checked → `409 CONFLICT` if taken
2. Password hashed (bcrypt)
3. User created with `role=user`, `credits=0`
4. Signup bonus credited (default: 100 — admin-configurable)
5. `CreditTransaction(type=grant, amount=100)` recorded
6. Access token (30 min) + refresh token (7 days) issued

**Response:**
```json
{
  "data": {
    "user_id": "...", "name": "...", "email": "...",
    "role": "user", "credits": 100,
    "tokens": { "access_token": "...", "refresh_token": "...", "token_type": "bearer" }
  }
}
```

Store both tokens. Send `access_token` as `Authorization: Bearer <token>` on every subsequent request.

---

## 2. Login

```
POST /api/v1/auth/login
Body: { email, password }
```

Same response shape as register. Replaces tokens on every login — refresh token rotates.

---

## 3. Token Lifecycle

**Access token expires in 30 min.** When you get a `401`, call refresh:

```
POST /api/v1/auth/refresh
Body: { refresh_token: "<stored refresh token>" }
```

Returns a new `access_token` + a new `refresh_token`. **The old refresh token is immediately revoked** — store the new one.

**Logout** revokes the refresh token server-side:

```
POST /api/v1/auth/logout
Body: { refresh_token: "..." }
```

---

## 4. User Profile

```
GET    /api/v1/users/me          → profile + current credit balance
PATCH  /api/v1/users/me          → update name and/or password
DELETE /api/v1/users/me          → soft-deactivate (token stops working immediately)
```

---

## 5. Credits

```
GET /api/v1/credits/balance          → { credits: 85 }
GET /api/v1/credits/transactions     → paginated history (grant, reserve, debit, refund)
```

**Credit transaction types:**

| Type | When | Amount |
|---|---|---|
| `grant` | Signup bonus or admin grant | +100 |
| `reserve` | Job starts — credits held | -N |
| `debit` | Job completes — actual cost charged | -N |
| `refund` | Job fails or overshoots reserved amount | +N |

**Example — job costs 10 credits, completes with 8 samples:**
```
balance: 100
→ reserve  -10  → balance: 90    (job starts)
→ debit     -8  → balance: 82    (actual cost on completion)
→ refund    +2  → balance: 84    (overshoot returned)
```

---

## 6. Creating a Job

```
POST /api/v1/jobs/
Body: {
  "name": "Q2 Support Dataset",
  "output_format": "jsonl",    // jsonl | json | csv
  "config": { ...JobConfig... }
}
```

**What happens immediately:**
1. `dataset.target_count` extracted → estimated credit cost calculated
2. User balance checked → `402 INSUFFICIENT_CREDITS` if short
3. Credits reserved → `CreditTransaction(type=reserve)` recorded
4. Job record created with `status=queued`
5. Background task started — runs the 6-stage engine pipeline

**Response:** Full job object with `status`, `credits_reserved`, `id`.

---

## 7. Watching a Job (SSE)

```
GET /api/v1/jobs/:id/stream
Headers: Authorization: Bearer <token>
Accept: text/event-stream
```

The server sends events as the engine progresses through stages:

```
event: stage
data: {"stage": "stage1_discover", "status": "done", "axes": {...}}

event: stage
data: {"stage": "stage4_generate", "status": "running"}

event: progress
data: {"type": "sample", "total_succeeded": 5, "target": 10}

event: stage
data: {"stage": "stage6_dedup", "status": "done", "removed": 1}

event: done
data: {}
```

**On disconnect:** Reconnect using the event replay endpoint — no events are lost:

```
GET /api/v1/jobs/:id/events   → full ordered event log
```

---

## 8. Job Status Polling

```
GET /api/v1/jobs/:id
```

Returns current status (`created | queued | running | completed | failed | cancelled`), credits used, elapsed time, error message if any.

```
GET /api/v1/jobs/
GET /api/v1/jobs/?page=2&limit=20
```

Paginated list of all your jobs.

---

## 9. Job Completion

When status is `completed`:

```
GET /api/v1/jobs/:id/output
```

Returns the generated dataset file as a download (`Content-Disposition: attachment`).

Credit transactions auto-recorded:
- `debit` for actual sample count
- `refund` for any overshoot vs reserved amount

---

## 10. Cancelling a Job

```
DELETE /api/v1/jobs/:id
```

Works when status is `created`, `queued`, or `running`. Returns `400` for terminal states (`completed`, `failed`).

Credits reserved for a cancelled job are **not automatically refunded** in the current version — this can be added as a policy decision (e.g. refund if cancelled before running, no refund if cancelled mid-run).

---

## 11. Admin — Credit Settings

Admin users only (`role=admin`). Regular users get `403 FORBIDDEN`.

```
GET   /api/v1/admin/credit-settings            → list all pricing knobs
PATCH /api/v1/admin/credit-settings/:key       → update a value
```

**Available keys:**

| Key | Default | Effect |
|---|---|---|
| `credits_per_sample` | `1` | Credits charged per generated sample |
| `free_credits_on_signup` | `100` | Credits granted on new user registration |
| `min_credits_per_job` | `5` | Minimum charge per job regardless of output |

Changes to `credits_per_sample` and `min_credits_per_job` take effect on the **next job created**. Changes to `free_credits_on_signup` take effect on the **next registration**.

---

## Error Codes Reference

| HTTP | Code | When |
|---|---|---|
| 400 | `BAD_REQUEST` | Invalid input (missing target_count, cancel completed job) |
| 401 | `UNAUTHORIZED` | Missing/invalid/expired token, wrong password, deactivated account |
| 402 | `INSUFFICIENT_CREDITS` | Not enough credits to start a job |
| 403 | `FORBIDDEN` | Regular user accessing admin routes |
| 404 | `NOT_FOUND` | Resource doesn't exist or belongs to another user |
| 409 | `CONFLICT` | Email already registered |
| 422 | `VALIDATION_ERROR` | Request body fails schema validation |
| 500 | `INTERNAL_ERROR` | Unhandled server error |

---

## Full User Journey (sequence)

```
POST /auth/register          → tokens + 100 credits
GET  /users/me               → confirm profile
GET  /credits/balance        → 100

POST /jobs/                  → job_id, credits reserved, status=queued
GET  /jobs/:id/stream        → SSE: watch stages tick through
GET  /jobs/:id               → status=completed
GET  /credits/balance        → reduced by actual cost
GET  /credits/transactions   → see reserve + debit + refund entries
GET  /jobs/:id/output        → download dataset

POST /auth/refresh           → rotate tokens when access_token expires
POST /auth/logout            → revoke refresh token
```
