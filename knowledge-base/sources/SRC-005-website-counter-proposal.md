# SRC-005 - Scope framework source conversion

- Author: Alex, TMA Laser Group, Inc. (document byline)
- Document date: November 2026; exact day unknown
- Added: 2026-11-15
- Subject: TMALG Client-Facing Website - Counter-Proposal & Project Framework
- Original: [Unchanged Word document](../../TMALG-Website-Counter-Proposal.docx)
- Original SHA-256: `c81854d3cd697348fb1607b1386d40099c6e0badede7d119d1c44ee8abbe0e85`
- Status: User identifies this as the current scope version; the document calls itself a framework, not a final specification. Acceptance/sign-off date unknown.
- Conversion: Body wording and order retained; Word headings/lists/tables represented as Markdown. No images, comments, tracked changes or substantive footnotes/endnotes found. No credential values found. Original Word formatting is retained in the linked original.
- File metadata: Created 2026-11-11T23:30:00Z; modified 2026-11-12T00:39:00Z; these are file metadata, not approval or communication dates.

## Converted document

# TMALG Client-Facing Website

Counter-Proposal & Project Framework

Prepared by: Alex, TMA Laser Group, Inc.

In response to: TMALG-ClientFacingWebsite Project Scope Document

Date: November 2026

## Introduction

Thank you for the thorough, well-organized project scope. It shows a strong understanding of what this website needs, and a lot of it carries forward as-is: the core technology choices, your focus on security, and your Kanban workflow.

This document is meant as a framework, not a final specification. It adjusts some areas of scope and technical direction based on how our operations platform is built and how TMA does business. The details of each phase will be worked out together once you start.

Summary of the main changes:

- The operations platform is in scope and will be extended to support the website. Work begins there.

- Phased releases instead of one complete initial release, with no fixed deadlines.

- Integration designed around the operations platform’s existing conventions: database-native sync, with one system owning each type of data.

- A curated catalog, customer-specific pricing, and business-buyer features (business accounts, purchase orders, tax exemption).

- AI and marketing move to later phases. Event tracking starts early so they have data to build on.

- Some items removed or deferred for now: real-time features, large-scale load testing, and Docker as a separate deliverable.

## 1. Role & Arrangement

Position: Part-time Software Developer (independent contractor) for TMA Laser Group, Inc., at USD $5.00 per hour.

Scope of work: You’ll work across both TMA systems: the existing operations platform and the new customer-facing website. Work begins on the operations platform backend, preparing it to support the customer site, and then moves to the customer site itself.

Working relationship: You’ll be the primary developer on the customer site. Alex will act as technical lead and co-developer: guiding architecture, reviewing pull requests, and building features alongside you.

Schedule & hours: You set your own hours around your internship and school. There are no hard deadlines. Work is organized into phases, with priorities set together. Your health and school come first, so please don’t burn yourself out. We’d rather have steady, sustainable hours than long weeks.

Time tracking & invoicing: Log each shift in the Notion Work Log (date, hours, tasks completed, links to pull requests). This replaces separate end-of-shift updates. Hours are totaled and paid on the 1st and the 15th of every month via Wise.

Tools & environment: TMA provides a GitHub account, a Google Workspace email, and a Codex Teams seat linked to that email. You’ll have a dedicated development environment: your own Supabase project with test data (including catalog data) and preview deployments for testing changes. All code lives in the TMA GitHub organization, and changes reach production only after review and approval through pull requests. Database changes are submitted as migration files and applied to production by TMA. Production systems, credentials, and live customer data remain under TMA’s control. Error monitoring is handled through Sentry, set up by TMA.

Ownership & confidentiality: All code, designs, documentation, and other work created for TMA are the exclusive property of TMA Laser Group, Inc. Customer, vendor, pricing, and business information is confidential. It may be used only for TMA work and may not be shared or kept after the engagement ends. Full terms will be set out in the contract.

Communication: Day-to-day communication is async through Notion, video messages, or email. We’ll meet live when schedules allow, weekends included.

Term & future: This contract covers part-time work. Our intention is to offer a full-time role once you finish school, based on performance and mutual fit.

## 2. Architecture Direction

Two independent systems. The operations platform (.net) and the customer website (.com) are separate applications. Each has its own Supabase projects (development and production), Vercel project, and credentials. A security problem in one should not expose the other.

