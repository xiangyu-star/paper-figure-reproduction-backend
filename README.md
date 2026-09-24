# Paper Figure Reproduction Backend Skill

这是一个面向 Codex 的可复用 Skill：根据论文、目标 panel、作者代码与可核验数据，制作不包含 runtime 的、可运行、可追踪、可解释、可审计的科学绘图后端交付包。

它不是从空白规范设想出来的。当前版本由 PlotXY 工作区中的旧版 bootstrap 方法、现行无 runtime 规范、Heatmap 报告模板，以及三个已完成案例反向归纳而成：投影 velocity field、ternary cell-state probability、circular heatmap。

## 安装

将仓库中的 `paper-figure-reproduction-backend` 目录复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force ".\paper-figure-reproduction-backend" "$env:CODEX_HOME\skills\paper-figure-reproduction-backend"
```

若未设置 `CODEX_HOME`，Windows 默认位置通常是：

```powershell
Copy-Item -Recurse -Force ".\paper-figure-reproduction-backend" "$HOME\.codex\skills\paper-figure-reproduction-backend"
```

复制后重启 Codex，或开启一个新任务。可用下面的提示触发：

> 使用 $paper-figure-reproduction-backend，复现【论文 DOI / 标题】的 Figure【panel】，优先使用作者代码和官方数据，并按 PlotXY 后端规范交付。

## 仓库结构

- `paper-figure-reproduction-backend/`：可直接安装的 Skill。
- `AGENTS.md`：在本仓库继续维护 Skill 时的约束。
- `docs/`：资料盘点、真实工作模式、设计说明、来源追踪、冲突与待确认项。

## 安全与边界

- 不生成或编辑科学图像来冒充代码复现。
- 不捆绑 runtime，只记录依赖和真实运行环境。
- 不把上游大型数据默认塞入发布包；优先交付最小、真实、可追踪的 Figure-ready 输入。
- 不因模板完整性虚构来源、参数、验证或成功状态。
- 受保护模板只能在维护者明确授权更新时修改；新项目必须复制后再适配。

## 维护者验证

```powershell
python "$env:CODEX_HOME\skills\.system\skill-creator\scripts\quick_validate.py" ".\paper-figure-reproduction-backend"
python ".\paper-figure-reproduction-backend\scripts\protected_manifest.py" verify ".\paper-figure-reproduction-backend\assets\protected-template"
```

项目交付包需另行运行：

```powershell
python ".\paper-figure-reproduction-backend\scripts\audit_package.py" "<case-directory>"
```

## 版本原则

项目实践优先，但每条关键规则必须标明证据强度。旧方法与新实践冲突时，不默默合并；当前选择及理由记录在 `docs/conflicts-and-decisions.md`。
