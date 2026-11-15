# TMA Operations Platform - processes and rules (context summary)

A summary of how work is done on the TMA Operations Platform (`tma-operations-platform-v2`): the
rules every contributor and AI agent follows, how changes are built, tested and reviewed, and the
business context behind them. It describes the current system only.

Sources (they win if this summary disagrees): `AGENTS.md`, `docs/business-context.md`,
`docs/onboarding/01-08`, `CURRENT_PROJECT/REVIEW_AND_MERGE.md`, `docs/decisions/README.md`,
`CURRENT_PROJECT/SECURITY_CHECKLIST.md`.

---

## 1. The business (`docs/business-context.md`)

- TMA Laser Group is a **B2B supplier**: toner and ink (OEM and compatible), office supplies,
  gloves and PPE, janitorial and medical supplies. It does not manufacture; it buys from vendors
  and distributors and resells, often shipped straight from the vendor to the customer.
- Customers are **organizations**: many schools and school districts, plus businesses such as
  hotels and offices. Some large customers buy through a **punchout catalog**.
- The ops platform (`tmalg.net`) is for **employees only**. Roles: **Owner** (runs the business,
  approves users, money and production changes), **Manager** (oversees salespeople, accounts,
  orders), **Salesperson** (owns accounts, works leads, builds quotes and orders), **Dialer**
  (outbound calling; role being reworked). Admin is permission-driven.

**How money moves:**
1. **Leads -> Accounts.** A converted lead becomes an Account. "Customer" is a lifecycle status of
   an Account (`lead` / `customer` / `inactive`), not a separate record ("Leads are Accounts",
   `docs/DECISIONS_LOG.md`).
2. **Catalog.** Vendor feeds (upload or nightly FTP/SFTP) merge into one **product** (keyed by
   manufacturer part number) with many **offers** (one per vendor, each with its own cost).
3. **Quote -> Order.** Built in the cart at TMA's sell price; an accepted quote becomes an order.
4. **Purchase orders.** Processing splits the order into POs per vendor, with freight rules by
   zone. Vendors never see the end customer's name where routing hides it.
5. **Fulfillment and tracking.** Shipments are tracked back onto the order.
6. **Accounting.** Customers, invoices, estimates and POs sync with **QuickBooks**; card payments go
   through a payment gateway and post to QuickBooks; sales tax through a tax integration.

**Favorites:** per account, a catalog item, its vendor and the **sell price** TMA charges that
customer: effectively a per-customer price book.

## 2. Architecture (`docs/onboarding/01-architecture-tour.md`)

```
Browser (Vite + React SPA, public bundle on Vercel)
  |  supabase-js with the ANON key (not a secret) + the user's JWT
  v
Supabase
  |- PostgREST: tables/views (RLS on every table) + RPCs (Postgres functions)
  |- Auth: sign-in; auth.uid() inside SQL identifies the caller
  |- Edge Functions (Deno): anything needing a secret or an outside service
  |- Storage: uploaded files, documents
  '- Postgres: functions, triggers, pg_cron jobs, Vault secrets
GitHub Actions workers: vendor FTP pulls, backups, QuickBooks worker
```

Three facts shape everything:
1. **The database is the security boundary.** The anon key is in the public bundle, so anyone can
   call the API directly. Access control lives in RLS, database functions and constraints.
2. **Most business logic lives in Postgres.** Order state changes, permission checks, invariants,
   audit logs and numbering are database functions and triggers; the SPA calls them as RPCs.
3. **Edge Functions are for secrets and outside services** (QuickBooks, Google/Gmail, the dialer,
   carrier tracking, card payments, outbound email, AI extraction).

**Environments:**

| Environment | What | Who |
|---|---|---|
| Local sandbox | Supabase in Docker, built from migrations, synthetic data | Contributor |
| DEV (`tma-catalog`) | Shared hosted dev/staging, synthetic data only | Alex and internal threads |
| PROD (`tma-catalog-prod`) | Real customer, vendor and order data | Alex only, through guarded SQL packages |

Flow of a change: **sandbox -> PR + independent review -> Alex merges -> DEV -> PROD.** No
credential is ever shared between a synthetic environment and production.

## 3. Working async with the Owner (`AGENTS.md`, `docs/onboarding/08-async-workflow.md`)

- **Work comes from GitHub Issues** (spec + acceptance criteria). Labels: `priority: high/normal/
  low`, `needs-owner`, `blocked`. One issue at a time; finish in-progress work first.
- **Answer it yourself first** from the code, migrations, tests and docs. Write what you learned in
  `docs/learning-notes/`.
