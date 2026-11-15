# Taskroom — local task board

A personal Kanban board and calendar for this knowledge base. Task commands and the UI share one authoritative task store. This is a local workspace tool, separate from the TMA customer website.

## Start

Double-click `app/start.cmd`, or from the repository root run:

```text
python app/server.py --open
```

Open **http://127.0.0.1:8765**. Keep the Python process running for live sync; Ctrl+C stops it. Python 3.12 is available on the implementation machine. No packages, npm, database server or account connection are required. An occupied port can be changed with `--port 8766`.

## Documentation

- [Context and agreed requirements](docs/context.md)
- [Architecture, task schema and interfaces](docs/architecture.md)
- [Usage, task helper and recovery](docs/usage.md)
- [Decisions and rationale](docs/decisions.md)
- [Changes, validation and remaining limitations](docs/changes.md)
- [Exact task page before migration](docs/tasks-before-migration.md) — historical archive; do not edit. Its original relative links resolve from `knowledge-base/`, where the page lived before migration.

## Checks

```text
python -m unittest discover -s app/tests -v
node --test app/tests/dates.test.js
node --check app/static/app.js
```

Tests mutate temporary fixtures only. Never use real task status changes merely to test the app. Runtime locks and Python caches are git-ignored. The app does not make commits or push changes.
