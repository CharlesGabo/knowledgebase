---
description: Ask the knowledge base and get a clear explanation with evidence
argument-hint: "Your project question"
---

Use only in a repository containing knowledge-base/index.md and knowledge-base/maintenance.md. Otherwise ask the user to open the knowledgebase repository without creating files elsewhere.
Read AGENTS.md, knowledge-base/index.md, knowledge-base/maintenance.md and knowledge-base/knowledge-commands.md. Follow the Ask a question procedure. Apply the fingerprint-and-review procedure in maintenance.md: verify unchanged files before reusing a retained full review; otherwise review all current topics, questions, decisions and tasks plus relevant source evidence/history. Include project-scope.md, integration.md and phase-0.md for project advice.

User question:
$ARGUMENTS

If no real question is supplied, or only literal placeholders/hints appear, ask what the user wants explained. Answer in clear, teaching-style language: direct answer first, define unfamiliar terms, explain why and use a small example when helpful. Cite evidence and distinguish Alex's answers, assistant interpretation and unknowns. Record substantive project questions with stable IDs and sources, reusing existing questions for follow-ups; administrative questions need no project Q-ID. Never archive this command wrapper as the user's verbatim question. Do not change task commitments merely because a question was asked. Recommend the user's Questions for Alex process for missing Owner answers; do not contact accounts.

Apply maintenance.md's fingerprint-and-review procedure to required reading. Unchanged content may be reused only with a matching reviewed fingerprint and sufficient retained evidence; after compaction or uncertainty, review again.

Task storage integration: before any task mutation, consult app/docs/usage.md. Read `python app/tasks.py list` for current data/token, then apply a structured JSON request via `python app/tasks.py apply --file <request-file>` (or stdin). Use a unique operation_id and the exact expected token. Never directly edit tasks.json, tasks.md or sources/task-events.md. Preserve manually supplied wording as SRC evidence first and link sources from the task. On conflicts, compare current data before retrying. The helper generates stable EVT history and Markdown. For a read-only listing, use the helper or generated view and create no task changes.
