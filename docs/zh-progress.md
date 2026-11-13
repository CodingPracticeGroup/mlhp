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

1. `src/chap4.qmd` 第 4 章 决策——进行中。已译：开头（学习目标、课时安排、本章内容安排、问题设定）、"不确定条件下的奖励最大化问题"、"线性/非线性目标下的汤普森采样"、"对决老虎机"（从多臂到对决、遗憾、"胜者"的概念、采集函数中的"均匀采样 / ε-贪心 / UCB"）。待译：交错筛选（Interleaved Filter）及其后的对决老虎机算法与应用、"偏好型贝叶斯优化"、"强化学习基础（选学）"、合作逆强化学习，以及本章小结与练习。
   注意：这一章原文有 12 个未闭合的 `:::` 框（见风格指南第 5 节第 15 条），校验脚本会报"收尾 12 层"，基线也一样，翻译时保持结构不动。
2. `src/chap5.qmd` 第 5 章 聚合、`src/chap6.qmd` 第 6 章 谁的偏好、`src/chap7.qmd` 第 7 章 结语。
3. 习题集 `src/psets/pset1–3.qmd`：加中文标题、`execute: eval: false`，接进构建与 CI，并把 `src/teaching.qmd` 的链接从上游地址改回本地路径。
4. 讲义 `src/slides/*.qmd`：在 CI 里生成，使 `/slides/chapN.html` 存在，再把 `src/teaching.qmd` 里的讲义链接改成相对路径。
5. 全书整站渲染、术语一致性复查、确认线上部署。

## 每译完一段要跑的三条命令

```bash
python3 scripts/check-translation.py src/chapN.qmd   # 标题、公式、代码、引用键、标签、短代码……
python3 scripts/check-blocks.py     src/chapN.qmd    # ::: 开合序列与上游逐一对齐
python3 scripts/find-english.py     src/chapN.qmd    # 还没译的正文行段
```
