# Current website scope and phased roadmap

## Status and authority

The user identifies Alex's November 2026 counter-proposal as the current project scope version. It is the working framework, explicitly not a final specification; phase details are refined together. No separate acceptance/sign-off evidence is supplied. All roadmap entries below are planned scope, not completed work or fixed deadlines. [SRC-005](sources/SRC-005-website-counter-proposal.md), Introduction and sections 1, 3, 6.

Work covers both systems: extend operations first, then build the customer site. Charles is primary customer-site developer; Alex is technical lead, co-developer and PR reviewer. The website serves business buyers with business accounts, customer pricing, purchase orders and tax-exemption support. See [integration design boundaries](integration.md) and [Phase 0 revision guide](phase-0.md).

## Phased roadmap

Phases follow dependencies, may overlap, and are scoped/estimated together when they begin. Each phase ends with demo/review; password-protected staging supports progress review. No fixed delivery dates. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 3, 6.

| Phase | Planned scope | Progress evidence |
|---|---|---|
| 0 - Foundations and plumbing design | Operations onboarding and shared learning notes; feature-to-data mapping; publishing, sync, inbox, linking and pricing design; business-account roles/optional approvals and signup design; investigate AvaTax/certificates and product content. | Operations sandbox/setup reported complete; KB started. Integration design and phase acceptance not evidenced. |
| 1 - Operations catalog foundation | Unified master categories with vendor mapping, AI-assisted classification/staff queue by vendor group; publication/editor tools; vendor-identity protection; minimum-margin guards and below-cost alerts; pilot content enrichment; outbound catalog sync/inbound inbox plumbing. | No implementation evidence supplied. |
| 2 - Customer site v1 | Layout/navigation/browse/search/filter/sort; staff-reviewed signup before pricing and unmatched signup-to-salesperson lead; multi-user business accounts/roles; favorites-based customer prices; My Products/reorder; inbox quote/order submission using existing ship-tos/invoicing; document uploads; account-owner attribution/alerts; Gmail transactional email; CRM support form; event/search tracking; groundwork for logged-in industry experiences, general public site. | No implementation evidence supplied. |
| 3 - Self-service | Order history/status/tracking; online quote acceptance; invoices/payment status with Skyline pay-online links. | No implementation evidence supplied. |
| 4 - Online checkout | Cart payment with method chosen at this phase; AvaTax checkout tax and exemption handling, subject to investigation. | No implementation evidence supplied. |
| Ongoing - Catalog expansion | More vendor groups (e.g. TD SYNNEX and D&H when content is ready), vendor APIs, search analytics to guide expansion. | No implementation evidence supplied. |
| 5+ - Growth and leads | In-house event-triggered marketing (welcome, abandonment, re-engagement, post-purchase), separate email service/subdomain; capture/scoring and hot-lead alerts; SEO, fuller industry storefronts and AI assistance (may move earlier). | No implementation evidence supplied. |

## Boundaries and deferred work

Real-time features are not initially needed; large-scale load testing and Docker as a separate deliverable are removed/deferred. Local Supabase CLI still uses Docker. No new GitHub Actions sync workers; existing vendor FTP worker/manual uploads continue. Event tracking starts in v1 so later analytics/marketing has data. Phase 1 classification is already in scope despite general AI assistance being deferred. [SRC-005](sources/SRC-005-website-counter-proposal.md), Introduction and sections 2, 3, 5.

## Standards across phases

Framework requirements: parameterized SQL; server-side Zod validation; RLS and customer/pricing isolation tests; sanitize content; type/size-check private uploads with short-lived signed URLs; Turnstile and rate limits on public forms/endpoints including events; untrusted browser input; no browser secrets or operations admin credentials on the site; security headers/CSP/dependency alerts; fail-closed checks. Security review every PR and audits before launch and checkout. [SRC-005](sources/SRC-005-website-counter-proposal.md), section 4.

Reliability includes duplicate-order prevention, integration audit logs and Sentry (TMA setup). Target WCAG 2.1 AA. Policies (sale, privacy, returns/shipping) precede order taking. Test pricing/orders/sync, maintain docs throughout, and follow reviewed designs/PRs/recorded releases. Transactional email uses the company mailbox; marketing uses a dedicated service/subdomain with unsubscribe handling. These are requirements to design/verify, not evidence of compliance or implementation. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 4-6.

## Open scope decisions

See [Q-010](questions.md#q-010) for the complete unresolved decision schedule, [Q-009](questions.md#q-009) for environment topology, and [Q-011](questions.md#q-011) for Notion/GitHub tracking boundaries. Do not treat a framework option as a settled design choice.

## History

2026-11-15: SRC-005 supplies the previously missing website framework and phase scope. Earlier statements that website stack/features/Phase 0 deliverables were unknown are superseded as knowledge gaps; the original sources remain unchanged. The earlier original proposal is referenced by the counter-proposal but is unavailable, so its full previous wording and acceptance cannot be reconstructed.
