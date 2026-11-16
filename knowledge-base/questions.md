# Questions and answers

## Q-019

- Question: Does Alex approve Charles's revised scope and proposed UI-first phase order, and which detailed rules or design additions are accepted?
- Context/source: Approval gap explicitly identified by the user in [SRC-025](sources/SRC-025-revised-scope-intake.md), received 2026-11-16; not an already-sent question or Owner answer.
- Status: open; awaiting Alex review.
- Answer/support: Draft received and preserved. See [scope comparison and review gaps](project-scope.md#revised-proposal-awaiting-review) for phase mapping, asserted decisions, missing supporting documents and internal sequencing questions.
- Remaining: Alex's approval/changes, evidence for draft rules labelled decided, launch boundaries and detailed tax/payment design. SRC-005 remains the designated framework in the meantime.
- Clarifier: Alex with Charles; use the existing Questions for Alex process or another appropriate format Alex accepts (SRC-024). No external posting/monitoring.

## Q-018

- Follow-up 2026-11-16: [SRC-024](sources/SRC-024-work-google-tools-and-questions.md) identifies additional [work collaboration tools](technology.md#work-collaboration-tools), distinct from the CC runtime services listed in this answer.

- Question (verbatim): can you give me the tools used in the C
- Source: [SRC-023](sources/SRC-023-cc-tools-question.md), 2026-11-16. "C" interpreted as Command Center (CC) from context.
- Status: answered from available reported inventory, with deployment limits retained.
- Answer/support: [Core architecture](technology.md#current-reported-operations-architecture) describes Vite/React on Vercel, Supabase/Postgres, Deno Edge Functions and GitHub Actions. [Operations services](operations-services.md) is the canonical external-service inventory from SRC-018, supplemented by Alex's payment clarification SRC-022. It covers accounting/payments, communication, tracking, catalog feeds, documents, AI/maps and backup tools.
- Limits: This is CC's reported stack, not the planned Next.js customer website stack. AvaTax's live arrangement, PDF-renderer hosting and backup provider remain unconfirmed under Q-015. Discovery branch/design findings are not proof of production deployment. No code, account or service was accessed for verification, and tasks were not changed.

## Q-017

- Question (verbatim): explain this to me
- Context/source: User asks for an explanation of Alex's VA purchase-card and website-payment message in [SRC-022](sources/SRC-022-va-pcard-payment-flow.md); received 2026-11-16.
- Status: answered from supplied messages.
- Answer/support: See [customer payment patterns](workflows.md#customer-payment-patterns): immediate VA purchase-card charges through USAePay in CC versus predominant invoice-link/check/ACH payments for others, with net-30 terms reported for most customers in SRC-021. Website card processing is a future option, not a chosen provider.
- Limits: Exact payment-status automation remains partially answered under Q-016; website processor remains open under Q-010-I. No implementation or task changes inferred.

## Q-016

- Alex follow-up, received 2026-11-16: [SRC-021](sources/SRC-021-net-30-payment-flexibility.md) confirms the need for multiple payment methods and customers outside the website, and states API payment retrieval should be possible. [SRC-022](sources/SRC-022-va-pcard-payment-flow.md) clarifies current customer/payment patterns. See [canonical workflows](workflows.md#customer-payment-patterns). The policy need for flexibility is answered; specific API coverage, automation readiness and delay remain unresolved. Overall status remains partially answered. The earlier SRC-020 note below records history before these replies.

- Follow-up 2026-11-16: [SRC-020](sources/SRC-020-website-only-payment-question.md) asks if website-only customer payments could simplify tracking. See [assistant design assessment](integration.md#website-as-a-payment-entry-point): a shared entry point may help, but it does not remove reconciliation or establish business approval to restrict payment channels. Status remains partially answered; no Alex reply to this proposal or task change.

- Question: Should CC automatically pick up payments recorded in QuickBooks outside CC (pay-now links, checks, bank transfers), or should the customer website handle this?
- Original question and Alex's reply: preserved verbatim in [SRC-019](sources/SRC-019-qb-cc-accounting-sync.md); original communication date unknown; received 2026-11-16.
- Status: partially answered by Alex.
- Answer/support: Alex wants more accounting functionality in CC and reports W76 work to align QB/CC documents, with preferred editing in CC and scanning of QB invoice/PO changes. Canonical status and the distinction between the user's payment premise and Alex's reply are in [accounting alignment](workflows.md#accounting-and-quickbooks-alignment).
- Remaining: Whether W76 detects external payments and updates invoice paid/balance status automatically, schedule/latency, remaining flaw and completion/deployment evidence, and the exact website-facing payment-status contract. Alex did not explicitly assign reconciliation implementation to the website.
- Interpretation: Existing SRC-005 framework still says reuse operations integrations and expose results; do not infer a new website-to-QB reconciliation responsibility or general bidirectional website data sync from "two way read." See [integration](integration.md#payment-status-and-w76).
- Clarifier: Alex. If needed, use the user's Notion Questions for Alex area; area label for this topic is unknown. Suggested follow-up (not sent): "Will W76 also update CC invoice balances/payment status for payments recorded directly in QuickBooks, and what delay should the website expect?"
- Pending work: Alex's own remaining flaw fix is [T-007](tasks.md#t-007); no Charles assignment or completion inferred.

## Q-015

- Question: What are the actual production tax connection, PDF-renderer hosting and backup storage provider for Command Center?
- Context/source: Inferred evidence gap from the supplied inventory [SRC-018](sources/SRC-018-cc-service-inventory.md), received 2026-11-16; not a question already asked of Alex.
- Status: open.
- Answer/support: The scan reports code-comment/test evidence and candidate providers, not live configuration. See the canonical [service inventory](operations-services.md) for each qualification.
- Remaining: Production evidence for these three details; source revision/branch and scan date also unknown. No external configuration checked.
- Clarifier: Alex. If needed, use the existing Notion Questions for Alex area, **Area: Access / tools**; no posting or monitoring authorized.

## Q-014

- Question (verbatim): what does this mean what is command center
- Source: [SRC-017](sources/SRC-017-command-center-explanation.md), 2026-11-16.
- Status: answered from supplied message and existing context.
- Answer/support: Command Center (CC) is the name given to the backend/operations site. See [overview](overview.md#current-understanding) for the canonical name/context and [business workflows](workflows.md#current-reported-operations-baseline) for its reported staff functions. The message says much work has gone into it, particularly order-processing screens, and development remains ongoing. The customer website is one large project within that broader work.
- Interpretation: The user may encounter a substantial existing order-processing interface; screen complexity does not establish implementation completeness. Website integration remains governed by the existing framework, not a new assignment inferred from this message.
- Limits: The excerpt's speaker and original date are not explicitly supplied; no code/UI inspection or new task/status change occurred.

## Q-013

- Follow-up 2026-11-15: [SRC-014](sources/SRC-014-phase-0-task-explanation.md) asks what to do for each current task T-001 through T-006. Explain practical actions and suggested outputs using the Phase 0 guide; actual schema names require operations-repository inspection. Exact phase acceptance remains unresolved. Task status and dates unchanged.

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

- Follow-up 2026-11-16: [SRC-024](sources/SRC-024-work-google-tools-and-questions.md) adds Alex-reported work-account Drive access and optional Sheets/Docs/Apps Script use; see [work collaboration tools](technology.md#work-collaboration-tools). This does not resolve development-environment access or release mechanics.

- Follow-up 2026-11-16: [SRC-018](sources/SRC-018-cc-service-inventory.md) adds a supplied operations-service scan, summarized in [operations services](operations-services.md). It supplements architecture context but does not verify live configuration, access or website stack changes. Status remains partially answered.

- Question: Which operations architecture, environments, access and review rules apply to website development?
- Status: partially answered
- Answer/support: SRC-003 establishes sandbox work and conditional shared DEV. [SRC-005](sources/SRC-005-website-counter-proposal.md) specifies Next.js App Router/React/TypeScript, Supabase and separate Vercel hosting/Auth/project boundaries; reviewed designs and PRs, Alex approval and TMA production migrations. See [technology](technology.md), [integration](integration.md), [development](development.md).
- Remaining: Shared/dedicated DEV relationship (Q-009), exact access/release mechanics (Q-007), concrete schemas/contracts and exact dependency versions.
- Clarifier: Alex.
- History: Initially unknown from SRC-001; partially answered by SRC-003, expanded by SRC-005. No detailed design completion claimed.

## Q-003

- Follow-up 2026-11-16: [SRC-019](sources/SRC-019-qb-cc-accounting-sync.md) adds Alex's reply about W76/accounting alignment. External payment-status automation and the website-facing contract remain partially answered under [Q-016](#q-016); checkout provider choices remain unchanged.

- Follow-up 2026-11-16: The [reported operations inventory](operations-services.md), from SRC-018, names existing payment/tracking/accounting candidates and distinguishes carrier links from integrations and vendor feeds from APIs. These are operations findings, not approval to expose each service on the website. Concrete website contracts and Phase 4 payment choice remain unresolved.

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

- Follow-up 2026-11-16: The user reports Alex plans the shared DEV database move this week. See [current timing and status](technology.md#website-environments-and-platform-direction) and [SRC-016](sources/SRC-016-shared-dev-week-plan.md). This partially answers timing with a planned window; exact date, completion and access remain unconfirmed. Original SRC-003 plan retained.

- Question: When will shared DEV be ready, what access will each participant receive, and who reviews/tests/promotes changes to production?
- Status: partially answered
- Answer/support: SRC-003 plans shared DEV for ready-for-review changes. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 4-6, states Alex reviews/approves PRs, main requires approval, PR tests/preview deployments run, operations changes are verified in DEV, and TMA applies production database migrations. Security review every PR and launch/checkout audits are required.
- Remaining: DEV availability/access, exact testing assignments, frontend deployment/rollback and promotion mechanics, and Q-009's topology.
- Clarifier: Alex.
- History: Previously open because SRC-003 did not name detailed review responsibilities; SRC-005 partially answers these.

## Q-008

- Follow-up 2026-11-16: SRC-025 supplies a scope draft marked Phase 0 drafted/under review. See [proposal status](project-scope.md#revised-proposal-awaiting-review). The linked full deliverable package and Alex's acceptance are not supplied; status remains partially answered and tasks are unchanged.

- Question: What deliverables define Phase 0 and when is it complete?
- Status: partially answered
- Answer/support: [SRC-005](sources/SRC-005-website-counter-proposal.md), Phase 0, defines onboarding/system notes, feature-to-data mapping, integration design, business-account/signup design and AvaTax/content investigations. See [Phase 0 guide](phase-0.md). Section 6 requires scoping at phase start and demo/review at phase end; no fixed deadlines.
- Remaining: Agreed acceptance checklist/estimates and evidence of Alex's review/completion. Setup completion is not Phase 0 design completion.
- Clarifier: Alex with Charles.
- History: Initially undefined in available material; SRC-005 now supplies deliverables, not a completion date.

## Q-009

- Follow-up 2026-11-16: [SRC-016](sources/SRC-016-shared-dev-week-plan.md) adds reported migration timing and shared-work intent, but does not identify the projects or resolve website/operations topology. Status remains open.

- Question: How do the dedicated development environment and separate website/operations dev projects in the framework relate to Alex's planned shared DEV organization? Which project is shared, and is a separate website sandbox needed for Phase 0?
- Context/source: [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 1-2/5, describes dedicated development plus separate per-system dev/prod projects; SRC-003 describes moving DEV into a shared organization. These could coexist, but their mapping is unconfirmed and original communication order is unknown.
- Status: open
- Answer/support: No definitive mapping supplied. Do not treat either source as silently overriding the other. Operations sandbox existence is resolved separately by SRC-004.
- Clarifier: Alex. Recommend Notion Questions for Alex, Area: Access / tools.

## Q-010

- Revised-scope intake, 2026-11-16: SRC-025 asserts some pricing/industry rules are decided, but the user identifies the draft as pending Alex review and supplies no underlying approvals for those claims. See [review gaps](project-scope.md#revised-proposal-awaiting-review). Keep existing subquestion statuses and SRC-005 timing as historical/current-framework references; proposed timing is separate.

- Payment evidence update, 2026-11-16: SRC-022 says USAePay or another card processor could serve the website; see [customer payment patterns](workflows.md#customer-payment-patterns). Q-010-I remains open because no final website processor/method selection is supplied. SRC-021 confirms flexible customer payment channels are required.

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

2026-11-16 evidence update: SRC-018 reports only comment references for AvaTax and no direct repo integration, and reports operations payment providers. See [operations services](operations-services.md). This does not answer Q-010-G's website feasibility/exemption handling or Q-010-I's checkout choice; both remain open.

## Q-011

- Follow-up 2026-11-16: [SRC-024](sources/SRC-024-work-google-tools-and-questions.md) accepts questions in any appropriate format. See [communication guidance](development.md#notion-questions-and-task-tracking). It does not settle where cross-system tasks or end-shift updates belong; status remains open.

- Question: For work spanning operations and the website, which tasks/updates belong in Notion versus GitHub Issues, and do end-shift issue comments remain required?
- Context/source: SRC-001 says operations work comes from GitHub Issues and requires issue comments. [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 1/6, specifies Notion Kanban and says Work Log replaces separate end-shift updates. This may be a scope distinction, but the cross-system process is not explicit.
- Status: open
- Answer/support: Use the known Notion Questions for Alex area to request clarification manually; no authority to change operations instructions is inferred.
- Clarifier: Alex. Other Notion area labels unknown.
