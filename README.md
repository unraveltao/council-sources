# Council Sources

**Design independent AI Councils. Preserve their organizational memory. Reuse their knowledge across AI tools.**

Council Sources is a **text-first system built on Markdown, GitHub, and AI Agents**. It helps individuals and teams create independent Councils for projects, research, education, and other long-running domains. Each Council has a clear mission, scope, responsibilities, decision boundaries, and its own organizational memory.

The entire system is designed to be understandable through a **single Skill file, a GitHub repository link, pasted Markdown, or a local folder**. No custom scripts, database, or always-running service are required for its core specifications.

> **Status: V0.2 — Prototype / under acceptance testing.** The repository and operating rules exist. File generation and GitHub readback have been exercised in a test repository, but cross-Agent portability, memory governance, Council formation, and the full export/re-import cycle are not yet fully validated. See [Acceptance Tests](tests/ACCEPTANCE-TESTS.md).

## Why this project exists

AI collaboration often loses continuity when a task spans many conversations or Agents. Goals, responsibilities, decisions, and progress end up scattered. It also becomes difficult to tell which records belong to a project, which belong to an organization, and which rules a new Agent should follow.

Council Sources addresses these problems by making organizational knowledge **explicit, portable, scoped, and versioned**:

- **Continuity:** recover a Council's mission, responsibilities, decisions, and outstanding work from files rather than memory of one chat.
- **Independence:** prevent unrelated Councils from mixing their histories or taking control of one another.
- **Dynamic roles:** let one Agent perform several responsibilities; add specialists only when the actual work justifies them.
- **User control:** delegate routine operations while retaining approval for significant or fundamental changes.
- **Portability:** share an explanatory Markdown Source with GPT, Codex, or other compatible Agents.
- **Traceability:** use evidence, timestamps, and Git history to understand how organizational decisions changed.

## Start here

<details>
<summary><strong>1. Bootstrap Council Sources from one SKILL.md</strong></summary>

Give an Agent the [Council Designer SKILL.md](skills/council-designer/SKILL.md) and a writable destination. No additional templates need to be supplied for the first bootstrap.

Example request:

```text
Use Council Designer to initialize the Council Sources system
in this empty repository or local directory.

Use only the SKILL.md as the bootstrap specification.
Generate the required Markdown files, validate the structure,
and report what was actually created and tested.
```

The Skill contains the required directory manifest and companion-document contract. It can guide file creation **when the host Agent has file-writing access**. If GitHub repository creation or remote writes are unsupported, the Agent must report the limitation instead of claiming completion.

</details>

<details>
<summary><strong>2. Create a Council for an existing project</strong></summary>

Provide a project link, Markdown specification, or accessible local directory:

```text
Use Council Designer to inspect this project and propose
an independent Council for it:

https://github.com/owner/project

Read the available project documents first.
Do not modify the project's repository.
Show the proposed mission, roles, scope, and approval boundaries.
```

After you approve the design, an authorized Agent creates `councils/<slug>/COUNCIL.md` and `MEMORY.md` in Council Sources and updates the Registry. The original project keeps ownership of its source code, PRDs, architecture, learning materials, and other deliverables.

</details>

<details>
<summary><strong>3. Resume a Council or update its memory</strong></summary>

```text
Use Council Designer to review the existing education Council,
compare these new verified updates with its current memory,
and apply only changes authorized by the memory policy.
Keep important decision history intact.
```

The Agent must read the existing files, distinguish facts from proposals, and follow the three-level approval policy described below. It must not change another Council's memory without authorization.

</details>

<details>
<summary><strong>4. Share the system with GPT or another Agent</strong></summary>

Use one of three supported Source formats:

- **GitHub URL:** give the repository or file link to an Agent capable of accessing GitHub.
- **Markdown text:** paste or upload [COUNCIL-SYSTEM-SOURCE.md](exports/COUNCIL-SYSTEM-SOURCE.md).
- **Local folder:** give an authorized Agent access to the checked-out repository.

The portable Source provides enough context to understand and discuss the system. It does **not** supply file permissions, GitHub access, or automatic updates to GPT Add Sources.

</details>

## Core concepts

