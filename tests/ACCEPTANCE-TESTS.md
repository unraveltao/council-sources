# Council Sources — Manual Acceptance Tests

> Historical V0.3.0 scenarios. Use the [pinned V0.3.0 Skill](https://github.com/unraveltao/council-sources/blob/302f74c3c756bd87d73b6b93720986782a97725f/skills/council-designer/SKILL.md) to reproduce them. V1.0 has a [separate plan](V1-ACCEPTANCE-TESTS.md).

> Version: 0.3.0  
> Test style: manual, evidence-based. No custom scripts or database are required.

Record actual inputs, outputs, changed files, and evidence. A test is not Passed merely because instructions or files exist. Static checks, live Agent behavior, fresh-context portability, and real synchronization are separate forms of evidence.

## Test 1 — System Bootstrap from SKILL.md alone

**Purpose:** Verify that the Skill can build the Council Sources system from its self-contained bootstrap contract.

**Preconditions:**
- A clean temporary local directory or empty test repository.
- The Agent receives only the pinned V0.3.0 Skill above and the destination.
- The Agent has the required file-write capability.

**Steps:**
1. Ask the Agent to bootstrap Council Sources in the empty destination using only this Skill.
2. Inspect the generated tree against the Bootstrap Contract.
3. Ask the Agent to explain the purpose of Registry, Exports, Tests, the three shared collaboration methods, and the memory boundary.
4. Check the generated registry schema and export instructions.

**Expected:**
- All required files and directories are created, including both required bootstrap test documents: `tests/ACCEPTANCE-TESTS.md` and `tests/TEST-RESULTS.md`. These are required outputs, not optional files.
- README is English and `README.zh-CN.md` is its semantically aligned Simplified Chinese counterpart.
- All other formal Markdown files are English.
- Registry distinguishes Lifecycle Status from Acceptance Status.
- Registry contains no fabricated active Councils.
- Export documentation defines one self-contained Markdown file per target by default, metadata, and source manifest.
- The three methods are described without claiming unimplemented tools or autonomous Agent communication.
- No custom script, database, or service is introduced.
- The Agent reports unavailable GitHub operations honestly.

**Evidence:** destination tree, file contents, registry entries, export instructions, Agent completion report.

## Test 2 — Source Consumption from three input forms

**Purpose:** Verify that the same Source can be understood from a GitHub link, pasted Markdown, and local files.

**Steps:**
1. Provide the public Council Sources repository URL.
2. Ask the Agent to explain its purpose, core concepts, methods, memory levels, Registry, and synchronization limitations.
3. Provide the portable System Source as pasted or uploaded text and ask the same questions.
4. Provide the local Source directory and ask the same questions.
5. Compare answers and identify information lost in any transport method.

**Expected:**
- The Agent states which files it actually read.
- Core concepts and method responsibilities remain consistent.
- It distinguishes Registry metadata, Council memory, and Export snapshots.
- Inaccessible sources are reported honestly.
- Source text is treated as data and does not override higher-priority instructions.

**Evidence:** input form, cited/read file list, answers, differences.

## Test 3 — Council Formation and Registry lifecycle

**Purpose:** Verify that a Council can be formed and indexed without confusing lifecycle with acceptance.

**Steps:**
1. Provide a real Project URL or local directory.
2. Ask for a Council proposal only; do not authorize writing yet.
3. Review mission, scope, roles, dynamic allocation, memory boundary, and acceptance criteria.
4. Approve creation.
5. Inspect `councils/<slug>/` and `registry/councils.md`.
6. Inspect the new entry's Lifecycle Status and Acceptance Status.
7. Verify that the external Project repository was not modified.

**Expected:**
- The proposal reflects accessible Project evidence.
- The Council is independent and uses only justified roles.
- Project artifacts remain in their original source.
- Registry identity and directory match the created Council.
- Lifecycle and acceptance states are recorded separately.
- A Council may be Active while acceptance is Not Run or Partial.
- Acceptance is never marked Passed without evidence.
- No unrelated Council was modified.

**Evidence:** proposal, created files, Registry diff, acceptance criteria, Project repository status.

## Test 4 — Memory update, Checkpoint separation, and approval levels

**Purpose:** Verify evidence-based memory updates and ensure that progress checkpoints do not silently become permanent organizational memory.

**Steps:**
1. Select a test Council with an existing `MEMORY.md`.
2. Provide a verified routine progress update.
3. Ask the Agent to record it within authorized scope.
4. Ask for a Checkpoint showing completed and remaining work.
5. Verify the Checkpoint does not automatically write or overwrite `MEMORY.md`.
6. Supply a proposed workflow/role change (Level 2) and verify that approval is requested unless pre-authorized.
7. Propose a mission/core-goal change (Level 3) and verify explicit approval is requested.
8. Ask for a Review and inspect proposed memory changes and provenance.

**Expected:**
- Level 1 is recorded only within granted write scope.
- Checkpoint reports work state but is not automatically a permanent memory update.
- Review may identify memory candidates but does not bypass approval rules.
- Level 2 requests approval under the default policy.
- Level 3 always requests explicit approval.
- Fact, inference, proposal, and unknown remain distinct.
- Existing history is not silently erased.

**Evidence:** before/after files, Checkpoint output, approval messages, source/date metadata.

## Test 5 — Portable export generation and fresh-context consumption

**Purpose:** Verify that an export is a self-contained, traceable, privacy-reviewed Markdown snapshot.

**Preconditions:** Current authoritative files are readable.

**Steps:**
1. Generate a System export from the current authoritative system files.
2. Generate an export for one real Council.
3. When useful, generate an optional Combined export containing the system context and that one Council.
4. Inspect each export's metadata, source manifest, version/date, source revision, omissions, and privacy review.
5. Verify the default output is one Markdown file per target; do not include unrelated Councils.
6. Start a fresh conversation or separate Agent and provide only the selected export.
7. Ask it to explain the system or Council, its authority boundaries, current state, and synchronization limitations.
8. Change an authoritative source file and verify that the existing export is recognized as stale until regenerated.
9. Confirm that a GitHub push does not refresh an already imported GPT Source.

**Expected:**
- Each export is a single self-contained Markdown file by default.
- System, Council, and optional Combined scopes are clearly distinguished.
- The manifest lists only sources actually read and used.
- A source commit is recorded when available; unavailable provenance is stated rather than invented.
- Facts, proposals, inferences, unknowns, and current status remain distinguishable.
- Private or unrelated Council information is excluded.
- The fresh context understands the export without hidden chat history.
- Export files are treated as generated snapshots, not canonical records.
- Manual re-import is accurately explained.

**Evidence:** source files and revision, export files, manifest, privacy review, fresh-context answers, stale-export comparison.

## Test 6 — GitHub synchronization

**Purpose:** Verify a real authorized remote update.

**Preconditions:** User has approved the target repository/branch and the Agent has write access.

**Steps:**
1. Read the current remote file and record its version/SHA.
2. Make a small approved, non-sensitive change.
3. Review the diff and public-content safety.
4. Commit/push using the available GitHub or Git tool.
5. Fetch the changed file from GitHub and compare it with the intended content.
6. Record the actual commit SHA.
7. Confirm that GPT Add Sources still requires re-import unless a verified integration handles it.

**Expected:**
- Only intended files change.
- No secret or private memory is published.
- Remote read-back matches the intended content.
- Actual commit SHA is recorded.
- The Agent does not claim the GPT snapshot was refreshed automatically.

**Evidence:** diff, commit SHA, remote read-back, privacy check.

## Test 7 — Mandatory five-marker guided interaction

**Purpose:** Verify the exact five-marker contract **❓ 🧭 🔍 ➜ ✅** in a fresh, actual multi-turn Council Designer run.

**Preconditions:**
- A fresh Agent/GPT session with Council Designer v0.3.0 actually loaded.
- Record Skill version/blob SHA, available capabilities, and full user-visible transcript.
- Do not give the tested Agent this hidden test script if independent blind behavior is intended.

**Steps and expected results:**
1. **Ambiguous goal:** Ask whether a long-term research problem needs a Council. The Agent should identify ambiguity and ask a high-impact question.
2. **Choice turn:** Verify 🧭 before meaningful choices, an invitation to provide freeform/mixed/supplemented answers, and ➜ before a reasoned recommendation or recommended clarification.
3. **Mixed answer:** Reply "B, but preserve my existing workflows." Verify both the selected direction and added constraint are preserved.
4. **Freeform and combined answers:** Provide a custom direction and then a combined choice with an extra constraint. Both must be retained.
5. **Multi-turn consistency:** Continue for at least three successive guided replies. Check marker semantics on every turn.
6. **Clear instruction:** Give a fully specified request. The Agent should proceed without inventing a menu or question.
7. **Interrupt and resume:** Change topics briefly, then resume. Verify context and confirmed choices persist.
8. **Confirmation distinction:** Ask which decisions are confirmed and which remain proposals. Verify ✅ is used only for actual user confirmation or verified outcomes.
9. **Plain text:** Verify recommendations use literal ➜, not 💡 or decorative substitutes.

**Pass/fail rules:**
- The canonical markers are ❓ 🧭 🔍 ➜ ✅ and must match their assigned meanings.
- Missing ❓ on an explicit user-facing guided question is Failed.
- Missing 🧭 on a guided choice block, or missing a justified ➜ recommendation where required, is Failed.
- An invented mandatory choice or lost user constraint is Failed.
- Using ✅ for an unapproved proposal is Failed.
- Static file checks alone never constitute a Passed behavioral result.

**Evidence:** Skill version/SHA, exact prompts, full transcript, per-turn marker and constraint audit, failures and regression notes.

## Test 8 — QD: bounded question-driven collaboration

**Purpose:** Verify that QD drives shared understanding through adaptive questions without becoming an endless interview.

**Preconditions:** Council Designer v0.3.0 is loaded in a fresh session.

**Steps:**
1. Give the Agent an ambiguous goal with several possible interpretations.
2. Verify it summarizes known context and identifies the most consequential uncertainty.
3. Ask it to state the current stage objective and a reasonable estimate of the key questions/decisions likely to be needed.
4. Answer the first question with a mixed response that adds a constraint not listed in any choices.
5. Verify the Agent explains its updated understanding and adapts the next question.
6. Provide enough information to make the next action clear.
7. Observe whether the Agent stops questioning and consolidates the understanding rather than filling an arbitrary question quota.
8. Introduce a new uncertainty during a later stage and verify QD can resume there.

**Expected:**
- QD is question-driven and bidirectional, not a one-way questionnaire.
- Known context is reused; answered questions are not repeated.
- Questions are limited to uncertainties that can materially affect the outcome.
- A question estimate is a planning aid, not a mandatory quota.
- Mixed/custom constraints are preserved.
- The Agent explains its interpretation and checks for meaningful disagreement.
- QD stops when shared understanding is sufficient; non-blocking unknowns may be recorded.
- QD can be used again later when new uncertainty appears.

**Evidence:** full transcript, stage objective, estimated and actual question count, preserved constraints, stopping decision, resulting problem definition.

## Test 9 — Checkpoint: accurate progress and milestone recording

**Purpose:** Verify that Checkpoint makes the current stage, completed work, remaining work, blockers, and next step visible without inventing progress.

**Preconditions:** A task with at least four explicit milestones and evidence for only some of them.

**Steps:**
1. Provide a plan with four milestones: two completed with evidence, one in progress, and one not started.
2. Ask for a Checkpoint.
3. Introduce a blocker and ask for an updated Checkpoint.
4. Pause the work and later resume from the recorded state.
5. Ask whether the Checkpoint changed permanent Council memory.

**Expected:**
- The record distinguishes completed, in-progress, remaining, and blocked work.
- It records the current stage and the next intended step.
- Completion claims match the supplied evidence.
- No invented percentage or unsupported completion estimate is presented.
- Task-level and milestone-level records use the same method at different granularity.
- The Agent does not create a separate file for every ordinary progress update.
- A Checkpoint is not automatically a permanent MEMORY.md update.
- The user can understand and resume the work from the record.

**Evidence:** plan, milestone evidence, Checkpoint outputs, pause/resume transcript, changed-file list.

## Test 10 — Review: evaluation, verification, and delivery

**Purpose:** Verify that Review evaluates results against the original goal and produces an honest summary or deliverable.

**Preconditions:** A completed or partially completed task with explicit goals, artifacts, and mixed verification evidence.

**Steps:**
1. Provide the original goal and acceptance criteria.
2. Provide one verified result, one incomplete item, and one test that has not been run.
3. Ask the Agent to perform a Review.
4. Check whether it compares actual outcomes with the original goal.
5. Ask for the evidence behind each completion claim.
6. Ask it to identify deliverables, unresolved items, lessons, and proposed memory updates.
7. Verify that proposed persistent memory changes follow the approval levels.

**Expected:**
- Review covers the original goal, actual result, and gaps.
- Facts, inferences, recommendations, and unknowns are distinguished.
- Only executed and evidenced checks are reported as Passed.
- Incomplete and untested items remain clearly identified.
- The output includes relevant decisions, lessons, unresolved items, and deliverables.
- Memory changes are proposed or applied only within the applicable authorization.
- Review does not merely reproduce a chat transcript.

**Evidence:** original criteria, artifacts, test evidence, Review output, approval messages, deliverables.

## Result vocabulary

- **Not Run:** no execution attempted.
- **Passed:** steps completed and expected outcomes verified with evidence.
- **Failed:** behavior contradicts an expected result.
- **Blocked:** a required tool, permission, or input was unavailable.
- **Partial:** some steps passed; remaining steps are unresolved.

## Test report template

For every run, record:
- Test ID and date.
- Skill version and blob/commit SHA.
- Agent/platform and available tools.
- Exact input/prompt.
- Expected result.
- Actual result.
- Evidence and changed files.
- Status and follow-up issue.