- **Ask the Owner only** for business intent, product or priority decisions, access, or anything
  risky (data, security, orders, QuickBooks, permissions). Format: **Context / Question / Options I
  see (with your pick) / Meanwhile**. Post on the issue, add `needs-owner`, **move to other work**.
- **Never guess a business rule silently.** List assumptions in the PR under "Assumptions".
- **Record decisions** in `docs/decisions/` in the same PR.
- **Start of shift** (`/start-shift`): pull `main`, read replies, pick work.
  **End of shift** (`/end-shift`): push (draft PR), comment on each issue touched, one Notion Work
  Log entry if you track hours (hour tracking is opt-in).
- Never put contract, pay, hours, hiring, grading, candidate or personal details in the repo, a
  branch, an issue or a PR.

## 4. Environments and access rules (`AGENTS.md`, `docs/onboarding/02-local-setup.md`)

- Contributors work only in their own sandbox. **Never connect to, query, migrate or deploy to
  production**, and never write to the shared DEV project. No task requires a production
  credential; never ask for or use one.
- Never `supabase db reset` a hosted project. Never deploy Edge Functions. Never change GitHub
  workflows, secrets, Vercel config or `tools/vercel-ignore-build.sh` unless that is the task.
- **Never paste production data, secrets, keys, passwords, tokens or `.env` contents into any AI
  tool, issue, PR, commit or log.** If real data reaches you, stop and tell Alex. If a secret may
  have leaked, tell Alex immediately.
- Integrations stay dark in the sandbox (email goes to Mailpit). Never wire a real credential in.

**Local setup:**
- `node tools/sandbox-reset.mjs` wipes and rebuilds the database by replaying every migration from
  zero, then loads synthetic seeds. It is the undo button.
- **Windows:** `git config --global core.autocrlf input` is mandatory (wrong line endings break
  migrations with misleading errors).
- `.env.local` is git-ignored, created by you: local URL, anon key, persona settings.
  **Anything prefixed `VITE_` ends up in the public bundle**; never give a secret a `VITE_` name.
  `npm run build` refuses to build in persona mode.
- Seeds are invented with fixed IDs. A real-looking company name in the sandbox is a bug. Need more
  data? Add a seed or fixture, never copy real records.
- **Personas:** Owner (Alex Marcel), Manager (Morgan Reed), Salesperson (Jordan Patel), Dialer
  (Katie Torres). Test every change as at least one privileged and one restricted persona.

## 5. Security rules (`docs/onboarding/06-security-rules.md`, `SECURITY_CHECKLIST.md`)

1. **Never build SQL from strings.** Parameters; for unavoidable dynamic SQL, `format()` with
   `%I`/`%L` or `execute ... using`. Whitelist caller-chosen columns, sort keys, JSON keys. Don't
   interpolate user input into PostgREST filter strings.
2. **Fail closed.** Anything not explicitly allowed is denied. **NULL is not false**: `if not
   (<null>) then raise` skips the raise. Use helpers that never return NULL (`has_permission()`
   returns `false`, `current_profile_role()` returns `''`), `coalesce`, `is distinct from`. Never
   copy an RLS `using (...)` predicate into an `IF NOT (...)` guard. Refuse with `42501`.
3. **Lock down every new table and function explicitly.** Tables: RLS `enable` + `force`,
   `revoke all ... from anon`, explicit policies per operation; prove it as `anon` against a table
   **with rows**. `SECURITY DEFINER` functions: pinned `search_path`, caller re-checked inside,
   input whitelist, `revoke ... from public, anon`, grant only where needed. `drop function` +
   `create` discards grants: restate them. Prefer `security_invoker = true` views.
4. **No secrets in the browser.** The browser gets only the URL and anon key. The service-role key
   lives only in Edge Function secrets and workers, used only after verifying the caller. Edge
   Functions with `verify_jwt = false` authenticate the request themselves.
5. **No production data or secrets in AI tools or anywhere else.** Never commit `.env*` files.
6. **Stay inside your environment.** Don't weaken a check (CI gate, known-failures entry, grant,
   policy) to pass.

Also: never raise SQLSTATE `40001` for a permanent condition (PostgREST retries it); respect the
**8-second** API statement timeout and flag heavy queries.

**Before opening a PR, ask:** What can an attacker do calling my table or RPC directly, as `anon`
and as the least-privileged role? Does every `SECURITY DEFINER` function pin `search_path`,
re-check the caller and have explicit grants? Can a NULL skip a guard? Did any secret or real data
end up in code, a commit, a log or an AI prompt?

