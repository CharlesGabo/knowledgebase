# Task event evidence

Generated from the append-only events in tasks.json. Each EVT ID is stable. UI events are user reports, not independent completion verification.

## EVT-000001

- Author: You via local UI
- Original/intake time: 2026-11-16T00:11:49+08:00
- Subject: update T-001
- Type: Task change / user report

```json
{
  "request": {
    "action": "update",
    "id": "T-001",
    "changes": {
      "status": "In progress",
      "order": 0
    },
    "expected": "bf9a32c26114bbc8a0fa877d0acabec9664ff6be153418e42e28301bf60705ad",
    "operation_id": "f735a957-8b08-4a9a-a5ed-edcbe998b395",
    "actor": "You via local UI"
  },
  "before": {
    "id": "T-001",
    "title": "Understand operations and write learning notes",
    "description": "Trace one sandbox product through catalog, pricing and order; note data model, FTP pipeline and business rules.",
    "owner": "Charles",
    "assigned_by": "You",
    "assignment_note": "User requested; adopted assistant breakdown",
    "sources": [
      "sources/SRC-011-monday-phase-0-tasks.md"
    ],
    "status": "To do",
    "priority": "Normal",
    "start": "2026-11-16",
    "end": null,
    "deadline": null,
    "dependencies": [
      "LEGACY-T-008"
    ],
    "order": 0,
    "archived": false,
    "notes": [],
    "revision": 1,
    "completed_at": null
  },
  "after": {
    "id": "T-001",
    "title": "Understand operations and write learning notes",
    "description": "Trace one sandbox product through catalog, pricing and order; note data model, FTP pipeline and business rules.",
    "owner": "Charles",
    "assigned_by": "You",
    "assignment_note": "User requested; adopted assistant breakdown",
    "sources": [
      "sources/SRC-011-monday-phase-0-tasks.md"
    ],
    "status": "In progress",
    "priority": "Normal",
    "start": "2026-11-16",
    "end": null,
    "deadline": null,
    "dependencies": [
      "LEGACY-T-008"
    ],
    "order": 0,
    "archived": false,
    "notes": [],
    "revision": 2,
    "completed_at": null
  }
}
```

## EVT-000002

- Author: You via local UI
- Original/intake time: 2026-11-16T00:11:58+08:00
- Subject: update T-001
- Type: Task change / user report

```json
{
  "request": {
    "action": "update",
    "id": "T-001",
    "changes": {
      "status": "To do",
      "order": 999
    },
    "expected": "09030fdf7b354536758eeb7076a2ca34d57082e0ebc9f61d5c61bf338a3a7b26",
    "operation_id": "0f469fe9-3b48-48ad-b1f2-152a82242654",
    "actor": "You via local UI"
  },
  "before": {
    "id": "T-001",
    "title": "Understand operations and write learning notes",
    "description": "Trace one sandbox product through catalog, pricing and order; note data model, FTP pipeline and business rules.",
    "owner": "Charles",
    "assigned_by": "You",
    "assignment_note": "User requested; adopted assistant breakdown",
    "sources": [
      "sources/SRC-011-monday-phase-0-tasks.md"
    ],
    "status": "In progress",
    "priority": "Normal",
    "start": "2026-11-16",
    "end": null,
    "deadline": null,
    "dependencies": [
      "LEGACY-T-008"
    ],
    "order": 0,
    "archived": false,
    "notes": [],
    "revision": 2,
    "completed_at": null
  },
  "after": {
    "id": "T-001",
    "title": "Understand operations and write learning notes",
    "description": "Trace one sandbox product through catalog, pricing and order; note data model, FTP pipeline and business rules.",
    "owner": "Charles",
    "assigned_by": "You",
    "assignment_note": "User requested; adopted assistant breakdown",
    "sources": [
      "sources/SRC-011-monday-phase-0-tasks.md"
    ],
    "status": "To do",
    "priority": "Normal",
    "start": "2026-11-16",
    "end": null,
    "deadline": null,
    "dependencies": [
      "LEGACY-T-008"
    ],
    "order": 999,
    "archived": false,
    "notes": [],
    "revision": 3,
    "completed_at": null
  }
}
```

