# Repository Agent Rules

适用于使用工具读取、创建、修改本仓库文件的 Agent。这里是仓库管理规范，不是管理各个 Council 日常业务的上级组织。

## 工作前

1. 阅读 README.md、目标 Council 的 COUNCIL.md / MEMORY.md 以及 shared/MEMORY-RULES.md。
2. 确认用户此次目标：创建、更新、导出、同步，还是审查。
3. 明确工作范围，只修改被授权的目录与文件；不要把不同 Council 的记忆混在一起。
4. 若对应项目已有 PRD、课程、笔记、任务或架构文档，尽量引用链接，禁止未经请求复制一整套项目知识。

## 创建 Council

- 先定义使命、边界、职责与授权；一人可兼任多个职责，严禁为了形式虚构多个 Agent。
- 复制 references/COUNCIL-TEMPLATE.md 为 councils/<slug>/COUNCIL.md，并补齐必要的 MEMORY.md。
- 更新 registry/councils.md 索引。
- 不擅自引入统一组织的业务指挥链；跨 Council 协作需明确请求与授权。

## 更新记忆

- 按 shared/MEMORY-RULES.md 分级。不得未经用户批准修改核心目标、组织使命和已确认的重大决策。
- 写入前检查现有文件，保留决策来源、状态、时间与替代关系；区分事实、假设、建议。
- 只在有真实证据时标记任务完成、测试通过或同步成功。
- 变更尽量小，检查 Markdown 引用、相对路径、索引、冲突与版本历史。

## GitHub 同步

- 本仓库为 public：任何提交前都要审查隐私、秘密及不适合公开的记忆，不能因已获写入许可就默认所有内容可公开。
- 同步前检查远程变更与冲突；不得 force push 或使用破坏性重置。
- 只有获得用户对远程写入的授权，且工具实际支持，才执行 commit / push；反馈真实 commit SHA 或阻碍原因。
- 生成 Add Sources 快照后，明确提示用户：GitHub 更新不会自动修改 GPT 中已导入的副本。

## 工作完成

给出修改摘要、受影响文件、验证情况、尚未完成的手动步骤。禁止宣称未发生的 Agent 协作、执行或测试。
