# TMALG Customer Website: Project Scope

**A guide to keep the project on track.** It explains what we're building, how it fits with the
operations platform, and which features arrive in which phase. It's meant to be easy to read.
Technical details live in the linked documents.

- **Based on:** TMA's project framework (November 2026) and the Phase 0 findings.
- **Last updated:** 16 November 2026
- **Status:** A framework, not a final specification. Each phase is planned in detail when it
  starts. The phase order below is **a proposed change** to the framework and needs Alex's OK
  (see "Why the UI comes first").

---

## Introduction

TMA Laser Group sells supplies such as toner, office supplies, gloves and janitorial products to
businesses, many of them schools. Today customers order by phone and email, and staff run
everything in the **operations platform** (the Command Center, or CC, at `tmalg.net`).

**The goal:** a customer website (`tmalg.com`) where customers **place and manage their own
orders**, while the **CC keeps doing the operations side**: buying from vendors, shipping,
invoicing and accounting.

On the website, business customers can:

- browse a catalog of products,
- see **their own prices**,
- request quotes and place orders,
- track their orders and see their invoices.

**The most important ideas, in one list:**

- The CC is **part of this project** and gets extended to support the website.
- We release in **phases**, not all at once, and there are **no fixed deadlines**.
- **Only chosen products** go online, with web-friendly names, pictures and descriptions.
- Each customer sees **their own pricing**.
- Business features matter: company accounts with several users, purchase orders, tax exemption.
- AI and marketing come **later**. We collect usage data early so they have something to build on.

---

## 1. How the two systems fit together

**Two separate systems.** The CC and the website are separate applications, each with its own
database, hosting and passwords. If something goes wrong with one, the other stays safe.

**Separate logins.** Staff sign in to the CC with company Google accounts. Customers have their
own accounts on the website. The two never share a login.

**Different frameworks, same foundation.** The CC is a React app built with Vite. The website uses
**Next.js**, because it helps search engines find the site and makes pages load fast. Both use
React, Supabase and Vercel.

**One owner for each kind of information.** Every kind of data belongs to one system and flows in
one direction:

| Flows from the CC → website | Flows from the website → CC |
|---|---|
| The chosen product catalog | New orders |
| Prices, including each customer's own prices | Quote requests |
| Availability ("In stock / ships in X days") | New customer signups |
| Order status and shipment tracking | Documents customers upload |
| Invoices and payment status | Support and contact messages |

**A curated catalog.** The CC has hundreds of thousands of products, but only the ones staff choose
go online, with web-friendly titles, descriptions, pictures and prices. **Vendor costs and vendor
names never leave the CC.**

**An "inbox" for everything customers send.** Orders, quotes and signups from the website land in
an inbox inside the CC. There they're checked, matched to the right customer account, and turned
into real orders by staff. From then on they follow the normal process (purchase orders, shipping,
QuickBooks). **The website never changes CC data directly.**

**Safe connections.** The website never holds the CC's admin passwords. The two connect using
tools the CC already has: scheduled database jobs, database triggers and a few small
purpose-built services. No new background workers.

**Reuse what already works.** Tracking, payments and QuickBooks already run in the CC. The website
**shows** their results; it doesn't rebuild them.

**Where the logic lives.** Most CC rules live in the database itself, not only in app code. Read
the [knowledge base](knowledge-base/) before changing anything.

---

## 2. Tools and services the CC already uses

The website should **reuse** these through the CC, not connect to them separately (except where
noted).

