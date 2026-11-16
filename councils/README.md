# Councils

Each real Council lives in its own directory: councils/<slug>/.

Minimum files:
- COUNCIL.md — mission, scope, responsibilities, decision boundaries, working practices, and Project references.
- MEMORY.md — current organizational memory and verified state.

Optional files, created only when useful:
- DECISIONS.md — decision history and rationale.
- TASKS.md — Council-owned tasks and status.
- ISSUES.md — unresolved organizational issues.
- workflows/ — recurring procedures that benefit from explicit documentation.

## Isolation

Different Councils must not share one combined MEMORY.md. They may share selected information through an explicit, task-scoped collaboration or a sanitized shared reference, but each Council remains responsible for its own records.

The Project's own repository remains authoritative for Project code, product requirements, architecture, learning materials, and deliverables. A Council should link to those sources rather than copy them wholesale.

After creating a Council, update registry/councils.md. Do not create placeholder Council folders merely to make the directory tree look complete.
