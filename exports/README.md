# Portable Source Exports

> These profiles apply to [earlier Council Sources snapshots](../docs/COUNCIL-SOURCES-LEGACY.md). Council Designer V1.0 uses one generic Markdown document.

Exports are generated, self-contained Markdown snapshots for a specific recipient and purpose. They help GPT, other Agents, or human collaborators understand the required system or Council context without browsing the entire repository.

The repository's modular source files remain authoritative. An export is a derived snapshot, not a second source of truth.

## 1. Default export format

**Default to one self-contained Markdown file per intended context.**

Choose the smallest export scope that gives the recipient enough context:

| Export profile | Use when | Default output |
| --- | --- | --- |
| **System** | The recipient needs to understand Council Sources as a framework. | `exports/COUNCIL-SYSTEM-SOURCE.md` |
| **Council** | The recipient needs to work with one specific Council. | `exports/<slug>/<COUNCIL-NAME>-COUNCIL-SOURCE.md` |
| **Combined (optional)** | The recipient needs both the system rules and one specific Council in one import. | `exports/<slug>/<COUNCIL-NAME>-FULL-SOURCE.md` |

Do not combine every Council into one large export by default. Councils have separate ownership and memory boundaries. Do not split one target into many files merely to mirror the repository's internal folder structure.

A combined export is appropriate when one recipient needs both the shared system context and one Council's context. It must not silently include unrelated Councils.

Split an export only when a real constraint requires it, such as a host upload/size limit, a privacy boundary, or distinct access permissions. If splitting is necessary, provide a small index that explains the parts, their order, and which context each part contains. Do not assume or invent a platform's file or token limit.

## 2. What each export contains

### System export

Include enough information to explain and discuss the framework independently:

- Identity, purpose, use cases, and core concepts.
- Core organization principles and system architecture.
- Council Designer's supported modes and important operating boundaries.
- Shared collaboration methods: QD, Checkpoint, and Review, with their current adoption status.
- Registry lifecycle and acceptance-state distinction.
- Memory ownership, update levels, evidence, and approval boundaries.
- Source transport, export, GitHub synchronization, and GPT-import limitations.
- Privacy requirements, known limitations, and current validation status.

The System export is not a copy of every repository file. It is a curated, self-contained explanation based on the authoritative files listed in its manifest.

### Individual Council export

Include only the selected Council's relevant context:

- Identity, mission, scope, outcomes, and responsibilities.
- Current confirmed organizational state and relevant memory.
- Decisions, tasks, or issues needed by the recipient.
- Authoritative Project references; do not copy the Project's whole documentation system.
- User authority, permissions, collaboration boundaries, and relevant shared operating methods.
- Unresolved questions, blockers, and known omissions.

A Council export should contain enough shared system context to be understood on its own. Do not include another Council's memory without explicit, task-scoped authorization.

### Combined export

Combine the relevant system context with one selected Council's context into one Markdown file. Preserve the distinction between system-wide rules and Council-specific facts. This is an optional convenience profile, not a new authority source.

## 3. Required export metadata

Every export must begin with a metadata block containing:

- **Export type:** System, Council, or Combined.
- **Target:** system name or Council name/slug.
- **Export version:** version of this export artifact, not the Council Designer Skill version.
- **Generated at:** date of generation.
- **Source repository:** canonical repository or local source location.
- **Source ref:** branch, tag, or local working-tree description.
- **Source commit:** exact commit SHA when available; otherwise state that it is unavailable.
- **Source manifest:** exact authoritative file paths actually read and used.
- **Omissions:** relevant files or content intentionally excluded, or "None known".
- **Privacy review:** confirmation that the export was checked for secrets, private information, and unauthorized third-party content.

Do not invent a source commit, file, test result, approval, or export date. The manifest should list the sources actually read, not files that merely exist in the repository.

## 4. Export procedure

1. **Define the recipient and purpose.** Decide whether the recipient needs System, one Council, or Combined context.
2. **Choose the canonical source revision.** Read the relevant authoritative files from one known branch/commit where possible. If sources come from a local working tree, identify that explicitly.
3. **Resolve source conflicts.** Check relevant Skill, AGENTS, core, memory, Council, and Project rules. Do not silently resolve contradictions; record unresolved conflicts.
4. **Select the minimum sufficient content.** Include necessary facts and rules, not every file or every conversation.
5. **Build one self-contained Markdown document.** Avoid relying on relative links or hidden conversation context. Canonical links may be included as provenance, but essential context must be present in the export itself.
6. **Preserve epistemic status.** Distinguish confirmed facts, proposals, inferences, unknowns, active work, and completed work.
7. **Add metadata and source manifest.** Record the exact source paths, revision, date, and known omissions.
8. **Review privacy and publication rights.** Remove or summarize private personal data, credentials, tokens, confidential project details, private chat transcripts, and third-party material without permission. A public repository requires a public-safe export.
9. **Read back and validate.** Check that the file is complete, readable without hidden context, internally consistent, and aligned with its manifest.
10. **Publish only with authorization.** If writing to GitHub, inspect the target branch, review the diff, commit only approved files, and fetch the result again. Record the actual commit SHA.
11. **Refresh the recipient deliberately.** Explain whether the recipient must manually re-import or replace the file.

The current export process is Agent-assisted/manual. No dedicated export generator or automatic synchronization service is defined by this repository. Do not claim that exports are automatically rebuilt or delivered.

## 5. Source of truth and synchronization

- Council Sources files are the canonical, editable records.
- Export files are generated derivatives for portability.
- Correct the authoritative source first, then regenerate the affected export.
- Do not treat an export as the canonical place to make an organizational decision or memory update.
- Regenerate an export when one of its included sources changes materially.
- A GitHub push does not refresh an already imported GPT Source. The user must re-import/replace the snapshot unless a specific platform integration has been tested and verified.
- A Markdown export provides context only. It does not grant filesystem, network, GitHub, or execution permissions.

## 6. Naming and storage

- System: `exports/COUNCIL-SYSTEM-SOURCE.md`.
- Individual Council: `exports/<slug>/<COUNCIL-NAME>-COUNCIL-SOURCE.md`.
- Optional combined System + Council: `exports/<slug>/<COUNCIL-NAME>-FULL-SOURCE.md`.

Keep the existing Council export location stable when possible. Create a Council-specific export directory only when that Council actually needs a portable export.

## 7. Review checklist

Before delivery, verify:

- [ ] The export profile matches the recipient's actual need.
- [ ] The file is self-contained and uses the one-file default.
- [ ] Metadata and source manifest describe the sources actually used.
- [ ] Facts, proposals, inferences, unknowns, and status are distinguishable.
- [ ] System-wide rules are not confused with Council-specific decisions.
- [ ] No unrelated Council memory or Project documentation was copied.
- [ ] Privacy and publication-rights checks were completed.
- [ ] The exported file was read back after writing.
- [ ] GitHub writes, if any, were authorized and verified.
- [ ] Manual re-import requirements were explained.