| Tool / service | What it does in the CC | Website's relationship |
|---|---|---|
| QuickBooks Online | Accounting: invoices, purchase orders, payments | Shows invoice and payment status from the CC |
| USAePay | Card payments taken inside the CC (mostly VA purchase-card transactions, according to Alex) | Possible checkout option (Phase 6) |
| Skyline Payments | "Pay now" links on QuickBooks invoices | Shows the pay links (Phase 5) |
| QuotaGuard | Gives some outgoing connections (QuickBooks, vendor FTP) a fixed internet address | Not used by the website |
| Google Workspace / Gmail / Calendar | Staff sign-in, email and calendar sync | Order emails are sent from a shared company Gmail mailbox |
| Intermedia | Phone calls and call tracking | Not used by the website |
| Gotenberg | Creates purchase order and invoice PDFs | Customers download the PDFs the CC makes |
| EasyPost, 17TRACK, 24hTrack | Shipment tracking | Shows tracking status from the CC |
| Vendor FTP/SFTP feeds | Bring vendor price and stock files into the catalog | Never used directly; the website gets the published catalog |
| Anthropic Claude API | Reading documents (PDF extraction) and Discovery research | Category sorting in the CC; an AI assistant later |
| OpenStreetMap (Overpass, Nominatim) | Business searches for leads; address and location lookup | Not planned |
| Leaflet | Shows maps | Not planned |
| NCES | Public school and district data used by Discovery | Could help match school signups later |
| S3-compatible storage (Cloudflare R2) + AWS CLI | Encrypted **backups** of the database, files and code. (Uploaded files themselves are kept in Supabase Storage.) | Not used by the website |

**New for the website:** Next.js, Tailwind CSS and shadcn/ui, Zod, Sentry, Cloudflare Turnstile,
Avalara (checkout tax), Icecat or distributor content (product pictures and descriptions).

---

## 3. Website pages and features

