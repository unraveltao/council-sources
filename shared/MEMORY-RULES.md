# Memory Rules — V0.1

## Ownership

每个 Council 拥有独立的记忆文件；仓库集中保存不代表其他 Council 有权管理其内容。项目原始文档留在原项目，Council 只保存引用与组织决策。

## Three update levels

- **Level 1 / Routine**：已核实的普通进度、会议摘要、一般问题记录。具有文件写入权限时可按授权自动记录。
- **Level 2 / Significant**：职责分工、工作流程、重要技术方案变化。先解释差异、影响与风险，等待用户确认（除非事先明确授予该范围自主权）。
- **Level 3 / Core**：使命、核心目标、根本权限、关键组织原则和用户确认的重大决策。必须取得用户明确授权。

## Evidence and history

每条重要记录尽量标记日期、来源、状态（confirmed/proposed/superseded）、影响范围与替代关系。旧记录不能自动充当永恒命令；不能凭猜测将任务、测试或同步记为完成。

## Synchronization

GitHub 仓库是 Markdown Source 的版本管理来源；GPT Add Sources 通常是导入时的快照。先更新仓库文件，检查变更后再按授权推送；需要更新 GPT 记忆时重新导出并手动导入。若远程发生冲突，停止覆盖并请求处理。
