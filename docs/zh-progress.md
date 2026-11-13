# 中文译本进度

翻译分支：`zh`（`main` 只作上游镜像，不把翻译并进 `main`）。
站点：https://codingpracticegroup.github.io/mlhp/ （由 `.github/workflows/render-zh.yml` 在每次推送到 `zh` 时构建并发布）。

翻译的原则、术语表和自查方法见 [`zh-style-guide.md`](zh-style-guide.md)。

## 已完成

| 文件 | 状态 | 校验 |
|---|---|---|
| `index.qmd`（引言）、`src/glossary.qmd`、`src/notation.qmd`、`src/teaching.qmd`、`license.qmd` | 已译 | `check-translation.py` 通过，偏差已登记 |
| `src/chap1.qmd` 第 1 章 基础 | 已译 | 同上 |
| `src/chap2.qmd` 第 2 章 学习 | 已译 | 同上 |
| `src/chap3.qmd` 第 3 章 偏好征询 | 已译 | 同上；`:::` 结构与原文逐一对齐 |

## 待做

1. `src/chap4.qmd` 第 4 章 决策——进行中（正文大部分已译）。已译：开头（学习目标、课时安排、本章内容安排、问题设定）、"不确定条件下的奖励最大化问题"、"线性/非线性目标下的汤普森采样"、"对决老虎机"（从多臂到对决、形式化模型与两条比较公理、遗憾、"胜者"的概念、均匀/ε-贪心/UCB、交错筛选、DBGD、Sparring EXP4、Feel-good 汤普森采样、算法选择要点、应用两例）、"偏好型贝叶斯优化"（问题描述、科佩兰与软科佩兰、采集函数：纯粹探索/POP-BO/qEUBO/qEI、遗憾分析与各核收敛速率）、"面向偏好优化的强化学习基础（选学）"的开头与 MDP 定义、"快问快答/讨论题/延伸阅读/必读文献"、本章要点各框。
   待译：同节剩余部分——"价值函数与优势""策略梯度定理""从 RLHF 到 GRPO""联系"；"人机协作与 CIRL"整节（含"教学还是示范""选择架构"）；"本章小结"；"练习"（基础/进阶/高级三档）。
   注意：这一章原文有 12 个未闭合的 `:::` 框（见风格指南第 5 节第 15 条），校验脚本会报"收尾 12 层"，基线也一样，翻译时保持结构不动；文末一大段 HTML 注释（被移走的机器人基础模型案例）按规则不译。
   注意：这一章原文有 12 个未闭合的 `:::` 框（见风格指南第 5 节第 15 条），校验脚本会报"收尾 12 层"，基线也一样，翻译时保持结构不动。
2. `src/chap5.qmd` 第 5 章 聚合——进行中（正文与后记标题大部分已译）。已译：标题、学习目标、课时安排、内容安排；社会选择理论（SWF/SCF 定义、四种投票规则、孔多塞悖、阿罗三条公理、完整算例、阿罗不可能定理及其证明思路、两个常见坑框、吉巴德—萨特斯维特、对 AI 对齐的影响）；绕开不可能性（单峰偏好定义与适用边界、广义中位投票者机制、穆林定理）；计分规则与博尔达—DPO 的关系（博尔达/软科佩兰定义、IIA′、博尔达性质定理、博尔达与 DPO 等价性定理与失效情形、证明要点）；多议题投票与可分偏好；"管得宽"的偏好与森的自由悖论（含清道夫例子）；Community Notes 案例；反演问题；隐私与个性化；家长主义；机制设计（拍卖、第二价格、Myerson 最优拍卖与保留价算例、Bulow–Klemperer、VCG 及落地困难、频谱拍卖、同伴互评案例、互信息范式）；本章小结、快问快答、后记各标题。
   待译：激励相容的在线学习案例正文（模型扩展四条、guinea pig 激励分析段）、讨论题、文献说明、延伸阅读、练习 1–10 的题干。
3. `src/chap6.qmd` 第 6 章 谁的偏好（约 591 行正文待译）、`src/chap7.qmd` 第 7 章 结语。
3. 习题集 `src/psets/pset1–3.qmd`：加中文标题、`execute: eval: false`，接进构建与 CI，并把 `src/teaching.qmd` 的链接从上游地址改回本地路径。
4. 讲义 `src/slides/*.qmd`：在 CI 里生成，使 `/slides/chapN.html` 存在，再把 `src/teaching.qmd` 里的讲义链接改成相对路径。
5. 全书整站渲染、术语一致性复查、确认线上部署。

## 每译完一段要跑的检查

```bash
python3 scripts/check-translation.py src/chapN.qmd   # 标题、公式、代码、引用键、标签、短代码……
python3 scripts/check-blocks.py     src/chapN.qmd    # ::: 开合序列与上游逐一对齐
python3 scripts/find-untranslated.py src/chapN.qmd   # 还没译的正文（跳过代码、公式、注释，会有少量误报）
python3 scripts/find-english.py     src/chapN.qmd    # 同上，按行段列出，粗一些
python3 scripts/check-attributes.py                  # 提示框标题等属性是否会被截断
```
