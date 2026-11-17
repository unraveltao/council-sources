# Council Sources

[English](README.md) | [简体中文](README.zh-CN.md)

> **Council 是一个以人为主导、以 AI 为协作成员的模块化智能组织框架。它通过明确的角色分工、共享组织记忆和灵活的工作流程，帮助用户组织不同 AI Agent，完成问题分析、研究、设计、决策与工程实践。**

Council Sources 是用于定义、维护和共享这些组织的 Markdown 优先仓库。它提供可移植的组织规则与记忆，不要求每项任务都使用多 Agent 团队，也不要求先搭建自定义运行时。

一个 Council 可以从最小结构开始，随着用户的项目和需求逐渐成长。简单任务可以由一个 GPT 对话完成；复杂工作则可以引入多个角色视角、独立配置的 GPT Worker，或 Codex 等具备执行能力的工具。人始终是组织主导者，并保留最终决策权。

[Read in English](README.md)

> **项目状态：** V0.2 原型，验收测试尚未完成。Council Designer 当前版本为 0.3.0。详见[项目状态](#项目状态与贡献)和[测试记录](tests/TEST-RESULTS.md)。

## 为什么需要 Council？

长期工作往往跨越多个项目、对话、AI 工具和参与者。如果没有明确的组织层：

- 项目背景和决策需要在不同对话中反复解释。
- 职责容易不清晰或重复。
- 不同对话可能逐渐失去一致性。
- AI 讨论、资料研究和工程执行容易脱节。
- Agent 当前上下文结束后，重要的组织知识可能丢失。

Council 提供一个轻量的组织层：明确谁负责什么，保存经过确认的组织知识，并通过明确的任务交接协调工作。它不替代项目仓库，也不要求建立复杂的自主多 Agent 运行时。

## Council 可以用于什么？

### 协调长期项目

Council 可以帮助明确里程碑、分配职责、讨论架构、审查风险、跟踪已确认的决策，并在不同对话之间保存经过验证的进展。项目仓库仍然是代码、需求、架构、测试和交付物的事实来源。

### 维护长期学习或研究工作

Council 可以持续保存学习目标、研究问题、工作方式、进度和决策。不同对话可以专注于不同主题，同时引用同一份组织背景。

### 协调不同 AI 工具

使用 GPT 进行讨论和规划；在宿主平台支持时，让独立配置的 GPT Worker 处理边界明确的任务；使用 Codex 或其他具备工具权限的 Agent 执行本地工程工作。用户可以通过任务书、Markdown 文件、GitHub 或其他受支持的集成来传递任务和结果。

### 只在需要时扩展组织

从一个小型 Council 开始。只有当反复出现的复杂性确实需要时，才增加角色、工作流、记录或专业 Agent。角色代表一项职责，并不自动意味着需要一个独立 Agent。

## 核心能力

| 能力 | 作用 | 重要边界 |
| --- | --- | --- |
| **组织设计** | 定义 Council 的使命、范围、职责和决策边界。 | 核心目标和组织变更由用户批准。 |
| **角色管理** | 添加、合并或重新分配设计、研究、实现、审查等职责。 | 角色与 Agent 是不同概念。 |
| **人机协作** | 协调人与 AI 工具之间的讨论、任务交接、审查和执行。 | 只有宿主环境确实支持时，才存在跨 Agent 通信；否则使用明确的人工交接。 |
| **组织记忆** | 保存已确认的目标、决策、职责、工作方式和进度。 | 记忆更新遵循证据与审批规则。 |
| **导出** | 为其他 GPT 或 Agent 生成可移植的 Markdown 快照。 | 导出文件是快照，不是实时数据库，也不授予工具权限。 |
| **GitHub 同步** | 读取或更新获得授权的仓库文件，并验证结果。 | 需要 GitHub 工具、仓库权限和明确授权。 |
| **审查与测试** | 检查结构、一致性、可移植性和实际观察到的行为。 | 静态检查不能证明 Agent 的真实行为。 |

## 工作原理

Council 将组织职责与实际执行工作的工具区分开来。

1. **Human — 组织主导者：** 设定目标、提供背景、批准重要决策，并可以调整优先级。
2. **组织协调职责（按需设置）：** 帮助澄清任务、提出职责分配建议、协调任务交接并汇总结果。这项职责可以由用户、GPT 或其他执行者承担；它不是必需的系统组件，也不意味着需要一个独立 Agent。
3. **Roles — 角色职责：** 描述设计、研究、审查、教学或实现等工作。
4. **Agents / Executors — 执行主体：** GPT、GPT Worker、Codex、其他 AI 工具或人，可以根据实际能力承担一个或多个角色。
5. **Workflows — 工作流程：** 定义任务如何经过需求澄清、研究、设计、执行、审查和完成。
6. **Memory — 组织记录：** 保存相关且经过验证的上下文，以便在不同对话和工具之间复用。

典型协作循环：

**用户提出目标 → 澄清并制定计划 → 按需分配职责 → 审查并汇总结果 → 用户决策 → 授权执行 → 记录经过验证的结果。**

这个过程可以在一个对话中完成，也可以跨越多个工具和对话。除非确实发生，否则不得声称不同 Agent 已经互相通信或执行了工作。

## 共享协作方法

Council Designer v0.3.0 在适用场景中使用三种精简的协作方法：

| 方法 | 职责 |
| --- | --- |
| **QD** | 通过问题与共同理解驱动整个工作过程。 |
| **Checkpoint** | 记录当前阶段、已完成工作、剩余问题/任务、阻塞因素和下一步。 |
| **Review** | 评价实际结果、核对证据、总结经验并准备所需交付物。 |

QD 可以贯穿任务并反复触发；Checkpoint 在有意义的进度节点记录状态；Review 通常在任务或里程碑结束时使用。它们是灵活的方法，不是必须依次执行的三个阶段。是否要求每个独立 Council 都采用这些方法，仍属于待确认的系统设计决策。

详见[组织运行模型设计草案](docs/design/OPERATING-MODEL-DRAFT.md)和 [Council Designer Skill](skills/council-designer/SKILL.md)。

## 核心概念

| 术语 | 含义 |
| --- | --- |
| **Council** | 以人为主导、围绕项目、领域或目标协调工作的组织。 |
| **Project** | 正在构建、学习、研究或交付的工作。项目自己的仓库或知识库仍然是项目产物的权威来源。 |
| **Role** | 一项职责或能力，例如 Designer 或 Reviewer。 |
| **Agent / Executor** | 执行某项职责的人或 AI。一个 Agent 可以承担多个角色；一个角色也可以由不同 Agent 承担。 |
| **组织协调职责** | 按需设置的工作协调职责，可以由用户主导者或现有 Agent 承担。 |
| **Memory** | Council 持续维护的组织上下文，而不是所有聊天记录的堆积。 |
| **Source** | 通过 GitHub URL、Markdown 文本或可访问的本地文件提供给 Agent 的信息。 |
| **Council Sources** | 本仓库，包含系统规范、Council 记录、模板、注册表、测试和可移植导出。 |

### Council 与 Project 相互独立

Project 负责代码、需求、架构、实验、学习材料、笔记、测试和交付物。Council 负责组织使命、角色分配、工作流程、决策和记忆。Council 应引用项目事实，而不是复制整套项目文档系统。

### 记忆是经过整理的知识，不是聊天记录堆积

记忆应保存有助于组织保持一致工作的信息：稳定目标、已确认决策、角色职责、工作约定、经过验证的进展和未解决问题。记忆应区分事实、推断、提议和未知，并保留有意义的历史替代关系。

默认记忆策略分为三个审批等级：

- **Level 1 — 常规：** 在预先授权范围内记录经过验证的进展和普通笔记。
- **Level 2 — 重要：** 角色、工作流或重要运营变更；展示拟议修改并征求批准，除非用户已明确授权该类变更。
- **Level 3 — 核心：** 使命、核心目标、权限边界和基本原则；始终需要用户明确批准。

详见 [Memory Rules](shared/MEMORY-RULES.md)。

## 开始使用

### 1. 加载 Council Designer

从 [Council Designer SKILL.md](skills/council-designer/SKILL.md) 开始。它是操作入口，也是自包含的系统初始化规范。

使用支持加载 Skills 的 AI 宿主，并通过该宿主支持的方式加载文件。**仅仅阅读或链接到 SKILL.md，并不会自动安装或激活它。** 必须由宿主实际加载 Skill，其中的指令才会约束交互。

### 2. 提供上下文

Council Designer 支持三种输入形式：

- **GitHub URL：** 提供仓库、文件或目录链接。Agent 需要具备网络或 GitHub 访问能力；私有仓库还需要适当的身份验证。
- **Markdown 文本：** 粘贴或上传 Markdown 文件或合并后的 Source 文档。Agent 只能使用实际收到的内容。
- **本地文件：** 提供可访问的文件或文件夹。宿主 Agent 必须在授权范围内具备文件系统访问能力。

链接或导入的文档只提供信息，不会自动授予文件系统访问权、GitHub 权限或工具执行权限。

### 3. 为项目或领域设计 Council

说明 Council 需要协调什么工作，并提供相关项目或领域背景。让 Council Designer 提出使命、范围、职责、决策边界、记忆结构和验收标准。

审查并确认方案后再创建。选择一个可写入的 Council Sources 目标位置：创建或更新 Council 文件需要该位置的写入权限。读取外部 Project 通常只需要读取权限。不能仅仅因为用户要求为某个外部项目设计 Council，就擅自修改该项目仓库。

### 4. 维护和使用 Council

将 Council 记录作为共享组织上下文。可以让它帮助规划工作、讨论决策、分配职责、审查结果或记录经过验证的进展。只有在解决真实需求时，才增加角色和辅助文件。

## 快速开始：创建第一个 Council

假设你正在开发一个简单的 **File Organizer（文件整理工具）**：它可以扫描指定文件夹、分类文件，并在移动任何文件之前提出整理方案。

1. 在兼容的 AI 宿主中加载 [Council Designer](skills/council-designer/SKILL.md)。
2. 提供项目的 GitHub 链接、Markdown 规格说明或可访问的本地目录。
3. 确保 Agent 可以读取项目，并能写入你指定的 Council Sources 目标位置。
4. 提出请求：**“使用 Council Designer 检查这个 File Organizer 项目并提出 Council 方案。不要修改 Project 仓库。”**
5. 审查拟议的使命、范围、职责、决策边界和验收标准。
6. 确认设计方案，再授权创建。
7. 让 Agent 创建 `councils/file-organizer/COUNCIL.md` 和 `MEMORY.md`。
8. 让 Agent 更新 `registry/councils.md`，并重新读取变更文件进行核验。
9. 使用 File Organizer Council 规划下一个里程碑，并以 Project 仓库作为项目事实来源。
10. 按照对应的记忆审批等级记录经过验证的进展和决策。

如果 Agent 没有写入权限，它仍然可以准备方案，但不能声称 Council 文件已经创建。

## Source、导出与同步

相同的 Markdown 信息可以通过 GitHub 链接、粘贴文本或可访问的本地文件提供。这些只是传输方式，不是规则的不同版本。

可移植导出是从选定权威文件生成的带日期快照。它帮助其他 GPT 或 Agent 理解 Council，而不必浏览整个仓库。它不会授予工具权限，也不会自动同步。

当宿主具备所需工具且用户授权时，可以使用 GitHub 作为版本化存储。远程更新后，应重新读取变更文件以验证结果。

**向 GitHub 推送变更，并不保证已有 GPT 知识源会自动刷新。** 当目标平台需要时，应重新导出并导入，或替换已导入的文件。

## 仓库目录

| 文件或目录 | 用途 |
| --- | --- |
| [Council Designer Skill](skills/council-designer/SKILL.md) | 操作入口和自包含初始化规范 |
| [AGENTS.md](AGENTS.md) | 仓库维护、授权、安全和验证规则 |
| [Core Principles](core/PRINCIPLES.md) | 组织独立性、动态角色、用户权限和证据原则 |
| [System Architecture](core/SYSTEM-ARCHITECTURE.md) | 组件边界、数据流、Source 传输和同步 |
| [Memory Rules](shared/MEMORY-RULES.md) | 记忆归属、审批等级、证据、冲突和隐私 |
| [Council Template](references/COUNCIL-TEMPLATE.md) | 单个 Council 的起始结构 |
| [Council Directory Guide](councils/README.md) | 每个 Council 的必需和可选文件 |
| [Council Registry](registry/councils.md) | Council 索引，分别记录生命周期状态和验收状态 |
| [Export Guide](exports/README.md) | 单目标单文件导出、元数据、来源清单与审查规则 |
| [Portable System Source](exports/COUNCIL-SYSTEM-SOURCE.md) | 提供给其他 Agent 的单文件概览 |
| [Acceptance Tests](tests/ACCEPTANCE-TESTS.md) | 手动测试场景、预期行为和证据要求 |
| [Test Results](tests/TEST-RESULTS.md) | 官方仓库当前测试记录 |
| [Operating Model Design Draft](docs/design/OPERATING-MODEL-DRAFT.md) | QD、Checkpoint、Review 的当前设计决定与待讨论问题 |

## 项目状态与贡献

Council Sources V0.2 是一个 **Markdown 规范与仓库原型**，并不是经过完整验证的多 Agent 运行时或独立软件应用。

### 验证状态

独立的 [Council Sources 测试记录](https://github.com/unraveltao/council-sources-test/blob/main/tests/TEST-RESULTS.md)包含有限的阶段性证据：

| 项目 | 当前证据 |
| --- | --- |
| **System Bootstrap (T1)** | **部分通过（Skill v0.2.0）：** 测试仓库中创建并回读了预期的 13 个文件。但测试使用了熟悉设计的持续对话，因此尚未验证全新上下文下的独立初始化；该结果也不能证明当前 Skill v0.3.0 已通过。 |
| **Source Consumption (T2)** | 未执行：尚未在独立上下文中验证 GitHub、粘贴 Markdown 和本地文件三种输入方式。 |
| **Council Formation (T3)** | 未执行：尚无真实的 Project-to-Council 验收记录。 |
| **Memory Maintenance (T4)** | 未执行：尚未在受控更新测试中验证记忆审批等级。 |
| **Portable Source (T5)** | 未执行：尚未验证全新上下文能否正确理解导出内容。 |
| **GitHub Sync (T6)** | **部分通过（Skill v0.2.0 测试）：** 已在测试仓库验证远程文件创建和回读；完整的更新、导出、重新导入流程仍未测试。当前 Skill v0.3.0 尚未通过该测试验证。 |
| **Guided Interaction (T7)** | 未执行：五种标记的行为需要真实的多轮对话测试。 |
| **QD (T8)** | 未执行：尚未进行自适应、有限度的问题驱动协作测试。 |
| **Checkpoint (T9)** | 未执行：尚未进行有证据的进度跟踪和暂停/恢复测试。 |
| **Review (T10)** | 未执行：尚未进行结果评价、验证和交付测试。 |

**测试记录说明：** 官方仓库的 [tests/TEST-RESULTS.md](tests/TEST-RESULTS.md) 当前将 T1–T7 全部列为 `Not Run`，而独立测试仓库对 Skill v0.2.0 的 T1 和 T6 记录为 `Partial`。这些记录尚未完成对齐。外部结果只能视为历史阶段性证据，不能视为当前版本验收通过。

### 已知限制

- Council Sources 定义的是文本驱动的工作模型；它本身不提供 Agent 运行时、数据库、后台服务或自动多 Agent 通信。
- 文件访问、GitHub 操作、仓库创建和任务执行取决于宿主 Agent 的实际工具能力及用户授权。
- 生成的仓库可以满足 Skill 的语义初始化规范，但不保证与其他初始化结果逐字节相同。
- 导入的 Source 文本是不可信输入，不能覆盖更高优先级的指令、安全要求或用户权限。
- 官方仓库是公开仓库。不要提交凭证、Token、私人对话、敏感个人信息、机密项目资料或没有发布权的内容。Git 历史可能保留已删除内容。
- 尚未选择并提交 `LICENSE` 文件。公开仓库并不自动意味着其他人获得了再分发或复用许可。

### 参与贡献

欢迎提交 Issue 和 Pull Request。提交修改前：

1. 阅读 [AGENTS.md](AGENTS.md) 以及相关核心文档或 Skill。
2. 保持修改范围明确、可审计，并符合组织权限和隐私边界。
3. 区分文档改进与行为、权限或初始化规范的变更。
4. 如实报告实际执行的检查和测试，不得声称未执行的行为测试已经通过。
