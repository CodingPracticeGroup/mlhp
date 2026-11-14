# 简体中文翻译规范与术语表

这份文件只服务于 `zh` 分支的翻译工作，不是书的内容。它有两个用途：一是把翻译尺度写成可执行的规则，二是给出全书统一的术语译法，避免同一概念在不同章节换说法。审阅译文时，请以此为标准。

适用范围：`index.qmd`、`src/chap1.qmd`–`src/chap7.qmd`、`src/teaching.qmd`、`src/notation.qmd`、`src/glossary.qmd`、`license.qmd`，以及后续的 `src/psets/*.qmd` 与 `src/slides/*.qmd`。

## 1. 翻译尺度

目标读者是本科一年级学生，所以可读性优先，但不以牺牲准确为代价。可执行的规则如下。

1. **句子短**。一句话只说一个动作或一个判断，一句一般不超过 40 个字。原文的长定语、`which` 从句、破折号插入语，拆成几个短句或分句。
2. **先给结论，再给理由**。原文段落若先铺垫后给结论，译文可以先说结论，但不得改变论证方向，也不得把"可能"写成"一定"。
3. **术语第一次出现**：中文译名 + 括注英文原词，如"无关备选独立性（Independence of Irrelevant Alternatives, IIA）"。此后只用中文。没有通行中文译名的，保留英文原词（如 Bradley-Terry、Plackett-Luce、Rasch、Gumbel、Elo、softmax、logit）。
4. **每个抽象定义后面跟一个具体例子或类比**。原文已有例子的照译，不另外编造；原文没有例子的，可以补一个日常场景（如比较奶茶店、排课程表），并保证不与原文结论冲突、不引入原文没有的事实。
5. **公式、变量、数字、单位一律不动**。符号第一次出现时，用一句白话说明"它读作什么、在算什么"，符号本身照抄原文。
6. **保留原文的限定与保留态度**：条件、例外、默认值、"在什么条件下成立/失效"必须译出，不许为了通顺删掉。
7. **不增删事实**。译者补充的解释只限于"把原句说明白"，不得新增结论、数据、因果或作者没说的话。确需补充时，写成对已有公式或上下文的说明，不引入新命题。
8. **人称与语气**：原文的 we 指作者，译为"我们"；面向读者的 you 译为"你"。命令句、设问句按原样保留语气。
9. **不美化、不缩写**：不为了显得精炼而合并段落；一章的段落顺序、小节顺序与原文一致。

## 2. 原文照抄不动的部分

以下内容必须与原文逐字符一致，交付前用 `scripts/check-translation.py` 做数量比对：

- 数学：行内 `$...$`、行间 `$$...$$`、`\(...\)`、`\[...\]`，以及公式内的 `\text{}` 标签
- 代码块与单元格内容、`#|` 单元格选项（`autorun`、`echo` 等）
- 伪代码块内容、`\label{}`、`{#sec-...}`、`{#fig-...}` 等标签
- 引用键 `@sec-...`、`@fig-...`、`@citekey`，以及 `src/references.bib` 全文
- `::: {data-latex}` 一类的格式条件、`::: {#id .class}` 的 id 与 class
- 图片路径、短代码调用 `{{< ... >}}` 的参数
- 读者要照抄使用的模板块（如 `src/chap6.qmd` 原则 1 的"公平性影响说明"模板）：块内保持英文，字段含义写在块**外面**的中文里。理由与公式相同——代码块内容逐字符比对，说明只加在块外。
- 署名行、BibTeX 条目、标准文献著录（如 "S. Truong, A. Haupt, and S. Koyejo. 2025. ..."）
- 人名、机构名、软件与数据集名、URL、DOI
- 数学式整体照抄。式内的逻辑符号（`\exists`、`\forall`、`\text{and}` 等）不改写成中文"存在/任意"，需要说明时只写在公式外面；改动式内内容会让公式本身发生变化，校验脚本会报出公式数量或内容不一致。
- HTML 注释 `<!-- ... -->` 里的内容（例如 `src/chap4.qmd` 中被注释掉的一段拉普拉斯推导草稿）不会渲染给读者，保持原文不动。

## 3. 标点与排版

