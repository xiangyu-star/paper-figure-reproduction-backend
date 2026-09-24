# 待确认项与后续沉淀

## 当前资料不足，待确认

- R 语言案例尚未完成与 Python 案例同等强度的真实发布验证；`main.R`/`plot.R` 角色已定义，但错误处理和证据原子写入仍需真实案例测试。
- 不同图类的视觉容差没有一个可通用的数值阈值；当前必须记录图类相关的检查，而不能用单一像素分数决定 PASS。
- 出版者图片的再分发许可需按论文逐案确认；Skill 只能要求记录来源与用途，不能统一断言可以随 ZIP 发布。
- HTML 自包含在超大参考图下的体积上限尚未统一；目前以浏览器可用性和发布需求判断。
- `APPROXIMATE_PUBLIC_RECONSTRUCTION` 在何种视觉差异下仍可接受，需要更多公开重建案例。

## 值得模板化

- 常见图类的参数候选表：scatter、heatmap、ternary、circular、vector field。
- source manifest 与 backend contract 的 JSON Schema。
- CN/EN 章节 parity 自动检查。

## 值得脚本化/自动化

- main 与 CLI/config 输出哈希对比。
- 证据文件时间戳和输入/代码哈希一致性检查。
- HTML 中缺图、溢出表格、旧图片引用和绝对路径扫描。
- fresh extraction、运行、Knit、静态审计、ZIP 和 SHA-256 的单命令发布脚本。
- reference/generated 的关键 crop 配置与像素锚点测量。

## 值得增加的测试

- 一个完整 R 案例。
- 一个 `PUBLIC_RECONSTRUCTION` 成功案例和一个因关键算法缺失而 `BLOCKED` 的案例。
- Windows、macOS、Linux 的字体替代与路径测试。
- 环形文字、长图例、极宽表格、小 panel 的视觉回归测试。

## 值得加入的新 reference

- 论文更正/撤稿与 panel 影响判断。
- 数据许可和参考图再分发边界。
- 不同随机算法的可复现记录方式。
- 复合 figure 的分层审计方法。
