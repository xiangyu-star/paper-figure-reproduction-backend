# 核心规则来源映射

证据标签：`明确规定`、`多项目验证`、`单项目经验`、`归纳建议`、`待验证`。

| Skill 规则 | 来源材料/项目 | 章节或证据 | 验证级别 | 备注 |
|---|---|---|---|---|
| 作者语言优先 | 根 `AGENTS.md`；现行 workflow；三个 Python 案例 | Required workflow 1；各 main/plot | 明确规定 + 多项目验证 | 取代旧 bootstrap 的 R 优先 |
| 不捆绑 runtime | 根 `AGENTS.md`；现行 workflow | repository rules；目标/交付树 | 明确规定 | 取代 v2.1 runtime 内容 |
| 锁定论文、DOI、panel、commit、对象 | 现有 Skill refs；三个 source manifest | source-discovery；manifest | 多项目验证 | 更正页也必须检查 |
| 五类来源标签 | 现行 AGENTS；circular/ternary manifest | AUTHOR_EXACT 等 | 明确规定 + 单项目扩展 | `AUTHOR_DERIVED` 来自 circular |
| 先写科学合同再绘图 | bootstrap scientific-data-contract；现有 Skill | contract workflow | 明确规定 | 防止视觉猜测进入科学值 |
| 最小 Figure-ready 输入 | 现行 workflow；velocity、ternary、circular | input boundary | 多项目验证 | 大数据不默认交付 |
| prepare 条件式存在 | 现行 workflow；ternary vs circular/velocity | package trees | 多项目验证 | 是否需要上游重建是判断条件 |
| main/plot 双层结构 | 现行 workflow；三个案例 | main/plot code | 多项目验证 | main 用户入口，plot 稳定 backend |
| 七类参数候选 | 现行 AGENTS/workflow；案例 main | parameter groups | 明确规定 + 多项目验证 | 不要求每类都一定有参数 |
| 参数全链路 | 现有 Skill style-and-parameters；contracts | main→config→backend→resolved→docs | 多项目验证 | 新参数缺任一环即未完成 |
| 三类失效范围 | 现行 workflow；ternary/velocity contract | invalidation | 多项目验证 | rerender/recompute/rebuild |
| success marker 最后写 | bootstrap evidence-release；案例 plot | run backend | 多项目验证 | 失败先删除旧 success |
| current-run evidence | bootstrap evidence-release；三个 example_output | run manifests/logs | 多项目验证 | 旧输出不能继承 PASS |
| 等像素视觉审计 | bootstrap visual-audit；环形图修订 | generated/reference comparison | 明确规定 + 单项目强化 | full view + critical crops |
| 两轮失败后测量几何 | bootstrap visual-audit；circular 标签修订 | pixel/anchor fixes | 单项目经验 + 方法规定 | 避免无限目测微调 |
| 视觉修复冻结科学层 | bootstrap；现行 AGENTS | visual-only fixes | 明确规定 | 不改值、顺序、筛选 |
| 环形标签专门规则 | 现行 AGENTS；circular case | upright genes、arc-mid category | 单项目验证 | 可迁移到 circular plot family |
| Heatmap 报告语法 | key_template_heatmap；三案例 Rmd/HTML | hero/cards/TOC/section rhythm | 多项目验证 | 复用样式，不复制科学内容 |
| Rmd 只读证据 | 现行 AGENTS；案例 Rmd | setup and evidence chunks | 多项目验证 | 不重跑昂贵分析 |
| 生成图先于参考图 | bootstrap Rmd contract；案例 | Figure preview | 多项目验证 | 便于审计当前输出 |
| 浏览器检查 HTML | bootstrap Rmd contract；circular 修订 | clipping/stale image | 单项目经验 + 明确规定 | Knit 成功不等于布局合格 |
| 最小 ZIP | 现行 AGENTS；三 release；validation 残留 | release trimming | 多项目验证 | 内部 QA 留在 validation |
| fresh extraction | bootstrap evidence-release；validation fresh dirs | replay | 明确规定 + 多项目验证 | COMPLETE 发布门 |
| 受保护模板只由维护者更新 | 根 AGENTS；protected manifest | authorization + SHA-256 | 明确规定 | 案例总是复制后适配 |
| 合法 cyan 为 `#65D1CF` | 根 AGENTS；当前案例代码 | palette validation | 已验证修正 | `#65D1CP` 无效 |

## 主要来源材料定位

- 当前规则：工作区根 `AGENTS.md`、`workflow/plotxy_backend_standard.md`。
- 旧方法论：`references/bootstrap_v2_spec/skill/r-paper-figure-reproduction/references/`。
- 报告样式：`references/key_template_heatmap/heatmap_2024_NatureImmunology_Fig2a_r/`。
- 成功案例：`deliveries/release/` 下的 projected velocity、ternary、circular heatmap。
- 过程证据：`deliveries/validation/` 的 fresh extraction、superseded package、截图和对比物；浏览器 profile/cache 仅是偶发残留，不是方法资产。

未来将本仓库独立迁移后，应把新增规则的上游文件、版本、哈希和验证案例继续追加到此表，不得只写“经验表明”。
