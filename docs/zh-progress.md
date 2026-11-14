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
| `src/chap4.qmd` 第 4 章 决策 | 已译 | 同上；先前记的"12 个未闭合 `:::`"经核实是校验脚本误报，已更正（风格指南第 5 节第 15 条） |
| `src/chap5.qmd` 第 5 章 聚合、`src/chap6.qmd` 第 6 章 谁的？、`src/chap7.qmd` 第 7 章 结语 | 已译 | 同上（含代码示例解读、练习、讨论题、文献说明、延伸阅读） |
| 习题集 `src/psets/pset1.qmd`–`pset3.qmd`（`pset4.qmd` 上游为空文件） | 已译 | 嵌套站点项目 `src/psets/_quarto.yml`（`lang: zh`、`execute: eval: false`）；`title` 中文化；callout 标题统一为"代码"；`check-translation.py` ALL_OK |

| 讲义 `src/slides/chap0.qmd`–`chap6.qmd`（7 个 revealjs 讲稿，4,991 行） | 已译 | 逐行 1:1 替换（`scripts/apply-line-translations.py`，会核对每行的 `$…$` 多重集合与结构标记）；`check-translation.py` 全部 ALL_OK；`check-blocks.py` 全部平衡；逐章渲染成功，公式排版实测 chap1 179/179、chap2 132、chap3 140/140、chap4 273/273、chap6 77/77 |

习题集与讲义的构建注意：

- `src/psets/resources` 是指向 `../../resources` 的符号链接。主题 scss 按项目根相对路径引用字体，缺这个链接时 `quarto render` 会报 `lstat '.../src/psets/resources/fonts/et-book/roman-line-figures.ttf'`。
- CI 里逐个文件渲染（`for f in pset1 pset2 pset3; do quarto render "$f.qmd"; done`）。一次传入多个文档时输出会互相覆盖：实测 `quarto render pset2.qmd pset3.qmd` 后 `pset2.html` 内容变成 pset3。
- 讲义同理：`src/slides/_quarto.yml` 是嵌套项目（revealjs，输出 `_book/slides/`），主项目不渲染它；嵌套项目只认自己目录下的 `_extensions/`，所以 CI 在 `src/slides` 里再装一次 `coatless-quarto/pyodide`。
- 仓库里原本同时跟踪着两份过期快照 `src/slides/_extensions/coatless/pyodide/` 和 `src/slides/_extensions/coatless-quarto/pyodide/`（各 8 个文件，都缺 `qpyodide-monaco-editor-init.html`，而它们自带的 `qpyodide.lua` 会去读它）。CI 里 `quarto add` 只刷新后一份，渲染却选中前一份，于是报 `Error reading dependencies from .../qpyodide-monaco-editor-init.html`、退出码 83，连续三次构建同样失败；本地因用 Quarto 1.11 重装过扩展，反而不复现。修复：在 `zh` 分支删掉不会被刷新的那份（`git rm -r src/slides/_extensions/coatless`），保留由 CI 现装的那份。删除后本地 7 个讲稿全部渲染通过，CI 构建 `success`。

## 待做

无。原定范围（正文、前后 matter、习题、讲义）已全部译出并通过校验。
2. ~~决定是否修掉第 4 章那 12 个未闭合 `:::`~~ —— 经核实这个"缺陷"不存在：那是我写的校验脚本把四冒号围栏（`:::: algorithm`）误判成未闭合。脚本已改对，正文无需改动。

## 已完成的复查

- 用户报告的两处线上显示问题（已修复并验证）：
  1. **难度星号被吞**：第 2 章"题目按难度标注：() 入门，() 中等…"。根因是同一段里出现成对的 `*`，被 Markdown 当粗体标记消费掉（上游站点同样如此）。全仓扫描后确认只有这一处真正被吞：`src/chap2.qmd:1503`，已按第 1 章已有写法加反斜杠转义。标题里的 `(*)`、`(**)` 是孤立单个星号，实测渲染正常（在 `_book/src/chap1.html` 中可见"离散选择模型 (**)"），未改动。
  2. **公式全部显示成源码**：根因是 `_quarto.yml` 里上游手写的 MathJax 3 脚本与 Quarto 1.11 自带的 MathJax 4 同时加载，v4 组件报版本冲突后抛 `TypeError`，整页没有排版。删掉那行 v3 脚本后实测：第 1 章 625/625、第 2 章 232/232、第 3 章 323/323、第 6 章 166/166 处公式全部排版，控制台零报错（上游同页 550 处，本站此前为 0）。
- 顺带更正了两条我自己记错的结论（风格指南第 5 节第 8、15 条）：三个引用键其实都在 `references.bib` 里且能正常渲染（`pandoc` 把 `@key` 换成作者年份，按键名去 HTML 里搜自然搜不到，这是当初误判的原因）；第 4 章的"12 个未闭合 `:::`"是校验脚本把 `::::` 误当开框。
- 术语一致性复查（整站 + 习题集）：按风格指南第 4 节逐词统计主译名，发现 `Fisher information` 混用两种写法，已统一为表中的"费雪信息"（18 处，提交见 `git log`）。检查中发现习题里 `elicitation` 有 8 处译作"引出"，与正文的"征询"不一致，已统一为"征询"。另外 4 处"引出"是"由此引出…"这类普通动词用法，保留。人名按表执行：Bradley-Terry、Dwork、Sen、Lipschitz、Gumbel 保留拉丁，阿罗、博尔达、孔多塞、贝叶斯、汤普森、拉普拉斯用中文；"无限臂老虎机"是 infinite-armed bandit 的构词，不是"多臂老虎机"的另一种译法。
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

