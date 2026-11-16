# Portable Source Exports

Exports are self-contained Markdown snapshots intended for GPT Add Sources, other Agents, or human review.

## System export

- File: COUNCIL-SYSTEM-SOURCE.md
- Includes: system identity, concepts, principles, architecture, operating modes, memory rules, permissions, privacy, and limitations.
- Purpose: help another AI understand and discuss Council Sources without browsing the entire repository.

## Individual Council export

Use <slug>-SOURCE.md for a Council-specific snapshot. Include its identity, mission, scope, responsibilities, confirmed memory, relevant decisions/tasks, Project references, collaboration boundaries, unresolved questions, version, date, and source-file manifest.

## Export procedure

1. Read the current authoritative files.
2. Include only material needed for the intended recipient and task.
3. Preserve the difference between confirmed facts, proposals, and unknowns.
4. Add version, export date, and source-file manifest.
5. Review for private information, credentials, confidential content, and third-party rights.
6. Read back the generated file and check that it is understandable without hidden context.

## Important synchronization boundary

GitHub is the versioned file source. GPT Add Sources is generally an imported snapshot. A GitHub push does not refresh an already imported file; the user must re-import or replace the snapshot unless a platform integration has been explicitly verified.
