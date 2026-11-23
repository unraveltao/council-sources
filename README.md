# Council Sources

[English](README.md) | [简体中文](README.zh-CN.md)

Council Sources is the home of [Council Designer v1.0.0](skills/council-designer/README.md) and the Council Sources documents created with earlier versions. Council Designer works independently from this repository. It helps you design a human-led Agent organization and maintain its rules and organizational memory.

## Start with Council Designer

1. Load [SKILL.md](skills/council-designer/SKILL.md) through a host that supports Skills, or provide its complete text to your Agent as context.
2. Describe your goal and constraints. For an existing organization, supply the document or accessible source text.
3. Ask for Design, Review, Update, or Export and identify decisions you have already approved.

> Design a small research Council for weekly topic reviews. Reuse one executor if that is sufficient. I retain approval over scope and sharing. Give me one Markdown draft with pending decisions labeled.

You can review a design before adopting it. For an update, expect one revised Markdown document with a short Change Summary and any replaced decisions kept in context.

## Organization and permissions

A Council defines responsibilities and handoffs. One executor may hold several roles. Each Council keeps its own authority and organizational memory, while its Project remains the source of truth for requirements, code, and deliverables. The user retains final authority over adoption and major decisions.

Council Designer uses QD, Checkpoint, and Review according to the situation. By default its output stays in the conversation, and you choose where to save it. The Skill requires no registry, repository layout, database, Agent provisioning, synchronization service, or persistent-memory integration.

## Repository navigation

| Start here | Purpose |
| --- | --- |
| [Council Designer guide](skills/council-designer/README.md) | Modes, examples, interaction markers, and approval levels |
| [Council Designer Skill](skills/council-designer/SKILL.md) | Self-contained behavior for V1.0 |
| [Legacy Council Sources guide](docs/COUNCIL-SOURCES-LEGACY.md) | V0.3.0 repository workflows, earlier templates and examples, exports, and evidence |
| [Repository operating rules](AGENTS.md) | Contribution, privacy, authorization, and verification rules for this repository |
| [V1.0 acceptance scenarios](tests/V1-ACCEPTANCE-TESTS.md) and [results](tests/V1-TEST-RESULTS.md) | Verification of the current Skill and its remaining test coverage |

## Validation and contributions

V1.0 static checks and behavioral acceptance are recorded separately. Live V1.0 interaction scenarios are **Not Run**. The older repository workflow has its own [V0.3.0 evidence](tests/TEST-RESULTS.md).

Read [AGENTS.md](AGENTS.md) before contributing. Check the affected version's instructions and preserve versioned evidence, user authorization, and private content boundaries.
