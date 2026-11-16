# Tasks and next steps

> Generated from tasks.json. Use the app or task helper to edit tasks; manual edits are detected and preserved for reconciliation.

## Dated task register

| ID | Task | Owner | Assigned by | Status | Priority | Planned dates | Hard deadline | Evidence |
|---|---|---|---|---|---|---|---|---|
| T-002 | Map initial website features to operations data | Charles | You | Done | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-003 | Draft the integration design | Charles | You | Done | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-001 | Understand operations and write learning notes | Charles | You | Done | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-004 | Draft business-account and signup flows | Charles | You | Done | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-005 | Investigate tax and product content | Charles | You | Done | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-006 | Prepare the Phase 0 review package for Alex | Charles | You | Done | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-007 | Fix the remaining W76 QuickBooks/CC alignment flaw | Alex | Alex | Backlog | Normal | Unscheduled | None stated | [SRC-019-qb-cc-accounting-sync](sources/SRC-019-qb-cc-accounting-sync.md) |
| T-008 | Review the revised scope and reconcile review gaps | Charles | Assistant suggestion | To do | Normal | 2026-11-17 | None stated | [SRC-026-tuesday-plan-and-day-filter](sources/SRC-026-tuesday-plan-and-day-filter.md), [SRC-025-revised-scope-intake](sources/SRC-025-revised-scope-intake.md) |
| T-009 | Prepare focused scope, account and access questions for Alex | Charles | Assistant suggestion | Archived / To do | Normal | 2026-11-17 | None stated | [SRC-026-tuesday-plan-and-day-filter](sources/SRC-026-tuesday-plan-and-day-filter.md), [SRC-025-revised-scope-intake](sources/SRC-025-revised-scope-intake.md), [SRC-027-cf-tuesday-task-revisions](sources/SRC-027-cf-tuesday-task-revisions.md) |
| T-010 | Prepare the new client-facing website repository | Charles | You | To do | Normal | 2026-11-17 | None stated | [SRC-026-tuesday-plan-and-day-filter](sources/SRC-026-tuesday-plan-and-day-filter.md), [SRC-025-revised-scope-intake](sources/SRC-025-revised-scope-intake.md), [SRC-027-cf-tuesday-task-revisions](sources/SRC-027-cf-tuesday-task-revisions.md) |
| T-011 | Integrate this knowledge base with the new knowledge base in the CC repository | Charles | You | To do | Normal | 2026-11-17 | None stated | [SRC-027-cf-tuesday-task-revisions](sources/SRC-027-cf-tuesday-task-revisions.md), [SRC-025-revised-scope-intake](sources/SRC-025-revised-scope-intake.md) |
| T-012 | Create a SKILL.md containing UI rules for the client-facing website | Charles | You | To do | Normal | 2026-11-17 | None stated | [SRC-027-cf-tuesday-task-revisions](sources/SRC-027-cf-tuesday-task-revisions.md), [SRC-025-revised-scope-intake](sources/SRC-025-revised-scope-intake.md) |
| T-013 | Develop the initial version of the client-facing website | Charles | You | To do | Normal | 2026-11-17 to 2026-11-18 | None stated | [SRC-027-cf-tuesday-task-revisions](sources/SRC-027-cf-tuesday-task-revisions.md), [SRC-025-revised-scope-intake](sources/SRC-025-revised-scope-intake.md) |

Planned dates use Asia/Manila. Done means user-reported completion, not Alex approval.

## Task details

### T-001

Trace one sandbox product through catalog, pricing and order; note data model, FTP pipeline and business rules.

Assignment context: User requested; adopted assistant breakdown
Dependencies: LEGACY-T-008

### T-002

Produce a feature/data-owner/source table; verify actual schema and function names in the operations repo.

Assignment context: User requested; adopted assistant breakdown
Dependencies: LEGACY-T-008

### T-003

Cover publication, sync, inbox validation, customer matching, pricing precedence, failure handling and duplicate prevention.

Assignment context: User requested; adopted assistant breakdown
Dependencies: LEGACY-T-008

### T-004

Describe organization membership, proposed roles, optional approvals and staff signup review; flag undecided rules.

Assignment context: User requested; adopted assistant breakdown
Dependencies: LEGACY-T-008

### T-005

Record AvaTax/exemption and Icecat/distributor-content findings and gaps; investigation only, no checkout implementation.

Assignment context: User requested; adopted assistant breakdown
Dependencies: LEGACY-T-008

### T-006

Assemble notes, feature/data map, design drafts, investigation findings and open questions; preparation does not mean submission or approval.

Assignment context: User requested; adopted assistant breakdown
Dependencies: LEGACY-T-008

### T-007

Alex reports W76 almost done, with a remaining flaw she plans to fix. Exact flaw and completion/deployment evidence not supplied. Source says tomorrow, but original message date is unknown; no calendar date or deadline inferred. External-payment status coverage remains unconfirmed (Q-016).

