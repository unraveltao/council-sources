# Council Sources — Test Results

> Version: 0.3.0  
> Last updated: 2026-11-18  
> This is an evidence log. Do not mark tests Passed until the relevant procedure has actually been executed and its evidence reviewed.

## Current status

| Test | Status | Evidence |
| --- | --- | --- |
| T1 — System Bootstrap from SKILL.md alone | Not Run | No isolated empty-destination bootstrap using only Skill v0.3.0. T1's expected output list has been clarified to name both required test documents. |
| T2 — Source Consumption | Not Run | No live comparison across GitHub, pasted Markdown, and local-file inputs. |
| T3 — Council Formation and Registry lifecycle | Not Run | No isolated, approved Project-to-Council formation run with Registry verification. |
| T4 — Memory update and Checkpoint separation | Not Run | No controlled live memory-write and approval-level test. |
| T5 — Portable export and fresh-context consumption | Not Run | No fresh-context comprehension test of generated System/Council exports. |
| T6 — GitHub synchronization | Blocked | No authorized test write/read-back was performed; this remains separate from the current PR's documentation commits. |
| T7 — Five-marker guided interaction | Partial | Independent live multi-turn transcript exists. Required markers and constraint preservation worked in the exercised turns; some prescribed freeform/combined-choice and full-turn audit coverage remains outstanding. |
| T8 — QD bounded question-driven collaboration | Partial | Independent adaptive QD transcript exists. The Agent clarified, adapted, stopped when sufficient, and resumed for a later privacy concern; actual note inspection and artifact production were not tested. |
| T9 — Checkpoint progress and milestone recording | Passed (exercised scope) | A fresh independent Agent read the full local v0.3.0 Skill snapshot and completed milestone, blocker, pause/resume, and memory-boundary scenarios. Evidence is in the report. |
| T10 — Review evaluation, verification, and delivery | Passed (exercised scope) | A separate fresh Agent read the full local v0.3.0 Skill snapshot and reviewed mixed completion/evidence, including incomplete criteria and an unrun test. Evidence is in the report. |

**Overall:** Council Designer v0.3.0 has partial behavioral acceptance evidence, not full T1–T10 acceptance. T9 and T10 passed only for the documented exercised scope. Do not describe the Skill or this PR as fully behaviorally validated.

## Full acceptance report

The complete independent report, including the T7/T8 transcripts, T9/T10 fresh-Agent transcripts, execution environment, limitations, and later rerun evidence, is stored at:

- [Council Designer v0.3.0 — Independent Acceptance Test Report](reports/COUNCIL-DESIGNER-V0.3.0-INDEPENDENT-ACCEPTANCE-REPORT.md)

The report's evidence update at the top explains that its later Sections 10–12 supersede conflicting preliminary statements in Sections 1–9. Preserve the transcripts and scope limitations; do not convert snapshot-loaded tests into claims of persistent Skill installation or independent GitHub access.

## Historical evidence

The separate `council-sources-test` repository contains limited historical Partial evidence for T1 and T6 against Council Designer v0.2.0. That evidence does not validate v0.3.0 and is not copied into the current-version status table.

## Static documentation validation

> Status: Passed (static documentation/structure checks only)  
> Original validation commit: `e5ca87fc35553ed4b508f145e8b5eaef00caee17`  
> Pre-merge recheck revision: `35004147701f9a9790626bab7771b9bbb8270a36`

Checks recorded:

- Confirmed Registry separates Lifecycle Status and Acceptance Status and that Active does not imply Passed.
- Confirmed Council Designer is v0.3.0 and defines QD, Checkpoint, and Review.
- Confirmed export guidance specifies one self-contained Markdown file per intended context, with metadata and source manifests.
- Confirmed source paths in the System and Personal Learning Council export manifests exist in the repository tree.
- Confirmed T1–T10 are defined in `ACCEPTANCE-TESTS.md`; current execution states are recorded separately in the table above.
- Confirmed the English and Simplified Chinese README files have matching top-level section counts (25 each). This is a structural check, not a full semantic translation review.
- Checked relative Markdown links in 15 core, Skill, Council, export, README, and test documents at the pre-merge recheck revision; no missing relative targets were found.
- No GitHub Actions check runs or commit status checks were reported for the PR head at the time of inspection.

Static checks do **not** establish live Agent behavior, fresh-context export comprehension, memory approval behavior, or end-to-end GitHub/GPT synchronization.

## Run log

### 2026-11-17 — Independent behavior tests

- T7: Partial — independent live multi-turn interaction; no Specification Failure observed in the exercised turns, but some required variants remain untested.
- T8: Partial — independent adaptive QD interaction; later privacy uncertainty triggered a resumed question; no notes or artifacts were actually processed.
- T9: Passed (exercised scope) — initially blocked by source retrieval, then completed by a fresh Agent using the complete local snapshot fetched from the verified branch.
- T10: Passed (exercised scope) — completed by a separate fresh Agent using the same complete local snapshot.
- T1–T5: Not Run.
- T6: Blocked pending a separately authorized remote write/read-back test.

### 2026-11-18 — Pre-merge documentation recheck

- Re-read the PR branch's Skill, acceptance plan, ledger, architecture, principles, memory rules, Council template, Registry, README pair, exports, and operating-model draft.
- Identified and corrected the T1 acceptance-specification gap: the expected bootstrap output now explicitly names both required test documents.
- Rechecked relative Markdown links in the selected 15 documents; no missing targets were found.
- No behavior tests, remote synchronization test, PR merge, or v0.4.0 branch creation were performed in this recheck.
