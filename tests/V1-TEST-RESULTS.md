# Council Designer V1.0 test results

This ledger applies to Council Designer v1.0.0. [V0.3.0 evidence](TEST-RESULTS.md) remains separate. The [acceptance scenarios](V1-ACCEPTANCE-TESTS.md) require real execution before any behavioral result changes.

## Behavior

| ID | Scope | Status |
| --- | --- | --- |
| V1-01 | Design from one Skill file | Not Run |
| V1-02 | Dynamic roles and independent Councils | Not Run |
| V1-03 | Adaptive QD and literal markers | Not Run |
| V1-04 | Checkpoint and resume in conversation | Not Run |
| V1-05 | Review mixed evidence and conflicting rules | Not Run |
| V1-06 | Three approval levels and decision history | Not Run |
| V1-07 | Update an earlier Council Sources document | Not Run |
| V1-08 | Export and re-read a single Markdown document | Not Run |
| V1-09 | Untrusted input and storage boundaries | Not Run |

No V1.0 interaction, host loading, or cross-host portability tests have been executed. The next validation should give only SKILL.md and scenario inputs to fresh sessions, record transcripts and tool calls, and use a separate reader for V1-08. Test a host with no write or network capabilities and one with mock tools for the permission checks.

## Static

| Check | Result |
| --- | --- |
| `python tests/check_v1_docs.py` | Passed. Checked the version and four modes, both marker tables, bilingual navigation, nine scenario IDs, and 65 local Markdown link targets. |
| YAML parse using PyYAML 6.0.3 | Passed. Verified the `council-designer` name, description, and string version `1.0.0` in `metadata`, consistent with the [Agent Skills specification](https://agentskills.io/specification). |
| PowerShell `ConvertFrom-Markdown -Path` for the root README pair and the Skill guide | Passed. All three render their example blocks and navigation or mode tables. |
| `git diff --check` | Passed with the repository checkout's normal line-ending configuration. |
| `git diff --exit-code 302f74c -- core/PRINCIPLES.md councils/personal-learning exports/COUNCIL-SYSTEM-SOURCE.md exports/personal-learning tests/reports` | Passed. Those principles, Council records, export snapshots, and historical reports match the pinned V0.3.0 base. |

These checks cover file structure and consistency. They do not exercise any of the interactive behaviors above.