Assignment context: Alex's own stated plan in a user-supplied reply; not an assignment to Charles. Timing: original message says tomorrow; communication date unknown. Pending work, not completion.
Dependencies: None recorded

### T-008

Review SRC-025 without repeating completed Phase 0 research. In a working copy, reconcile Phase 2 connection work versus Phase 3 catalog work, launch dashboard data versus Phase 5 self-service, missing supporting-document links, and claims labelled decided. Link evidence or mark assumptions/questions; preserve the intake source. Output: concise change list and a review-ready draft or corrections. No Alex approval inferred.

Assignment context: User requested Tuesday 2026-11-17 planning; assistant-derived task selection and sequence, not an Alex assignment. Schedule basis: User requested date; proposed workload/sequence. Availability and effort unknown; work one or two items at a time. Revised phase order still awaits Alex review.
Dependencies: None recorded

### T-009

Cancelled from the active plan at the user's request in SRC-027; archived rather than completed. Previous question-preparation task and its original wording remain in SRC-026 and event history.

Assignment context: User requested Tuesday 2026-11-17 planning; assistant-derived task selection and sequence, not an Alex assignment. Schedule basis: User requested date; proposed workload/sequence. Availability and effort unknown; work one or two items at a time. Revised phase order still awaits Alex review.
Dependencies: T-008

### T-010

Prepare the CF repository for initial UI work: confirm the TMA repository location, owner/access and local development setup, follow its instructions, and establish a documented starting structure. Use the existing operations sandbox as context; do not assume a new website environment is provisioned. Coordinate any Alex-owned repository/access step through the user. Actual creation/setup awaits required access and scope decisions; this task is not evidence it has happened. Replaces the earlier UI kickoff checklist by user request.

Assignment context: Explicit user assignment/revision in SRC-027. Schedule basis: User requested Tuesday 2026-11-17 plan; initial development also Wednesday 2026-11-18. Not an Alex assignment or evidence of phase approval. Repository/environment availability and scope approval remain unconfirmed.
Dependencies: T-008

### T-011

Locate and review the user-reported newer CC-repo knowledge base alongside this one. Compare sources, dates, facts, open questions, decisions and task references; reconcile duplicate/conflicting entries and define canonical homes with cross-links. Preserve original evidence, history and the unchanged operations source; do not promote proposals into Alex-approved decisions. CC-repo path and content still need inspection; no merge has been performed.

Assignment context: Explicit user assignment/revision in SRC-027. Schedule basis: User requested Tuesday 2026-11-17 plan; initial development also Wednesday 2026-11-18. Not an Alex assignment or evidence of phase approval. Repository/environment availability and scope approval remain unconfirmed.
Dependencies: None recorded

### T-012

Create a reusable CF UI-rules skill from the reviewed scope, design requirements and available evidence. Cover layout/navigation, workflow clarity, accessibility, responsive behavior, component consistency and interaction states as supported; clearly distinguish approved rules from suggested defaults and unresolved decisions. Keep employee-only CC requirements separate from customer website rules. Read the skill-creator instructions when performing this task; validate the actual skill. Do not treat this task entry as a completed skill.

Assignment context: Explicit user assignment/revision in SRC-027. Schedule basis: User requested Tuesday 2026-11-17 plan; initial development also Wednesday 2026-11-18. Not an Alex assignment or evidence of phase approval. Repository/environment availability and scope approval remain unconfirmed.
Dependencies: T-011

### T-013

Build the initial CF UI version in the prepared website repository, following the UI-rules skill and reviewed page/flow plan. In the current draft this means sample data and clickable customer journeys, without CC integration or live payments/tax. Confirm Alex approval of the UI-first phase sequence, repository access and environment before actual implementation; no approval or provisioning is inferred from this user task. Record validation and unfinished scope. Tuesday-Wednesday is a requested work window, not a promise to finish the entire production website.

Assignment context: Explicit user assignment/revision in SRC-027. Schedule basis: User requested Tuesday 2026-11-17 plan; initial development also Wednesday 2026-11-18. Not an Alex assignment or evidence of phase approval. Repository/environment availability and scope approval remain unconfirmed.
Dependencies: T-010, T-012


## Live task history

[Task event evidence](sources/task-events.md). Existing source archives and earlier ID mappings are preserved below.

## Task ID migration

On 2026-11-15 the user explicitly requested that their six Phase 0 tasks start at T-001. This is a one-time exception to the stable-ID rule, authorized by [SRC-012](sources/SRC-012-task-numbering-and-token-question.md). Current project tasks are T-001 through T-006; the next new task is T-007. Earlier administrative records, Alex-owned plans and the parent task remain under LEGACY-T-001 through LEGACY-T-008 with their status and sources intact. These legacy records remain relevant when listing pending work by owner.

