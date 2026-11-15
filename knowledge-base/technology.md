# Technical baseline and access

## Current reported operations architecture

This describes the existing operations platform only. The operations summary alone does not decide website technology; see the Owner direction below. [SRC-001 ??2,6](../tma-ops-processes.md)

- Vite/React SPA on Vercel calls Supabase through `supabase-js`, using the public anon key and user JWT.
- Supabase provides Auth, PostgREST tables/views/RPCs, Storage, and Postgres functions, triggers, `pg_cron` and Vault.
- Database RLS, functions and constraints enforce access and business invariants. Browser permission checks are UX only. Keep database role permissions and the JS matrix in parity.
- RPCs handle business actions; helpers identify callers and permissions; triggers enforce every-write rules and audit. Triggers avoid external/long work and execute alphabetically by name.
- Deno Edge Functions handle secrets and external services: QuickBooks, Google/Gmail, dialer, tracking, payments, outbound email and AI extraction. GitHub Actions workers handle vendor FTP pulls, backups and QuickBooks work.

## Website environments and platform direction

Current Owner direction and reported status come from [SRC-003](sources/SRC-003-website-environments.md); full decisions and supersession limits are in [D-003](decisions.md#d-003) and [D-004](decisions.md#d-004).

| Area | Current understanding | Status |
|---|---|---|
| Phase 0 | Sandbox work/documentation permitted by Alex. Operations sandbox reported running by the user (SRC-004); separate website sandbox not evidenced. | Operations setup self-reported complete; Phase 0 design pending |
| Shared DEV | Alex plans to move DEV to its own Supabase organization and clean it up, then share it with the user, Alex and Chaze. | Pending; no completion/access evidence or date |
| Production | Keep fully separate from shared development. | Approved boundary; no production access granted |
| DEV test data | Alex plans better test data including real vendor catalogs. | Pending; no evidence seeded |
| Platform | Stay on Supabase within the framework (SRC-003); Next.js/React/TypeScript and Vercel specified in SRC-005. | Current framework direction; no implementation verified |

Alex reports that DEV and PROD currently share one Supabase organization and gives organization-level access as the reason for separation. This is the Owner's explanation, not an independently verified statement about Supabase capabilities. The exchange gives no new project IDs or credentials.

Catalogs in planned DEV are an explicit change from SRC-001's synthetic-only baseline for that environment. This does not authorize copying customer/order data, exposing secrets, using real integrations in a sandbox or treating DEV as ready. See [catalog context](workflows.md#website-catalog-direction).

## Completed operations setup (user report)

The user reports all checked weekend setup items completed: work email and 2-step verification; Claude/Notion access (website teamspace and Charles's private page); GitHub account/2FA/username sent and repository invite accepted; listed tools installed (VS Code, Git, Node 20+, Python 3.11+, Docker, Claude Code, optional Codex item, `gh` authentication); Windows line-ending setting; operations repo cloned; local setup guide followed; app run with `npm run dev` and a test persona. Readings are marked done, hour tracking enabled, and shift commands tried. Completion dates, actual tool versions, current permission level and independent test evidence are not supplied. [SRC-004](sources/SRC-004-completed-setup.md)

No need to re-provision that existing operations sandbox merely because the website repository is pending. Separate website environment requirements remain [partially unresolved](questions.md#q-006). No passwords or tokens are recorded.

## Website stack in the current framework

This is intended technology, not a deployed inventory. [SRC-005](sources/SRC-005-website-counter-proposal.md), section 5. See [integration](integration.md) for system separation, data ownership and sync boundaries.

| Area | Framework choice |
|---|---|
| Language/UI | TypeScript; Next.js App Router/React; Tailwind CSS; shadcn/ui |
| App logic/validation | Next.js server actions/route handlers; Zod on all server input |
| Shared logic/data | Postgres functions/triggers, Supabase Edge Functions; Supabase DB/Auth/Storage and Supavisor pooling |
| Jobs/search/events | pg_cron and Edge Functions; Queues only if needed; Postgres full-text search, dedicated search later if needed; in-house event tables |
| Email | Gmail API/company mailbox for transactional; later dedicated marketing service/subdomain |
| Monitoring/protection | Sentry set up by TMA; Cloudflare Turnstile |
| Tax/content | AvaTax API feasibility and certificates under investigation; Icecat/distributor content pending |
| Payments | Phase 3 Skyline links; Phase 4 method undecided (framework lists QuickBooks Payments, USAePay and/or Skyline) |
| AI | Later Claude via Vercel AI SDK or Anthropic SDK; timing open |
| Tests/CI | Unit/integration plus Playwright E2E, operations conventions where practical; GitHub Actions tests every PR |
| Local/hosting/code | Supabase CLI using Docker; separate Vercel project; Git/GitHub in TMA organization |

The framework describes a dedicated development environment and separate operations/website Supabase dev/prod projects. Alex's other reply describes planned shared DEV. Their exact relationship is unresolved, not silently superseded: [Q-009](questions.md#q-009). Preview/staging/Sentry setup is planned, not confirmed complete.

## Existing operations environment context

SRC-001 sections 2 and 4 report local Docker sandboxes, DEV `tma-catalog`, and PROD `tma-catalog-prod`. Current project identities/availability have not been verified. Production access is Alex-only through guarded SQL packages in that baseline. Credentials must not be shared between synthetic and production environments. [SRC-001](../tma-ops-processes.md)

For website work, the earlier shared-DEV write prohibition and synthetic-only DEV rule are superseded only by the conditional future shared-DEV policy and catalog plan in SRC-003. Until readiness/access is confirmed, use the sandbox. See [history](decisions.md#d-003).

## Security and setup baseline

Source-reported rules, not commands to run in this knowledge-base repository: rebuild local sandbox with `node tools/sandbox-reset.mjs`; use synthetic fixed-ID seeds, never copied records. Windows setup requires `core.autocrlf input`; `.env.local` is ignored. `VITE_` values are public; persona-mode builds are refused. Test privileged and restricted personas. Source personas: Owner Alex Marcel, Manager Morgan Reed, Salesperson Jordan Patel, Dialer Katie Torres. [SRC-001 ?4](../tma-ops-processes.md)

Use parameterized SQL; whitelist dynamic identifiers and filters. Fail closed on NULL and deny with `42501`. New tables explicitly enable/force RLS, revoke anon access and define operation policies. Test anon against populated tables. Security-definer functions pin `search_path`, recheck callers and explicitly restrict grants; recreate grants after function replacement. Prefer security-invoker views. Service-role credentials stay server-side, with caller checks; functions disabling JWT verification authenticate themselves. Do not use `40001` for permanent errors; respect the eight-second API timeout. [SRC-001 ?5](../tma-ops-processes.md)

Never reset a hosted database, deploy Edge Functions, or alter workflows/Vercel configuration unless explicitly in task scope. Never expose secrets or production data; the source calls for notifying Alex if exposure occurs. Production writes require a successful backup within two hours; all production SQL carries a database fingerprint guard. These are Alex's operational procedures, not authorization for this repository to access production. [SRC-001 ??4,11](../tma-ops-processes.md)

## History

2026-11-15: SRC-003 partially answers website architecture/access and establishes a conditional shared-DEV workflow. Earlier DEV restrictions are retained with their scoped replacement in D-003. Website setup and rollout details remain [partially answered](questions.md#q-002).

2026-11-15: SRC-004 resolves the earlier lack of operations sandbox completion evidence by user report. SRC-005 specifies the intended website stack and separate project boundary; dedicated/shared DEV ambiguity is retained as Q-009.
