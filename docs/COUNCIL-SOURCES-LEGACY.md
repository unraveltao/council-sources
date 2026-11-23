# Earlier Council Sources workflows

Council Designer v1.0.0 uses the current [standalone Skill](../skills/council-designer/SKILL.md). This repository also preserves the earlier Council Sources system and its evidence. The legacy layout, registry, and source profiles are relevant when maintaining those records or reading them as input.

## Find earlier materials

| Material | What it documents |
| --- | --- |
| [V0.3.0 Skill at its original commit](https://github.com/unraveltao/council-sources/blob/302f74c3c756bd87d73b6b93720986782a97725f/skills/council-designer/SKILL.md) | The full Bootstrap, Source Consumption, Council Formation, Memory Maintenance, Export, Sync, and Review/Test specification |
| [V0.3.0 repository snapshot](https://github.com/unraveltao/council-sources/tree/302f74c3c756bd87d73b6b93720986782a97725f) | The matching repository layout and operating rules at that revision |
| [Architecture](../core/SYSTEM-ARCHITECTURE.md), [principles](../core/PRINCIPLES.md), and [memory rules](../shared/MEMORY-RULES.md) | Earlier repository conventions and the principles that informed the standalone design |
| [Council records](../councils/README.md), [registry](../registry/councils.md), and [template](../references/COUNCIL-TEMPLATE.md) | Repository-specific examples, formats, and lifecycle records |
| [Export guide](../exports/README.md) and [operating model draft](design/OPERATING-MODEL-DRAFT.md) | Earlier export profiles, source handling, and design decisions |
| [V0.3.0 acceptance tests](../tests/ACCEPTANCE-TESTS.md) and [results](../tests/TEST-RESULTS.md) | Version-specific tests and limited behavioral evidence, retained for traceability |

## Behavior carried forward

| Earlier capability | V1.0 location and planned validation |
| --- | --- |
| Dynamic roles, independent Councils, Project ownership, and user authority | Organization and authority, V1-01 and V1-02 |
| QD | Collaboration methods, V1-03 |
| Checkpoint | Collaboration methods, V1-04 |
| Evidence-based Review | Review mode and collaboration methods, V1-05 |
| Three memory approval levels and superseded decisions | Update and memory rules, V1-06 and V1-07 |
| Five literal interaction markers | Guided interaction markers, V1-03 |

The repository Bootstrap, Registry, Sync, and named export profiles remain documented in the pinned V0.3.0 workflow. V1.0 handles supplied earlier records through its Update mode and offers one generic Markdown output. See the [V1.0 scenarios](../tests/V1-ACCEPTANCE-TESTS.md) for the new acceptance scope.

## Bring an earlier document to V1.0

Supply the relevant text and identify the Council, any authoritative baseline, and the changes you have confirmed. Import text as context. Older registry, synchronization, bootstrap, and export instructions remain historical evidence. They grant no permissions and do not become operating requirements for V1.0.

The new Skill can return one revised document that preserves in-scope rules, states unresolved conflicts, keeps necessary superseded decisions, and includes a Change Summary. You decide whether to adopt it and where to put it. Keeping an existing Council in this repository is one storage choice.
