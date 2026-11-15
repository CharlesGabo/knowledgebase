# Context and requirements

## User intent

On 2026-11-15 the user requested a Zoho-inspired task board, using their supplied screenshot as visual context. Tasks created through this conversation should appear in the UI; UI changes should update the knowledge base. The user also requested day, week and month planning, a separate app folder, and maintained documentation for every future update. [Request source](../../knowledge-base/sources/SRC-015-local-task-app.md).

## Confirmed choices

- This computer only; a local browser app, no hosted service or account connection.
- Board plus calendar; date-based scheduling, without hourly slots.
- Backlog, To do, In progress, Review and Done.
- Full task management including notes, priorities, dates, deadlines and reversible archiving.
- Structured canonical task file with an automatically generated Markdown view.
- Existing task IDs, assignments, dates, sources and legacy mapping must survive migration.

## Scope and interpretation

This app supports the user's project planning. It is not a new customer website deliverable, does not connect to Zoho or Notion, and does not replace Alex's approval process. UI actions are explicit user reports. Marking Done cannot establish Owner approval or Phase 0 acceptance. Alex-owned legacy plans remain separate from assignments to Charles.

Current tasks T-001 through T-006 entered the app in To do because the user explicitly scheduled them for Monday, 2026-11-16. This maps the previous Pending display into a board column without claiming work started. Dates use Asia/Manila; weeks run Monday–Sunday. Defaults: Charles as owner, You as assigner, Normal priority, Backlog and no schedule.

## Success criteria

One task record is authoritative. Both entry points use the same save logic, errors are visible, and conflicting edits cannot silently replace one another. Readers can inspect sources and history in Markdown. The UI aims to reflect valid helper changes within two seconds while its local service runs. Task commands work without the server running.

Implemented behavior and actual verification are recorded in [changes](changes.md); planned behavior must never be described as tested without evidence.
