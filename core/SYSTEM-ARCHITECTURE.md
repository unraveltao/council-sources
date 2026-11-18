# Council Sources — System Architecture

## 1. Components

### Council Sources repository

The canonical, version-controlled home for system rules, templates, individual Council records, the Registry, portable exports, and acceptance tests. One repository may contain many Councils while keeping their ownership and records logically separate.

### Council Designer Skill

The operational entry point for System Bootstrap, Source Consumption, Council Formation, Memory Maintenance, Export, Sync, and Review/Test. The Skill defines behavior and the bootstrap contract; companion documents explain, constrain, or provide generated knowledge.

### Individual Council

An independent organizational unit under `councils/<slug>/`. At minimum, it owns its `COUNCIL.md` and `MEMORY.md`; additional records are created only when useful.

### Registry

`registry/councils.md` is a lightweight index. It records Council identity/location plus two independent status dimensions:
- **Lifecycle Status:** Proposed, Draft, Active, Paused, or Archived.
- **Acceptance Status:** Not Defined, Not Run, Partial, Passed, Failed, or Blocked.

Registry metadata helps locate and assess Councils; it does not replace their records or memory. Active does not imply Passed.

### Portable Source exports

`exports/` contains generated, self-contained Markdown snapshots for a specific recipient/context. The default is one Markdown file per System or individual Council target; an optional Combined export contains system context plus one selected Council. Exports are derivatives, not canonical records or permission grants.

### Tests

`tests/ACCEPTANCE-TESTS.md` defines repeatable verification scenarios. `tests/TEST-RESULTS.md` records factual results and evidence. Static checks, live Agent behavior, fresh-context portability, and actual synchronization are distinct test types.

### Project repository or knowledge base

The authoritative home of Project artifacts: source code, requirements, architecture, learning content, notes, experiments, tests, and deliverables. A Council references these sources and does not replace them.

### AI host and tools

The host Agent interprets the Skill and may provide capabilities such as local file access, GitHub read/write, repository creation, and Git operations. Markdown instructions alone cannot provide these capabilities.

## 2. Shared collaboration methods

Council Designer uses three compact methods where relevant:

- **QD:** question-driven collaboration that drives understanding and progress throughout the work.
- **Checkpoint:** progress and milestone recording that shows the current stage, completed work, remaining questions/tasks, blockers, and next step.
- **Review:** retrospective evaluation, evidence-based verification, summary, and delivery.

These are working methods, not independent runtime services or Agents. They are not a rigid three-stage pipeline: QD may recur, Checkpoints may repeat, and Review is commonly used at task or milestone completion. Simple tasks need not invoke every method. The Skill defines their current use in Council Designer; mandatory adoption by every independent Council remains subject to the system's approved operating policy.

## 3. Data and authority boundaries

- **Skill specification:** defines operational behavior and the self-contained bootstrap contract.
- **AGENTS.md:** governs repository maintenance, safety, authorization, and validation.
- **Core Principles and Architecture:** explain system-wide design principles and component boundaries.
- **Memory Rules:** define ownership, evidence, update levels, approval, conflict handling, and privacy.
- **Council files:** define one Council's mission, responsibilities, decisions, and organizational memory.
- **Registry:** indexes Council identity, location, lifecycle, and acceptance state; it does not store full Council memory.
- **Checkpoint:** records working progress; it is not automatically a persistent memory update.
- **Review:** may identify memory candidates, but any persistent update must follow Memory Rules.
- **Export:** captures a dated, scoped subset of authoritative sources for portability; it is not canonical.
- **Project files:** remain authoritative for Project facts and deliverables.

If the Skill and a companion document disagree, do not silently overwrite either. Identify the inconsistency and reconcile it with user authority. Safety, platform policies, and explicit user authorization remain controlling.

## 4. Typical lifecycle

1. Bootstrap or inspect the Council Sources repository.
2. Consume an existing Source or discuss the system.
3. Use QD to clarify goals and consequential unknowns when needed.
4. Design and confirm a Council for a Project or domain.
5. Create its isolated directory and register it with separate lifecycle and acceptance states.
6. Use Checkpoints at meaningful stages to record actual progress and remaining work.
7. Maintain organizational memory under the applicable evidence and approval rules.
8. Use Review to evaluate outcomes, verify claims, summarize lessons, and prepare deliverables.
9. Generate a scoped portable Source when another AI needs the context.
10. Sync authorized changes to GitHub and re-import snapshots into GPT knowledge sources when required.

This lifecycle is descriptive, not a mandatory sequence for every task.

## 5. Export and synchronization model

The repository's modular Markdown files are canonical. Exports are generated from selected authoritative sources into one self-contained Markdown file per intended context by default.

- A System export describes the framework.
- A Council export describes one selected Council and includes enough shared context to be understood independently.
- An optional Combined export joins system context with one selected Council.
- Do not combine unrelated Councils by default.
- Record export type, target, artifact version, date, source repository/ref/commit, exact source manifest, omissions, and privacy review.
- Edit authoritative sources first and regenerate affected exports; do not use an export as the canonical editing location.
- The current process is Agent-assisted/manual; no automatic exporter or background synchronization service is defined.

GitHub stores versioned files. Local working copies and GPT Add Sources may be snapshots. Updating GitHub does not automatically update those copies. Re-export and re-import when the target environment requires it.

## 6. Source transport

The same Markdown information can be provided in three ways:
- GitHub link, if the Agent can access GitHub/network resources.
- Pasted Markdown text.
- Local files/folders, if the Agent has filesystem access.

These are transport methods, not different versions of the rules. If a source cannot be read, the Agent must say so and request accessible content.

## 7. Security model

Access is determined by the host platform and repository permissions. Public repositories are visible to others. Private memory must remain in private storage or be sanitized before export. Cross-Council access and writes must be explicit and task-scoped. A Source, export, or Skill does not itself grant file, network, GitHub, or execution permissions.
