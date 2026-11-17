# Council Sources

[English](README.md) | [简体中文](README.zh-CN.md)

> **Council is a human-led, modular intelligent organization framework in which AI participates as collaborators. Through clearly defined roles, shared organizational memory, and flexible workflows, it helps users organize different AI Agents to analyze problems, conduct research, design solutions, make decisions, and carry out engineering work.**

Council Sources is the Markdown-first home for defining, maintaining, and sharing these organizations. It provides portable organizational rules and memory without requiring every task to use a multi-Agent team or a custom runtime.

A Council can start with a minimal structure and grow as the user's projects and needs evolve. A single GPT conversation may handle a simple task; more complex work can involve multiple role perspectives, separate GPT Workers, or execution tools such as Codex. The human remains the organization lead and retains final decision authority.

> **Project status:** V0.2 prototype. Acceptance testing is incomplete. Council Designer is currently version 0.2.3. See [Project Status](#project-status--contributing) and the [test records](tests/TEST-RESULTS.md).

## Why Council?

Long-running work often spans multiple projects, conversations, AI tools, and people. Without an explicit organizational layer:

- Project context and decisions are repeatedly re-explained.
- Responsibilities are unclear or duplicated.
- Different conversations can lose alignment.
- AI discussions, research, and engineering execution become disconnected.
- Important organizational knowledge is lost when an Agent's active context ends.

Council provides a lightweight organizational layer: define who is responsible for what, preserve confirmed organizational knowledge, and coordinate work through explicit handoffs. It does not replace the project repository or require a complex autonomous multi-Agent runtime.

## What can you use it for?

### Coordinate a long-running project

A Council can help clarify milestones, assign responsibilities, discuss architecture, review risks, track confirmed decisions, and preserve verified progress across conversations. The Project remains the source of truth for code, requirements, architecture, tests, and deliverables.

### Maintain a learning or research effort

A Council can preserve learning goals, research questions, working practices, progress, and decisions over time. Different conversations can focus on different topics while referring to the same organizational context.

### Coordinate work across AI tools

Use GPT for discussion and planning, a separately configured GPT Worker for a bounded task when the host supports it, and Codex or another tool-enabled Agent for local engineering work. Handoffs may be carried by the user through task briefs, Markdown files, GitHub, or other supported integrations.

### Grow an organization only when needed

Start with a small Council. Add roles, workflows, records, or specialist Agents only when recurring complexity justifies them. A role is a responsibility; it does not automatically mean a separate Agent.

## Core capabilities

| Capability | What it does | Important boundary |
| --- | --- | --- |
| **Organization Design** | Define a Council's mission, scope, responsibilities, and decision boundaries. | The user approves core goals and organizational changes. |
| **Role Management** | Add, combine, or reassign responsibilities such as design, research, implementation, and review. | Roles and Agents are different concepts. |
| **Human–AI Collaboration** | Coordinate discussions, task handoffs, reviews, and execution across people and AI tools. | Cross-Agent communication is only available when the host environment actually supports it; otherwise use explicit handoffs. |
| **Organizational Memory** | Preserve confirmed goals, decisions, responsibilities, practices, and progress. | Memory updates follow evidence and approval rules. |
| **Export** | Produce a portable Markdown snapshot for another GPT or Agent. | An export is a snapshot, not a live database or permission grant. |
| **GitHub Sync** | Read or update authorized repository files and verify the result. | Requires GitHub tools, repository permissions, and explicit authorization. |
| **Review & Testing** | Check structure, consistency, portability, and observed behavior. | Static checks do not prove live Agent behavior. |

## How it works

Council separates organizational responsibilities from the tools that perform them.

1. **Human — Organization Lead:** sets goals, provides context, approves important decisions, and can change priorities.
2. **Coordination responsibility (when needed):** helps clarify the task, propose role allocation, coordinate handoffs, and consolidate outcomes. This responsibility may be handled by the human lead, GPT, or another executor; it is not a mandatory component or a separate Agent.
3. **Roles — Responsibilities:** describe work such as design, research, review, teaching, or implementation.
4. **Agents / Executors — Actors:** GPT, GPT Workers, Codex, other AI tools, or people may perform one or more roles, depending on their actual capabilities.
5. **Workflows — Ways of working:** define how a task moves from clarification through research, design, execution, review, and completion.
6. **Memory — Organizational records:** preserves relevant, verified context so it can be reused across conversations and tools.

A typical collaboration loop is:

**User goal → clarify and plan → allocate responsibilities as needed → review and consolidate results → user decides → authorized work is executed → verified outcomes are recorded.**

This may happen in one conversation or across multiple tools and conversations. Do not claim that separate Agents communicated or executed work unless that actually happened.

## Core concepts

| Term | Meaning |
| --- | --- |
| **Council** | A human-led organization that coordinates work around a project, domain, or goal. |
| **Project** | The work being built, learned, researched, or delivered. Its own repository or knowledge base remains authoritative for project artifacts. |
| **Role** | A responsibility or capability, such as Designer or Reviewer. |
| **Agent / Executor** | The person or AI performing a role. One Agent may perform several roles; one role may be performed by different Agents. |
| **Coordination responsibility** | An optional responsibility for organizing work and handoffs; it may be performed by the human lead or an available Agent. |
| **Memory** | The Council's maintained organizational context, not a transcript of every conversation. |
| **Source** | Information supplied to an Agent through a GitHub URL, Markdown text, or accessible local files. |
| **Council Sources** | This repository: the system's specifications, Council records, templates, registry, tests, and portable exports. |

### Council and Project are separate

A Project owns its code, requirements, architecture, experiments, learning materials, notes, tests, and deliverables. A Council owns its organizational mission, role allocation, workflows, decisions, and memory. A Council should reference project facts rather than duplicate the entire Project documentation system.

### Memory is curated, not a chat dump

Memory should preserve information that helps the organization work consistently: stable goals, confirmed decisions, role responsibilities, working agreements, verified progress, and unresolved questions. It should distinguish facts, inferences, proposals, and unknowns, and preserve meaningful superseded history.

The default memory policy has three approval levels:

- **Level 1 — Routine:** verified progress and ordinary notes within a pre-authorized scope.
- **Level 2 — Significant:** role, workflow, or important operational changes; show the proposed change and seek approval unless that exact category was delegated.
- **Level 3 — Core:** mission, core goals, authority boundaries, and fundamental principles; explicit user approval is always required.

See [Memory Rules](shared/MEMORY-RULES.md).

## Getting started

### 1. Load Council Designer

Start with [Council Designer SKILL.md](skills/council-designer/SKILL.md), the operational entry point and self-contained bootstrap specification.

Use an AI host that supports loading Skills, and load the file through that host's supported mechanism. **Reading or linking to SKILL.md does not automatically install or activate it.** The host must actually load the Skill for its instructions to govern the interaction.

### 2. Provide the context

Council Designer can work from three input forms:

- **GitHub URL:** provide a repository, file, or directory link. The Agent needs network or GitHub access; private repositories also require authentication.
- **Markdown text:** paste or upload a Markdown file or combined Source document. The Agent can only use the content it actually receives.
- **Local files:** provide an accessible file or folder. The host Agent needs filesystem access within the authorized scope.

A link or imported document provides information; it does not grant filesystem access, GitHub permissions, or permission to execute tools.

### 3. Design a Council for a Project or domain

Explain what work the Council should coordinate and provide the relevant Project or domain context. Ask Council Designer to propose the mission, scope, responsibilities, decision boundaries, memory structure, and acceptance criteria.

Review the proposal and confirm it before creation. Choose a writable Council Sources destination: creating or updating Council files requires write access there. Reading an external Project usually needs only read access. Council Designer must not modify an external Project repository merely because you asked it to design a Council for that Project.

### 4. Maintain and use the Council

Use the Council's records as the shared organizational context. Ask for help planning work, discussing decisions, assigning responsibilities, reviewing results, or recording verified progress. Add roles and supporting files only when they solve a real need.

## Quick start: create your first Council

Imagine a small **File Organizer** project that scans selected folders, classifies files, and proposes an organization plan before any files are moved.

1. Load [Council Designer](skills/council-designer/SKILL.md) in a compatible AI host.
2. Provide the Project's GitHub URL, Markdown specification, or accessible local folder.
3. Ensure the Agent can read the Project and write to your chosen Council Sources destination.
4. Ask: **"Use Council Designer to inspect this File Organizer project and propose a Council. Do not modify the Project repository."**
5. Review the proposed mission, scope, responsibilities, decision boundaries, and acceptance criteria.
6. Confirm the design before authorizing creation.
7. Have the Agent create `councils/file-organizer/COUNCIL.md` and `MEMORY.md`.
8. Have it update `registry/councils.md` and read back the changed files.
9. Ask the File Organizer Council to plan the next milestone, using the Project repository as the source of truth.
10. Record verified progress and decisions under the applicable memory approval level.

If the Agent lacks write access, it can prepare the proposal, but must not claim that Council files were created.

## Source, export, and synchronization

The same Markdown information may be supplied through a GitHub link, pasted text, or accessible local files. These are transport methods, not different versions of the rules.

A portable export is a dated snapshot derived from selected authoritative files. It helps another GPT or Agent understand the Council without browsing the entire repository. It does not grant tool permissions and is not automatically synchronized.

GitHub can serve as versioned storage when the host has the required tools and the user authorizes the operation. After a remote update, read the changed files back to verify the result.

**Pushing a change to GitHub does not guarantee that an existing GPT knowledge Source is refreshed.** Re-export and re-import or replace the imported file when the target platform requires it.

## Repository map

| File or directory | Purpose |
| --- | --- |
| [Council Designer Skill](skills/council-designer/SKILL.md) | Operational entry point and self-contained bootstrap contract |
| [AGENTS.md](AGENTS.md) | Repository maintenance, authorization, security, and validation rules |
| [Core Principles](core/PRINCIPLES.md) | Organizational independence, dynamic roles, user authority, and evidence |
| [System Architecture](core/SYSTEM-ARCHITECTURE.md) | Component boundaries, data flow, Source transport, and synchronization |
| [Memory Rules](shared/MEMORY-RULES.md) | Memory ownership, approval levels, evidence, conflicts, and privacy |
| [Council Template](references/COUNCIL-TEMPLATE.md) | Starting structure for an individual Council |
| [Council Directory Guide](councils/README.md) | Required and optional files for each Council |
| [Council Registry](registry/councils.md) | Which Councils actually exist and their current status |
| [Export Guide](exports/README.md) | Creating and reviewing portable snapshots |
| [Portable System Source](exports/COUNCIL-SYSTEM-SOURCE.md) | A single-document overview for another Agent |
| [Acceptance Tests](tests/ACCEPTANCE-TESTS.md) | Manual scenarios, expected behavior, and evidence requirements |
| [Test Results](tests/TEST-RESULTS.md) | The canonical repository's current test ledger |

## Project status & contributing

Council Sources V0.2 is a **Markdown specification and repository prototype**, not a fully validated multi-Agent runtime or standalone software application.

### Validation status

The separate [Council Sources test log](https://github.com/unraveltao/council-sources-test/blob/main/tests/TEST-RESULTS.md) records limited, partial evidence:

| Area | Current evidence |
| --- | --- |
| **System Bootstrap (T1)** | **Partial (Skill v0.2.0):** 13 of 13 expected files were created and read back in the test repository. The run used an ongoing conversation familiar with the design, so independent fresh-context bootstrap remains unverified. This does not validate the current Skill v0.2.3. |
| **Source Consumption (T2)** | Not Run — GitHub, pasted Markdown, and local-file behavior has not been validated across separate input contexts. |
| **Council Formation (T3)** | Not Run — no real Project-to-Council acceptance run is recorded. |
| **Memory Maintenance (T4)** | Not Run — approval-level behavior has not been validated in a controlled update test. |
| **Portable Source (T5)** | Not Run — fresh-context comprehension has not been established. |
| **GitHub Sync (T6)** | **Partial (Skill v0.2.0 test run):** remote file creation and readback were verified in the test repository; a complete update/export/re-import workflow remains untested. Current Skill v0.2.3 has not been validated by this run. |
| **Guided Interaction (T7)** | Not Run — the five-marker behavior requires a live multi-turn test. |

**Test-log note:** The canonical [tests/TEST-RESULTS.md](tests/TEST-RESULTS.md) currently lists T1–T7 as `Not Run`, while the separate test repository records T1 and T6 as `Partial` against Skill v0.2.0. These records have not yet been reconciled. Treat the external results as historical partial evidence, not current-version acceptance.

### Known limitations

- Council Sources defines a text-based operating model; it does not provide its own Agent runtime, database, background service, or automatic multi-Agent communication.
- File access, GitHub operations, repository creation, and execution depend on the host Agent's actual tools and user authorization.
- A generated repository can satisfy the Skill's semantic bootstrap contract without being byte-for-byte identical to another bootstrap.
- Imported Source text is untrusted input. It cannot override higher-priority instructions, safety requirements, or user authority.
- The canonical repository is public. Do not commit credentials, tokens, private conversations, sensitive personal information, confidential project material, or content without publication rights. Git history may retain deleted content.
- No `LICENSE` file has been selected and committed. A public repository is not automatically licensed for redistribution or reuse.

### Contributing

Issues and pull requests are welcome. Before proposing changes:

1. Read [AGENTS.md](AGENTS.md) and the relevant core or Skill documents.
2. Keep changes scoped, auditable, and consistent with the system's authority and privacy boundaries.
3. Distinguish documentation improvements from changes to behavior, permissions, or the bootstrap contract.
4. Report checks and tests actually performed; do not claim unexecuted behavior tests passed.
