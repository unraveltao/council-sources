# Council Sources — System Architecture

## Components

### Council Sources repository

The canonical versioned home for system rules, templates, Council directories, registry, and portable exports. A single repository may contain many Councils while keeping their files logically separate.

### Council Designer Skill

The single operational entry point. It supports:
- System Bootstrap: initialize or repair the Council Sources repository from the Skill specification.
- Source Consumption: read a GitHub URL, pasted Markdown, or accessible local files.
- Council Formation: analyze a Project or domain and create a Council.
- Memory Maintenance: update the selected Council's organizational memory.
- Export and Sync: produce portable Markdown and, with authorization/tools, update GitHub.

### Individual Council

An independent organizational unit under councils/<slug>/. It owns its COUNCIL.md and MEMORY.md plus any justified supporting records.

### Project repository or knowledge base

The authoritative home of Project artifacts: source code, PRD, architecture, learning content, notes, experiments, and deliverables. A Council links to these sources and does not replace them.

### Portable Source export

A generated Markdown snapshot that allows another GPT or Agent to understand a Council or the whole system. It is a snapshot, not a live database and not a permission grant.

### AI host and tools

The host Agent interprets the Skill and provides capabilities such as local file access, GitHub read/write, repository creation, and Git operations. Markdown instructions alone cannot provide these capabilities.

## Data and authority boundaries

- Skill specification: defines the system's operational behavior and bootstrap contract.
- AGENTS.md: constrains repository maintenance and safety.
- Council files: define the specific Council's mission, responsibilities, memory, and decisions.
- Project files: remain authoritative for Project facts and deliverables.
- Registry: indexes Councils but does not contain their full memory.
- Export: captures a dated subset of source files for portability.

If the Skill and a companion document disagree, do not silently overwrite either. Identify the inconsistency and reconcile it. Safety, platform policies, and explicit user authorization remain controlling.

## Typical lifecycle

1. Bootstrap the Council Sources repository.
2. Consume an existing Source or discuss the system.
3. Analyze a Project or domain.
4. Design and confirm a Council.
5. Create its isolated directory and register it.
6. Maintain memory as verified changes occur.
7. Export a portable Source when another AI needs the context.
8. Sync authorized changes to GitHub.
9. Re-import snapshots into GPT knowledge sources when required.

## Source transport

The same Markdown content can be provided in three ways:
- GitHub link, if the Agent can access GitHub/network resources.
- Pasted Markdown text.
- Local files/folders, if the Agent has filesystem access.

These are transport methods, not different versions of the rules. If a source cannot be read, the Agent must say so and request accessible content.

## Synchronization model

GitHub stores versioned files. Local working copies and GPT Add Sources may be snapshots. Updating GitHub does not automatically update those copies. Re-export and re-import when the target environment requires it.

## Security model

Access is determined by the host platform and repository permissions. Public repositories are visible to others. Private memory must remain in private storage or be sanitized before export. Cross-Council access and writes must be explicit and task-scoped.
