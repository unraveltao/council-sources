# Council Designer v1.0.0

Council Designer helps you design a human-led Agent organization and maintain its rules, decisions, and organizational memory. Load [SKILL.md](SKILL.md) through your Agent host or supply it as context. The Skill can work in a conversation using only the material you provide.

## What it does

| Mode | Give it | Expect |
| --- | --- | --- |
| Design | A goal, available people or Agents, and known constraints | Role and authority design, handoffs, and a Markdown draft when requested |
| Review | Existing organizational rules or an earlier proposal | Evidence-based findings on conflicts, duplicated duties, gaps, and practical improvements |
| Update | Your existing organizational document and confirmed changes | One revised Markdown document that preserves valid rules and decision history, with a short Change Summary |
| Export | The relevant organizational state and intended audience | One self-contained Markdown document suitable for review and manual sharing |

## Quick start

1. Load Council Designer using your host's Skill mechanism, or provide the full contents of [SKILL.md](SKILL.md). Access to a repository link alone may depend on the host.
2. Describe your target goal, current organization if any, and decision or privacy boundaries.
3. Ask for Design, Review, Update, or Export. Tell the Agent which supplied decisions are approved.

For a new organization:

> Design a lightweight Council to coordinate my research notes and monthly reviews. Start with a single executor if that is enough. I approve scope changes. Draft one Markdown document and mark unapproved choices as proposals.

To update an existing organization:

> Update the organizational Markdown below. I approve moving weekly review from the Coordinator to the Reviewer. Keep the mission and access rules, preserve the prior assignment as superseded, and include a Change Summary.

## How it works

Roles represent responsibilities. An executor can hold several roles, and roles can be split or reassigned as needed. Each Council keeps its own authority and memory. Project requirements, code, and deliverables stay with their authoritative Project.

Use **QD** for questions that change the next decision, **Checkpoint** to record evidence and pending work at meaningful boundaries, and **Review** to assess actual outcomes. Checkpoints and reviews can stay in the conversation.

| Marker | Meaning |
| --- | --- |
| ❓ | A question for the user |
| 🧭 | A choice that can be combined, qualified, or answered freely |
| 🔍 | Analysis of scope, evidence, uncertainty, or trade-offs |
| ➜ | The Agent's reasoned recommendation |
| ✅ | A user-confirmed decision or an evidence-verified outcome |

Memory updates distinguish facts, inferences, proposals, and unknowns. **Level 1 Routine** stays within authorized scope. **Level 2 Significant** requires confirmation unless explicitly delegated for that class of change. **Level 3 Core** requires explicit approval for the specific decision. Material superseded decisions remain traceable.

## Boundaries

You choose whether to adopt the output and where to store it. Council Designer drafts Markdown in the conversation by default. It requires no designated repository, registry, database, or folder layout. It performs no automatic Agent creation, synchronization, or writes to ChatGPT Memory or other storage. Host access and any separate write or publication require authorization. It uses selected Project references and protects private organizational material.

Earlier Council Sources layouts and exports are documented in the [legacy guide](../../docs/COUNCIL-SOURCES-LEGACY.md). You can supply their text as input when reviewing or updating an existing organization. For V1.0 verification and unrun scenarios, see [test results](../../tests/V1-TEST-RESULTS.md).
