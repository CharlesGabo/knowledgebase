# App change log

## 2026-11-16 - Daily-history usage clarification

After SRC-026, documented existing Day/date/owner filters for separating Tuesday work from Monday's Done records. No code, schema, migration, automatic archiving or default-view behavior changed. A Node check executed the actual app.js date predicate against current saved tasks: Tuesday 2026-11-17 with owner Charles selects T-008 through T-010; Monday retains six Done tasks. Browser interaction was not exercised. Startup still defaults to All tasks, date grouping uses planned dates, unscheduled work stays visible, and an overnight browser session requires a reload to refresh its local-day value. See [daily usage](usage.md#daily-plans-and-completed-history).

## 2026-11-15 — Initial local task board

Implemented the user-authorized [local app request](../../knowledge-base/sources/SRC-015-local-task-app.md). Added five-column Kanban, drag-and-drop status/order, a day/week/month calendar, search and attribution filters, full task editing, notes, history, source links, archive/restore and read-only legacy records. Keyboard-accessible task fields provide alternatives for status, dates and order.

Migrated six current tasks (T-001 through T-006) and eight legacy records into tasks.json. Monday 2026-11-16 planning and user assignment remain intact; migration does not report completion or Alex approval. Preserved the exact original Markdown in tasks-before-migration.md. Its relative links retain their original knowledge-base/ base directory.

UI and command helper now share a locked, version-checked store, stable change events and recoverable Markdown generation. Repository command prompts and maintenance instructions require the helper for subsequent task changes. App documentation is required with future behavior changes, including decisions, migrations, validation and limitations. App Markdown is included in the knowledge-review fingerprint.

### Validation performed

- Python unittest: 17 tests passed. Covers migration, scheduling, completion/reopening, archive/restore, attribution, invalid values, dependency cycles, stale edits, duplicate retries, manual projection edits, failed/interrupted writes, malformed storage and competing processes.
- HTTP integration test passed: snapshot, mutation, static assets, cross-origin rejection and live SSE notification after a separate helper/store update. Tests use temporary data, never the user's tasks.
- Node test runner: 6 date tests passed, including Monday-based weeks, year/month/leap boundaries and duration-preserving rescheduling without changing deadlines.
- JavaScript syntax checks passed for app.js and dates.js.

### Limitations and follow-up verification

Browser visual and interactive verification is **not completed**. The in-app browser was unavailable and native browser control could not reliably establish its current URL. No screenshot or successful drag/drop browser test is claimed. On first launch, check the board and calendar layout and use task details for precise edits. Automated tests validate storage and date behavior, not rendered accessibility or pointer interactions.

The server must run locally for browser sync. No cloud hosting, mobile synchronization, authentication or account integrations are included. Source links open plain Markdown. Direct generated-Markdown edits deliberately block saves until reconciled; see [recovery](usage.md#recovery). Back up or commit the repository as usual; runtime persistence is not a backup service.

## 2026-11-16 ? Final integration checks

Validated 249 relative Markdown links and anchors, resolving the immutable pre-migration archive from its original knowledge-base/ location. Confirmed all six current tasks remain To do on 2026-11-16, all eight legacy records remain present, and no test events were added to the real task store. The original tma-ops-processes.md SHA-256 remains 169f2606519a39a3d74c850f92747e4ae37887a935e03e440f274f81675b528a.

Updated the seven installed Codex prompt files (add, ask, task, tasks, task-plan, task-done, task-move) from their repository copies and verified matching hashes. Reload the IDE/CLI session to load updated prompt content if it was already cached. Menu visibility is not independently verified. The verification server was stopped; use start.cmd to launch the app for everyday use.
