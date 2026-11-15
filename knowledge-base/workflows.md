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

## Website catalog direction

Alex says the catalog is crucial to the website and understanding vendor-file ingestion through the FTP puller is important. Alex plans to seed shared DEV with real vendor catalogs and share vendor FTP logins separately for examining file formats. Both are pending; credential values must remain outside the knowledge base. The user could help connect vendor APIs later; this is a possibility, not an assigned implementation task or approved API scope. [SRC-003](sources/SRC-003-website-environments.md)

## Unknown details

Actual vendor schemas/endpoints and detailed pricing/role rules remain unknown. SRC-005 names later expansion examples, existing payment candidates, AvaTax investigation and business-account requirements; it does not settle all provider choices or make punchout an explicit website deliverable. See [integration](integration.md), [scope](project-scope.md) and [open decisions](questions.md#q-010). No credentials are recorded. [SRC-005](sources/SRC-005-website-counter-proposal.md)

## History

2026-11-15: SRC-003 confirms website catalog relevance and adds planned DEV catalog/FTP access; the remaining operations workflows are not automatically website requirements. SRC-005 now defines explicit reuse of operations flows through publication and inbox boundaries; see integration and scope.
