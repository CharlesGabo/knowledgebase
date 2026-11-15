# Development and review baseline

## Scope

The operations rules below come from SRC-001. SRC-005 explicitly adopts the existing development process for website work and adds website workflow details. These project policies do not authorize operational actions from this knowledge-base task. Refer to sources for exact procedures. [SRC-001 ??3?13](../tma-ops-processes.md)

## Website workflow

Alex approves this sequence: unfinished work stays in the sandbox; once shared DEV is available, changes go there only when ready for review and headed for production soon. Participants are the user, Alex and Chaze, as named in the reply; do not merge participant identities. Phase 0 may start with sandbox/documentation work. See [D-003](decisions.md#d-003) and [environment readiness](technology.md#website-environments-and-platform-direction). [SRC-003](sources/SRC-003-website-environments.md)

SRC-005 now specifies: significant features/database changes start with a reviewed design note; feature branches in TMA GitHub; PRs run tests and preview deploys; Alex reviews/approves and main requires approval; TMA applies database migration files to production. Operations changes require smaller PRs, affected-area tests and DEV verification before release. Password-protected staging keeps progress visible. These are prescribed processes, not confirmed deployed tooling. Detailed DEV readiness/promotion mechanics remain in [Q-007](questions.md#q-007). [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 4-6.

### Notion questions and task tracking

The user has a Notion **Questions for Alex** area. If the knowledge base cannot answer an Owner question, recommend posting there manually, with the missing context/decision and a suggested question. For access/tool blockers use **Area: Access / tools**. Do not recommend asking again about facts already answered here; cite the answer first. No Notion URL is supplied and no posting/monitoring is authorized. [SRC-004](sources/SRC-004-completed-setup.md)

The website framework uses a shared Notion Kanban board (Backlog -> To Do -> In Progress -> Review -> Done), WIP limit 1-2, plus Work Log, Knowledge Base and Decision Log. Each phase starts with scoping and ends with demo/review; flag blockers lasting more than a shift. Log each shift with date, hours, tasks, PR links and blockers. The user reports hour tracking enabled and shift commands tried; actual Work Log submissions are not verified. [SRC-004](sources/SRC-004-completed-setup.md); [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 1, 6.

SRC-001 says operations work comes from GitHub Issues and has separate end-shift issue updates. The website framework describes Notion tracking and says Work Log replaces separate end-shift updates. Keep these scoped to their sources; cross-system task/update expectations need clarification in [Q-011](questions.md#q-011).

## Operations work and review

- GitHub Issues hold specs and acceptance criteria; prioritize in-progress work. Investigate code/tests/docs first and record learning notes. Business intent, priorities, access and risky decisions go to Owner with Context / Question / Options (recommendation) / Meanwhile; label `needs-owner` and proceed with other work.
- Record assumptions in PRs and decisions in the same PR. Start-shift pulls main and reads replies; end-shift pushes a draft PR and comments on touched issues. Optional hours tracking uses a Notion Work Log. Exclude personal, hiring, pay and contract details from that repository.
- Branch from current main; keep PRs small, never commit directly to main, merge main rather than rebasing shared branches. Review responses use new commits, not force pushes.
- PR sections: What, Why, Migration (or No migration), Tests, Risks / notes for review; add assumptions/questions where needed. State change type and scope exclusions. Open draft, ready only with green CI and complete description.
- Report unrelated issues separately. If design conflicts with technical constraints, finish clear work and stop at the unresolved boundary.
- Protected contributor areas include work board, unsolicited roadmap changes, production SQL packages, workflows, Vercel config/secrets and merged migrations.
- Claude handles design/UI and small diagnosed fixes; Codex handles backend. Every PR needs independent Codex SHIP review; large features also need independent design review. Alex reviews scope, sensitive areas and maintainability before merging. Source prompt convention: one fenced block containing thread title and folder; describe risk rather than a Codex tier.

## Migration and validation baseline

Migration version is 10000 above the highest version across GitHub branches, work board and local unpushed branches, confirmed by the orchestrator; do not use timestamps or `supabase migration new`. Use transaction, two-second local lock timeout, ASCII and LF, explanatory/undo header, ledger insertion before commit and schema reload notification afterward. Separate data changes and record row counts; never edit merged migrations. New tables need security checks and indexes. [SRC-001 ?7](../tma-ops-processes.md)

Rebuild from zero, exercise personas, prove allowed and denied access in rolled-back SQL transactions and test anon on populated tables. Service-role/postgres tests do not prove RLS. PR migration evidence lists versions, objects, changes, rollback, personas and heavy queries. Alex deploys guarded preflight/apply/verify/rollback packages; database changes precede dependent frontend releases. [SRC-001 ?7](../tma-ops-processes.md)

| Check | Source command |
|---|---|
| Node | `npm run test:ci` |
| Deno | `npm run test:deno` / `npm run test:deno:run` |
| Replay | `node tools/sandbox-reset.mjs` |
| Ledger | `node tools/check-migration-ledger-lines.mjs origin/main` |
| Architecture | `npm run arch:check` |
| Combined | `npm run verify` |

Known failures are a ratchet, never expanded to get green; remove newly passing known failures. Distinguish stale assertions from regressions. Include test summaries, access evidence and UI screenshot/description as relevant. CI replay uses checks from main and rejects public functions executable by anon/PUBLIC. These commands belong to the operations repository and were not run here. [SRC-001 ??7?8](../tma-ops-processes.md)

## Merge and deployment

See [D-002](decisions.md#d-002) for merge restrictions and rationale. Confirm code deployment by a new Ready Vercel deployment row; a green tick alone may represent a skipped build. No deployment row for docs-only work is expected. The source reports correcting a skipped code deployment through a commit touching a watched path. [SRC-001 ?10](../tma-ops-processes.md)

## History

2026-11-15: SRC-003 establishes the website sandbox-to-shared-DEV review direction. SRC-005 subsequently supplies website PR approval and TMA migration responsibilities, while shared-DEV readiness remains open. SRC-004 records completed setup and Notion Questions for Alex. Tracking/update differences remain in Q-011.
