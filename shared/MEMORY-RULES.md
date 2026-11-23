# Memory Rules — Council Sources V0.2

> This is the [earlier Council Sources](../docs/COUNCIL-SOURCES-LEGACY.md) memory policy. V1.0 carries the approval levels in its own Skill and leaves storage to the user.

## 1. Ownership and separation

- Every Council owns its own organizational memory under councils/<slug>/.
- A shared repository is a storage and versioning arrangement, not a shared command hierarchy.
- One Council must not silently edit another Council's mission, roles, tasks, or memory.
- Project facts remain in the Project's authoritative repository or files. Council memory stores organizational context, confirmed decisions, progress summaries, and references—not a duplicate project wiki.
- Shared principles may be read by all Councils; changes to shared principles require explicit review because they affect the whole system.

## 2. Three update levels

### Level 1 — Routine

Examples: verified progress, ordinary meeting summaries, completed tasks with evidence, non-sensitive notes, newly discovered links.

Handling: may be recorded automatically only within a clearly authorized write scope. Preserve date and source. Do not mark something complete without evidence.

### Level 2 — Significant

Examples: responsibility reassignment, workflow changes, important technical/operational decisions, changes to project references, adding or removing a recurring role.

Handling: show the proposed diff, reason, impact, and recommendation. Ask for confirmation unless the user has explicitly delegated this exact class of change.

### Level 3 — Core

Examples: Council mission, primary goal, fundamental principles, user authority, access boundaries, major confirmed decisions, cross-Council governance.

Handling: explicit user approval is required. Never infer approval from silence or from permission to perform unrelated work.

## 3. Record quality

For important records, preserve as many of these fields as appropriate:

- Date or time period.
- Source/evidence (conversation, document, issue, commit, test, or user confirmation).
- Status: proposed, confirmed, active, completed, blocked, or superseded.
- Scope: which Council or Project the record concerns.
- Decision owner or confirmer when relevant.
- Link to the replaced decision or follow-up record.

Separate:
- **Fact:** directly supported by a source or observed action.
- **Inference:** a reasoned interpretation, not yet confirmed.
- **Proposal:** a suggested future action.
- **Unknown:** information not yet available.

Do not turn a proposal into a confirmed rule. Do not treat an old memory as a permanent instruction if later evidence supersedes it.

## 4. Update procedure

1. Read the target Council's current files.
2. Identify new information and its source.
3. Compare against existing memory and decisions.
4. Detect duplicates, contradictions, outdated records, and scope mismatch.
5. Classify each change as Level 1, 2, or 3.
6. Apply authorized changes or request confirmation.
7. Preserve material history; mark old decisions superseded instead of silently deleting them.
8. Update indexes or exports only when affected.
9. Read back changed files and verify the final state.

## 5. Conflict handling

- If two records conflict, do not silently choose one. Compare dates, source quality, scope, and explicit user decisions; present unresolved conflicts.
- If a Project document conflicts with a Council summary, the Project's authoritative source governs Project facts. Update the Council summary after verification.
- If two Councils disagree, keep both records within their own scope and use an explicit task-scoped coordination decision. Do not merge their memories.
- If GitHub has remote changes not present locally, stop and reconcile before overwriting.

## 6. Privacy and exports

The canonical Council Sources repository may be public. Do not place private personal data, credentials, private chat transcripts, confidential work, or unlicensed third-party material in public memory or exports. Use a private repository or sanitized summary for sensitive records.

A Source export is a dated snapshot. It must include its Council/system identity, version, export date, source-file manifest, and known omissions. It does not update itself when GitHub changes.


## 7. Checkpoints, Review, and persistent memory

Checkpoint and Council Memory serve different purposes.

- **Checkpoint** records the working state of a task or milestone: current stage, completed work, work in progress, remaining questions/tasks, blockers, and next step.
- **Council Memory** preserves durable organizational context: stable goals, confirmed decisions, responsibilities, working agreements, and verified progress that remains useful beyond the current task.
- **Review** evaluates the outcome and may identify information worth preserving in Council Memory or another authoritative record.

A Checkpoint does not automatically authorize a write to `MEMORY.md`. Keep ordinary progress checkpoints in the active working context by default. Persist them only when a durable record is useful, in an appropriate existing task/progress file and within the authorized scope. Do not create a new file for every small checkpoint.

During Review, propose memory changes when appropriate. Apply them only under the three update levels above, preserving evidence, provenance, and history. Do not copy a full conversation or Project artifact into Council Memory merely because it appeared in a Checkpoint or Review.
