---
name: council-designer
description: Design, create, update, and export independent Council organizations with Markdown memory and optional GitHub sync.
---

# Council Designer — V0.1

## Purpose

将用户的项目或领域目标转化为独立、可维护的 Council 组织。Council 负责组织与协调工作，而不是替代项目本身的文档或强迫多 Agent 分工。

## Entry routing

先判断用户意图，不要求用户使用固定命令：

- **Create**：建立一个新的 Council，明确使命、职责、权限、协作机制并生成文件。
- **Update**：读取现有 Council 记忆，整理实际变化、区分更新等级，提出或执行修改。
- **Export**：合成供 GPT Add Sources 导入的 Markdown 快照，并标注版本与来源。
- **Sync**：在工具允许且用户授权后提交、推送到 GitHub。不得把仓库推送等同 GPT 知识源更新。

## Create workflow

1. 快速厘清目标、组织服务的项目/领域、主要任务与预期成果。
2. 只有对设计有影响的不确定性才追问；每轮尽量只问一个关键问题。用户已确定的事项不反复追问。
3. 动态分配职责：任务简单可由一个 Agent 兼任多职；高频、复杂或需独立审查时再拆分。
4. 明确用户保留的决策权、对外操作权限、跨 Council 访问边界。
5. 区分 Council 组织记忆和 Project 的原始资料，明确引用关系与唯一可信来源。
6. 汇总设计、验收标准和待确认事项，用户确认后才写文件；若环境无法写入，则生成可复制文件内容。
7. 在 councils/<slug>/ 使用模板创建 COUNCIL.md 与 MEMORY.md，更新 registry/councils.md。
8. 按需要执行 Export / Sync，并如实记录成功与否。

## Update workflow

1. 先读取现有 Council 文件及相关项目资料，找出当前有效的决策与状态。
2. 比较新信息与旧记录，区分事实、假设、建议和被取代的决策。
3. 按 shared/MEMORY-RULES.md 分类：普通更新自动处理（仅在有写入权限时），重要/核心变化请求确认。
4. 只修改目标 Council 的文件，保留必要的历史与来源；更新后检查目录、引用和冲突。
5. 可按用户授权生成新 Source 快照、同步 GitHub，并提醒需要手动重新导入 Add Sources。

## Interaction and limitations

- 遇到与主线无关的独立新任务，先提示当前主线及阶段，询问是否切换；相关延伸无需打断。
- 用户可以介入或覆盖普通职责分配；遇到高风险操作或未授权外部访问必须征求确认。
- 不得虚构工具权限、Agent 间通信、自动 GitHub 同步或 Add Sources 更新。
- Local/Remote 描述 Skill 的加载或存储位置，不代表不同执行能力；各平台需实际验证如何加载该 SKILL.md。
- 用户亲自使用并明确确认预期效果后，才可以说该 Council 已完成验收。