- 用中文全角标点：，。、；：？！""''（）。并列用顿号，不用逗号串接。
- 原文的 `---`（em dash）按语义改写：补充说明用逗号或冒号，转折用"但""不过"。
- 中英文之间、中文与数字之间加一个半角空格；全角标点两侧不加空格。
- 引号：引用原文字句用""，术语强调用粗体（沿用原文 `**…**` 位置）。
- 列表与表格结构、`:::` 分块数量、标题层级与原文一致。
- 章节交叉引用交给 Quarto 生成：配置里 `sec-prefix: "§"`，所以 `@sec-measurement` 会渲染成"§3.1"，不手写"第 3.1 节"。正文里"见 @sec-xxx"直接写成"见 @sec-xxx"。
- 图、表、定理、引理、定义的编号前缀同样由配置和 Quarto 中文语言包给出，正文不手写"图 1"。
- 章标题只写中文（如"基础"），英文原名在章首正文中给出一次。

## 4. 术语速查表

译法以 [术语表](../src/glossary.qmd)（`src/glossary.qmd`）为准，这里是正文写作时的速查。**同一概念全书只用一个译名**；表中"首次括注"列要求在该词第一次出现处括注英文。

### 4.1 核心概念

| 英文 | 统一译名 | 首次括注 |
|---|---|---|
| preference / preferences | 偏好 | — |
| preference learning | 偏好学习 | 是 |
| preference data | 偏好数据 | — |
| pairwise comparison | 成对比较、两两比较 | 是 |
| utility | 效用 | 是 |
| random utility model (RUM) | 随机效用模型 | 是 |
| latent utility | 潜在效用 | — |
| reward function | 奖励函数 | 是 |
| reward model | 奖励模型 | 是 |
| reward hacking | 奖励作弊 | 是 |
| policy | 策略 | 是 |
| reference policy | 参考策略 | — |
| policy gradient | 策略梯度 | — |
| elicitation | （偏好）征询 | 是 |
| aggregation | 聚合 | 是 |
| preference aggregation | 偏好聚合 | 是 |
| stated / revealed preference | 陈述偏好 / 显示偏好 | 是 |
| single-peaked preferences | 单峰偏好 | 是 |
| nosy preferences | 多管闲事的偏好 | 是 |
| choice probability | 选择概率 | — |
| discrete choice | 离散选择 | — |
| choice theory | 选择理论 | — |
| social choice | 社会选择 | — |
| social welfare function | 社会福利函数 | 是 |
| mechanism design | 机制设计 | 是 |
| voting rule / scoring rule | 投票规则 / 评分规则 | — |

### 4.2 模型与方法

| 英文 | 统一译名 | 首次括注 |
|---|---|---|
| Bradley-Terry model | Bradley-Terry 模型（简称 BT 模型） | 是 |
| Rasch model | Rasch 模型 | 是 |
| Plackett-Luce model | Plackett-Luce 模型 | 是 |
| Thurstone model | Thurstone 模型 | 是 |
| Elo rating system | Elo 等级分系统 | 是 |
| item response theory (IRT) | 项目反应理论 | 是 |
| factor model | 因子模型 | — |
| Gaussian process (GP) | 高斯过程 | 是 |
| kernel function | 核函数 | — |
| Thompson Sampling | 汤普森采样 | 是 |
| Upper Confidence Bound (UCB) | 上置信界 | 是 |
| multi-armed bandit | 多臂老虎机 | — |
| dueling bandits | 对决老虎机 | 是 |
| Interleaved Filter | 交错筛选（Interleaved Filter） | 是 |
| Dueling Bandit Gradient Descent (DBGD) | 对决老虎机梯度下降（DBGD）；正文简称 DBGD | 是 |
| Sparring EXP4 | Sparring EXP4（算法名保留原文；"sparring"在正文里译作"对练"） | 是 |
| Feel-good Thompson Sampling | Feel-good 汤普森采样 | 是 |
| feel-good exploration | Feel-good 探索 | 是 |
| qEUBO / qEI / qTS | 保留缩写；qEUBO 全称译作"最优选项的期望效用（expected utility of the best option）" | 是 |
| POP-BO | 有原则的乐观偏好型贝叶斯优化（POP-BO） | 是 |
| knowledge gradient | 知识梯度 | 是 |
| Copeland score / soft-Copeland score | 科佩兰分数 / 软科佩兰分数 | 是 |
| maximum information gain | 最大信息增益 | 是 |
| preferential Bayesian optimization (PBO) | 偏好型贝叶斯优化 | 是 |
| Bayesian optimization / inference | 贝叶斯优化 / 贝叶斯推断 | 是 |
| Laplace approximation | 拉普拉斯近似 | 是 |
| maximum likelihood estimation (MLE) | 最大似然估计 | 是 |
| cross-validation | 交叉验证 | 是 |
| acquisition function | 采集函数 | 是 |
| active learning | 主动学习 | 是 |
| D-optimal / A-optimal / E-optimal design | D-最优 / A-最优 / E-最优设计 | 是 |
| Fisher information | 费雪信息 | 是 |
| reinforcement learning from human feedback (RLHF) | 人类反馈强化学习 | 是 |
| direct preference optimization (DPO) | 直接偏好优化 | 是 |
| language model / LLM | 语言模型 / 大语言模型 | 是 |
| model alignment | 模型对齐 | 是 |
| computerized adaptive testing (CAT) | 计算机化自适应测验 | 是 |
| cooperative inverse reinforcement learning (CIRL) | 合作逆强化学习 | 是 |
| von Neumann winner / Condorcet winner / Borda winner | 冯·诺依曼胜者 / 孔多塞胜者 / 博尔达胜者 | 是 |
| Borda count | 博尔达计数 | 是 |
| Arrow's impossibility theorem | 阿罗不可能定理 | 是 |
| Gibbard-Satterthwaite theorem | Gibbard-Satterthwaite 定理 | 是 |
| liberal paradox | 自由主义悖论 | 是 |
| community notes | 社区笔记 | 是 |
| peer prediction / peer review | 同伴预测 / 同行评审 | 是 |