Separate logins. Staff sign in to the operations platform with company Google accounts. Customers have their own accounts in the customer site’s Supabase project. The two never share a login system.

Different frameworks, same foundation. The operations platform is a React single-page app built with Vite. The customer site will use Next.js for search-engine visibility and page speed. Both share React, TypeScript, Supabase, and Vercel.

Curated catalog, published from operations. The operations catalog (vendors, products, vendor offers) stays the source of truth. Not every product goes online. Staff choose which products appear on the website, along with web-ready titles, descriptions, images, and display pricing. Only that published set syncs to the customer site. Vendor costs, offers, and internal data never leave operations. Building the publishing tools in operations is part of the early backend work.

One owner per type of data. Each kind of data is owned by one system and flows in one direction:

- Operations → Customer site: published catalog, pricing (including customer-specific pricing), availability, order status, shipment tracking, invoices.

- Customer site → Operations: new orders, quote requests, new customer signups, uploaded documents.

Inbox pattern. Orders, quotes, and signups from the website land in inbox tables in operations. Operations logic validates them, matches web customers to existing accounts (reusing the current duplicate-matching), and turns them into real orders. From there they follow the existing order, purchase order, and QuickBooks flow. The website never writes directly to operations tables.

Minimal-access connections. The customer site never holds operations admin credentials. Sync uses database-native tools already in use (scheduled database jobs and database webhooks), plus a small set of purpose-built endpoints where business logic is needed. No new GitHub Actions workers are needed for sync. The exact mechanism is chosen during the design phase.

The operations platform is in scope. Unlike the original proposal, the operations platform will be extended to support the website (catalog publishing, inbox processing, customer linking, pricing). That work comes first and goes through the same review process.

Vendor catalog pipeline. Vendor price and stock files continue to arrive through the existing FTP worker and manual uploads. You’ll get familiar with the FTP worker early on. API-based vendor integrations are planned for a later phase.

Reuse existing integrations. Shipment tracking, payments, and QuickBooks sync already run in operations. The website shows their results; it doesn’t duplicate them.

Where logic lives. Much of the operations platform’s business logic lives in the database itself (SQL functions, triggers, and row-level security policies) and in Supabase Edge Functions, not only in application code. If you’re coming from MySQL, this is the biggest difference to get used to. An onboarding guide will cover these conventions before work begins.

## 3. Phased Roadmap

Phases are sequenced by dependency, not deadline. They may overlap. Each phase is detailed and estimated together when it begins. A password-protected staging version of the site will be available throughout so progress can be reviewed at any time.

### Phase 0: Foundations & Plumbing Design

- Onboarding on the operations platform: database-centered logic, Edge Functions, the catalog and order data model, the vendor FTP worker, and the existing development process.

- Documentation deliverable: onboarding and system notes written while learning, which start a shared knowledge base.

- Map all initial customer-site features and the operations data each one needs.

- Integration design for review: catalog publishing, sync, inbox tables, customer-to-account linking, and pricing precedence.

- Design business accounts (multiple users per organization, roles, optional order approval) and the signup approval flow.

- Investigate: Avalara AvaTax API for checkout tax and tax-exemption certificates; product content sources (e.g., Icecat, distributor feeds).

### Phase 1: Catalog Foundation (Operations Platform)

- Master category system: one unified set of categories that vendor categories map into, built in operations so both systems benefit. Uses AI-assisted classification with a staff review queue, rolled out one vendor group at a time.

- Catalog publishing tools: staff choose which products go online and edit web-ready titles, descriptions, and images.

- Vendor-identity protection: listings, images (watermarks, filenames, metadata), SKUs, URLs, and stock display reveal no vendor or source. Stock is shown as combined availability (e.g., “In stock / ships in X days”).

- Price safety guards: minimum-margin checks, and alerts when vendor cost changes push a customer’s price below cost.

- Product content enrichment (images, descriptions, specifications) for a pilot vendor group.

- Sync plumbing: published catalog out, inbox tables in.

### Phase 2: Customer Site v1

- Site layout, navigation, category browsing, and search, filtering, and sorting.

- Customer registration and login. New signups are reviewed by staff before pricing is visible. Unmatched signups become CRM leads assigned to a salesperson.

- Business accounts: multiple users per organization, with roles.

- Customer-specific pricing: prices salespeople set through CRM favorites in the operations platform appear in that customer’s logged-in view.