| Page | What customers can do | Phase | Changes needed in the CC |
|---|---|---|---|
| **Home** | See categories and featured products; request an account | 1 (design), 4 (live) | **New:** staff pick featured products in the publishing tool |
| **Categories and product lists** | Browse, filter and sort | 1, 4 | **New:** one master category list; a publishing tool to choose what goes online; sending the published catalog to the website |
| **Search** | Search by product name or part number | 1, 4 | None beyond the published catalog (search runs on the website's own copy) |
| **Product page** | See pictures, description, specs and availability. Logged in: their own price, or "Request a quote" if the product isn't in their price list. Not logged in: no price | 1, 4 | **New:** web-ready titles, descriptions and pictures; pictures cleaned of vendor marks; one combined availability ("In stock / ships in X days") |
| **Printer supplies finder** | Pick a printer, see matching ink and toner | 1, 4 | **Reuse:** the printer-compatibility data the CC already has, sent with the catalog. Improve it where vendor files lack it |
| **Request an account / sign up** | Ask for access; TMA approves it | 1, 4 | **New:** a signup inbox; a staff screen to review, match to an existing customer or create a lead; assigning the lead to a salesperson |
| **Log in, forgot password, invitations** | Get into their account | 1, 4 | None (website only) |
| **Contact / support form** | Send a question to the sales team | 1, 4 | **New:** messages land in the CC as a lead or as activity on the customer's account |
| **My account dashboard** | See open quotes, recent orders, unpaid invoices, their salesperson | 1, 4 | **New:** send each customer's summary and their salesperson's name and contact |
| **My Products** | Their usual items at their own prices; reorder quickly | 1, 4 | **Reuse:** the favorites and prices salespeople already set. **New:** sending them to the website; price safety checks |
| **Cart** | Collect items, then request a quote or place an order | 1, 4 | **New:** an inbox for quote requests and orders; a staff screen that checks them, re-prices them and turns them into real orders; credit and an alert for the customer's salesperson |
| **Quick order** | Paste part numbers or upload a list | 1, 4 | None beyond the published catalog |
| **Documents** | Upload purchase orders, tax certificates and other papers | 1, 4 | **New:** a document inbox that attaches each file to the right customer or order |
| **Company users** | Invite other staff from the customer's company and set what each can do | 1, 4 | None (website only) |
| **Approvals** | Approve orders from other staff at the same company (if the company turns this on) | 1, 4 | None (website only; only approved orders reach the CC) |
| **My quotes** | See quotes from TMA and accept them online | 1, 5 | **New:** send quotes to the website (prices only, no costs); an inbox for acceptances. **Reuse:** the CC's existing "quote to order" step |
| **My orders and tracking** | Order history, status and shipment tracking | 1, 5 | **New:** send a customer-safe copy of orders and shipments (no costs, no vendor names). **Reuse:** existing tracking |
| **Invoices** | See invoices, what's paid and what's owed; pay online | 1, 5 | **New:** a regular check of QuickBooks for payments, and sending invoices with their paid status. **Reuse:** Skyline pay links |
| **Addresses** | See delivery and billing addresses; request changes | 1, 5 | **New:** send saved addresses; an inbox for change requests that staff approve |
| **Checkout** | Pay by card with tax calculated automatically | 1, 6 | **New:** receive website payments and record each one in QuickBooks exactly once; share the customer's tax identity with the website |
| **Tax exemption** | Submit and track tax-exemption certificates | 1, 6 | **New:** send each customer's exemption status; link it to Avalara's certificate service |
| **About, shipping, returns, privacy, terms, accessibility** | Read company policies | 1, 4 | None |

Phase 1 designs **every page** with sample data, so the whole site can be seen before anything is
connected. Pages go live in the phase shown.

**In short:** most CC changes are **new additions**: a publishing tool, inboxes, sending
customer-safe copies, a payment check. The CC's existing catalog, orders, shipping and QuickBooks
work stays as it is and is **reused**. Most of these changes are built in **Phase 3**, and the rest
are added in the phase each page goes live.

---

## 4. Why the UI comes first (proposed change)

The framework starts with catalog work in the CC. This plan **starts with the website's design**
instead, for one reason: **it's safer to see the integration than to assume it.**

- A clickable design with sample data shows exactly which information each page needs, and where
  it must come from in the CC.
- The data flow (Phase 2) is then mapped against real screens, not only written plans, and the
  connection is built to match them.
- Mistakes are found on screen, before anything touches the CC, which runs the business every day.
- The CC isn't touched in Phase 1. In Phase 2 the connection is built and tested in the
  **development environment only**. The live CC isn't affected until Phase 3, when the connection
  is switched on together with a published catalog.

The Phase 0 documents (feature-to-data map, integration design) become the starting point for
Phase 2 and are checked against the design.

**Needs Alex's confirmation** before Phase 1 starts.

---

## 5. Roadmap

Phases are ordered by what depends on what, not by dates. They can overlap. Each phase starts with
a planning session and ends with a demo. A password-protected preview of the website is kept up
to date throughout.

| Phase | Goal | Main system |
|---|---|---|
| **0. Foundations and planning** ✅ drafted | Learn the CC; plan the connection | Both (no code) |
| **1. Website UI design** | Design every page with sample data | Website |
| **2. Data flow and connection** | Map each screen to its CC data; build the connection between the two systems (development only) | Both |
| **3. Catalog foundation** | Build the CC catalog tools; switch the connection on in the live system | CC |
| **4. Website first version** | Open the site: browse, prices, quotes, orders | Website + CC |
| **5. Customer self-service** | Orders, tracking, quotes and invoices online | Website + CC |
| **6. Online checkout** | Pay online, with tax | Website + CC |
| **Ongoing** | Grow the catalog | CC |
| **7+. Growth and lead generation** | Marketing, leads, SEO, AI | Website + CC |


### Changes to the CC, phase by phase

| Phase | Changes in the CC |
|---|---|
| 0. Planning | None |
| 1. UI design | **None.** The CC isn't touched |
| 2. Data flow and connection | **The connection is built** in the development environment: inboxes for signups, orders and messages, and the jobs that send data to the website. Reviewed through pull requests, **not switched on in the live system yet** |
| 3. Catalog foundation | **The catalog tools:** master categories, the publishing tool, web-ready product content, removing vendor identity from pictures, price safety checks. Then **the connection is switched on** in the live system, once there's a published catalog to send |
| 4. Website first version | Staff screens to review signups and turn inbox orders and quotes into real orders; sending each customer's prices; salesperson credit and alerts; a document inbox; contact messages into the CRM |
| 5. Self-service | Sending customer-safe copies of orders, tracking, quotes and invoices; an inbox for quote acceptances and address changes; a regular QuickBooks payment check |
| 6. Online checkout | Receiving website payments and recording each one in QuickBooks once; sharing the customer's tax identity; linking exemption status to Avalara |
| Ongoing | Publishing more vendor groups; connecting to vendor APIs |
| 7+. Growth | Leads and lead scoring from website activity; alerts to salespeople |

The CC's existing catalog, orders, shipping and QuickBooks work **stays as it is and is reused**.
The changes are **additions next to it**, not rewrites, so daily operations aren't disrupted.

### Phase 0: Foundations and planning ✅ drafted, under review

**Adds:** no features. Produces the plans.
- Notes on how the CC works, which start the shared knowledge base.
- A list of every website feature and the CC information each one needs.
- The design for connecting the two systems, company accounts and signups.
- Research on checkout tax (Avalara) and product pictures and descriptions.
- **CC changes:** none.
- **Tax:** research done. How Avalara works, how TMA uses it today (inside QuickBooks), and the
  gaps.
- **AI:** none.

### Phase 1: Website UI design

**Adds:** the whole website as a clickable design, with sample data only.
- Every page in §3, on desktop and mobile.
- The look and feel: Tailwind CSS and shadcn/ui, built to accessibility standards (WCAG 2.1 AA).
- Navigation, search, filters and sorting.
- Signup, login, company users and approvals screens.
- Cart, quote request, order and checkout screens.
- My orders, tracking, quotes and invoices screens.
- Each page labels **which information will come from the CC** and **what the customer sends
  back**.
- Built in the website's own project, connected to nothing in the CC.
- **CC changes:** none. The CC isn't touched.
- **Tax:** the cart and checkout screens show where tax will appear ("estimated tax", "tax-exempt"
  badge). No real calculation.
- **AI:** leave space in the design for a future assistant (e.g. a help button), but build nothing.

**Done when:** the full design can be clicked through and is reviewed by the team.

### Phase 2: Data flow and connection

**Adds:** no customer features. Maps the data and builds the connection between the two systems.
- For every screen: which CC information it shows, and which requests it sends to the CC.
- Agree the exact "shape" of each piece of information passed between the two systems.
- Decide the rules: how signups are matched to accounts, and how duplicates and failures are
  handled.
- **Build the connection in the CC:** the inboxes that receive signups, orders, quote requests and
  messages, and the jobs that send data to the website.
- Test it end to end with **test data**: the Phase 1 screens show data coming from the CC's test
  environment, and sample orders arrive in a test inbox.
- Update the Phase 0 documents to match.
- **CC changes:** the connection is built and tested in the **development environment**, reviewed
  through pull requests, but **not switched on in the live system yet**.
- **Tax:** confirm with Alex which states TMA collects tax in, and whether TMA's Avalara plan
  includes certificate management.
- **AI:** decide which data the AI features will need (categories, usage tracking) and the rules for
  using it.

**Done when:** every screen has an agreed data source, and the connection works end to end with
test data.

### Phase 3: Catalog foundation (CC)

**Adds:** the CC catalog tools needed to publish safely, then the connection goes live.
- **One set of categories** that every vendor's categories fit into, sorted with AI help and
  checked by staff.
- **Publishing tools:** staff choose what goes online and edit web-friendly titles, descriptions
  and pictures.
- **Vendor identity hidden everywhere:** names, pictures (watermarks, file names, hidden picture
  data), product codes, web addresses and stock.
- **Price safety checks:** a minimum profit margin, and an alert if a vendor's price change would
  make a customer's price lower than TMA's cost.
- **Better product content** for a first pilot group of products.
- **Switch the connection on** (built in Phase 2) in the live system, once there's a published
  catalog to send.
- **CC changes:** the catalog tools above, all built in the CC, and switching the connection on.
- **AI (first AI work):** AI suggests a category for each product, and staff approve or fix it in
  a review queue. Optionally, AI drafts web-friendly titles and descriptions for the pilot products,
  also approved by staff.
- **Tax:** none.

### Phase 4: Website first version

**Adds:** the site goes live for customers.
- Browse, search, filter and sort the published catalog.
- Sign up and log in. **Staff approve every signup before prices are shown**; new companies
  become leads for a salesperson.
- Company accounts with several users and roles.
- Each customer's own prices, from the prices salespeople already set in the CC.
- My Products and quick reorder.
- Quote requests and orders sent to the CC inbox, invoiced the normal way, delivered to saved
  addresses.
- Document uploads (purchase orders, tax certificates).
- Salesperson credit and alerts for website orders.
- Order emails (received, quote ready, shipped) from a shared company mailbox.
- Contact / support form into the CC.
- Usage tracking (views, searches, carts, signups, quotes, orders).
- Groundwork for industry-specific experiences for logged-in customers. **No industry is fixed**:
  it works for any industry (for example, using the customer's type of business already stored in
  the CC). The public site stays general.
- **CC changes:** staff screens to review signups and turn inbox orders and quotes into real
  orders; sending each customer's prices; salesperson credit and alerts; a document inbox;
  contact messages into the CRM.
- **Tax:** customers see "tax calculated on your invoice". The real tax is worked out by
  QuickBooks with Avalara when TMA makes the invoice, exactly as today. Tax-exempt customers can
  upload their certificate.
- **AI:** none for customers. Usage tracking starts collecting the data future AI will use.

### Phase 5: Customer self-service

**Adds:** customers check things themselves instead of calling.
- Order history, status and shipment tracking.
- Accept quotes online.
- Invoices and payment status, with "pay online" links (Skyline).
- *Needs:* the CC checking QuickBooks regularly, so "paid" is right even for checks and bank
  transfers.
- **CC changes:** sending customer-safe copies of orders, tracking, quotes and invoices; an inbox
  for quote acceptances and address changes; a regular QuickBooks payment check.
- **Tax:** invoices on the website show the real tax from QuickBooks.
- **AI:** after this phase, the team decides what the AI assistant should do and when.

### Phase 6: Online checkout

**Adds:** paying online.
- Card checkout (method chosen in this phase: QuickBooks Payments, USAePay and/or Skyline).
- Sales tax calculated with Avalara, including tax-exempt customers and certificates (see
  "Checkout tax with Avalara" below).
- **AI:** none.
- **CC changes:** receiving website payments and recording each one in QuickBooks once; sharing
  the customer's tax identity with the website; linking exemption status to Avalara.

### Ongoing: Growing the catalog

- More vendor product groups once their content is ready (e.g. TD SYNNEX and D&H technology).
- Vendor connections through APIs, not only files.
- Search data decides what to add next.
- **CC changes:** publishing more vendor groups; connecting to vendor APIs.

### Phase 7 and later: Growth and lead generation

- Automatic marketing emails built in-house (welcome, items left in cart, re-engagement,
  follow-ups), sent from a separate email service and address.
- Email capture and lead scoring, with alerts to salespeople.
- Search-engine improvements, industry storefronts.
- **AI assistant on the website** (may come earlier): e.g. help customers find the right product
  or cartridge, answer order questions, suggest reorders. Built on Anthropic Claude.
- **AI for sales:** scoring leads from usage data and alerting salespeople about promising ones.
- **CC changes:** leads and lead scoring from website activity; alerts to salespeople.
- **Tax:** none.

### AI across the phases

| Phase | AI work | Who checks it |
|---|---|---|
| 0–2 | None. Plan the data AI will need | — |
| 3 | Suggest a category for each product; optionally draft web titles and descriptions | Staff approve every suggestion |
| 4 | None for customers; usage tracking collects data for later | — |
| 5 | Decide what the AI assistant should do | Alex and the team |
| 7+ | AI assistant for customers; AI help with lead scoring | Rules agreed before launch |

**Rules for AI in this project:**
- It uses **Anthropic Claude**, the provider the CC already uses.
- **AI suggests, people decide.** Nothing AI produces goes online without staff approval.
- AI **never** sets prices, approves accounts or changes orders.
- Never send passwords or more customer data than a feature needs, and never send production
  data to an AI tool while developing.

### Checkout tax with Avalara: how it fits

**Today:** TMA already uses Avalara, but only **inside QuickBooks**. When TMA creates an invoice,
QuickBooks asks Avalara for the tax and adds it to the invoice. The CC reads that tax back. The
CC never talks to Avalara itself. It only stores a simple "tax-exempt: yes/no" per customer, and
keeps no exemption certificates.

**The plan, step by step:**

| Phase | What happens with tax |
|---|---|
| 0 | Research done (details in the [tax and content research](customer-site/04-INVESTIGATION_TAX_AND_CONTENT.md)) |
| 1 | The design shows where tax appears; no calculation |
| 4 | Orders are invoiced the normal way: QuickBooks + Avalara add the real tax. Customers see "tax calculated on your invoice". Tax-exempt customers upload certificates |
| 5 | Customers see the real tax on their invoices on the website |
| 6 | **Checkout:** the website asks Avalara for an **estimate** while the customer pays |

**How checkout tax would work (Phase 6):**

```
Customer checks out on the website
   │  website sends the cart + delivery address + customer's tax ID to Avalara
   ▼
Avalara returns an ESTIMATE  ──►  shown to the customer, nothing is recorded yet
   │
   ▼
Order goes to the CC inbox ──► staff process it ──► QuickBooks invoice
                                                      │
                                                      ▼
                                   QuickBooks + Avalara record the FINAL tax (as today)
```

- **Only one place records tax: the QuickBooks invoice, as today.** The website only shows an
  estimate, so the same sale is never taxed twice.
- **The same customer identity** is used by the website and QuickBooks, so the estimate and the
  invoice match.
- **Tax-exempt customers:** their certificates are stored in Avalara's certificate service and
  linked to their account. Avalara then leaves tax off automatically. The exemption applies to the
  **company's** orders, not to someone paying with a personal card.
- **Before building:** test it with an Avalara test account and a QuickBooks test company. Confirm
  which states TMA collects tax in, and whether TMA's Avalara plan includes certificate
  management.

If card payment at checkout later needs the tax to be **final** at the moment of paying, the
website would record the tax itself and QuickBooks's own Avalara calculation would be switched off
for those orders. That is a Phase 6 decision.

---

## 6. What's not included (for now)

- Live, real-time updates on the website.
- Large-scale load testing.
- A separate Docker setup (local development uses the Supabase tools).
- New background workers for syncing.
- Rebuilding tracking, payments or QuickBooks on the website.
- Any change to the CC in Phase 1, or to the **live** CC in Phase 2 (Phase 2 work stays in the
  development environment).

---

## 7. Standards for every phase

**Security comes first on the public website:**
- Never build database queries by joining text together.
- Check every input on the server, not just in the browser.
- Customers only ever see their own company's data and prices, and tests prove it.
- Clean up vendor or user text before showing it.
- Uploaded files are checked, stored privately and shared only through short-lived links.
- Public forms are protected from bots and spam.
- No secrets in the browser; the website never holds CC admin passwords.
- If a security check fails or errors, **access is denied**.
- Security review on every change; a full security audit before launch and before online checkout.

**Also:** no duplicate orders, limits on repeated requests, a log of what the connection does,
error monitoring (Sentry), accessibility (WCAG 2.1 AA), legal policies before taking orders,
automated tests for pricing, orders and the connection, and notes written as we go.

---

## 8. Technology at a glance

| Area | Website uses |
|---|---|
| Language and framework | TypeScript, Next.js, React |
| Look and feel | Tailwind CSS, shadcn/ui |
| Input checking | Zod, on the server |
| Database, logins, file storage | Supabase (its own, separate from the CC) |
| Connection to the CC | Scheduled database jobs and database triggers, with the inbox |
| Search | Built-in database search (a dedicated tool later if needed) |
| Usage tracking | Our own tables |
| Order emails | Gmail, from a shared company mailbox |
| Error monitoring | Sentry |
| Bot protection | Cloudflare Turnstile |
| Tax (Phase 6) | Avalara |
| Payments (Phase 6) | QuickBooks Payments, USAePay and/or Skyline |
| Product content | Icecat and distributor feeds (being researched) |
| AI (later) | Anthropic Claude |
| Testing | Unit, integration and end-to-end (Playwright) |
| Hosting | Vercel, a separate project from the CC |

---

## 9. How we work

- **Task board (Notion):** Backlog → To Do → In Progress → Review → Done, one or two tasks in
  progress at a time. Notion also holds the Work Log, Knowledge Base and Decision Log.
- **Each phase** starts with a planning session and ends with a demo.
- **For every change:** a short design note for bigger work → a separate branch in TMA's GitHub →
  a pull request with automatic tests and a preview → Alex reviews and approves → database changes
  are submitted as files and TMA applies them to the live system.
- **Extra care for the CC:** it runs the business every day, so changes are small, tested and
  checked in the test environment first.
- **AI tools are welcome,** but understand and test what you submit, and never paste real customer
  data, production data or passwords into one.
- **Stuck for more than a shift?** Say so instead of waiting.

---

## 10. Decisions still to make

| Decision | When |
|---|---|
| **Confirm the new phase order (UI design first)** | **Before Phase 1** |
| ~~Whether prices are public~~ **Decided: login-only**, because every customer's prices differ | Done |
| ~~Price for products not in a customer's price list~~ **Decided: "Request a quote"** | Done |
| Minimum-margin rules for the price safety checks | Phase 2 |
| Company account roles and order approval | Phase 1–2 |
| Which salesperson gets a lead from a new signup | Phase 2 |
| ~~Which industry first~~ **Decided: no fixed industry**; tailoring works for any industry | Done |
| Website text, branding and pictures: who provides what | Phase 1 |
| The first pilot group of products | Phase 2–3 |
| Where product pictures and descriptions come from | Phase 2–3 |
| How Avalara and tax-exemption certificates will work | Phase 6 (researched in Phase 0) |
| Whether any medical products need license or prescription checks | Before they go online |
| Payment method(s) for online checkout | Phase 6 |
| Terms of sale, returns, shipping and privacy policies | Before taking orders |
| When and how to add an AI assistant | After Phase 5 |
| Which service sends marketing emails | Phase 7 |

All open questions, with recommendations, are in the [Phase 0 README](README.md).

---

## 11. Staying on track: a quick checklist

Before starting any task, ask:

1. **Which phase is this in?** If it's a later phase, park it in the Backlog.
2. **Which system does it belong to?** Business information stays owned by the CC; the website
   only shows it or sends requests in.
3. **Could it reveal a vendor, a cost or another customer's data?** If yes, stop and redesign.
4. **Does it need a design note first?** Yes for anything big or any database change.
5. **Is there an open decision behind it?** Check §10. If it isn't decided, use sample data and
   write down your assumption.
6. **Is it small enough for one pull request?**

---

## 12. Where to find the details

| You need | Read |
|---|---|
| How the CC works | [Knowledge base](knowledge-base/) |
| Every website feature and the data it uses | [Feature map](customer-site/01-FEATURE_MAP.md) and [feature-to-data map](customer-site/08-FEATURE_DATA_MAP.md) |
| How the two systems connect | [Integration design](customer-site/02-INTEGRATION_DESIGN.md) |
| Company accounts and signups | [Business accounts](customer-site/03-BUSINESS_ACCOUNTS_AND_SIGNUP.md) |
| Tax and product content research | [Tax and content](customer-site/04-INVESTIGATION_TAX_AND_CONTENT.md) |
| Website pages and plan | [Site plan](customer-site/05-SITE_PLAN.md) |
| Task lists for each system | [CC tasks](customer-site/06-IMPLEMENTATION_CC.md) and [website tasks](customer-site/07-IMPLEMENTATION_SITE.md) |
| All CC tools and services in detail | [External services](knowledge-base/external-services.md) |
| All open questions | [Phase 0 README](README.md) |
| Discussions so far | [Discussion log](customer-site/DISCUSSION_LOG.md) |
