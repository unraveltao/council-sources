# Council Registry

This file is a lightweight index of real Council instances. It records where each Council lives and its current lifecycle and acceptance states. It is not a central memory store, task tracker, or command hierarchy.

| Council | Type / Scope | Related Project or Domain | Directory | Lifecycle Status | Acceptance Status | Last Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Personal Learning Council | Domain / Education | Unravel Language + AI Engineering | `councils/personal-learning/` | Active | Not Run | 2026-11-17 |

## Lifecycle status

Lifecycle describes whether the Council exists and is currently operating. It is independent of acceptance status.

- **Proposed** — a specific Council has been proposed for formal design/evaluation at the user's request; the decision to authorize creation is still pending. Do not register speculative ideas.
- **Draft** — creation has been authorized and the initial Council files are being prepared or reviewed.
- **Active** — the Council exists and is in use. Active does not mean that it has passed acceptance.
- **Paused** — the Council exists but is intentionally not operating for now.
- **Archived** — the Council is retained for reference but is no longer active.

## Acceptance status

Acceptance describes the latest evidence-backed validation state of the Council's defined acceptance criteria.

- **Not Defined** — no observable acceptance criteria have been established.
- **Not Run** — criteria exist, but no acceptance run has been performed.
- **Partial** — some checks have been performed, but the full acceptance scope is incomplete.
- **Passed** — all required acceptance criteria for the recorded scope and version have passed with evidence.
- **Failed** — at least one required criterion failed in the latest relevant run.
- **Blocked** — acceptance cannot proceed because a required input, tool, permission, or environment is unavailable.

Do not infer acceptance status from lifecycle status. A Council may be Active while acceptance is Not Run, Partial, or Failed. A Passed result applies only to the tested scope/version and must be supported by a test record.

## Registry rules

1. Register only a concrete Council proposal that the user has explicitly asked to design/evaluate. Proposed does not authorize creation; do not register casual ideas, examples, or unrequested suggestions.
2. Use a stable, lowercase slug for each Council directory. For Proposed entries, the directory may be the intended path; create it only after creation is authorized.
3. Keep the Council's mission, roles, memory, decisions, and tasks in its own directory. Do not copy those details into this index.
4. Maintain Lifecycle Status and Acceptance Status as separate fields. Use only the values defined above.
5. Update the entry when a Council is created, activated, paused, resumed, archived, or when its acceptance evidence changes.
6. Update Last Reviewed when the entry is materially changed or its state is checked.
7. Never mark acceptance Passed based only on file existence, documentation, or an unexecuted test plan.
8. Do not change another Council's status or ownership without authorization.
