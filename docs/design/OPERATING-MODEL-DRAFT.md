# Council Operating Model — Design Draft

> Status: Discussion draft / Stage checkpoint  
> Scope: Records the current operating-model decisions. Council Designer v0.3.0 now uses QD, Checkpoint, and Review as default collaboration methods where relevant. This does not by itself establish mandatory adoption by every independent Council. Live behavior acceptance remains pending.  
> Language: English, following the repository documentation policy.

## 1. Purpose

This document records the current design direction for how a Council organizes collaborative work. It is intended to preserve the decisions reached so far and provide a stable point for further discussion.

The current model is built around three small, reusable atomic methods:

- **QD** drives the work through questions and shared understanding.
- **Checkpoint** makes progress, completed work, and remaining work visible.
- **Review** evaluates the outcome, verifies completion, and produces a useful summary or deliverable.

The intention is to solve many recurring collaboration problems with a small number of stable methods, rather than creating a large catalogue of narrowly specialized methods.

## 2. Relationship to the Council workflow

The three methods have distinct responsibilities and are not three sequential project phases.

| Method | Primary responsibility | Main question |
| --- | --- | --- |
| QD | Question-driven clarification and collaboration throughout the work | What are we trying to understand or solve? |
| Checkpoint | Progress and state tracking at meaningful points | Where are we now, what is done, and what remains? |
| Review | Retrospective, evaluation, verification, and delivery | What did we accomplish, and does it meet the goal? |

QD is the central interaction mechanism and may be used at any point where clarification is needed. Checkpoints can occur repeatedly during work. Review is commonly used at task or milestone completion, and may also be triggered by a significant event when an explicit evaluation is useful.

These methods support a flexible workflow. They do not require every task to follow a fixed sequence or invoke all three methods.

## 3. AM-01 — QD (Question-driven Clarification)

### 3.1 Purpose

QD is a bidirectional, question-driven method for developing shared understanding between the user and the AI collaborators. It helps clarify ambiguous ideas, concepts, requirements, goals, assumptions, and decisions.

QD is intended to drive the work, not merely to collect answers. The AI should explain its interpretation and reasoning so the user can correct, refine, or confirm the shared understanding.

### 3.2 When to use it

Consider QD when:

- The user's intent, goal, or request is ambiguous.
- A concept has multiple plausible interpretations.
- Important requirements, constraints, or decisions are unknown.
- The user and AI appear to understand the issue differently.
- A complex task needs progressive clarification before a useful plan can be formed.
- New uncertainty appears during planning or execution.

Do not force a full QD interaction for a simple, sufficiently clear request.

### 3.3 Working principles

1. Start from the context and information already available; do not ask the user to repeat known facts.
2. Identify the uncertainties that materially affect the outcome.
3. Ask focused questions. Prefer one central question at a time; combine only closely related, low-effort questions when that reduces friction.
4. After the user's answer, explain the AI's current understanding and identify any remaining mismatch.
5. Use follow-up questions only when the answer can change the understanding, decision, or next action.
6. Adapt the next question to the user's response rather than following a rigid questionnaire.
7. Make assumptions explicit. Distinguish confirmed facts, interpretations, proposals, and unknowns.
8. Stop clarifying when there is enough shared understanding to proceed safely and usefully.
9. Preserve unresolved questions when they do not block the next step; do not keep questioning merely to make the design exhaustive.
10. The user may pause, redirect, add a topic, or decide to proceed with an explicitly recorded assumption.

### 3.4 Expected result

Depending on the task, QD should produce a sufficiently clear set of:

- Goal and intended outcome.
- Relevant context and constraints.
- Agreed interpretation or problem definition.
- Important assumptions and decisions.
- Open questions and blockers.
- A suitable next action.

QD does not always need to produce a separate file.

## 4. AM-02 — Checkpoint (Progress Checkpoint)

### 4.1 Purpose

Checkpoint is a progress-recording and state-alignment method. It gives the user and AI collaborators a shared view of the current stage, what has actually been completed, what remains, and what should happen next.

A Checkpoint is more than a percentage estimate. It records evidence-backed progress and makes the remaining work visible.

### 4.2 When to use it

A Checkpoint may be appropriate when:

- A discussion or design stage has reached a meaningful boundary.
- A group of important questions has been resolved.
- A task or milestone is completed.
- A significant change affects the plan or current state.
- The user wants to pause or later resume the work.
- A long-running task needs a progress update.
- The user explicitly asks where the work stands.

Do not create a Checkpoint after every ordinary message.

### 4.3 Working procedure

1. Capture the current state based on what has actually happened.
2. Record completed stages, tasks, resolved questions, and confirmed decisions.
3. Identify remaining tasks, unresolved questions, blockers, dependencies, and risks.
4. Compare the current state with the intended goal or milestones.
5. Note material deviations and propose adjustments when needed.
6. State the next stage or most useful next action.
7. Make the record understandable enough that work can resume later without reconstructing the entire conversation.

### 4.4 Standard record

A Checkpoint should include the fields relevant to the task:

- **Task / Project:** what work is being tracked.
- **Current stage:** where the work currently stands.
- **Completed:** verified tasks, questions, decisions, or milestones.
- **In progress:** work currently underway.
- **Remaining:** unresolved tasks and questions.
- **Blockers / Risks:** issues that prevent or threaten progress.
- **Next step:** the next intended action.
- **Status:** for example, Not started, In progress, Blocked, or Completed.

The record should distinguish task-level checkpoints from milestone-level checkpoints when useful. Both use the same method; they differ in scope and granularity.

### 4.5 Record maintenance

