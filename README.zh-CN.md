# Council Sources

[English](README.md) | [简体中文](README.zh-CN.md)

这里保存 [Council Designer v1.0.0](skills/council-designer/README.md) 和早期版本生成的 Council Sources 文档。Council Designer 可以独立于本仓库使用，帮助你设计由人主导的 Agent 组织，并维护组织规则和组织记忆。

## 开始使用 Council Designer

1. 在支持 Skills 的宿主中加载 [SKILL.md](skills/council-designer/SKILL.md)，或把完整文本作为上下文提供给 Agent。
2. 描述目标和约束。如果已有组织，请提供组织文档或可访问的源文本。
3. 请求设计（Design）、审查（Review）、更新（Update）或导出（Export），并指出你已经批准的决定。

> 为每周主题回顾设计一个小型研究 Council。如果一位执行者足够，就复用同一位执行者。范围和共享事项由我审批。请给出一份 Markdown 草稿，并标明待决事项。

采纳前可以先审阅设计。更新时会收到一份完整的 Markdown 修订稿，内含简短的变更摘要，并保留被替代决策的必要上下文。

## 组织与权限

Council 定义职责与交接关系。一位执行者可以承担多个角色。各 Council 的权限和组织记忆保持独立，Project 仍是需求、代码和交付物的权威来源。用户保留是否采纳文档及重大决策的最终决定权。

Council Designer 按情境使用 QD、Checkpoint 和 Review。输出默认留在对话中，由你选择保存位置。Skill 无需 Registry、固定仓库结构、数据库、Agent 创建机制、同步服务或长期记忆集成。

## 仓库导航

| 入口 | 用途 |
| --- | --- |
| [Council Designer 使用指南](skills/council-designer/README.md) | 四种模式、示例、交互标记和审批级别 |
| [Council Designer Skill](skills/council-designer/SKILL.md) | V1.0 的自包含行为规范 |
| [旧版 Council Sources 指南](docs/COUNCIL-SOURCES-LEGACY.md) | V0.3.0 仓库流程、早期模板和实例、导出与证据 |
| [仓库操作规则](AGENTS.md) | 本仓库的贡献、隐私、授权与验证规则 |
| [V1.0 验收用例](tests/V1-ACCEPTANCE-TESTS.md)和[结果](tests/V1-TEST-RESULTS.md) | 当前 Skill 的验证和剩余测试范围 |

## 验证与贡献

V1.0 的静态检查与行为验收分别记录。真实 V1.0 交互用例为 **Not Run（未运行）**。旧版仓库流程有自己的 [V0.3.0 验证记录](tests/TEST-RESULTS.md)。

贡献前请阅读 [AGENTS.md](AGENTS.md)。核对所涉版本的说明，并保留版本证据、用户授权和私有内容边界。
