# Business workflows

## Current reported operations baseline

All entries below come from [SRC-001 ?1](../tma-ops-processes.md). Website reuse and boundaries are now defined by SRC-005 in [integration](integration.md); individual customer capabilities are sequenced in [scope](project-scope.md).

| Area | Reported behavior |
|---|---|
| Accounts | A converted lead becomes an Account. Customer is an Account lifecycle status (`lead`, `customer`, `inactive`), not a separate record. See [D-001](decisions.md#d-001). |
| Catalog | Uploaded or nightly FTP/SFTP vendor feeds consolidate products by manufacturer part number; each product can have multiple vendor offers with separate costs. |
| Favorites | Account-specific catalog item, vendor and sell price form a per-customer price book. |
| Sales | Cart uses TMA sell prices; accepted quotes become orders. |
| Purchasing | Order processing splits POs by vendor, applying freight rules by zone. Routing can hide the end customer's name from vendors. |
| Fulfillment | Shipment tracking returns to the order. |
| Accounting | Customers, invoices, estimates and POs sync with QuickBooks. Card payments use a gateway and post to QuickBooks; tax uses a tax integration. |

## Accounting and QuickBooks alignment

**Alex's answer, received 2026-11-16:** Alex wants to add more accounting functionality to Command Center (CC). She describes W76 as a long-running effort to keep QuickBooks (QB) and CC aligned: orders should ideally be edited in CC, while CC scans documents and records invoice/purchase-order changes made in QB when those occur. She describes this as difficult "sort of a two way read" and reports W76 almost done, with a remaining flaw to fix. This is reported work in progress, not a completed/deployed reconciliation guarantee. [SRC-019](sources/SRC-019-qb-cc-accounting-sync.md)

**User's question/premise:** Card charges inside CC immediately mark invoices paid, whereas pay-now links, checks and bank transfers are recorded in QB without automatic CC awareness. Preserve this as the user's description; Alex's reply does not explicitly verify every payment path or confirm automatic paid-status updates, payment matching, polling frequency or coverage of externally recorded payments. [Q-016](questions.md#q-016) remains partially answered.

**Pending Alex-owned plan:** [T-007](tasks.md#t-007) tracks the remaining W76 flaw fix. Alex says "tomorrow," but the communication date is unknown, so no calendar date or deadline is inferred. No work is assigned to Charles by this exchange. The website responsibility boundary remains in [integration](integration.md#payment-status-and-w76).

## Customer payment patterns

**Alex's clarification, received 2026-11-16:** Most customers have **net 30**, meaning 30 days to pay, and customers must retain flexibility to use checks, cards or ACH (electronic bank payments). Not all customers use the website. Alex expects payments can be retrieved through the API; the message does not establish which API, live automation or timing. [SRC-021](sources/SRC-021-net-30-payment-flexibility.md)

Alex reports that card transactions run through **USAePay in Command Center** are mostly for **VA (Veterans Administration) hospital customers**. Those customers supply a **p-card (purchase card)** with an order, and staff charge it immediately. She says just about everyone else pays using the **QuickBooks pay link via Skyline, a check or ACH**. These are reported predominant patterns, not exclusive rules for every customer. [SRC-022](sources/SRC-022-va-pcard-payment-flow.md)

For example (hypothetical), a VA order could be charged to its purchase card at order time, while a net-30 customer could place an order and pay the invoice later through an available channel. Payment timing and payment method are separate choices. These clarifications refine the user's earlier payment premise without proving all invoice-status behavior. See [Q-016](questions.md#q-016).

Alex says the customer site could use USAePay or another card merchant/processor for card transactions. This is an option, not a final provider selection or completed integration. In her latest message, "CC" names Command Center, while "cc transactions" means credit-card transactions. See [Q-017](questions.md#q-017) and [integration implications](integration.md#website-as-a-payment-entry-point).

## Website catalog direction

Alex says the catalog is crucial to the website and understanding vendor-file ingestion through the FTP puller is important. Alex plans to seed shared DEV with real vendor catalogs and share vendor FTP logins separately for examining file formats. Both are pending; credential values must remain outside the knowledge base. The user could help connect vendor APIs later; this is a possibility, not an assigned implementation task or approved API scope. [SRC-003](sources/SRC-003-website-environments.md)

## Unknown details

Actual vendor schemas/endpoints and detailed pricing/role rules remain unknown. SRC-005 names later expansion examples, existing payment candidates, AvaTax investigation and business-account requirements; it does not settle all provider choices or make punchout an explicit website deliverable. See [integration](integration.md), [scope](project-scope.md) and [open decisions](questions.md#q-010). No credentials are recorded. [SRC-005](sources/SRC-005-website-counter-proposal.md)

## History

2026-11-15: SRC-003 confirms website catalog relevance and adds planned DEV catalog/FTP access; the remaining operations workflows are not automatically website requirements. SRC-005 now defines explicit reuse of operations flows through publication and inbox boundaries; see integration and scope.