### 4.3 统计与机器学习通用词

| 英文 | 统一译名 |
|---|---|
| posterior / prior / likelihood | 后验 / 先验 / 似然 |
| posterior distribution | 后验分布 |
| latent variable | 隐变量 |
| parameter / estimate / estimator | 参数 / 估计 / 估计量 |
| unbiased / biased | 无偏 / 有偏 |
| variance / covariance / precision matrix | 方差 / 协方差 / 精度矩阵 |
| entropy / mutual information / information gain | 熵 / 互信息 / 信息增益 |
| calibration | 校准 |
| reliability | 信度 |
| uncertainty / uncertainty quantification | 不确定性 / 不确定性量化 |
| regret | 遗憾 |
| exploration / exploitation | 探索 / 利用 |
| exploration-exploitation tradeoff | 探索与利用的权衡 |
| regularization | 正则化 |
| hyperparameter | 超参数 |
| gradient descent / ascent | 梯度下降 / 梯度上升 |
| learning rate | 学习率 |
| convergence | 收敛 |
| bound / upper bound | 界 / 上界 |
| assumption | 假设 |
| ground truth | 真值 |
| oracle | 神谕 |
| dataset / annotation / label | 数据集 / 标注 / 标签 |
| sample (n./v.) / sampling | 样本 / 采样 |
| noise | 噪声 |
| context / prompt / response | 上下文 / 提示 / 回答 |
| evaluation / held-out data | 评估 / 留出数据 |

### 4.4 公平性

| 英文 | 统一译名 |
|---|---|
| fairness | 公平（性） |
| group / individual fairness | 群体公平 / 个体公平 |
| demographic parity | 人口统计均等 |
| equalized odds | 机会均等 |
| outcome fairness | 结果公平 |
| protected group | 受保护群体 |
| fairness constraint | 公平性约束 |
| inversion problem | 反转问题 |
| contextual integrity | 情境完整性 |
| human-centered design | 以人为中心的设计 |
| value alignment | 价值对齐 |

### 4.5 提示框标题

提示框的类型名由 Quarto 中文语言包生成（说明 / 提示 / 警示 / 重要），不要自己写 "Note"。自定义标题的固定译法：

| 原文标题 | 译文标题 |
|---|---|
| Key insight | 关键洞见 |
| Essential Reading | 必读文献 |
| Suggested Lecture Plan | 建议课时安排 |
| Proof Sketch | 证明要点 |
| Code | 代码 |
| Optional | 可选 |
| Beyond Bradley-Terry | 超出 Bradley-Terry 之外 |
| Quick Check | 快问快答 |
| Discussion Questions | 讨论题 |

