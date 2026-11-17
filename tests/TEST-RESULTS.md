# Council Sources — Test Results

> Version: 0.3.0  
> This file is an evidence log. Do not mark tests Passed until they have actually been executed and verified.

## Current status

| Test | Status | Evidence |
| --- | --- | --- |
| T1 — System Bootstrap from SKILL.md alone | Not Run | Pending isolated bootstrap with Skill v0.3.0 |
| T2 — Source Consumption | Not Run | Pending GitHub / pasted Markdown / local-file comparison |
| T3 — Council Formation and Registry lifecycle | Not Run | Pending real Project-to-Council run and dual-status check |
| T4 — Memory update and Checkpoint separation | Not Run | Pending controlled memory and approval test |
| T5 — Portable export and fresh-context consumption | Not Run | Pending System / Council export and fresh-context test |
| T6 — GitHub synchronization | Not Run | Pending authorized write/read-back test |
| T7 — Five-marker guided interaction | Not Run | Pending fresh live multi-turn test |
| T8 — QD bounded question-driven collaboration | Not Run | Pending adaptive clarification and stopping test |
| T9 — Checkpoint progress and milestone recording | Not Run | Pending evidence-backed progress and resume test |
| T10 — Review evaluation, verification, and delivery | Not Run | Pending final review with mixed verification evidence |

## Historical evidence

The separate `council-sources-test` repository contains limited historical Partial evidence for T1 and T6 against Council Designer v0.2.0. That evidence does not validate v0.3.0 and is not copied into the current-version status table.

## Documentation validation

No v0.3.0 documentation validation has been recorded yet. Add the exact files read back, checks performed, result, and commit SHA after the documentation update is committed.

## Run log

No live functional acceptance test for Council Designer v0.3.0 has been recorded.


## Static documentation validation — 2026-11-17

> Status: Passed (static documentation/structure checks only)  
> Validated source commit: e5ca87fc35553ed4b508f145e8b5eaef00caee17

Checks performed by reading the committed files back from the PR branch:

- Confirmed the Registry has separate Lifecycle Status and Acceptance Status columns, the defined values, and the rule that Active does not imply Passed.
- Confirmed Council Designer is version 0.3.0 and contains the QD, Checkpoint, and Review method definitions.
- Confirmed the Skill and Export Guide specify one self-contained Markdown file per intended context by default, with source metadata and an exact source manifest.
- Confirmed System and Personal Learning Council exports were regenerated from source revision e5ca87fc35553ed4b508f145e8b5eaef00caee17 and contain matching source-manifest revisions.
- Confirmed all source paths listed in the two export manifests exist in the repository tree.
- Confirmed T1–T10 are defined in ACCEPTANCE-TESTS.md and all ten current-version test statuses remain Not Run.
- Confirmed the English and Simplified Chinese README versions both reference Skill v0.3.0 and describe the three methods.
- Checked relative Markdown links in README.md, README.zh-CN.md, AGENTS.md, core/SYSTEM-ARCHITECTURE.md, exports/README.md, and docs/design/OPERATING-MODEL-DRAFT.md; no missing targets were found.

This static validation does **not** establish live Agent behavior, fresh-context export comprehension, memory approval behavior, or end-to-end GitHub/GPT synchronization. T1–T10 remain Not Run until their actual procedures are executed with evidence.