## 全站复查（译完之后的整站核对）

做法：本地按 CI 的顺序完整渲染一遍（正文 → 习题 → 讲义，顺序不能颠倒，根目录的 `quarto render` 会清空 `_book`），再用 `scripts/check-links.py` 解析 `_book` 里每个页面真实存在的 `<a>`/`<img>`/`<script>`/`<iframe>` 等标签，把相对路径按"原样 / 补 `.html` / 补 `/index.html`"三种写法逐一落点，`#锚点` 与全站收集到的 `id`/`name` 对照。当前结果：23 个页面、1762 条引用，站内引用全部解析通过，断链与失效锚点 0 条；指向上游 `mlhp.stanford.edu` 的 3 条是刻意保留的（首页两条说明"原著在这里"，`slides/chap0` 一条注明教材地址，旁边都给了本站译本链接）。

### 查出并已修的问题

1. **习题页顶栏 404**：`src/psets/_quarto.yml` 的两条导航写成 `.qmd`，嵌套项目解析不到，输出里原样保留 → 改指 `.html`。见风格指南第 5 节第 21 条。
2. **7 处失效引用**：上游 LaTeX 转 Markdown 留下的 `reference-type="ref"` 与 `[1.1](#fig-…)`，目标在两边都不存在。第 4 章 3 处改为真正的交叉引用（新增 `{#sec-interleaved-filter}`、`{#sec-pbo-setup}` 两个标签），1 处指向已有小节；第 5 章 3 处删掉失效编号、保留正文。见风格指南第 5 节第 20 条。
3. **我此前批量插译文时留下的重复与残句**：`src/chap5.qmd` 的"第 4 讲"计划被整段写了两遍（一份中文、一份英文），`src/psets/pset2.qmd` 一道小题的前两行重复，`src/psets/pset3.qmd` 有 3 行是跨行句子的英文后半句（`on the heatmap).`、`answer the following:`、`multi-objective case.`），`pset2` 另有 `normalization constant. …` 半句没并进去。这些行删掉或并入译文后，结构与上游重新对齐（重复是我造成的，不是上游的）。
4. **确实漏译的可见文字**：正文零散句子与整段（第 1 章 120 行那段追问、第 3 章"Visualize the results:"与 DPO 设定开头、第 6 章分配论文那句）、第 4 章 6 段伪代码的英文步骤（交错筛选、DBGD、在线 DPO、POP-BO、qTS、批量 qTS——它们后面的解释早就是中文了，中英夹着读不下去）、9 个标题（第 4 章 qEI/qTS 两个小节、第 5 章"对 RLHF 的含义"、第 7 章 4 个、习题 4 个"Question N: …"）。
5. `src/teaching.qmd` 里两段过期说明（说习题和讲义还没接进站点）已改成与现状一致的写法。

### 核对过、决定不改

- 参考文献与"延伸阅读"的条目、算法名（Sparring EXP4）、模型输入模板（`<bos><start_of_turn>user`）、被 HTML 注释包住的整段（第 4 章文末那个被上游移走的机器人基础模型案例，页面上不显示）。
- 讲义里有两处"第 2 章""第 4 章"章节号与实际不符（见第 5 节第 19 条），按原文照译。
- 全站没有 `site-url`，因此不生成 `sitemap.xml`、页面里也没有 `canonical`/`og:url`；上游同样如此，属于原站行为，不算译本缺陷。若要加，只需在 `_quarto.yml` 的 `website:` 下写 `site-url: "https://codingpracticegroup.github.io/mlhp/"`。

### 现在每次交付前跑的检查

```bash
python3 scripts/check-translation.py src/chapN.qmd   # 结构不变量
python3 scripts/check-blocks.py      src/chapN.qmd   # ::: 开合
python3 scripts/check-attributes.py                  # 提示框标题截断
python3 scripts/find-untranslated.py src/chapN.qmd   # 还没译的正文
# 整站核对（必须先渲染正文，再渲染习题、讲义）
export PATH="$HOME/.local/opt/quarto-1.11.9/bin:$PATH" QUARTO_PYTHON=/tmp/mlhpvenv/bin/python
quarto render --to html
(cd src/psets && for f in pset1 pset2 pset3; do quarto render "$f.qmd"; done)
(cd src/slides && for f in chap0 chap1 chap2 chap3 chap4 chap5 chap6; do quarto render "$f.qmd"; done)
python3 scripts/check-links.py                       # 逐条解析链接与锚点
```

`find-untranslated.py` 这次改严了：除了连续英文词数，还要求这一行里出现至少 3 个英文虚词，`IIA Gumbel Bradley Terry` 这类专名连排不再报出来；反过来说，它**报出的基本就是真要译的句子**。它也有看不见的地方——标题里的两个词（`### What Broke`）要靠单独扫标题才能抓到，所以扫标题这一步在 `check-links.py` 之外另跑了一次。