## 5. 相对 upstream 的有意偏离

只列结构性偏离，供审阅时对照；未列出的改动都属于文字翻译。

1. `docs/`、`scripts/`、`.github/` 是本分支新增的，不属于书的内容。
2. `index.qmd` 开头增加一个"关于这个中文译本"的说明框（原文没有）。
3. `_quarto.yml`：新增 `lang: zh`；`crossref` 前缀改为中文/`§`；删掉 `language.crossref-ch-prefix`、`google-analytics`、`downloads: [pdf]`；`repo-url` 指向本 fork；书名副标题注明是译本。
4. 习题：`src/psets/pset1.qmd`–`pset3.qmd` 原文没有 YAML front matter，译稿加上带标题的头部，否则直接渲染出来是没有标题、没有书壳的裸页。习题现已接入发布：新增嵌套站点项目 `src/psets/_quarto.yml`（`lang: zh`、`execute: eval: false`，输出到 `_book/src/psets/`），book 项目本身不会渲染这些文件，因此 `.github/workflows/render-zh.yml` 在主项目渲染后单独渲染它们。两点必要说明：(a) 主题 scss 按项目根相对路径引用字体，缺 `src/psets/resources`（指向 `../../resources` 的符号链接）时构建报 `lstat .../src/psets/resources/fonts/et-book/roman-line-figures.ttf` 不存在；(b) CI 里必须逐个文件渲染，实测 `quarto render pset2.qmd pset3.qmd` 会让 `pset2.html` 的内容变成 pset3（输出互相覆盖）。`src/teaching.qmd` 的习题链接已从 GitHub 源文件地址改回本地 `psets/psetN.html`。
5. `src/teaching.qmd`：习题 4 一行注明"上游仓库里的这个文件是空的，暂未提供内容"（`src/psets/pset4.qmd` 为 0 字节）。
6. `license.qmd`：删掉 hits.seeyoufarm 访客计数徽章（它统计的是 mlhp.stanford.edu 的访问量，放在译本上会误导读者），改为写明原作与本译本的授权归属。
7. `src/notation.qmd`：原英文那句"Introduced 列标明符号首次出现的章节"，表里其实没有这一列，因此译成"每一节标明这些记号主要出现在哪一章"。这是 upstream 自身的文实不符。
8. 【更正】先前这里写着"上游正文有 3 处引用在 `src/references.bib` 里没有对应条目，渲染时显示为空"。**这条不成立**，是核对方法错了：pandoc 把 `@key` 渲染成正文里的作者年份（如 `Auer等2002年`），HTML 里不会出现这个键，所以按键名去生成页里搜会搜不到，误以为没渲染。

    重新核对的结果：`auer_cesa-bianchi_fischer_2002`、`kahneman_tversky_1979`、`mcfadden1981econometric` 三个键在 `src/references.bib` 里都有条目，在本站构建中也都正常渲染——第 5 章那句显示为"(Russo和Roy2015年;Auer等2002年;Lai和Robbins1985年)"，第 1 章显示为"(Train2009年;Ben-Akiva和Lerman1985年;McFadden1981年)"，第 4 章延伸阅读里那条显示为"Kahneman 和 Tversky (1979年)"。反过来，上游站点用旧版构建，`Prospect Theory` 那条在他们的页面里反而找不到。也就是说这不是译稿的差异，本分支未增删任何引用键。

9. `src/chap1.qmd`：原"本章视频导览"框里的 `{{< video animations/ch1/chapter1_narrated.mp4 >}}` 已删除，改为一句说明：该 mp4 被仓库 `.gitignore` 的 `*.html`/`*.mp4` 规则排除、未随仓库发布，且上游站点同一路径返回 404。
10. `src/chap1.qmd`：Metropolis-Hastings 那段原文有一句语法不完整的句子（`the distribution is a proposal $P$ for $x_{t+1}$ is made via sampling from ...`，其中 $P$ 在下文没有出现，公式里用的是 $\tilde Q$）。译文按上下文与公式译为"从概率核 $Q(\bullet | x_t)$ 采样得到提议分布 $\tilde Q(\bullet | x_t)$"，未保留悬空的 $P$（$x_{t+1}$ 与 $\tilde Q$ 均保留）。
11. `src/chap1.qmd`：一处把 `[@breiman2001statistical; @rudin2022interpretable]` 写成两条并排的 `@` 引用，渲染结果相同。

