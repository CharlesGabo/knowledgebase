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

## Payment status and W76

The [accounting alignment status](workflows.md#accounting-and-quickbooks-alignment) records Alex's SRC-019 reply about extending CC accounting and W76's QB/CC document alignment. It does not confirm external-payment reconciliation is complete or that invoice paid status is automatically available to the website. See [Q-016](questions.md#q-016).

The existing SRC-005 direction remains: reuse operations integrations and expose their results. Interpreting Alex's reply as placing accounting expansion in CC is supported by her stated intent, but she does not explicitly settle the detailed external-payment/website responsibility question. Her description of QB/CC "two way read" does not change the framework's separate operations-to-website and website-to-operations data ownership rules. No new integration decision supersedes that framework.

## Website as a payment entry point

The user asks whether requiring customer payments through the website would simplify tracking. [SRC-020](sources/SRC-020-website-only-payment-question.md) This is a proposal/question, not approved payment policy. **Assistant assessment:** a common website payment entry point could simplify the customer journey and link payment attempts to invoices, while still offering multiple payment methods. It would not by itself keep processor, CC and QuickBooks records aligned. The design must distinguish payment initiation from confirmed payment and handle subsequent adjustments and exceptions.

**Earlier assistant suggestion for review (SRC-020):** prefer a common payment entry point using the existing operations/payment integrations, with a defined path for confirmed payment status to reach CC/QB and then the website. Do not create an independent website accounting record as a shortcut around reconciliation. At that point, requirements for retaining other payment channels were unknown.

**Alex's subsequent clarification:** Customer payment flexibility and non-website payments must remain supported; see [customer payment patterns](workflows.md#customer-payment-patterns), [SRC-021](sources/SRC-021-net-30-payment-flexibility.md) and [SRC-022](sources/SRC-022-va-pcard-payment-flow.md). A website payment page can be an additional entry point, but website-only payment cannot be assumed as the tracking solution. Alex expects API retrieval of payments; implementation and timing remain unconfirmed. She offers USAePay or another card processor as website options, without selecting a provider or moving checkout into Phase 0.

This does not replace W76's invoice/PO alignment work or settle Q-016. Phase 3's invoice payment links and Phase 4's checkout scope remain as stated in SRC-005; no implementation, provider choice or new task is approved by the question.

## Design work still needed

SRC-025 supplies a proposed revised scope with development-only connection work in proposed Phase 2, live catalog/connection activation in proposed Phase 3, and detailed payment/tax options. These are unapproved proposals, not changes to SRC-005's phase numbering or completed contracts. See the canonical [comparison and review gaps](project-scope.md#revised-proposal-awaiting-review); the linked detailed design package remains unavailable here.

The [reported operations service inventory](operations-services.md) supplies provider and callback context from SRC-018 for investigation. It does not establish concrete cross-system contracts or authorize copying operations integrations into the website; production details and branch-only findings retain their stated limits.

See [Phase 0](phase-0.md) for the review checklist and [Q-010](questions.md#q-010) for pricing, business accounts, pilot vendor, tax and content decisions. Neither the operations code nor migrations are available in this workspace, so no actual schema/function mapping or implementation readiness is claimed.

## History

2026-11-15: SRC-005 establishes the first supplied cross-system integration framework. No earlier approved detailed integration design is available; SRC-003's general Supabase direction remains compatible, with environment topology unresolved.
