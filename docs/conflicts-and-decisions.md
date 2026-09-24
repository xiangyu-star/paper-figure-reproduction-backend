# 冲突、版本与当前决策

| 冲突 | 旧做法 | 新实践/证据 | 当前决策 | 置信度 |
|---|---|---|---|---|
| 实现语言 | bootstrap 默认优先 R | 三个案例均沿用作者 Python 路径；现行规范要求作者语言 | 保留作者支持语言；只有用户明确要求时翻译 | 已有资料明确规定 + 多项目验证 |
| runtime | v2.1 包含 offline runtime | 当前 AGENTS 与交付规范明确不包含 runtime | Skill 和 case ZIP 均不捆绑 runtime | 已有资料明确规定 |
| 来源分类 | 旧核心类缺少 `AUTHOR_DERIVED` | circular heatmap 的 Figure-ready TSV 可追溯地从作者对象推导 | 增加 `AUTHOR_DERIVED`，并要求写出变换与哈希 | 单项目验证 + 资料归纳 |
| prepare | 模板树容易让人默认创建 | ternary 需要重建大型数据；circular 和 velocity routine 不需要 | 仅当用户需要从昂贵/大型上游重建时保留 | 多项目共同验证 |
| 报告章节 | bootstrap 规定严格章节序列 | circular 案例按语义合并接口与输出章节仍可用 | 必须保持 Heatmap 页面语法和 CN/EN 对称；章节可做有依据的语义合并 | 多项目验证；需继续测试 |
| CSS | 旧文本偏向字节级复制 | 案例需要少量图宽/页面修正 | 受保护 base CSS 不改；只允许窄范围、记录过的追加覆盖 | 已有资料 + 单项目经验 |
| 状态名 | 现有 Skill 有固定状态；circular 使用 `PLOT_READY_COMPLETE` | 状态词不统一 | 新项目只用标准状态；`PLOT_READY_COMPLETE` 作为 legacy alias，不再生成 | 资料归纳建议 |
| manifest | 旧 release 清单部分文字暗示删除 manifest | 当前三个案例都依赖 source/run manifest | 保留 `source_manifest.json` 与当前 run manifest | 多项目共同验证 |
| fresh extraction | 理论规范要求发布前 fresh replay | 个别赶工轮次只做静态检查 | 对公开发布的 `COMPLETE` 强制 fresh replay；未运行必须降级并标 `not_run` | 已有资料明确规定 |
| 色板 | 历史输入出现无效 `#65D1CP` | 当前规范和代码均使用 `#65D1CF` | 只允许合法色值；PlotXY 适配标 `USER_MODIFIED_BASELINE` | 已验证修正 |

无法由当前材料决定的事项保留在 `pending-and-roadmap.md`，不伪造统一答案。
