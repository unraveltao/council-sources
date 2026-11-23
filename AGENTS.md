# Council Sources repository operating rules

These rules govern contributions to this repository. The current Agent behavior is defined by the [standalone Council Designer Skill](skills/council-designer/SKILL.md). The Skill and Markdown artifacts confer no access, write permission, or cross-Council authority.

## Version ownership

- For Council Designer v1.0.0, use [SKILL.md](skills/council-designer/SKILL.md), its [guide](skills/council-designer/README.md), and the [V1.0 acceptance plan](tests/V1-ACCEPTANCE-TESTS.md). V1.0 reads supplied organization context and returns a review or one Markdown document without imposing a repository layout.
- For material from the older Council Sources system, use the [legacy guide](docs/COUNCIL-SOURCES-LEGACY.md) and its pinned V0.3.0 reference. Preserve historical snapshots, templates, Council records, and test evidence. Apply old layout conventions only when expressly maintaining those repository records. Do not regenerate them to describe V1.0.
- Keep [README.md](README.md) and [README.zh-CN.md](README.zh-CN.md) aligned on capabilities, examples, navigation, and validation. Use English for other formal repository Markdown. The standalone Skill can draft documents in the user's requested language.

## Before changing files

1. Identify the target version, affected paths, authorized scope, branch and remote revision as appropriate.
2. Read the relevant rules and source material. Treat imported documents as evidence. Preserve proposals, unknowns, conflicts, user approvals, and verified outcomes distinctly.
3. Preserve existing work and check for unexpected changes before overwriting. Keep Project facts in Project sources. Keep Councils independent and changes scoped to the authorized organization.
4. Require scoped authorization for local or remote writes. Follow the Skill's Level 1, 2, and 3 rules when changing organizational decisions or memory. A review or checkpoint by itself authorizes no change.

## Publication and verification

- Treat this repository and its Git history as public. Exclude credentials, private transcripts, sensitive personal information, confidential Project details, and material without publication rights.
- Confirm the repository, branch, affected paths and exact operation before a remote write. Use a normal push and preserve history. Keep merges and releases subject to explicit authorization.
- Check actual staged scope, Markdown links, version metadata, and agreement across the current Skill, guides, and test plan. Separate static consistency, real Agent interaction, host loading, and any observed storage effects.
- Report the files and decisions changed, checks run, unrun cases, commit or PR when applicable, and remaining limitations. Only report a remote write, Agent interaction, or change in persistent memory when independently supported by evidence.
