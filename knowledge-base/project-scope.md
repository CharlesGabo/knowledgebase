# Current website scope and phased roadmap

## Status and authority

The user identifies Alex's November 2026 counter-proposal as the current project scope version. It is the working framework, explicitly not a final specification; phase details are refined together. No separate acceptance/sign-off evidence is supplied. All roadmap entries below are planned scope, not completed work or fixed deadlines. [SRC-005](sources/SRC-005-website-counter-proposal.md), Introduction and sections 1, 3, 6.

Work covers both systems: extend operations first, then build the customer site. Charles is primary customer-site developer; Alex is technical lead, co-developer and PR reviewer. The website serves business buyers with business accounts, customer pricing, purchase orders and tax-exemption support. See [integration design boundaries](integration.md) and [Phase 0 revision guide](phase-0.md).

## Revised proposal awaiting review

On 2026-11-16, Charles supplied a [revised project scope](<Phase 0-PROJECT_SCOPE.md>) and explicitly said it is **still up for review by Alex**. [SRC-025](sources/SRC-025-revised-scope-intake.md) preserves the intake and an exact document snapshot. This is the latest user-authored proposal, not an approved replacement for SRC-005. The roadmap below this section still describes SRC-005; name the source when using phase numbers.

The draft's rationale is to inspect a full clickable website using sample data before changing CC, then map each screen to its required data and test the connection in development before enabling it live with the catalog.

| Work | SRC-005 framework | SRC-025 proposed sequence |
|---|---|---|
| Foundations/design | Phase 0 | Phase 0, marked drafted/under review |
| Complete clickable UI with sample data | No separate phase | New Phase 1; no CC connection |
| Map/build/test the connection | Phase 0 design; Phase 1 plumbing | New Phase 2; development only |
| Catalog tools and live connection | Phase 1 | Phase 3 |
| Customer website v1 / launch | Phase 2 | Phase 4 |
| Customer self-service | Phase 3 | Phase 5 |
| Checkout and tax | Phase 4 | Phase 6 |
| Catalog expansion | Ongoing | Ongoing |
| Growth/marketing and later AI | Phase 5+ | Phase 7+ |

All proposed implementation, launch and live activation steps remain subject to design/review and existing deployment authority. They are not dated assignments, permission to change production, or evidence of provisioning. Existing tasks are unchanged.

**Review gaps and evidence limits:**

- Section 10 calls login-only prices, "Request a quote" for products outside a price list, and no fixed industry "Decided." The user has submitted the whole draft for review; no supporting Alex answers for these specific decisions were supplied with it. Keep Q-010-A/B/D open and distinguish the draft's asserted rules from approved rules.
- The draft names Cloudflare R2 as the backup provider and describes a definite QuickBooks/Avalara tax setup. Earlier inventory evidence was qualified (Q-015); these are now user-authored assertions, not independently checked configuration or an Owner confirmation. Detailed tax-estimate/final-invoice and certificate handling is proposed design, not demonstrated capability or proof of matching tax amounts.
- Additional page details include a printer-supplies finder, quick-order uploads, address-change requests and a tax-exemption page. Existing printer data and CC behavior are assertions in the draft; supporting code/data and linked design documents have not been supplied here.
- Phase 4's account dashboard lists recent orders and unpaid invoices, while detailed orders/invoices are assigned to Phase 5. Clarify the minimum data needed at first launch. Section 3 also says most CC changes are built in Phase 3 while Phase 2 explicitly builds the connection; reconcile that summary with the detailed sequence.
- Links to `customer-site/`, nested `knowledge-base/` and `README.md` refer to a supporting package absent at those locations in this repository. Preserve the original; missing references limit verification of its research, schema checks and design details.
- Phase 0 is described as drafted/under review. This supplies a scope draft, not the full linked package, Alex acceptance, or evidence that all Phase 0 work is complete.

Approval tracking: [Q-019](questions.md#q-019). Relevant existing questions remain Q-008 (acceptance), Q-009 (environment mapping), Q-010 (business choices), Q-015 (production service details) and Q-016 (payment reconciliation). No earlier decision is superseded merely because this draft is newer.

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