The preferred direction is to maintain a clear current-state record and retain meaningful checkpoint history without generating a separate file for every small update. The exact storage format and history mechanism remain to be decided.

Never mark planned work as completed. Do not invent progress percentages or completion claims without evidence.

## 5. AM-03 — Review (Reflection, Validation, and Summary)

### 5.1 Purpose

Review is the method for looking back over a task or meaningful body of work, evaluating its outcome, checking whether the original goal was met, and producing an appropriate summary or deliverable.

Review is not merely a transcript summary. It should assess results against the intended outcome.

### 5.2 When to use it

Review is commonly used when:

- A task or project milestone is finished.
- A learning, research, design, or engineering activity reaches its intended endpoint.
- The user requests a summary or retrospective.
- A significant event requires a focused evaluation.
- A deliverable or acceptance decision is required.

A significant event may justify a focused Review before the entire project is finished. Ordinary progress recording remains the responsibility of Checkpoint.

### 5.3 Working procedure

1. **Recall:** revisit the original goal, context, key steps, and decisions.
2. **Evaluate:** compare actual outcomes with the intended goal and identify gaps.
3. **Verify:** perform or review the checks, tests, evidence, or acceptance criteria appropriate to the task.
4. **Summarize:** state the results, important decisions, lessons, and unresolved issues.
5. **Deliver:** produce the requested artifact or clearly state what can and cannot be delivered.
6. **Preserve:** identify information that should be retained in Council memory, project documentation, or the user's knowledge base, subject to the applicable authorization and memory rules.

### 5.4 Expected output

A Review may include:

- Original goal.
- Actual result.
- Verification evidence and test status.
- Confirmed decisions.
- Lessons and improvement opportunities.
- Unresolved items.
- Deliverables and their locations.
- Proposed memory or documentation updates.

### 5.5 Integrity requirements

- Distinguish completed, partially completed, blocked, and uncompleted work.
- Do not present plans as results.
- Do not claim tests passed unless they were actually performed and supported by evidence.
- Distinguish facts, interpretations, and recommendations.
- Do not update organizational memory beyond the applicable authority and approval scope.

## 6. How the three methods work together

The methods complement each other:

- **QD drives understanding and problem-solving through questions.**
- **Checkpoint tracks the state and remaining work as the task progresses.**
- **Review evaluates the final outcome, verifies it where appropriate, and produces a summary or deliverable.**

A typical complex task may repeatedly use QD while progressing through several checkpoints, then use Review for final evaluation and delivery.

A simple task may need only a direct answer. A task with a clear goal but many execution steps may use Checkpoint frequently without repeated QD. A task may also require a focused Review at a major milestone.

The methods are not mutually exclusive, and their use should match task complexity.

## 7. Progressive clarification and bounded discussion

QD must not become an endless sequence of questions. For structured design or planning discussions:

- State the current stage and its objective.
- Give a reasonable estimate of the key questions or decisions likely to be needed.
- Ask only questions that materially affect the outcome.
- Prefer one focused question at a time, while combining simple related questions when appropriate.
- Adjust the estimate as the discussion develops; it is a planning aid, not a quota.
- Stop early when the stage objective is satisfied.
- At the end of a stage, use Checkpoint to report what is settled, what remains open, and what comes next.
- Allow the user to pause, redirect, or defer non-blocking questions.

The exact default question budget and interaction format remain open for further design.

## 8. Relationship to organizational memory

The methods and organizational memory have different responsibilities:

- QD clarifies what the user means and what has been decided.
- Checkpoint records the current state of the work.
- Review identifies what is worth preserving after evaluation.
- Memory rules determine ownership, authorization, approval level, conflict handling, and where persistent organizational knowledge belongs.

A Checkpoint is not automatically a permanent memory update. A Review may propose memory changes, but those changes must follow the applicable approval rules. Project artifacts should remain in their authoritative Project repository or knowledge base rather than being copied wholesale into Council memory.

## 9. Current design decisions

The following points reflect the discussion so far:

1. Council should use a small number of stable, reusable atomic methods rather than a large catalogue of methods.
2. The initial three methods are QD, Checkpoint, and Review.
3. QD is question-driven and is the central interaction mechanism throughout the work.
4. Checkpoint records current stage, completed work, remaining questions/tasks, blockers, and next steps.
5. Review provides retrospective, evaluation, appropriate verification, summary, and delivery.
6. The methods should be used according to task needs; not every task must invoke all three.
7. Discussion should be bounded and stage-aware. Checkpoints should make progress and remaining work visible.
8. The user remains the organization lead and retains the relevant decision and approval authority.

## 10. Open design decisions

These items are intentionally not finalized in this draft:

- Whether the three methods are globally mandatory defaults, globally defined methods with Council-level configuration, or loaded through another mechanism.
- Whether every independent Council must adopt the methods by default, or whether each Council configures their use. Council Designer's default use is defined in SKILL.md v0.3.0.
- Whether Checkpoint current state and history should live in one file or use another storage pattern.
- The final placement and naming of the operating guide, memory rules, and Council template.
- The exact default question budget and the point at which a discussion stage is considered complete.
- The final relationship between this operating model and the existing Core Principles and System Architecture documents.
- The acceptance scenarios and evidence needed to validate the methods in real Agent interactions. T8–T10 now define the manual QD, Checkpoint, and Review behavior tests; none is marked Passed until executed.

## 11. Status and next step

This draft is a discussion checkpoint, not an approved system specification. It records the current shared understanding so that later discussion can continue without losing decisions already reached.

The next design step is to review the open decisions, clarify the methods' authority and loading model, and then decide how to consolidate the existing repository documents. No existing Skill behavior, permissions, memory policy, or repository architecture is changed by this draft alone.
