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
| `src/chap4.qmd` 第 4 章 决策 | 已译 | 同上；原文 12 个未闭合 `:::` 保持原样（见风格指南第 5 节第 15 条） |
| `src/chap5.qmd` 第 5 章 聚合、`src/chap6.qmd` 第 6 章 谁的？、`src/chap7.qmd` 第 7 章 结语 | 已译 | 同上（含代码示例解读、练习、讨论题、文献说明、延伸阅读） |
| 习题集 `src/psets/pset1.qmd`–`pset3.qmd`（`pset4.qmd` 上游为空文件） | 已译 | 嵌套站点项目 `src/psets/_quarto.yml`（`lang: zh`、`execute: eval: false`）；`title` 中文化；callout 标题统一为"代码"；`check-translation.py` ALL_OK |

习题集的两处构建注意：

- `src/psets/resources` 是指向 `../../resources` 的符号链接。主题 scss 按项目根相对路径引用字体，缺这个链接时 `quarto render` 会报 `lstat '.../src/psets/resources/fonts/et-book/roman-line-figures.ttf'`。
- CI 里逐个文件渲染（`for f in pset1 pset2 pset3; do quarto render "$f.qmd"; done`）。一次传入多个文档时输出会互相覆盖：实测 `quarto render pset2.qmd pset3.qmd` 后 `pset2.html` 内容变成 pset3。

## 待做

1. 讲义 `src/slides/*.qmd`：在 CI 里生成，使 `/slides/chapN.html` 存在，再把 `src/teaching.qmd` 里的讲义链接改成相对路径。（不在原定目标范围内，属于额外工作，未开工。）
2. 决定是否修掉 `src/chap4.qmd` 中上游那 12 个未闭合的 `:::`（风格指南第 5 节第 15 条），这属于有意偏离原文，需要你先确认。

## 已完成的复查

- 术语一致性复查（整站 + 习题集）：按风格指南第 4 节逐词统计主译名，未发现同一概念两个译名。检查中发现习题里 `elicitation` 有 8 处译作"引出"，与正文的"征询"不一致，已统一为"征询"（提交 `zh: 术语统一——习题中的 elicitation 改为与正文一致的"征询"`）。另外 4 处"引出"是"由此引出…"这类普通动词用法，保留。人名按表执行：Bradley-Terry、Dwork、Sen、Lipschitz、Gumbel 保留拉丁，阿罗、博尔达、孔多塞、贝叶斯、汤普森、拉普拉斯用中文；"无限臂老虎机"是 infinite-armed bandit 的构词，不是"多臂老虎机"的另一种译法。
- 结构与不变量：15 个文件逐个跑 `check-translation.py`，`license`/`chap4–7`/`notation`/`teaching`/`pset1–3` 全部 ALL_OK；`index`、`chap1`、`chap2`、`chap3`、`glossary` 显示 HAS_DIFF，差异全部对应风格指南第 5 节已登记的条目（第 2、9、10、12 条），无新增偏离。
- 整站渲染：`.github/workflows/render-zh.yml` 对分支 `zh` 的最新提交 `0d8f619` 构建并部署成功（`gh run watch 43465352846 --exit-status` 退出码 0）。线上已核对：首页、`src/chap4.html`、`src/chap7.html`、`src/psets/pset2.html`、`src/psets/pset3.html` 均返回 200 且标题为中文；`src/teaching.html` 的习题链接指向相对路径 `psets/psetN.html`。


## 已放弃的旧条目

下面几条在早期阶段列过，现已完成，保留说明以便对照：

1. `src/chap4.qmd` 第 4 章 决策——已完成。这一章文末一大段 HTML 注释（被移走的机器人基础模型案例）按规则不译。
2. `src/chap5.qmd`／`src/chap6.qmd`／`src/chap7.qmd`——已完成，见上表。
3. 习题集接进构建与 CI、`src/teaching.qmd` 的链接从上游地址改回本地路径——已完成（`psets/psetN.html`）。

## 每译完一段要跑的检查

```bash
python3 scripts/check-translation.py src/chapN.qmd   # 标题、公式、代码、引用键、标签、短代码……
python3 scripts/check-blocks.py     src/chapN.qmd    # ::: 开合序列与上游逐一对齐
python3 scripts/find-untranslated.py src/chapN.qmd   # 还没译的正文（跳过代码、公式、注释，会有少量误报）
python3 scripts/find-english.py     src/chapN.qmd    # 同上，按行段列出，粗一些
python3 scripts/check-attributes.py                  # 提示框标题等属性是否会被截断
```