12. 原稿有少量排版疏漏，译文按正常排版写出，校验会显示为公式片段的增删（只改排版与标点，不改含义）：
    (a) 个别变量漏写数学定界符，译文按上下文补上 `$`。已遇到 `src/chap2.qmd` 的 `(V)`、`src/chap3.qmd` 的 `(U)`、`((x,y))`、`(x_{jk})`、`(\Delta_D)`、`(\hat\theta \Sigma)`（此处原文还漏了逗号）、`src/chap1.qmd` 练习题中原文写成裸文本的 `K-dimensional factor model`（译文作 `$K$ 维因子模型`，与同一文件其余 `$K$` 写法一致）；`src/glossary.qmd` 的 Individual Fairness 条目原文只说 "for a Lipschitz constant $L$ and appropriate metrics"，译文为了读者能读懂记号，补出"$d$ 是事先约定的相似度度量"，因而多出 `$d$` 这个片段。后续章节若再遇到同类疏漏，按同样处理，不必逐条另立条目，但要在提交说明里点明。
    (b) `src/chap3.qmd` 中 "maximizes expected \textbf{incremental} information" 用的是原始 LaTeX 命令，实测渲染结果是页面上直接显示 "\textbf{incremental}" 这几个字符（见 `_book/src/chap3.html`），译文改成 Markdown 粗体"**增量**"。
13. `src/chap2.qmd` 交叉验证一节有一句正文直接印出了代码里的格式化占位符（`{cv_scores.mean():.4f} ± {cv_scores.std():.4f}`），没有代入数值。这是 upstream 的笔误。本分支不擅自填入数字（那是代码运行结果，不是原文内容），只在该句后补了一句说明，指出按原样保留。

14. 章节交叉引用编号：原稿正文里有几处"Chapter N"与实际章节号相差一章（书稿早期含有一篇引言章，后来合并了，编号没跟着改；例如第 2 章开头称隐变量模型在"Chapter 2"，第 3 章的学习目标称学习问题在"Chapter 3"）。译文按**本书实际章节编号**翻译，不逐处加注；这样读者按编号跳转才对得上。涉及文件：`src/chap2.qmd`（开头一段）、`src/chap3.qmd`（学习目标、"Chapters 2-3"）。

15. 【更正】先前这里写着"上游第 4 章有 12 个 `:::` 框未闭合"。**这个结论是错的，问题出在校验脚本本身**：`scripts/check-blocks.py` 早先只把"恰好三个冒号"当作合法闭合，于是把第 4 章 6 个 `:::: algorithm`（四冒号开、四冒号闭）的闭合行也算成了开框，凑出"收尾 12 层"。

    实际核查结果：pandoc 的自定义块要求闭合的冒号数与开头一致，`:::: outer` 里可以嵌 `::: inner`，用 `:::` 闭内层、`::::` 闭外层（已用最小例子实测，两个 div 都正确闭合）；本站第 4 章构建出的 `_book/src/chap4.html` 里 6 个 `algorithm` div 也都在下一个标题之前闭合。脚本已按冒号个数重写配对逻辑，重写后第 1–7 章、术语表、习题集全部"结构与基线一致、两端平衡"。文档正文没有为此改动。


16. 第 2 章"题目按难度标注：(*) 入门，(**) 中等，(***) 较难。"一行：原文这样写在同一段里，`**` 会两两配对成粗体标记，页面上显示成 `() 入门，() 中等，() 较难`（星号被吃掉，上游站点同样如此）。译文按第 1 章同位置已有的写法加了反斜杠转义，页面恢复显示 `(*) (**) (***)`。其余各章标题里的 `(*)`、`(**)` 是孤立的单个星号串，不会配对，实测渲染正常，因此没有改动。

17. `_quarto.yml` 的 `format.html.include-in-header` 里原本手写了一个 MathJax 3 的 `<script>`（上游为旧版 Quarto 加的）。Quarto 1.11 自己会加载 MathJax 4，两个版本同时加载时 v4 的组件会报 `Component core uses 4.1.3 of MathJax; version in use is 3.2.2` 并抛 `TypeError`，结果整页公式都不排版：实测本页 `mjx-container` 为 0（页面里有 232 处公式标记），上游同页为 550。现在删掉这行手写脚本，只保留 Quarto 管理的引擎，`mathjax: macros:` 配置保留。修好后实测：第 1 章 625/625、第 2 章 232/232、第 3 章 323/323、第 6 章 166/166 处公式全部排版，控制台无报错。