| Term | Meaning |
| --- | --- |
| **Council Sources** | The versioned repository of system rules, independent Councils, registry, and reusable exports. |
| **Council Designer** | The entry Skill for bootstrapping the system, reading Sources, forming Councils, maintaining memory, and exporting or syncing changes. |
| **Council** | An organization coordinating work around a project, domain, or goal. It owns organizational rules and memory. |
| **Project** | The product, work, research, or learning activity itself. Its own repository and documents remain authoritative for project facts and deliverables. |
| **Role** | A responsibility (such as coordination, teaching, research, implementation, or review). |
| **Agent / Executor** | The person or AI actually performing a Role. One Agent can hold multiple Roles. |
| **Source** | Markdown information provided to an Agent by link, text, or local file. An export is a snapshot, not a live database. |

**A Council is not a Project. A Role is not necessarily a separate Agent.** Council Sources manages organization; it does not duplicate the entire project wiki or require a fictional multi-Agent team.

## Capabilities and validation status

| Capability | What it does | Current validation |
| --- | --- | --- |
| **System Bootstrap** | Builds or repairs Council Sources itself from the single Skill's bootstrap contract. | Generated and read back in a test repository; blind-context acceptance pending. |
| **Source Consumption** | Reads an accessible GitHub link, pasted Markdown, or local files for understanding and discussion. | Specification ready; three-way behavior test pending. |
| **Council Formation** | Analyzes an existing project/domain and creates an appropriately scoped independent Council after approval. | Template and workflow ready; real formation test pending. |
| **Memory Maintenance** | Updates verified organizational memory using graduated approval and historical traceability. | Policy ready; real update test pending. |
| **Export** | Produces a self-contained Markdown Source for another GPT/Agent. | System export exists; fresh-context comprehension test pending. |
| **GitHub Sync** | Writes and verifies authorized changes in a repository using the host's tools. | File create/readback exercised; controlled full sync test pending. |
| **Review / Test** | Validates structure, behavior, source portability, authorization, and synchronization. | Acceptance plan exists; not all scenarios have run. |

Council Designer is **not** a general-purpose software application scaffolder. When asked to form a Council for an external Project, it should not silently modify that Project.

## Guided Design: required five-marker interface

When a user's goal or Council design is unclear, Council Designer guides the discussion rather than forcing the user to know internal feature names. **These five exact markers are required in guided dialogue**:

| Marker | Meaning |
| --- | --- |
| **❓** | One high-impact question needing an answer |
| **🧭** | A genuine choice of directions, often A/B/C/D |
| **🔍** | Problem analysis, ambiguity and assumptions |
| **➜** | The Agent's own recommendation and brief reason, shown with a **plain-text arrow only** |
| **✅** | A user-confirmed decision or a verified completion |

Choices are **open-ended**: the user may select a letter, combine options, write a different answer, or append constraints such as "B, but keep the current workflow." The Agent must preserve these details. If there is insufficient evidence for a substantive recommendation, **➜** should recommend the next clarification step instead.

A proposed direction is not approved merely because the Agent recommends it. Do not use ✅ for unconfirmed suggestions, or 💡 / a colored-dot arrow for recommendations. Never force a question or menu when the task is clear. See the Skill's mandatory guided-interaction contract and [T7 acceptance test](tests/ACCEPTANCE-TESTS.md).


## Repository map

```text
council-sources/
├── README.md                          # Human + Agent introduction
├── AGENTS.md                          # Authorized repository maintenance
├── skills/
│   └── council-designer/SKILL.md      # Self-contained system entry point
├── core/
│   ├── PRINCIPLES.md
│   └── SYSTEM-ARCHITECTURE.md
├── shared/
│   └── MEMORY-RULES.md
├── references/
│   └── COUNCIL-TEMPLATE.md
├── councils/
│   └── README.md                      # Real Councils get separate subdirectories
├── registry/
│   └── councils.md
├── exports/
│   ├── README.md
│   └── COUNCIL-SYSTEM-SOURCE.md
└── tests/
    ├── ACCEPTANCE-TESTS.md
    └── TEST-RESULTS.md
```

