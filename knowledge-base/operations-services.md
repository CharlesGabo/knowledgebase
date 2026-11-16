# Command Center tools and outside services

## Evidence and scope

This is a **reported operations inventory** from the user-supplied scan in [SRC-018](sources/SRC-018-cc-service-inventory.md), received 2026-11-16. Author, scan date, repository revision and branch are unknown. The report says it scanned code URLs, setting names and scheduled jobs; no code or production configuration was independently inspected here. It is not a complete verified deployment inventory or an approved customer-website stack. The existing [architecture](technology.md#current-reported-operations-architecture) and [website framework](technology.md#website-stack-in-the-current-framework) retain their separate scope.

## Reported services and tools

All roles below are assertions from SRC-018; branch/design references and uncertain providers remain explicitly qualified.

| Area | Service/tool | Reported role and limits |
|---|---|---|
| Platform | Supabase | Postgres, sign-in, API, Edge Functions, file storage, live updates and jobs using `pg_cron`/`pg_net`. Report counts 89 Edge Functions; count is scan-specific and unverified. |
| Hosting | Vercel | Hosts the operations React app at `tmalg.net`. |
| Code/automation | GitHub / GitHub Actions | Code/tests; database, code and storage backups; catalog publishing; QuickBooks D2 worker; vendor FTP pull. Edge Functions reportedly trigger workflows via GitHub API. This does not authorize new website sync workers. |
| Backups | S3-compatible storage; AWS CLI | Backup destination accessed using AWS CLI. Cloudflare R2 or Backblaze B2 suggested; exact provider unconfirmed. S3 compatibility does not establish AWS hosting. |
| Accounting | QuickBooks Online (Intuit) | Customers, vendors, estimates, invoices, POs and payments; OAuth and sandbox/production endpoints. Report counts 34 functions; not independently counted. |
| Network | QuotaGuard | Fixed-IP proxy for QuickBooks and vendor FTP where needed. |
| Payments | USAePay; Skyline Payments | Card payments/saved cards; Skyline invoice-email pay-now links. Existing operations usage does not settle Phase 4 website payment choice. |
| Tax | AvaTax (Avalara) | Comments reportedly name it as QuickBooks' tax source; scan found no direct repo integration. Live setup unconfirmed; website feasibility investigation remains open. |
| Communication | Google Workspace / Gmail | Staff Google sign-in, Calendar sync, document sending and reply checks. |
| Phone | Intermedia | Click-to-call, call-event webhook feeding the Community leaderboard, subscription renewal reportedly every 15 minutes. |
| Documents | Gotenberg PDF renderer | Separate PO/invoice PDF service at setting `PDF_RENDERER_URL`; PO fallback to QuickBooks PDF reported. Google Cloud Run hosting inferred from test `run.app` address, not confirmed production hosting. |
| Tracking | EasyPost; 17TRACK; 24hTrack | Tracking providers, reportedly sharing `carrier-webhook`. |
| Carrier links | UPS, FedEx, USPS, DHL, OnTrac, TForce | View-on-carrier-site links; not direct carrier API integrations in this report. |
| Catalog | Vendor FTP/SFTP; TD Synnex, SP Richards, ACM | Nightly feeds via worker in a separate private repo; vendor feeds are data sources, not live vendor APIs. TD Synnex invoice/AP setting reported. |
| AI | Anthropic / Claude API | PDF Document Extractor; Discovery buyer research specifically described as on an unidentified branch, not verified live. |
| Maps | OpenStreetMap Overpass / Nominatim | Business search through `generate-leads`; browser-side address/geographic-coordinate conversion. |
| Map UI | Leaflet | Leads-screen map library, rather than a hosted external service. |
| Discovery data | NCES (US Department of Education) | School/district directory referenced in an unidentified branch's design; implementation/deployment not established. |

Alex subsequently supplied a description of W76's QB/CC alignment work; see [current accounting status](workflows.md#accounting-and-quickbooks-alignment) and [SRC-019](sources/SRC-019-qb-cc-accounting-sync.md). This adds Owner-reported work status without independently validating this scan's service counts or proving payment reconciliation is live.

Alex's later [payment clarification](workflows.md#customer-payment-patterns), in SRC-021/SRC-022, adds Owner-reported usage context for USAePay and Skyline beyond the scan. Website processor choice remains open.

## Reported callbacks and sandbox state

- Event webhooks (incoming event notifications): `carrier-webhook` for the three tracking providers, identifying senders through signature headers; `intermedia-webhook` for phone calls.
- OAuth callbacks (returns after service authorization): `qb-callback`, `google-callback`, `intermedia-callback`.
- Machine-to-machine endpoints: `worker-*`, `run-vendor-ftp-pulls`, `tracking-sheet-intake` and QuickBooks scheduled runs; report says each checks its own secret. This is not a security audit or proof of correct authentication.

SRC-018 states these integrations are disabled in the referenced sandbox because local credentials are absent. That is a report about an unidentified sandbox at an unknown time, not a verified guarantee about every local environment. No credentials were provided or stored.

## Open verification and history

Exact production tax arrangement, renderer hosting and backup provider remain unknown; see [Q-015](questions.md#q-015). Branch-only Discovery findings and function counts require revision/deployment evidence before claiming current live state. No new tasks, completed work, decisions or website scope changes follow from this inventory.

2026-11-16: Added from SRC-018, supplementing SRC-001's broad operations architecture without replacing its history. Website integration continues to [reuse operations results](integration.md), with checkout/tax choices still governed by the framework.