## 6. Where logic lives (`docs/onboarding/03-where-logic-lives.md`)

**Guiding rule: anything that must hold no matter who calls the API belongs in the database.**

| You need to... | Put it in |
|---|---|
| Decide which rows a user may read/write | RLS policy |
| Perform a business action (multi-table write, state change, validation, numbering) | Database function (RPC), usually `SECURITY DEFINER` + pinned `search_path` + permission check inside |
| Answer "who is calling, what may they do" | Helper functions: `current_profile_id()`, `current_profile_role()`, `has_permission()` |
| Enforce a rule on every write; keep derived data; append-only audit | Trigger |
| A rule both the SPA and an Edge Function need | One database function both call |
| Call an outside service or use a secret | Edge Function |
| Run on a schedule | `pg_cron` (long or external work: GitHub Actions worker) |
| Display, form state, hiding controls | Front end (UX only; `can()` mirrors the database) |

Rules of thumb: **one rule, one home**; UI permission checks mirror database checks and never
replace them (keep `role_permissions` and the JS matrix in parity); prefer an RPC to direct table
writes when the write has rules; triggers stay boring (no outside calls or long work); multiple
triggers fire in alphabetical order by name.

## 7. Migrations (`docs/onboarding/04-migrations.md`)

1. **Version number** = 10000 above the highest version found on every GitHub branch, on the work
   board (`CURRENT_PROJECT/WORKTREE_REGISTER.md`), and on your own unpushed branches. Use the
   one-line command in the guide. Never use the clock or `supabase migration new`. The orchestrator
   confirms or renames it at review.
2. **Write it:** `begin; set local lock_timeout = '2s'; ... commit;`; **ASCII only** (the production
   SQL Editor mangles non-ASCII); LF line endings (spell newlines in literals as `chr(10)`); header
   comment with what, why, design doc, how to undo; the **ledger line** (`insert into
   supabase_migrations.schema_migrations(version, name) values (...)`) before `commit`; then
   `notify pgrst, 'reload schema'`. New tables: RLS checklist + indexes for policy/RPC filters, and
   say "new table" in the PR. Data changes in their own migration, with row counts.
   **Never edit a merged migration.**
3. **Test locally:** rebuild from zero; click through as affected personas; prove in SQL (act as a
   persona inside a rolled-back transaction): allowed persona succeeds, restricted gets `42501`,
   `anon` refused at the grant, RLS hides rows with data present. `postgres`/`service_role` bypass
   RLS, so tests run as them prove nothing.
4. **CI:** migration replay from zero (checker and floor taken from `main`, so a PR cannot weaken
   the gate; fails if any `public` function is executable by `anon`/`PUBLIC`), migration ledger
   check, tests.
5. **Submit:** Migration section in the PR (versions, objects, new table / data change / replaced
   function, how to undo, persona evidence, expected heavy queries).
6. **Production (Alex):** guarded package (preflight -> apply -> verify -> rollback), starting with
   a fresh backup and refusing the wrong database. Migrations go to production before the front end
   that needs them.

## 8. Testing (`docs/onboarding/05-testing.md`)

| Suite | Command | CI |
|---|---|---|
| Node tests | `npm run test:ci` | Required |
| Deno type check / assertions | `npm run test:deno` / `npm run test:deno:run` | Yes; assertions fully green |
| Migration replay | `node tools/sandbox-reset.mjs` | On database PRs |
| Migration ledger | `node tools/check-migration-ledger-lines.mjs origin/main` | Yes |
| Architecture map | `npm run arch:check` | Yes |
| Quick all-in-one | `npm run verify` | - |

- **Ratchet:** `tests/known-failures.json` lists tolerated old failures. A new failure blocks merge;
  a known failure that now passes is removed in the same PR. **Never add a line to get green.**
- On a failure, decide first: **stale guard** (update or retire the assertion and say why) or
  **real regression** (fix the code).
- A PR includes: tests for the change, pasted summaries (pass / known / new), sandbox rebuilt from
  zero if there is a migration, persona allowed/refused (and `anon`) evidence for anything access
  related, and a screenshot or description for UI changes.

## 9. Pull requests (`docs/onboarding/07-pull-requests.md`)

- Branch from the latest `main` (`fix/`, `feat/`, `catalog/`, `platform/`). Small scope; one
  finished, verified chunk per PR. Merge `main` into your branch; don't rebase shared branches.
  Never commit to `main`.
- Commits: one logical change, message says what changed and why. Check `git status` and the diff
  first (no `.env*`, credentials, real data, debug output). Messages are permanent: keep technical.