- My Products / quick reorder from favorites and past orders.

- Quote requests and order submission through the inbox, invoiced through the existing process. Customers choose from their existing ship-to locations.

- Document uploads: customers can upload their own purchase order PDFs, tax-exemption certificates, and other order documents.

- Salesperson attribution and alerts: web orders and quotes are credited to the account owner, who is notified.

- Transactional email (order received, quote ready, shipped) sent through the Gmail API from a shared company mailbox.

- Inquiry / support form routed into the CRM.

- Event and search tracking (product views, searches, carts, signups, quotes, orders) to support analytics now and marketing automation later.

- Groundwork for industry-tailored experiences (e.g., schools, law enforcement) for logged-in customers. The public site stays general.

### Phase 3: Customer Self-Service

- Order history, order status, and shipment tracking from the operations platform.

- Online quote acceptance.

- Invoices and payment status, with pay-online links through Skyline.

### Phase 4: Online Checkout

- Cart checkout with online payment (payment method decided at this phase).

- Tax calculated at checkout via Avalara AvaTax, including tax-exemption handling.

### Ongoing: Catalog Expansion

- Additional vendor product groups phased in over time (e.g., technology products from TD SYNNEX and D&H once product content is in place).

- API-based vendor integrations.

- Search analytics guide which product groups to add next.

### Phase 5+: Growth & Lead Generation

- Marketing automation built in-house on a trigger model, using TMA’s own event data and business rules: welcome series, browse / product / cart / checkout abandonment, re-engagement of registered customers who haven’t ordered, and post-purchase follow-up. Sent through a dedicated email service on a separate subdomain.

- Email capture and lead scoring, with hot-lead alerts to salespeople, so the site becomes a lead-generation channel for the CRM.

- SEO optimization, fuller industry-specific storefronts, and AI assistance (AI may move earlier).

## 4. Standards (All Phases)

Security. Security is a top priority for the public site:

- All database access uses parameterized queries. No SQL is ever built by joining strings, including inside database functions.

- All input is validated on the server (Zod). Browser-side checks are for convenience only.

- Row-level security on every table, with tests confirming customers can’t reach each other’s data or pricing.

- Vendor and user content is sanitized before display; raw HTML is never rendered unsanitized.

- Uploads are type- and size-checked, stored in private buckets, and reached only through short-lived signed links.

- Public forms and endpoints (including event tracking) use bot protection (Cloudflare Turnstile) and rate limiting. Data from the browser is treated as untrusted.

- Secrets never reach the browser, and the customer site holds no operations admin credentials.

- Strict security headers and a Content Security Policy; automated dependency alerts.

- Access checks fail closed: if a check errors, access is denied.

- Security review on every pull request, and a security audit before launch and again before online checkout.

Reliability. Duplicate-order prevention, rate limiting, audit logging of integration activity, and error monitoring through Sentry.

Accessibility. Built to WCAG 2.1 AA from the start, which supports Section 508 requirements common with government and education buyers.

Legal. Terms of sale, privacy policy, and returns and shipping policies are in place before the site takes orders.

Quality. Automated tests for pricing, orders, and sync. Documentation is written and maintained throughout, not saved for the end.

Process. Follow the operations platform’s existing development process: design notes before significant work, reviewed pull requests, and recorded releases.

Email. Transactional email is sent from a company mailbox. Marketing email goes only through a dedicated service on a separate subdomain, with unsubscribe handling (CAN-SPAM), to protect the main domain’s reputation.

## 5. Technology Stack

Based on your original proposal, adjusted to align with the existing operations platform.

