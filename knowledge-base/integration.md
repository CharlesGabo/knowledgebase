# Operations and customer-site integration

## Current framework direction

These are Alex's framework requirements, identified by the user as the current scope; detailed design remains pending. [SRC-005](sources/SRC-005-website-counter-proposal.md), section 2. This file is the canonical integration outline; the existing operations behavior is in [workflows](workflows.md).

Operations (.net) and website (.com) are separate applications, with separate Supabase development/production projects, Vercel projects and credentials in the framework. Staff use company Google sign-in on operations; customer Auth lives in the website Supabase project, without shared logins. The website uses Next.js; operations remains Vite/React. The pending shared-DEV organization plan needs reconciliation with this project topology: [Q-009](questions.md#q-009).

## Data ownership and flow

One system owns each data type; each type flows one way. Exact payloads, tables and endpoint contracts are not yet designed. [SRC-005](sources/SRC-005-website-counter-proposal.md), section 2.

| Direction | Data / handling |
|---|---|
| Operations to website | Only published catalog, pricing including customer-specific prices, availability, order status, tracking and invoices. |
| Website to operations | New orders, quote requests, new signups and uploaded documents. Orders/quotes/signups enter operations inbox tables for validation and processing. |

Operations owns the full vendor/product/offer catalog. Staff curate web products and their titles/descriptions/images/display prices. Internal vendor costs, offers and internal data never leave operations. Listings, image watermarks/filenames/metadata, SKUs, URLs and stock display must protect vendor identity; show combined availability. Publish tools and safeguards are Phase 1 work, not existing verified features. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 2-3.

Operations validates inbound records, reuses duplicate matching to link web customers to existing Accounts, and converts accepted submissions to real orders through existing PO/QuickBooks flows. The website never writes directly to operations business tables and never holds operations admin credentials. Inbox ingestion permissions must be designed explicitly; this direction does not grant general table write access. [SRC-005](sources/SRC-005-website-counter-proposal.md), section 2.

Use existing database-native patterns: scheduled jobs/database webhooks and purpose-built business endpoints. Stack names `pg_cron` and Edge Functions; Queues only if needed. No new GitHub Actions workers for sync. Final mechanism is a Phase 0 review choice, not completed implementation. The existing vendor FTP worker remains separate from this cross-system sync. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 2, 5.

Reuse operations shipment tracking, payment and QuickBooks integrations; expose results instead of duplicating integration logic. Phase 3 uses Skyline pay-online links. Phase 4 payment method is still undecided; AvaTax feasibility/exemption handling is investigated in Phase 0. See [scope](project-scope.md). [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 2-3, 5, 7.

## Design work still needed

See [Phase 0](phase-0.md) for the review checklist and [Q-010](questions.md#q-010) for pricing, business accounts, pilot vendor, tax and content decisions. Neither the operations code nor migrations are available in this workspace, so no actual schema/function mapping or implementation readiness is claimed.

## History

2026-11-15: SRC-005 establishes the first supplied cross-system integration framework. No earlier approved detailed integration design is available; SRC-003's general Supabase direction remains compatible, with environment topology unresolved.