- **PR description:** `## What` (and what it does NOT change) / `## Why` (task or design doc) /
  `## Migration` (or "No migration") / `## Tests` / `## Risks / notes for review`, plus
  "Assumptions" and "Open questions" where needed. State the kind of change: UI only / migration /
  Edge Function / CI or tooling.
- Open as a **draft**; mark ready when CI is green and the description is complete.
- **Do only what the description says.** Note unrelated problems; don't fold fixes in. If a
  technical constraint conflicts with the design, build the clear part, write the question under
  "Open questions", and stop at that boundary.
- Answer review findings with **new commits, not force-pushes**.
- **Files contributors don't edit:** the work board (`WORKTREE_REGISTER.md`), the roadmap (unless
  asked), production packages under `tools/sql/prod-apply-*`, GitHub workflows, Vercel config and
  secrets, merged migrations.

## 10. How Alex reviews and merges (`CURRENT_PROJECT/REVIEW_AND_MERGE.md`)

1. **CI green:** Node test suite (required), Deno checks, architecture map, migration ledger,
   migration replay when it runs.
2. **Independent review returns SHIP** (an AI review run by Alex). Big features get a design review
   **before** building.
3. **Alex reads the diff with three questions:**
   - Does it do what the description says? (A change that does more than it claims gets pushed
     back.)
   - Does it touch anything outside its scope? (Migrations, workflows, `vercel.json`,
     `tools/vercel-ignore-build.sh`, `supabase/functions/` get a closer look.)
   - Would it make sense in six months? (If not, he asks the author to add a comment.)
4. **Approve, then merge with "Create a merge commit" or "Squash and merge". Never "Rebase and
   merge".** The Vercel ignore script compares one commit with its parent; a rebase merge can make
   it judge the whole push by the last commit and **silently skip a real deploy** (this happened on
   2026-09-15: production stayed 23 hours behind). Command-line merges use `--no-ff`.
5. **Confirm it deployed:** a **new row** in Vercel Deployments with status Ready. A green tick
   proves nothing (a skipped build reports success). Docs-only change with no row is correct; code
   change with no row means production is stale, fixed by a commit touching a watched path.

## 11. Production (Alex's side, for context only)

- Every production SQL that **writes** starts with a backup (`gh workflow run db-backup.yml`), and
  needs a green backup that finished within the last 2 hours.
- Every production SQL (read or write) starts with a fingerprint guard line that divides by zero on
  any other database.
- Read-only probes get no backup but still carry the guard and must truly only read.

## 12. Roles (`AGENTS.md`)

Claude designs (what to build) and builds UI/UX. Codex builds backend: migrations, RLS, RPCs, Edge
Functions, sync, parsing. Small, already-diagnosed fixes Claude makes directly. **Every PR gets an
independent Codex review (SHIP) before merge**; big features also get an independent design review
before building. Never name a Codex tier; state the risk instead. Every Codex prompt is one fenced
block with a thread title and the folder.

## 13. Decisions and documentation

| Where | Holds | Confirmed by |
|---|---|---|
| `AGENTS.md` | The rules everyone follows | Owner |
| `docs/decisions/` | Why something was chosen (one file per decision) | Owner |
| `docs/DECISIONS_LOG.md` | Older accepted decisions (identity, roles, lifecycle) | Owner |
| `docs/learning-notes/` | How something works, as found | Nobody: shared notes |
| `CURRENT_PROJECT/` | Living plan, per-feature designs, release evidence | - |

**Decision record** (`docs/decisions/YYYY-MM-DD-short-title.md`): written when an Owner answer
changes how something works, for a design choice someone will later wonder about, or for a
reversal. Fields: Date, Decided by, Issue or PR, Status (Proposed / Accepted / Superseded); sections
Context, Decision, Why (including rejected options), Consequences. Added in the same PR as the work.

## Words you'll see

| Term | Meaning |
|---|---|
| Account | A customer or prospect organization (the durable parent record) |
| Lead | A prospect being worked, before conversion |
| Offer | One vendor's listing of a product, with that vendor's cost |
| OEM / compatible | Brand-name cartridge / third-party equivalent |
| PO | Purchase order from TMA to a vendor |
| House | System owner for accounts with no salesperson |
| W-number | A workstream ID; design docs in `CURRENT_PROJECT/` are named by it |
| SHIP | The independent reviewer's approval to merge |
| RLS | Row Level Security: Postgres policies deciding which rows a caller sees |
| RPC | A Postgres function called through the API |
