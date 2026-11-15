# Tasks and next steps

> Generated from tasks.json. Use the app or task helper to edit tasks; manual edits are detected and preserved for reconciliation.

## Dated task register

| ID | Task | Owner | Assigned by | Status | Priority | Planned dates | Hard deadline | Evidence |
|---|---|---|---|---|---|---|---|---|
| T-001 | Understand operations and write learning notes | Charles | You | To do | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-002 | Map initial website features to operations data | Charles | You | To do | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-003 | Draft the integration design | Charles | You | To do | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-004 | Draft business-account and signup flows | Charles | You | To do | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-005 | Investigate tax and product content | Charles | You | To do | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |
| T-006 | Prepare the Phase 0 review package for Alex | Charles | You | To do | Normal | 2026-11-16 | None stated | [SRC-011-monday-phase-0-tasks](sources/SRC-011-monday-phase-0-tasks.md) |

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

