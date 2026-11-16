# SRC-018 - Supplied Command Center service inventory

- Author: User (intake request); inventory author unknown
- Original inventory date, repository revision and branch: Unknown
- Intake date: 2026-11-16 (Asia/Manila)
- Subject: Outside services, tools and callbacks found in the operations repository
- Type: User-supplied repo-scan report; not independently verified here
- Redactions: None required; only setting names and public URL patterns supplied

## User request (verbatim)

add this foor the tools used for this system

## Supplied inventory (verbatim, including formatting escapes)

```text
Here's every outside service I found in the repo. I built this by scanning the code for outside web addresses, setting names (only the names, no values) and scheduled jobs.\
\
\### Platform and hosting\
\| Service | What it does here |\
\|---|---|\
\| \*\*Supabase\*\* | The whole backend: Postgres database, sign-in, the API, 89 Edge Functions, file storage, live updates, and scheduled jobs (\`pg_cron\`, \`pg_net\`) |\
\| \*\*Vercel\*\* | Hosts the React website (\`tmalg.net\`) |\
\| \*\*GitHub / GitHub Actions\*\* | Code, tests, and the scheduled workers: database, code and storage backups, the catalog publish worker, the QuickBooks D2 worker and the vendor FTP pull. The Edge Functions trigger GitHub workflows through the GitHub API. |\
\| \*\*S3-compatible storage\*\* (Cloudflare R2 or Backblaze B2) | Where the database and storage backups are kept. The backup workflow uses the AWS command-line tool to talk to it. |\
\
\### Accounting and payments\
\| Service | What it does here |\
\|---|---|\
\| \*\*QuickBooks Online\*\* (Intuit) | The financial books: customers, vendors, estimates, invoices, POs and payments. Connected by OAuth, with both sandbox and production endpoints. It's the biggest integration (34 functions). |\
\| \*\*QuotaGuard\*\* | A fixed-IP proxy. QuickBooks calls (and vendor FTP when needed) go out through one fixed address, so partners can allowlist it. |\
\| \*\*USAePay\*\* | Card payments, including saving cards |\
\| \*\*Skyline Payments\*\* | The "Pay now" link inside invoice emails (\`app.skylinepayments.com/paynow/…\`) |\
\| \*\*AvaTax\*\* (Avalara) | Sales tax. It's mentioned in code comments as the tax source that QuickBooks runs. I found no direct connection to it in this repo. |\
\
\### Communication\
\| Service | What it does here |\
\|---|---|\
\| \*\*Google Workspace\*\* | Staff sign-in (Google only), Google Calendar sync, and \*\*Gmail\*\* for sending documents and checking replies |\
\| \*\*Intermedia\*\* | The company phone system: click-to-call, the \*\*call-event webhook\*\* (\`intermedia-webhook\`) that feeds the Community leaderboard, and a subscription renewal every 15 minutes |\
\| \*\*PDF renderer (Gotenberg)\*\* | Turns PO and invoice pages into PDFs. It runs as a separate service, apparently on Google Cloud Run (the tests use a \`run.app\` address), and is reached at \`PDF_RENDERER_URL\`. Without it, PO PDFs fall back to QuickBooks' own PDF. |\
\
\### Shipping and tracking\
\| Service | What it does here |\
\|---|---|\
\| \*\*EasyPost\*\* | Tracks the major carriers |\
\| \*\*17TRACK\*\* | Tracks the long tail of smaller carriers |\
\| \*\*24hTrack\*\* | A third tracking provider |\
\| \*\*Carrier websites\*\* (UPS, FedEx, USPS, DHL, OnTrac, TForce) | Only "view on carrier site" links, not connections |\
\
All three tracking services send updates back to one webhook, \`carrier-webhook\`, which works out the sender from the request's signature headers.\
\
\### Vendors and catalog\
\| Service | What it does here |\
\|---|---|\
\| \*\*Vendor FTP/SFTP servers\*\* | Nightly product-feed pulls, run by a GitHub Actions worker that lives in a \*\*separate private repo\*\* |\
\| \*\*Vendors such as TD Synnex, SP Richards, ACM\*\* | Their feeds go into the catalog. TD Synnex has its own invoice ("AP") setting. These are data sources, not live APIs. |\
\
\### Leads and AI\
\| Service | What it does here |\
\|---|---|\
\| \*\*Anthropic (Claude API)\*\* | The PDF Document Extractor and Discovery's buyer research (on your branch) |\
\| \*\*OpenStreetMap: Overpass\*\* | Lead-Gen's map search for businesses near a location (\`generate-leads\`) |\
\| \*\*OpenStreetMap: Nominatim\*\* | Turns addresses into map points and back, called from the browser |\
\| \*\*Leaflet\*\* | The map display library on the Leads screens |\
\| \*\*NCES\*\* (US Department of Education) | The school and district directory Discovery is built on (from your branch's design) |\
\
\### Webhooks and callbacks: outside services calling in\
\- \*\*Event webhooks:\*\* \`carrier-webhook\` (EasyPost, 17TRACK, 24hTrack) and \`intermedia-webhook\` (phone calls).\
\- \*\*OAuth sign-in returns:\*\* \`qb-callback\`, \`google-callback\` and \`intermedia-callback\`.\
\- \*\*Machine-to-machine endpoints:\*\* \`worker-\*\`, \`run-vendor-ftp-pulls\`, \`tracking-sheet-intake\` and the QuickBooks scheduled runs. Each checks its own secret.\
\
All of these are switched off in your sandbox, because no credentials exist locally.\
\
I found a few of these only in code comments or tests, not in a live connection: AvaTax, the PDF renderer's hosting, and the backup storage provider. Alex would know the exact production setup for those.
```

## Evidence limits

The original repo, revision, scan output and deployment settings were not supplied or inspected. Counts, schedules, authentication checks and sandbox state are the report's assertions, not verified current configuration. "Your branch" has no identified owner or branch name; do not infer deployment or ownership. Canonical summary: [operations services](../operations-services.md). This intake creates no tasks or approved decisions.