18. 讲义（`src/slides/`）接入本站。它和习题集一样是嵌套项目（`src/slides/_quarto.yml`，输出目录 `../../_book/slides`，格式 revealjs），主项目不会渲染它，所以 `.github/workflows/render-zh.yml` 里增加了一个"渲染讲义"的步骤：先在 `src/slides` 目录里 `quarto add coatless-quarto/pyodide`（嵌套项目只认自己目录下的 `_extensions/`，仓库根装的扩展对它无效），再逐章 `quarto render chapN.qmd`。仓库里同时跟踪着两份 pyodide 快照：`src/slides/_extensions/coatless/pyodide/` 与 `src/slides/_extensions/coatless-quarto/pyodide/`，两份都缺 `qpyodide-monaco-editor-init.html`，而它们自带的 `qpyodide.lua` 会去读这个文件；`quarto add coatless-quarto/pyodide` 只刷新后者，渲染却选中了前者，于是 CI 报 `Error reading dependencies from …` 并失败（连续三次同样报错，本地因 Quarto 1.11 重装过扩展反而不复现）。修复方式是在 `zh` 分支删掉没人刷新的那份（`git rm -r src/slides/_extensions/coatless`），只留 CI 每次现装的那份。同时 `src/teaching.qmd` 里 7 个指向 `https://mlhp.stanford.edu/slides/chapN.html` 的链接改为相对路径 `../slides/chapN.html`；`src/slides/_quarto.yml` 的项目标题 `CS329H Slides` 译为 `CS329H 讲义`。

19. 讲义里有两处章节交叉引用与本书的实际编号不符：`src/slides/chap2.qmd` 开头写"Chapter 2 established models (Rasch, Bradley-Terry, factor models)"（建立模型的是第 1 章），第 322 行写"Connects to **active learning** (Chapter 4)"（主动学习在第 3 章）。这两处按原文照译成"第 2 章""第 4 章"，没有替作者改正——和上游一致更容易核对，读者若按中文站点的目录去找会发现对不上。

20. 上游从 LaTeX 转 Markdown 时留下了 7 处**指向不存在的锚点**的引用（第 4 章 4 处形如 `[\[fig-if\]](…){reference-type="ref" …}`、`[\[th:quebo_regret\]](…)`，第 5 章 3 处形如 `在图 [1.1](#fig-planner-agent){…}`、`（[1](#4optim){…}）`）。这些目标在**上游生成的页面里同样不存在**，点上去没有反应，属于上游的遗留缺陷，不是翻译引入的。处理分两种：第 4 章有 2 处所指内容就在本节，给小标题补上真正的标签 `{#sec-interleaved-filter}`、`{#sec-pbo-setup}`，引用改成 `@sec-interleaved-filter`、`@sec-pbo-setup`（与本书其余 175 处交叉引用同一写法，渲染后是可点击的小节号）；1 处指向本小节已有的定理锚点 `#qeubo-regret`。第 5 章那 3 处所指内容在书里没有对应编号，只删掉失效的编号，正文句子原样保留。因此 `check-translation.py` 对第 4 章会报 `labels`、`cite_keys` 各多出上述几项，已在此登记。
21. 习题集顶栏的两条导航原本写 `href: ../../index.qmd`、`href: ../teaching.qmd`。习题页由嵌套项目 `src/psets` 单独渲染，那两个 `.qmd` 不在它的项目目录里，Quarto 解析不了，生成的 HTML 里**原样**留下了 `.qmd` 后缀，在 Pages 上是 404。已改为指向已发布页面 `../../index.html`、`../teaching.html`。同时给 `src/psets/_quarto.yml` 补了 `repo-url: "https://github.com/CodingPracticeGroup/mlhp"` 与 `repo-actions: [source]`，让习题页和正文页一样有"查看源码"入口。

## 5.1 校验脚本的输出怎么读

`scripts/check-translation.py` 有两类已知的假阳性，出现时要人工核对而不是直接改正文：

