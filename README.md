# Council Sources

**Design independent AI Councils. Keep their rules, responsibilities, and memory organized, versioned, and reusable.**

Council Sources 是一个以 **Markdown + GitHub** 为基础的 AI 组织 Source 仓库。它帮助个人或团队根据项目、领域或长期目标，设计和维护独立的 **Council（组织/委员会）**，并把组织规则与记忆整理为可以交给 GPT 或其他 Agent 阅读的资料。

> **Status: V0.1 · Early prototype / 尚待真实使用验收。** 当前交付的是文件模板、Skill 指引和维护规范；不包含持续运行的 Agent 服务、自动化后台或直接更新 GPT Add Sources 的接口。

## 为什么需要 Council Sources？

当多个 AI 对话和项目不断增长，常见困难包括：

- 项目目标、组织职责、历史决策和待办事项散落在不同对话中，重新开始时难以恢复上下文。
- 一个 Agent 能完成的简单任务被强行拆成多个角色；真正复杂的任务又缺乏明确的负责人。
- 软件研发、教育、研究和个人知识管理需要不同工作方式，不能套用同一套僵硬组织结构。
- GPT 中已导入的 **Add Sources** 与 GitHub 文件不是实时同步的，修改后容易出现版本不一致。

**目标：** 通过简单、可读、可审查的文件，让各个 Council 有清晰的使命、职责、协作方式、更新规则与持续工作的记忆。

## 三个核心概念

| 概念 | 职责 | 不做什么 |
| --- | --- | --- |
| **Council Designer Skill** | 设计组织、创建文件、提出记忆更新、导出 Source、在授权后同步 GitHub | 不假装拥有未授权的执行能力 |
| **Council** | 为某个项目或领域组织工作、按需分工、处理问题、维护自己的组织记忆 | 不擅自接管其他 Council |
| **Repository Agent / AGENTS.md** | 指导具有文件权限的 Agent 安全维护目录、索引、历史和 GitHub 提交 | 不充当各个组织的业务上级 |

**Council ≠ Project。** Council 管理「如何组织工作」；项目原有的代码、课程、PRD、架构文档和笔记仍以其原始位置为准，这里只记录必要的组织信息及引用。

## 快速开始

### 1. 创建一个 Council

1. 阅读 [Council Designer Skill](skills/council-designer/SKILL.md)，在支持的 Agent 平台安装它，或直接把其文本提供给 Agent 作为工作说明。实际加载方式取决于平台。
2. 向 Agent 说：**“使用 Council Designer，帮我为 Python 学习体系设计一个 Education Council。”**
3. 先确定使命、工作边界、职责、可用执行者与授权范围；简单任务允许一个 Agent 兼任多个职责。
4. 确认设计后，让有文件写入权限的 Agent 参考[模板](references/COUNCIL-TEMPLATE.md)，建立 `councils/<slug>/COUNCIL.md` 和 `MEMORY.md`，并更新[组织索引](registry/councils.md)。
5. 根据目标平台需要，将 Council 的必要规则和记忆组合成一个 Markdown Source 快照，导入对应的 GPT Add Sources。

### 2. 恢复工作 / 更新记忆

向 Agent 说：**“读取 education Council，整理新学习进度，按记忆规则更新，并告诉我需要重新导入哪些 Source。”**

Agent 应先读取目标 Council 的现有文件，区分已验证事实、待确认建议和历史决策，并依据[分级更新规则](shared/MEMORY-RULES.md)决定哪些可以直接记录、哪些需要你的确认。更新应保留历史与来源。

### 3. 同步 GitHub → GPT Add Sources

```text
已有 Council Source（GitHub 仓库中的 Markdown）
             ↓ 读取并确认差异
        修改对应 Council 文件
             ↓ 检查权限/隐私/冲突
        Git commit + push（需授权和工具支持）
             ↓ 导出新快照
       更新 GPT Add Sources（通常手动）
             ↓
       新对话按最新资料继续工作
```

**重要：GitHub push 不会自动刷新 GPT 的 Add Sources。** 仅当实际重新导入或替换时，GPT 才能使用相应的新快照。不要把仓库链接等同于平台支持的自动远程加载。