| Category | Technology | Change from proposal |
| --- | --- | --- |
| Language | TypeScript | — |
| Framework | Next.js (App Router), React | — |
| Styling / UI | Tailwind CSS, shadcn/ui | — |
| Validation | Zod, server-side on every input | — |
| App server logic | Next.js server actions and route handlers | — |
| Shared business logic | Postgres functions and triggers; Supabase Edge Functions | Changed: follows ops conventions |
| Database / Auth / Storage | Supabase, with separate dev and prod projects for the website | — |
| Connection pooling | Supabase pooled connections (Supavisor) | — |
| Sync with operations | pg_cron scheduled jobs and database webhooks, with inbox tables | Changed: existing tools, no new workers |
| Background jobs | pg_cron and Edge Functions; Supabase Queues only if needed | Changed: Queues optional |
| Real-time | Not needed initially | Removed for now |
| Search | Postgres full-text search; dedicated search engine later if needed | Added |
| Event tracking & analytics | In-house event tables (foundation for marketing automation) | Added |
| Transactional email | Gmail API from a shared company mailbox | Added |
| Marketing email (later) | Dedicated sending service on a separate subdomain, driven by the in-house trigger system | Added |
| Error monitoring | Sentry (set up by TMA) | Added |
| Bot protection | Cloudflare Turnstile | Added |
| Tax (pending investigation) | Avalara AvaTax API | Added |
| Payments (decided in Phase 4) | QuickBooks Payments, USAePay, and/or Skyline | Changed: existing providers |
| Product content (pending) | Icecat and distributor feeds | Added |
| AI (later phase) | Anthropic Claude (the provider ops already uses), via Vercel AI SDK or Anthropic SDK | Changed: provider named |
| Testing | Unit and integration tests plus Playwright end-to-end, matching ops conventions where practical | Added |
| CI | GitHub Actions running tests on every pull request | Added |
| Local development | Supabase CLI (uses Docker) | Changed: no separate Docker deliverable |
| Hosting | Vercel, as a separate project from operations | — |
| Version control | Git and GitHub (TMA organization) | — |

## 6. Workflow & Communication

Task tracking (Notion). Work is tracked on a shared Notion board using your proposed Kanban flow: Backlog → To Do → In Progress → Review → Done, with a work-in-progress limit of one or two tasks. The workspace also holds:

- Work Log: one entry per shift (date, hours, tasks, pull request links, blockers). Used for invoicing and progress updates.

- Knowledge Base: onboarding notes, system documentation, and how-tos written while learning.

- Decision Log: a short record of each significant technical or business decision and why it was made.

Phases. Each phase starts with a scoping session that breaks it into tasks and rough sizes, and ends with a demo and review before the next phase begins.

Development flow:

- Significant features or database changes start with a short design note, reviewed before coding begins.

- Work happens on a feature branch in the TMA GitHub organization.

- A pull request triggers automated tests and a preview deployment.

- Alex reviews and approves. Nothing merges to the main branch without approval.

- Database changes are submitted as migration files and applied to production by TMA.

Operations platform changes. The operations platform runs the business every day, so changes to it get extra care: smaller pull requests, tests for affected areas, and verification in the development environment before release.

AI coding tools. Codex and other AI assistants are encouraged. You’re responsible for understanding and testing all code you submit. Never paste production data, customer information, or credentials into AI tools. Project conventions are documented in the repository for both people and AI assistants to follow.

Communication. Day-to-day communication is async through Notion comments, video messages, and email. Live meetings happen when schedules allow, weekends included. If something blocks progress for more than a shift, flag it rather than waiting.

Progress visibility. A password-protected staging version of the customer site will be kept up to date so TMA can review progress at any time.

## 7. Open Decisions

These will be settled at the start of the relevant phase, not now:

| Decision | When |
| --- | --- |
| Public pricing vs. login-to-view vs. request-a-quote (likely a per-product setting) | Phase 0 |
| Pricing precedence and public price rules (markups, minimum margins) | Phase 0 |
| Business account structure: user roles and order approval | Phase 0 |
| Industry segments and how they shape the logged-in experience | Phase 0–2 |
| First pilot vendor group | Phase 0 |
| Product content sources (Icecat coverage, distributor feeds) | Phase 0–1 |
| Avalara API feasibility and tax-exemption certificate handling | Phase 0 (investigate), Phase 4 (build) |
| Regulated medical products: whether any items need license or prescription verification | Before those products go online |
| Payment method(s) for online checkout | Phase 4 |
| Website copy, branding, and imagery: who provides what | Phase 2 |
| Policy content (terms of sale, returns, shipping, privacy) | Before taking orders |
| AI assistant timing and scope | Revisit after Phase 3 |
| Marketing email sending service | Phase 5 |

## Next Steps

Please review this framework and send any questions, concerns, or suggestions. Nothing here is set in stone, and your input is welcome. Once we agree on the overall direction, we’ll send the contract and get your accounts and development environment set up so Phase 0 can begin.

Thank you again for the thoughtful proposal. We’re excited to build this with you.

Alex

TMA Laser Group, Inc.
