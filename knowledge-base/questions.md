# Questions and answers

## Q-013

- Question (verbatim): explain what i have to do for phase 0
- Source: [SRC-009](sources/SRC-009-phase-0-explanation.md), 2026-11-15.
- Status: partially answered; linked follow-up to Q-008.
- Answer/support: SRC-005 defines operations learning/system notes, initial feature-to-data mapping, integration design for review, business-account/signup design, and AvaTax/exemption/product-content investigations. See the canonical [Phase 0 guide](phase-0.md). Operations setup is already complete by user report (SRC-004); design completion is not evidenced. Suggested working order and document packaging are assistant interpretations, not additional Owner assignments.
- Remaining: Exact acceptance checklist/estimates and Alex's review remain unresolved in Q-008; business choices in Q-010 and environments in Q-009 remain open. No dates or new individual commitments created.

## Q-012

- Question (verbatim): are there any task for me tomorrow
- Context/source: [SRC-006](sources/SRC-006-tomorrow-tasks-question.md), asked 2026-11-15; tomorrow is 2026-11-16 in Asia/Manila.
- Status: answered from available records; no Owner reply supplied
- Answer/support: [LEGACY-T-008](tasks.md#reported-progress-and-next-session) records Charles's intention to revise the Phase 0 operations-to-website integration approach using the current framework. SRC-004's original date is unknown, so its earlier relative 'tomorrow' is not independently a confirmed November 16 appointment. No fixed Owner deadline or additional dated assignment is recorded. Operations setup LEGACY-T-007 is already complete by user report.
- Suggested session focus: Use the [Phase 0 checklist](phase-0.md#suggested-revision-checklist) to map features/data, draft publication/sync/inbox/customer-linking/pricing design, and flag open decisions. These are suggestions, not new commitments.
- Remaining limits: No live task board inspected; the supplied knowledge base cannot establish whether later assignments exist.
- Recorded: 2026-11-15. No task status or deadline changed.


Q-001 through Q-004 were inferred during initial organization. Q-005 and Q-006 summarize the user's supplied question; Q-007 and Q-008 are follow-ups inferred from the reply. Q-009 through Q-011 arise from the newly supplied setup/scope; Q-010 sub-IDs preserve the framework's open decisions. The original exchange is preserved in SRC-003. Entries added/updated 2026-11-15; original communication dates unknown and no deadlines assigned.

## Q-001

- Question: What audience, features and workflows are approved for the client-facing website, and how does it relate to the employee-only platform?
- Context/source: Initially a gap between SRC-002's website request and SRC-001's employee-only context.
- Status: partially answered
- Answer/support: [SRC-005](sources/SRC-005-website-counter-proposal.md) supplies the user-designated current framework: business-customer website, separate app/Auth, operations-first integration and phased scope. See [scope](project-scope.md) and [integration](integration.md).
- Remaining: Detailed phase specifications and approval of unresolved business choices; framework is not final. See Q-010.
- Clarifier: Alex, technical lead/Owner, with Charles.
- History: Initially unknown; SRC-003 gave environment direction, SRC-005 now supplies scope. No earlier approved website scope is silently replaced.

## Q-002

- Question: Which operations architecture, environments, access and review rules apply to website development?
- Status: partially answered
- Answer/support: SRC-003 establishes sandbox work and conditional shared DEV. [SRC-005](sources/SRC-005-website-counter-proposal.md) specifies Next.js App Router/React/TypeScript, Supabase and separate Vercel hosting/Auth/project boundaries; reviewed designs and PRs, Alex approval and TMA production migrations. See [technology](technology.md), [integration](integration.md), [development](development.md).
- Remaining: Shared/dedicated DEV relationship (Q-009), exact access/release mechanics (Q-007), concrete schemas/contracts and exact dependency versions.
- Clarifier: Alex.
- History: Initially unknown from SRC-001; partially answered by SRC-003, expanded by SRC-005. No detailed design completion claimed.

## Q-003

- Question: Which catalog, pricing, punchout, order, payment, tax and accounting integrations must the website expose, and through what interfaces?
- Status: partially answered
- Answer/support: [SRC-005](sources/SRC-005-website-counter-proposal.md) defines curated publishing, customer favorites pricing, inbound order/quote/signup inboxes, reuse of operations order/PO/QuickBooks flows, tracking/payment results, Phase 3 Skyline links, and AvaTax investigation before Phase 4. Existing FTP/manual ingestion continues; vendor APIs are later scope. See [integration](integration.md).
- Remaining: Concrete interfaces/schema mappings, pricing/business rules, content sources, checkout payment method, and whether punchout belongs in website scope (not explicitly included).
- Clarifier: Alex; unresolved scheduled choices in Q-010.
- History: SRC-003 first confirmed catalog relevance; SRC-005 expands planned integration scope without proving implementation.

## Q-004

- Question: Can the relevant upstream authoritative documents and their versions be supplied when needed to validate implementation decisions?
- Context/source: SRC-001 says upstream documents prevail over its summary, but they are unavailable in this workspace.
- Status: open
- Answer/support: Unknown; initial KB can still use the summary with its stated limitations.
- Clarifier: User or document owner (unknown).

## Q-005

- Question: For the client-facing website, should the user work in a sandbox or directly in DEV, and how does work progress toward production?
- Context/source: User's question and Alex's answer in [SRC-003](sources/SRC-003-website-environments.md).
- Status: partially answered
- Answer/support: Phase 0 can happen entirely in the sandbox. Later, once DEV is shared, unfinished work stays in the sandbox and only review-ready changes headed for production soon go to DEV. Production stays separate. [D-003](decisions.md#d-003)
- Remaining: Shared DEV readiness/access and exact production testing/promotion procedure (Q-007).
- Clarifier: Alex.

## Q-006

- Question: Will Alex set up the website repository and sandbox environments?
- Status: partially answered
- Answer/support: SRC-003 says no website repository yet and Alex can create it when needed. [SRC-004](sources/SRC-004-completed-setup.md) now confirms Charles already has a working operations sandbox and completed setup; no need to treat that setup as undone. [SRC-005](sources/SRC-005-website-counter-proposal.md) describes a dedicated development environment and preview deployments as intended provisions, not verified creation.
- Remaining: Website repo creation timing, whether a distinct website sandbox is needed now and who provisions it; dedicated/shared DEV topology (Q-009).
- Clarifier: Alex.
- History: Earlier sandbox completion was unknown. SRC-004 resolves operations sandbox existence by user report, not website/shared DEV provisioning.

## Q-007

- Question: When will shared DEV be ready, what access will each participant receive, and who reviews/tests/promotes changes to production?
- Status: partially answered
- Answer/support: SRC-003 plans shared DEV for ready-for-review changes. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 4-6, states Alex reviews/approves PRs, main requires approval, PR tests/preview deployments run, operations changes are verified in DEV, and TMA applies production database migrations. Security review every PR and launch/checkout audits are required.
- Remaining: DEV availability/access, exact testing assignments, frontend deployment/rollback and promotion mechanics, and Q-009's topology.
- Clarifier: Alex.
- History: Previously open because SRC-003 did not name detailed review responsibilities; SRC-005 partially answers these.

## Q-008

- Question: What deliverables define Phase 0 and when is it complete?
- Status: partially answered
- Answer/support: [SRC-005](sources/SRC-005-website-counter-proposal.md), Phase 0, defines onboarding/system notes, feature-to-data mapping, integration design, business-account/signup design and AvaTax/content investigations. See [Phase 0 guide](phase-0.md). Section 6 requires scoping at phase start and demo/review at phase end; no fixed deadlines.
- Remaining: Agreed acceptance checklist/estimates and evidence of Alex's review/completion. Setup completion is not Phase 0 design completion.
- Clarifier: Alex with Charles.
- History: Initially undefined in available material; SRC-005 now supplies deliverables, not a completion date.

## Q-009

- Question: How do the dedicated development environment and separate website/operations dev projects in the framework relate to Alex's planned shared DEV organization? Which project is shared, and is a separate website sandbox needed for Phase 0?
- Context/source: [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 1-2/5, describes dedicated development plus separate per-system dev/prod projects; SRC-003 describes moving DEV into a shared organization. These could coexist, but their mapping is unconfirmed and original communication order is unknown.
- Status: open
- Answer/support: No definitive mapping supplied. Do not treat either source as silently overriding the other. Operations sandbox existence is resolved separately by SRC-004.
- Clarifier: Alex. Recommend Notion Questions for Alex, Area: Access / tools.

## Q-010

- Question: Which open framework choices have now been decided, and what are the answers?
- Context/source: [SRC-005](sources/SRC-005-website-counter-proposal.md), section 7. The document deliberately schedules these decisions rather than resolving them.
- Status: open
- Answer/support: No approved answers supplied. Track each row separately by its stable sub-ID; close individual rows only with evidence.
- Clarifier: Alex with Charles; recommend Notion Questions for Alex when needed. Other area labels unknown.

| Sub-ID | Open decision | Framework timing | Status |
|---|---|---|---|
| Q-010-A | Public pricing vs login-to-view vs quote request; likely per-product setting is an option, not approval | Phase 0 | open |
| Q-010-B | Pricing precedence, public markups and minimum margins | Phase 0 | open |
| Q-010-C | Business-account roles and order approval | Phase 0 | open |
| Q-010-D | Industry segments and logged-in experience | Phase 0-2 | open |
| Q-010-E | First pilot vendor group | Phase 0 | open |
| Q-010-F | Product content sources, Icecat coverage and distributor feeds | Phase 0-1 | open |
| Q-010-G | AvaTax feasibility and exemption-certificate handling | Investigate Phase 0; build Phase 4 | open |
| Q-010-H | License/prescription verification for regulated medical products | Before those products go online | open |
| Q-010-I | Checkout payment method(s) | Phase 4 | open |
| Q-010-J | Who provides copy, branding and imagery | Phase 2 | open |
| Q-010-K | Policy content: sale, returns, shipping, privacy | Before taking orders | open |
| Q-010-L | AI assistant timing/scope | Revisit after Phase 3; may move earlier | open |
| Q-010-M | Marketing sending service | Phase 5 | open |

Each row currently has answer/support unknown beyond SRC-005's stated options/timing. Framework tensions to resolve under Q-010-A: Phase 2 says staff approval before pricing is visible while section 7 leaves public pricing open. Do not infer a final public pricing rule.

## Q-011

- Question: For work spanning operations and the website, which tasks/updates belong in Notion versus GitHub Issues, and do end-shift issue comments remain required?
- Context/source: SRC-001 says operations work comes from GitHub Issues and requires issue comments. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 1/6, specifies Notion Kanban and says Work Log replaces separate end-shift updates. This may be a scope distinction, but the cross-system process is not explicit.
- Status: open
- Answer/support: Use the known Notion Questions for Alex area to request clarification manually; no authority to change operations instructions is inferred.
- Clarifier: Alex. Other Notion area labels unknown.