1. `inline_math`：脚本按行用 `$` 配对切分，中英混排时切分边界会偏移，导致若干条目"看似丢失/新增"（例如原文 `$k > 2$` 与译文 `$k>2$` 会被算成两条）。核对方法是把差异条目在译文里逐个搜索。第 1 章已逐条核对，5 处"丢失"均在正文中。
2. 有意偏离（见本节）产生的 `div_blocks`、`shortcodes` 差异。
3. **不要在生成页里按引用键名搜索来判断引用有没有渲染。** pandoc 会把 `@key` 换成作者年份，HTML 里没有键名；正确的核法是回到正文看那句有没有出现"（××年）"这样的引文。第 5 节第 8 条当初就是这么误判的。

其余项（标题、行间公式、代码块、引用键、标签、单元格选项、`\text{}` 等命令）必须完全一致。

## 6. 交付前自查

```bash
python3 scripts/check-translation.py index.qmd src/chap1.qmd   # 基线取 main
python3 scripts/check-blocks.py src/chapN.qmd                  # ::: 开合序列
python3 scripts/find-untranslated.py src/chapN.qmd             # 还没译的正文（会有误报）
python3 scripts/check-attributes.py                            # 提示框标题属性是否会被截断
```

它比对的项：标题层级、行间/行内公式数量、代码围栏数量、`:::` 分块数量、引用键集合、标签集合、短代码调用、单元格选项、`\ref` 类命令、数学命令集合。任一不一致都会打印出具体是哪几处。允许的偏差只有两种，且必须在本文件第 5 节登记：译者为说明已有符号而新增的行内符号，以及登记过的结构改动。

成段翻译（一行一段的长段落）建议用批量替换脚本，它会在写入前拦住两类最常见的错：

```bash
python3 scripts/apply-translations.py src/chapN.qmd <<'EOF'
@ <原文某行的唯一前缀>
<译好的整行>
@@
EOF
```

前缀在文件里必须**恰好匹配一行**；替换前后行内 `$…$` 的集合必须相同，否则整批不写入。需要同时改多行时把新内容写成多行即可（脚本自底向上替换，行号不会串）。

除此之外，每章还需人工确认：术语命中上表、没有把"可能"写成"一定"、没有删掉任何限定条件。

改文件时的几条操作约定：

- 替换前先取到**整行**原文再动手。第 4 章往后不少段落是一行写完的长句，用 `awk 'NR==812'`（不加 `cut`）或 read 工具看全文；按截断后的半句翻译，会把后半句连同其中的公式、引用键一起丢掉（已经犯过三次：两次表现为"公式丢失"，一次表现为"引用键少了 `@christiano2018supervising` 等三个"——引用键的数量检查正是为这类错误准备的，每次批量改完都要跑）。
- 同一个毛病还有一种更隐蔽的表现：**只看了截断的开头就凭印象意译**，字面通顺、结构检查也过，但内容已经和原文不同。第 6 章文献说明有 7 条是这样被我"补"出来的（引用键少了 `@sloane2020participation`、`@rakova2021responsible` 等，同时凭空多了几个键），另有一些延伸阅读条目被顺手加了原文没有的 `@sec-` 引用。做法：这类条目一律先 `git show main:<文件>` 取出整行原文再译；译完用引用键集合做差集比对（脚本已做，但要会读它报的 missing/added）。引用记号后面的标点和原文保持一致（原文是 `@sec-x.` 句点收尾的，译文也在记号后留 ASCII 句点），否则引用键会被切分出不一致的 token。
- 一次改多处时从文件**底部往上看**、按行号从大到小执行，前面的行号才不会因后面的改动失准；`scripts/replace-by-key.py` 会自己定位行号，但同一段里两条片段落到同一行时它只保留第一条。
- 替换文本里**不要**包含 `:::` 收尾；每次批量修改后跑一次 `scripts/check-blocks.py`。
- `--expect` 只写行首的原文，不要顺手加反斜杠。脚本能容忍多余的反斜杠（`\*` → `*`），但 LaTeX 命令里的反斜杠（`\theta`）会照原样比较，写错仍会拒绝执行。
- 公式按原样照搬，包括原文写得别扭的地方（如 `$T$, e.g.` 这类把英文词写进定界符的写法）；需要通顺时改的是公式外面的中文，不是式内内容。