| Prior ID (before migration) | Current ID |
|---|---|
| T-001 | LEGACY-T-001 |
| T-002 | LEGACY-T-002 |
| T-003 | LEGACY-T-003 |
| T-004 | LEGACY-T-004 |
| T-005 | LEGACY-T-005 |
| T-006 | LEGACY-T-006 |
| T-007 | LEGACY-T-007 |
| T-008 | LEGACY-T-008 |
| T-009 | T-001 |
| T-010 | T-002 |
| T-011 | T-003 |
| T-012 | T-004 |
| T-013 | T-005 |
| T-014 | T-006 |

Archived sources and earlier conversation messages keep their original IDs. Interpret those IDs using this mapping; never treat an old source reference to T-001 as the current Phase 0 task. A bare current task command uses the current ID; if the user cites an older source or message and the intended task is ambiguous, resolve through this mapping or ask. No dates, assignments, status or deadlines changed.

## Task change history

- 2026-11-15: Renumbered the six Phase 0 tasks to T-001 through T-006 by explicit user request; moved prior T-001 through T-008 to LEGACY-T-001 through LEGACY-T-008. Updated current cross-references; original source wording retained. Historical entries below show migrated IDs for clarity. [SRC-012](sources/SRC-012-task-numbering-and-token-question.md)

Record future additions, rescheduling, completion reports and cancellations here with date, T-ID, previous/new values and SRC-ID. Preserve original assignment evidence when the user changes a planned work date. Completed means reported completion unless verification evidence is supplied.

- 2026-11-15: Added T-001 through T-006 as pending, user-assigned subtasks of LEGACY-T-008 for 2026-11-16. LEGACY-T-008 previously had undated relative timing; this request explicitly schedules its six-part breakdown. No hard deadline, completion or Alex approval inferred. [SRC-011](sources/SRC-011-monday-phase-0-tasks.md)

## Agreed work

| ID | Task | Owner | Status | Date/deadline | Source |
|---|---|---|---|---|---|
| LEGACY-T-001 | Create the initial linked knowledge base and maintenance instructions | Codex | Completed | Added/completed 2026-11-15; deadline not stated | [SRC-002](sources/SRC-002-request.md) |
| LEGACY-T-002 | Process future manually supplied material using the maintenance procedure | Codex when material is provided | Pending future input | No deadline stated | SRC-002 |

## Owner plans and conditional next steps

All entries below are from [SRC-003](sources/SRC-003-website-environments.md). Original dates and deadlines are unknown. These track stated plans/offers; none is verified complete.

| ID | Task or offer | Owner | Status | Date/deadline |
|---|---|---|---|---|
| LEGACY-T-003 | Move DEV into a separate Supabase organization, clean it up and make it the shared development space | Alex | Planned; pending completion/access evidence | Not stated |
| LEGACY-T-004 | Seed DEV with better test data including real vendor catalogs | Alex | Planned; no seeding evidence | Not stated |
| LEGACY-T-005 | Share vendor FTP logins separately for examining vendor files | Alex | Stated intention; no access receipt confirmed; store no credentials here | Not stated |
| LEGACY-T-006 | Create website repository when needed | Alex | Conditional offer; need/creation not confirmed | When needed; no date |

## Reported progress and next session

| ID | Work | Owner | Status | Timing/source |
|---|---|---|---|---|
| LEGACY-T-007 | Complete operations weekend setup/checklist and run local sandbox with test persona | Charles | Completed by user report; not independently tested | Completion date unknown; recorded 2026-11-15; [SRC-004](sources/SRC-004-completed-setup.md) |
| LEGACY-T-008 | Revise the operations-to-website integration approach for Phase 0 using the current framework | Charles | User-stated intention; pending; actual draft not supplied | Original intention: 'tomorrow' (original date unknown), [SRC-004](sources/SRC-004-completed-setup.md). Six subtasks T-001 through T-006 now planned for 2026-11-16 by user request, [SRC-011](sources/SRC-011-monday-phase-0-tasks.md); no Owner deadline |

Phase 0 design is pending; completing setup/starting this KB does not complete the phase. Current deliverables and suggested revision checks are in [Phase 0](phase-0.md). The full [roadmap](project-scope.md) is planned scope, not a list of invented individual delivery commitments.

## Suggested actions (not agreed commitments)

Use the [Phase 0 revision checklist](phase-0.md#suggested-revision-checklist) for LEGACY-T-008. Clarify environment mapping ([Q-009](questions.md#q-009)), Phase 0 acceptance ([Q-008](questions.md#q-008)) and applicable open design choices ([Q-010](questions.md#q-010)). Recommend the user's Notion Questions for Alex area for unanswered Owner questions; Access / tools only for access/tool issues. These suggestions have no assigned deadlines. Vendor API implementation stays later scope and has no assigned individual task yet.