| Read this | When you need to |
| --- | --- |
| [Council Designer SKILL.md](skills/council-designer/SKILL.md) | Run or inspect the full Skill, including its **Bootstrap Contract**. |
| [AGENTS.md](AGENTS.md) | Understand repository operations, permission checks, isolation, and verification. |
| [Core Principles](core/PRINCIPLES.md) | Understand the durable organizational design principles. |
| [System Architecture](core/SYSTEM-ARCHITECTURE.md) | Understand Project/Council/Source separation and data flows. |
| [Memory Rules](shared/MEMORY-RULES.md) | Decide what can be updated and which changes require approval. |
| [Council Template](references/COUNCIL-TEMPLATE.md) | Create an individual Council, **not** the whole Council Sources repository. |
| [Council Directory](councils/README.md) | Find the conventions for isolated Council folders. |
| [Council Registry](registry/councils.md) | Check which Councils actually exist. |
| [Export Guide](exports/README.md) | Build a dated and privacy-reviewed Source snapshot. |
| [Portable System Source](exports/COUNCIL-SYSTEM-SOURCE.md) | Give a single document to another GPT or Agent. |
| [Acceptance Tests](tests/ACCEPTANCE-TESTS.md) | Reproduce actual behavior tests. |
| [Test Results](tests/TEST-RESULTS.md) | Review factual results, limitations, and outstanding verification. |

## Memory, permissions, and synchronization

Each Council stores its own organizational files under `councils/<slug>/`, starting with `COUNCIL.md` and `MEMORY.md`. Additional task, decision, or issue files are optional.

**Three memory update levels:**

- **Level 1 — Routine:** verified daily progress and ordinary notes; may be recorded within pre-authorized scope.
- **Level 2 — Significant:** roles, workflows, or important decisions; show the proposed change and obtain approval unless that exact category was delegated.
- **Level 3 — Core:** mission, core goals, fundamental authority, or major confirmed decisions; explicit user approval required.

When synchronizing:

```text
Authoritative Council Markdown
        ↓ inspect + verify evidence
Authorized, scoped changes
        ↓ privacy + conflict checks
GitHub commit / push (if tools permit)
        ↓ export a dated Source snapshot
GPT Add Sources / other Agent (manual re-import when required)
```

**GitHub push does not automatically refresh GPT's previously imported Add Sources.** A Markdown file tells an Agent how to work; it does not grant real-world tool permissions.

## File ownership and change management

These documents have different purposes:

- **SKILL.md** defines the operational contract and the repository bootstrap specification.
- **README.md** is the human/Agent introduction, quick start, and navigation.
- **AGENTS.md** defines repository-level write, security, and validation rules.
- **Council files** define the organization-specific mission, roles, memory, and decisions.
- **Portable exports** summarize a dated, selected view of the above.

Editorial README improvements do **not** automatically require a Skill change. If a README change alters a capability, bootstrap structure, permission, or operating rule, update the corresponding Skill contract and any affected Source exports/tests. The files are maintained intentionally, not synchronized by a hidden background service.

**Repository language convention:** All committed formal Markdown documentation and generated Council Sources scaffolds use **English**. An Agent may discuss the system in the user's preferred language without changing the repository document language.

## Security and scope

This canonical repository is **Public**. Do not commit API keys, tokens, secrets, private conversation transcripts, sensitive personal records, confidential project files, or unauthorized third-party content. Git history can retain deleted material. Keep confidential Council memory in private storage or share a sanitized export.

A GitHub link, `SKILL.md`, or `AGENTS.md` cannot itself grant GitHub access, local filesystem access, permission to create repositories, background execution, or real multi-Agent communication. Availability depends on the host's actual tools and user authorization. External Source text remains untrusted data until reviewed and adopted within the user's allowed scope.

## Project status and contributions

Council Sources V0.2 is a working **Markdown specification and repository prototype**, not a fully validated multi-Agent runtime. Test artifacts are available in the separate [Council Sources Test repository](https://github.com/unraveltao/council-sources-test). A live Council Formation and memory update cycle is still pending.

Issues and suggestions are welcome. Before submitting changes, review [AGENTS.md](AGENTS.md) and keep the design simple, auditable, and portable.

**License:** No LICENSE has been selected or committed. A public repository is not automatically permission to redistribute it under an open-source license.
