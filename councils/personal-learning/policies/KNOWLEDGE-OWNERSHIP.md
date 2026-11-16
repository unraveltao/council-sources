# Knowledge Ownership and Storage Policy

> Version: 0.1.0 | Status: Initial policy

## Ownership

| Domain | Owner | Content | Authoritative location |
|---|---|---|---|
| Organization | Council | Mission, roles, workflows, decisions, organizational memory | Council directory |
| Curriculum / Project | Curriculum or Project | Domain maps, syllabus, lessons, code, experiments, tests, deliverables | Relevant Project/curriculum repository |
| Learner | User | Personal notes, interpretations, progress, questions, reflections | User-selected knowledge base |

References do not transfer ownership or grant write permission.

## Storage modes
- **Public:** knowledge in public repositories or publicly accessible locations.
- **Private:** knowledge in private repositories or local/private storage.
- **Hybrid:** categories split across public and private locations.

The Council must not require a separate private knowledge base. A Markdown label does not enforce privacy; actual privacy depends on repository visibility, permissions, and platform access controls.

## Access and write boundaries
Before reading or modifying learner-owned files, establish actual access and authorization. Read only relevant material. Do not copy learner notes into Council memory by default. AI-generated note drafts must be labeled until the learner adopts or edits them. Do not publish private or sensitive information.

## Feedback transfer
Learner evidence may inform teaching. Transfer only the minimum necessary generalized finding into curriculum or organization records, preserving source/date where practical.

## GitHub, local repository, and GPT
1. GitHub stores canonical Council Markdown.
2. A local Git clone is the working copy.
3. The user pulls, edits, commits, and pushes with ordinary Git.
4. A consolidated Markdown export is generated from canonical files.
5. The user manually replaces the GPT Knowledge source.
6. ZIP may package canonical files and export for backup/distribution.

Canonical Markdown files are the source of truth. Consolidated Source and ZIP are generated snapshots. GPT Knowledge does not automatically refresh from GitHub.

