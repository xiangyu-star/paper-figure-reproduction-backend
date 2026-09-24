# 从真实项目反推的工作模式

## 最终目标

把“复现某论文某图”的请求转化为一个紧凑的科学绘图后端：作者来源可追踪，科学输入诚实，日常入口可运行，参数可选但不破坏科学含义，输出和验证属于当前版本，CN/EN 手册可读，最终 ZIP 无 runtime 和维护者残留。

## 使用前输入

最低输入为论文标题或 DOI、figure/panel、可用参考图。理想输入还包括作者仓库/notebook、数据链接或本地文件、用户允许的视觉适配、目标语言和交付状态要求。缺少 panel 身份或关键科学定义时不得进入绘图实现。

## 标准阶段

| 阶段 | 目标 | 关键判断 | 固定输出 |
|---|---|---|---|
| 1. 身份锁定 | 消除“复现哪张图”的歧义 | 是否存在更正；panel 是否为复合图；用户图是否经过裁剪/修改 | case identity、task class、初始状态 |
| 2. 来源发现 | 找到最权威的代码和数据 | 作者代码是否直接生成 panel；数据是否公开；版本能否锁定 | source map、manifest 草稿 |
| 3. 科学合同 | 固定不能靠视觉猜测的内容 | 哪些是作者精确、作者推导、公开重建、样式参考、用户修改 | schema、映射、变换、顺序、随机性、限制 |
| 4. 输入边界 | 制作最小诚实的 Figure-ready 输入 | routine 是否需要大型数据；用户是否需要从上游重建 | compact input；条件式 prepare |
| 5. 后端实现 | 建立稳定入口和可重放后端 | 参数影响重绘、科学重算还是输入重建 | main、plot、contract、resolved config |
| 6. 执行证据 | 证明当前代码真的运行 | main 与 CLI/config 是否一致；失败时是否残留 success | 图、统计、validation、manifest、log、success-last |
| 7. 视觉审计 | 对齐构图、文字、图例和层次 | 差异是科学层还是显示层；两次目测修订是否仍失败 | 等像素对比、必要的几何测量、视觉结论 |
| 8. 报告 | 让用户能理解和调用 | CN/EN 是否对称；HTML 是否展示最新图且无截断 | Rmd、HTML、CSS、依赖与环境记录 |
| 9. 发布 | 只交付必要内容 | fresh copy 是否可运行；是否混入缓存、runtime、内部 QA | audit、fresh replay、最小 ZIP、SHA-256 |

## 固定动作与灵活动作

固定动作包括身份锁定、来源分类、科学合同、相对路径、main/plot 分工、参数全链路、当前执行证据、等像素比较、CN/EN 对称、静态审计和 success-last。

灵活动作包括作者语言、Figure-ready 格式、绘图库、是否保留 prepare、参数数量、统计输出、reference 来源、视觉容差以及 docs 是否合并。灵活不等于任意：每项都由来源、科学边界、用户需求或可验证结果决定。

## 完成标准

只有以下条件同时满足才可标记 `COMPLETE`：panel 身份明确；关键对象有来源映射；routine input 可读且通过硬验证；main 和 backend replay 均在当前版本成功；contract 与 resolved 参数一致；PNG/PDF 和证据非空；生成图与参考图完成等像素审计；CN/EN HTML 当前且可读；发布审计和 fresh extraction 通过；最终 ZIP 只含必要文件并记录哈希。

某个 gate 未运行时必须记录 `not_run`，并使用较低状态，不得用“看起来能运行”代替证据。

## 最常见错误

- 先画图后查来源，导致科学对象和 panel 映射返工。
- 把样式相似误写成作者精确复现。
- 为“完整”捆绑大型矩阵、runtime、notebook 或无用 preparation。
- 参数只出现在 `main`，没有进入 backend、resolved evidence、contract 和手册。
- 用改变排序、数值或筛选来掩盖标签重叠。
- 只看生成图，不与原图等像素并排；环形标签方向尤其容易错。
- 更新 PNG 后没有重新 Knit，HTML 仍显示旧图或文字溢出。
- 把浏览器 profile、截图、overlay、probe 和 release ledger 塞入用户 ZIP。
- 在未 fresh replay 的情况下宣称发布完成。

## 文档与实践的差异

- 旧 bootstrap 偏好 R，真实案例证明应保留作者语言；当前规范已改为作者语言优先。
- 旧 bootstrap 包含 offline runtime，当前交付明确禁止 runtime。
- 旧清单倾向固定文件集合，真实案例显示目录是角色合同，`prepare/` 和部分 docs 应按信息是否真实需要决定。
- 理论文档强调视觉检查，环形图实践进一步证明：文字方向、弧中点、字号、中心数字和 HTML 缓存必须作为独立检查对象。
