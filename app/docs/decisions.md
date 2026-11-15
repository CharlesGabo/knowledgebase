# App decisions

## APP-D-001 — Local-only shared task store

- Date: 2026-11-15
- Status: Accepted implementation direction from user-selected plan
- Decision: One JSON task store, shared Python persistence module, generated Markdown, and localhost UI.
- Why: The user explicitly chose this computer only and structured storage. A hosted app would require authentication and a separate connection to local files. Parsing freely edited Markdown in two directions would make conflict detection and history harder.
- Consequences: The local service must run for live UI updates. Task commands can operate offline through the helper. Direct Markdown writes are unsupported and detected.

## APP-D-002 — Five stages and date-only calendar

- Date: 2026-11-15
- Status: Accepted user choice
- Decision: Backlog, To do, In progress, Review, Done; day/week/month calendar without hour slots.
- Why: The user selected Review to match the framework and date-only planning. Six already scheduled pending tasks migrate to To do, not In progress.
- Consequences: Done is a user completion report, not Owner acceptance. The app does not decide business requirements or auto-complete parent tasks.

## APP-D-003 — Conflict rejection and recoverable projections

- Date: 2026-11-15
- Status: Implemented technical choice within approved plan
- Decision: Global content token, OS file lock, operation-ID deduplication, atomic canonical replacement and hash-guarded projection recovery.
- Why: Silent last-write-wins could erase a chat/UI edit. A global token may reject unrelated simultaneous edits, but it is conservative and easy to understand for one user. JSON avoids extra database installation.
- Consequences: Stale drafts require explicit comparison/retry. Event IDs remain stable; UI events use EVT IDs in one registered evidence log to avoid SRC allocation races. Original SRC archives are not rewritten.

## APP-D-004 — Documentation is part of each change

- Date: 2026-11-15
- Status: Explicit user requirement
- Decision: app/ owns application source and docs; root instructions require context review and corresponding doc updates for future work.
- Consequences: Record intent, decisions, migrations, actual checks and limits. Never turn an unverified plan into a completion claim. Preserve original source and decision history.
