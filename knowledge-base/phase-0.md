# Phase 0 review and revision guide

## Current deliverable

Phase 0 is Foundations and Plumbing Design. It covers operations learning and documentation, mapping initial website features to operations data, integration design for review, business-account/signup design, and investigations into AvaTax/exemptions and product content. [SRC-005](sources/SRC-005-website-counter-proposal.md), section 3. Exact acceptance checklist and estimates are still to be agreed; completing setup alone does not complete Phase 0.

Charles reports the operations sandbox running with a test persona and the weekend checklist complete. This supports doing operations learning/design now; it does not establish a separate website environment or working sync. [SRC-004](sources/SRC-004-completed-setup.md)

## Suggested revision checklist

These are assistant suggestions for Charles's stated next-work-session revision, derived from the framework. They are not extra approved deliverables or implementation decisions. The actual draft to revise has not been supplied.

1. Describe two separate applications and Auth/data boundaries, using the [integration framework](integration.md). Do not propose direct website writes into operations business tables or operations admin credentials on the site.
2. Map each initial customer feature to data owner, operations source, safe outbound projection or inbound inbox, identity/permission checks and target phase. Inspect actual schema/RPCs in the operations repository before naming contracts.
3. Design catalog publication: staff curation, public-safe fields, vendor-identity removal, combined availability and price safety. Keep vendor offers/costs private to operations.
4. Document sync candidates (`pg_cron`, webhooks, Edge Functions) and the selected design for Alex's review. Include proposed duplicate prevention, retries, error/audit handling and tests; these mechanisms are design suggestions until approved. No new sync Actions worker.
5. Outline order/quote/signup inbox validation, customer-to-Account duplicate matching, staff signup approval, existing ship-tos, account-owner attribution and the existing order/PO/QuickBooks path.
6. Separate customer organization membership/roles/optional order approval from staff accounts. Propose pricing precedence, favorite-price handling, public-price visibility and minimum-margin rules, marking unresolved rules for Alex.
7. Record AvaTax/exemption and content-source investigation findings; do not start checkout/payment implementation as Phase 0 scope. Keep vendor APIs in later expansion unless Alex changes scope.
8. Identify security/test evidence needed: cross-customer/pricing isolation, fail-closed access, private uploads, input validation, public endpoint protection and duplicate-order prevention. Link the [cross-phase standards](project-scope.md#standards-across-phases).
9. Split the reviewed design into operations-first implementation tasks for later phases. Flag [environment topology](questions.md#q-009) and [open business decisions](questions.md#q-010); record known facts and assumptions separately.

## Asking Alex

First use the knowledge base for an answer. For an Owner decision or missing answer, recommend the existing Notion **Questions for Alex** area, with context, question, options/recommendation and what can proceed meanwhile. Use **Area: Access / tools** for access/tool issues only; other area labels are unknown. The user posts manually and can paste the response here for updates. [SRC-004](sources/SRC-004-completed-setup.md)

## History

2026-11-15: Created from the current scope and user's intention to revise the integration approach 'tomorrow'. This is relative timing supplied by the user, not an Owner-imposed deadline. No Phase 0 design approval or completion is recorded.
