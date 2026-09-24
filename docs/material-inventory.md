# 现有资料盘点

盘点日期：2026-09-24。来源工作区：PlotXY `velocity` 项目。此文档描述资料角色，不把本机路径写入可安装 Skill 的运行规则。

| 类别 | 主要材料 | 对 Skill 的作用 | 复用判断 |
|---|---|---|---|
| 原始参考资料 | 论文页、DOI、更正页、Source Data、作者 GitHub、作者 notebook、数据存放页、原始 panel 图 | 锁定论文/panel 身份，建立代码和数据证据链 | 高；每个新案例必须重新查证，不能复制旧案例结论 |
| 方法论 | `r-paper-figure-reproduction-bootstrap-v2.1.0` 的 workflow、scientific-data-contract、evidence-release、visual-audit、Rmd/HTML contract | 提供证据分级、fresh replay、视觉审计、报告语法等成熟做法 | 高，但旧版 R 优先和 runtime 规则已废止 |
| 现行规范 | 根目录 `AGENTS.md`、`workflow/plotxy_backend_standard.md` | 定义无 runtime、作者语言优先、最小交付树、参数链路和发布裁剪 | 最高；作为当前规则基线 |
| 报告模板 | Heatmap 案例的 CN/EN Rmd、HTML、CSS | 提供标题块、浮动目录、hero、四卡片、章节节奏、表格与图片顺序 | 高；复用页面语法，不复制 Heatmap 科学内容 |
| 项目案例 | projected velocity field、ternary cell-state probability、circular heatmap | 证明三种数据边界、参数化、prepare 条件、视觉修订与精简发布可行 | 最高；真实成功路径的主要来源 |
| 最终交付物 | 三个 release 目录及 ZIP | 观察最终文件树、入口、backend、evidence、双语手册和裁剪结果 | 高；文件树是角色目录，不是文件数量配额 |
| 中间过程文件 | working、superseded、fresh-extraction、截图、overlay、probe、release ledger | 解释错误如何被发现与修复 | 中；只提炼经验，绝大多数不进入用户 ZIP 或 Skill |
| 工具/脚本 | `new_case.py`、`audit_package.py`、`protected_manifest.py`、案例 main/plot | 固化脚手架、静态审计、模板完整性和主后端职责 | 高；脚本需有明确边界，不能代替科学/视觉判断 |
| Prompt/指令 | 历史对话修订、根 `AGENTS.md`、现有 Skill | 提供用户真实验收条件：命名、字号、标签方向、HTML 更新、最小文件 | 高，但对话中的单图数值必须去项目化 |
| 经验规则 | success-last、等像素比较、冻结科学层、参数全链路、相对路径 | 稳定操作原则 | 高；已被多个文件或案例验证 |
| 异常/踩坑 | 环形文字方向、中心重叠数字、HTML 旧图、超宽表、错误色值、浏览器缓存、无用 prepare | 形成视觉、文档和发布检查项 | 中到高；标注单案例或多案例证据强度 |

## 资料关系

旧 bootstrap 提供“为什么要证据化和审计”；现行规范决定“当前版本允许什么”；Heatmap 模板定义“报告长什么样”；真实案例证明“规则如何落地”；validation 和 superseded 目录解释“哪些看似合理的做法会失败”。核心 Skill 只保留执行者必须知道的顺序和判断，细节分流至 references、templates、examples 与 scripts。

## 可复用内容

- 来源优先级与分类；panel 到代码/数据对象的精确映射。
- Figure-ready 边界和 `prepare/` 条件。
- `main` 作为用户入口、`plot` 作为稳定后端的结构。
- 参数候选分组、全链路同步和失效范围。
- 当前运行证据、success-last、CLI/config replay。
- 等像素视觉比较、科学层冻结、重复失败后的几何测量。
- 双语报告的 Heatmap 页面语法与浏览器检查。
- 最小 ZIP、fresh extraction 和维护者验证外置。

## 仅属于单个项目的内容

- 具体基因、细胞状态、样本、panel 顺序和数值范围。
- 环形图某个扇区的角度偏移、中心数字坐标。
- ternary KDE 的具体 bandwidth、颜色和点数。
- velocity 输入的具体 H5AD 哈希、细胞数和字段名。

这些内容只保留在 examples 中作为判断示例，不能成为所有新项目的默认值。
