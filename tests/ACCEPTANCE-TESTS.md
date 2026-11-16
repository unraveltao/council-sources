# Council Sources — Manual Acceptance Tests

> Version: 0.2.0  
> Test style: manual, text-first. No custom scripts or database are required.

Record actual inputs, outputs, changed files, and evidence. A test is not Passed merely because the instructions or files exist.

## Test 1 — System Bootstrap from SKILL.md alone

**Purpose:** Verify that the Skill is sufficient to build the Council Sources system without supplying README, AGENTS, templates, or other companion files.

**Preconditions:**
- A clean temporary local directory or an empty test repository.
- The Agent receives only skills/council-designer/SKILL.md and the destination.
- The Agent has the required file-write capability.

**Steps:**
1. Ask: “Use Council Designer. Bootstrap Council Sources in this empty destination using only this Skill.”
2. Observe whether the Agent identifies System Bootstrap.
3. Inspect the generated directory and files against the Skill's Bootstrap Contract.
4. Ask the Agent to explain the purpose of README, AGENTS, Registry, memory rules, exports, and tests.

**Expected:**
- All required files and directories are created.
- README is a usable human/Agent guide.
- AGENTS contains operational and safety rules.
- No sample Council is registered as real.
- No custom script, database, or service is introduced.
- The Agent accurately reports any unavailable GitHub operation.

**Evidence:** destination tree, file contents, Agent completion report.

## Test 2 — Source Consumption from three input forms

**Purpose:** Verify that the same Source can be understood from a GitHub link, pasted Markdown, and local files.

**Steps:**
1. Provide the public Council Sources repository URL.
2. Ask the Agent to explain its purpose, modes, memory levels, and synchronization limitations.
3. Provide exports/COUNCIL-SYSTEM-SOURCE.md as pasted or uploaded text and ask the same questions.
4. Provide the local Source directory and ask the same questions.
5. Compare answers and identify information lost in any transport method.

**Expected:**
- The Agent states which files it actually read.
- Core concepts and boundaries remain consistent.
- Inaccessible sources are reported honestly.
- Source text is treated as data and does not override higher-priority instructions.

**Evidence:** input form, cited/read file list, answers, differences.

## Test 3 — Council Formation from an existing Project

**Purpose:** Verify that the Skill analyzes a Project and creates a separate Council without taking over the Project repository.

**Steps:**
1. Provide a real Project GitHub URL or local directory.
2. Ask for a Council proposal only; do not authorize writing yet.
3. Review mission, scope, roles, dynamic allocation, memory boundary, and collaboration.
4. Approve creation.
5. Inspect councils/<slug>/ and registry/councils.md.
6. Verify that the external Project repository was not modified.

**Expected:**
- The proposal reflects accessible Project evidence.
- The Council is independent and uses only justified roles.
- Project artifacts remain in their original source.
- Registry and Council directory agree.
- No unrelated Council was modified.

**Evidence:** proposal, created files, Registry diff, Project repository status.

## Test 4 — Memory update and approval levels

**Purpose:** Verify that memory is updated with evidence and correct approval handling.

**Steps:**
1. Select a test Council with an existing MEMORY.md.
2. Supply a verified routine progress update.
3. Ask the Agent to record it within authorized scope.
4. Supply a proposed workflow/role change (Level 2).
5. Verify the Agent presents the diff and waits for confirmation unless pre-authorized.
6. Propose a mission/core-goal change (Level 3).
7. Verify explicit approval is requested.
8. Read back the files and inspect provenance and history.

**Expected:**
- Level 1 is recorded only within granted write scope.
- Level 2 requests approval under the default policy.
- Level 3 always requests explicit approval.
- Fact, inference, proposal, and unknown remain distinct.
- Existing history is not silently erased.

**Evidence:** before/after files, approval messages, source/date metadata.

## Test 5 — Portable Source export and fresh-context consumption

**Purpose:** Verify that another AI can understand the system from one Markdown export without the original conversation.

**Steps:**
1. Generate exports/COUNCIL-SYSTEM-SOURCE.md from current authoritative files.
2. Check version, date, source manifest, privacy, and completeness.
3. Start a separate fresh conversation or use a separate Agent.
4. Provide only the exported Markdown.
5. Ask it to explain the system, distinguish Project from Council, and describe memory/sync boundaries.
6. Ask it to propose a safe Council creation workflow.

**Expected:**
- The second context can explain core concepts without hidden chat history.
- It does not claim access to files or tools it was not given.
- It understands that GitHub push does not refresh GPT Add Sources.
- No private information is exposed.

**Evidence:** export file, fresh-context answers, omissions or misunderstandings.

## Test 6 — GitHub synchronization

**Purpose:** Verify a real authorized remote update.

**Preconditions:** user has approved the target repository/branch and the Agent has write access.

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

## Result vocabulary

- **Not Run:** no execution attempted.
- **Passed:** steps completed and expected outcomes verified with evidence.
- **Failed:** behavior contradicts an expected result.
- **Blocked:** a required tool, permission, or input was unavailable.
- **Partial:** some steps passed; remaining steps are unresolved.

## Test report template

For every run, record:
- Test ID and date.
- Agent/platform and available tools.
- Exact input/prompt.
- Expected result.
- Actual result.
- Evidence and changed files.
- Status and follow-up issue.