## 仓库导航

| 入口 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 仓库级 Agent 维护规则及安全边界 |
| [Council Designer / SKILL.md](skills/council-designer/SKILL.md) | Create / Update / Export / Sync 四种入口 |
| [Council 模板](references/COUNCIL-TEMPLATE.md) | 创建组织的最小结构 |
| [Council 目录](councils/README.md) | 每个 Council 的独立组织资料 |
| [Council Registry](registry/councils.md) | 已创建组织的目录和状态索引 |
| [Memory Rules](shared/MEMORY-RULES.md) | 分级记忆更新、历史与审批 |
| [Exports](exports/README.md) | GPT Add Sources 快照的导出约定 |

```text
council-sources/
├── README.md                         # 人和 Agent 的仓库入口
├── AGENTS.md                         # 仓库文件维护规范
├── skills/
│   └── council-designer/SKILL.md     # 唯一维护源（可发布副本到 Skills 仓库）
├── references/
│   └── COUNCIL-TEMPLATE.md           # 最小 Council 模板
├── shared/
│   └── MEMORY-RULES.md               # 共享的记忆更新规则
├── councils/
│   └── README.md                     # 各 Council 独立子目录
├── registry/
│   └── councils.md                   # 组织索引
└── exports/
    └── README.md                     # 导出快照说明
```

## 组织设计原则

1. **一个仓库、多个独立组织**：统一版本管理，但组织的使命、职责、任务和记忆不混在一起。
2. **按需分工**：职责不等于 Agent 数量。简单任务可由一个执行者承担，复杂或重复任务再专业化。
3. **自主运行、用户保留控制权**：Council 可以处理普通问题和日常分工，用户可介入调整，重要变化按权限确认。
4. **出现问题，再解决问题**：不为未知情况提前建立庞大部门和流程。
5. **共享的是必要信息，不是全部管理权限**：跨 Council 协作需明确访问和修改边界。
6. **项目资料有唯一维护源**：Council 不复制、替代其他项目的事实和成果。
7. **先核实再记忆**：历史记录可以复核和被替代，不能被当作永远正确的命令。

## 示例

- **Education Council**：长期管理学习方向；一个 Agent 可以先负责大纲、授课、练习和笔记，频率增加后再拆分职责。
- **Lattice Council**：协调软件产品、架构、工程与质量职能，引用现有代码库和项目文档，而非复制它们。
- **Research Council**：围绕研究问题组织调查、分析和审查，需要时与其他 Council 共享成果。

上述是**使用场景，不是已经创建或上线的组织**。真实的 Council 必须按需设计、登记并测试。

## 公开仓库与隐私

本仓库当前为 **Public**。所有提交的文件和 Git 历史都可能被公开访问。**不要上传** API Key、令牌、私人聊天原文、个人隐私、未授权第三方资料、商业机密或其他不应公开的记录。删除当前文件不等于从 Git 历史中抹除内容。未来若需要保存敏感记忆，优先使用私有仓库或把公开规则与私人记录分离。

`AGENTS.md`、`SKILL.md` 和 Markdown 目录**不会自动提供**文件写入、跨 Agent 通信、GitHub 同步或 GPT Source 修改权限；这些取决于实际接入的平台、工具和授权。

## 当前范围与状态

**V0.1 / Draft**：已设计最小创建、记忆更新、导出与 GitHub 同步规范；真实 GPT 导入、跨 Agent 协作、记忆更新全链路与用户体验仍需验证。完成技术检查不等于完成实际验收。

后续优先用一个真实 Council 验证闭环：创建 → 记录真实变化 → GitHub 更新 → 重新导出 → GPT 手动导入 → 新对话恢复，然后根据问题迭代。

## 贡献与使用

欢迎通过 GitHub Issues 提出问题、使用案例和改进建议。提交修改前请阅读 [AGENTS.md](AGENTS.md)，不要将测试数据误作真实组织历史。尚未确认开源许可证；在选择并添加 LICENSE 之前，不应假定仓库内容可以按任意开源许可再分发。
