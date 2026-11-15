# Architecture and interfaces

## Components and ownership

`server.py` serves static HTML/CSS/JavaScript and localhost HTTP endpoints using Python's standard library. `store.py` is shared by the server and `tasks.py` CLI. No browser local storage is authoritative. `knowledge-base/tasks.json` is the only current task store. `tasks.md` and `sources/task-events.md` are deterministic projections. Existing SRC archives remain immutable.

The browser renders task text with textContent, not HTML. The server binds to 127.0.0.1, validates Host and Origin, requires application/json mutations, restricts file-serving paths and sends a restrictive content security policy. The UI reads source Markdown as plain text. No authentication is needed for this single-user loopback design; it is not designed for network exposure or multi-user hosting.

## Schema version 1

Top level: schema, revision, next_id, tasks, legacy, legacy_markdown, events, projection_before. IDs are permanent and allocated under the shared lock. New tasks begin at T-007. Legacy entries retain original status/context and are read-only in the UI.

Task fields: id, title, description, owner, assigned_by, assignment_note, sources, status, priority, start, end, deadline, dependencies, order, archived, notes, revision, completed_at. Sources are relative paths to existing source Markdown. Dates are YYYY-MM-DD or null; end is inclusive. Task notes contain at/text/actor. Completion timestamps are user reports in UTC+08:00. Priority is Low/Normal/High; statuses are the five displayed columns.

Assigned_by is You, Alex, Unknown or Assistant suggestion. An Alex assignment requires a linked source or a nonempty report. With no source, the report is prefixed User-reported. Editing a task keeps previous values in event history; it does not rewrite original sources or claim authenticated Alex actions.

## HTTP and CLI

- GET `/api/tasks`: current snapshot including an opaque `token`, the SHA-256 of canonical bytes. Never derive expected revisions from display timestamps.
- POST `/api/commands`: JSON with `action` (create/update/note), `operation_id` (unique identifier), `expected` (snapshot token), `id` for existing tasks, and `changes` or `text`. Returns the new snapshot after persistence and projection recovery. Create assigns the ID server-side. Update handles archiving through `archived` and reordering through integer `order`.
- GET `/api/events`: SSE, emits token changes or errors; polls every second and sends heartbeats. Connections recycle after five minutes and EventSource reconnects.
- GET `/source/sources/<file>.md`: existing source as plain text.
- CLI: `python app/tasks.py list`, `apply --file request.json` (or stdin with `--file -`), `recover`, and one-time `migrate`.

HTTP actor is always You via local UI; helper actor is You via task command. Neither accepts Alex as the actor. Status 409 reports a stale token, reused operation ID with different content, busy lock or manually edited projection. Invalid fields are 400, missing tasks 404 and unreadable canonical state 503. HTTP body limit is 250 KB. CLI writes no shell-interpolated user text; supply structured JSON through stdin or a temporary UTF-8 file.

## Save and recovery protocol

Every reader/writer acquires one OS-backed byte/file lock at app/.runtime/tasks.lock (msvcrt on Windows, flock on Unix). A crashed process releases its lock; do not delete lock files as a recovery shortcut. Contention times out after five seconds.

Before a mutation, validate canonical data and reconcile pending projections. Compare expected token; reject stale changes. Deduplicate operation IDs so retries after interrupted connections do not create duplicate tasks/events. A duplicate with different content is an error.

Append an EVT event with action, actor, timestamp, exact structured request, before and after values. Save the full canonical state by fsync plus same-directory atomic replacement; this is the commit point. Then update both projections atomically per file. projection_before records the previous allowed hashes. On restart, targets matching the previous or desired hash can safely recover. Any other contents are preserved and block writes for manual reconciliation. There is no unsupported claim of one atomic filesystem transaction across all three files.

Valid helper changes are observed by the running server and streamed to the UI. Direct JSON edits are unsupported: they can omit history and invalidate projection recovery. Manual Markdown edits are not imported automatically. Keep a copy and reconcile with the helper as described in [usage](usage.md).

## Planning behavior

Scheduling Backlog moves it to To do. Moving an existing non-backlog task to Backlog clears planned dates. Other moves preserve dates. Calendar dragging preserves a date range's duration, never modifies deadlines and rejects conflicts against the drag-start token. Board order uses integer positions; equal positions sort by stable task ID. A soft warning appears above two In progress tasks. Archive is a reversible flag. Reopening clears the current completion timestamp but retains completion history.

## Boundaries

Events use stable EVT IDs rather than allocating a new SRC ID and rewriting the source register on every drag. The registered event log is task evidence, and the original manual message archive remains the authority for an Alex assignment. This avoids competing SRC allocation during UI and chat updates. The service never interprets general project decisions or resolves Q entries automatically; substantive Owner answers continue through knowledge intake.
