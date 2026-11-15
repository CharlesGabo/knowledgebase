# Decisions and history

D-001 and D-002 are reported operations-platform decisions from [SRC-001](../tma-ops-processes.md). D-003 and D-004 record Owner direction for the website from [SRC-003](sources/SRC-003-website-environments.md).

## D-001

- Decision: Leads are Accounts; Customer is an Account lifecycle status, not a separate entity.
- Status: Reported accepted operations baseline.
- Decided by: Owner according to the source's decision-document authority table; individual approval and date unknown.
- Evidence: SRC-001 ??1,13 cites upstream `docs/DECISIONS_LOG.md`, unavailable here.
- Rationale: Not supplied. Consequence: Account is the durable organization record.
- History: First recorded here 2026-11-15; no supersession received.

## D-002

- Decision: Merge commit or squash merge; never rebase-and-merge; CLI merges use `--no-ff`.
- Status: Reported operations instruction.
- Decided by / decision date: Unknown; Alex is the reported merger.
- Evidence: SRC-001 ?10.
- Rationale: Vercel's ignore script compares one commit with its parent. Source reports a rebase merge skipped a real deployment on 2026-09-15, leaving production 23 hours behind.
- Consequence: Verify a new Ready deployment row for code changes.
- History: First recorded here 2026-11-15. Incident date is not the decision date.

## D-003

- Decision: Phase 0 may proceed in the sandbox and begin as documentation. Future shared DEV receives only review-ready changes headed for production soon; unfinished work stays in the sandbox. Keep production separate.
- Status: Approved direction; DEV rollout and access pending, not completed.
- Decided by: Alex, identified as Owner by the user.
- Decision/effective dates: Original communication date unknown; future DEV policy applies once DEV is shared. Added 2026-11-15.
- Evidence: [SRC-003](sources/SRC-003-website-environments.md); related [Q-005](questions.md#q-005).
- Context/rationale: Alex plans to move DEV out of the organization currently shared with PROD, clean it up and improve test data to support collaboration without overlap. See [current technical status](technology.md#website-environments-and-platform-direction).
- Consequences: Sandbox now, conditional shared DEV later. Planned DEV data includes real vendor catalogs. No production access or general production-data copying permission follows.
- History/supersession: SRC-001 sections 2 and 4 previously stated DEV is synthetic-only, for Alex/internal threads, and contributors must never write to shared DEV. SRC-003 explicitly changes the intended future website DEV participation/data policy; retain those older statements as historical operations context, not unconditional current website rules. Broader operations policy changes and actual rollout are not evidenced. Supersession is based on explicit Owner direction, not message recency. No earlier approved website decision was supplied.

## D-004

- Decision: Keep the website on Supabase and within the existing project framework; alternatives may be proposed to Alex.
- Status: Approved direction/preference; no alternative approved.
- Decided by: Alex, Owner.
- Decision date: Unknown; added 2026-11-15.
- Evidence: [SRC-003](sources/SRC-003-website-environments.md).
- Context/rationale: Preserve the existing platform/framework; further rationale not supplied.
- Consequences: SRC-003 alone did not resolve frontend technology, hosting or schema/API boundaries. SRC-005 now supplies the intended stack and integration framework; exact contracts/environment topology remain unresolved. See [Q-002](questions.md#q-002).
- History: Replaces the earlier lack of website platform evidence; no earlier platform approval is known to be superseded.

## D-005

- Direction: Two separate applications/Auth systems; operations owns and publishes curated data; website submissions enter operations inbox processing; reuse existing business integrations. See [integration](integration.md) and [scope](project-scope.md) for the canonical details.
- Status: Current working framework, designated by the user; not a final detailed specification or evidence of completed implementation.
- Author: Alex, technical lead/co-developer in the framework. Separate final approval/sign-off date unknown.
- Document date: November 2026; added 2026-11-15.
- Source: [SRC-005](sources/SRC-005-website-counter-proposal.md), sections 2-7; user designation in [SRC-004](sources/SRC-004-completed-setup.md).
- Rationale/consequences: Isolate security boundaries, use operations conventions and one owner per data type. Operations extension comes first; design/review before significant work. No new sync Actions worker. Open choices are tracked in Q-010.
- History: Supersedes the knowledge base's earlier missing-scope/stack statements with evidence, not an earlier approved design. The referenced original proposal is unavailable. Do not infer SRC-005 supersedes SRC-003's shared DEV plan; chronology/effect is unresolved in Q-009.

## Recording future changes

Use stable D-IDs with status, decision date, decision-maker/authority, source, context, rationale, consequences and affected topic links. For supersession retain the previous wording and source, replacement ID/link, reason and effective date (unknown if absent). Newer evidence alone does not establish authority. Unresolved conflicts belong in the question register.
