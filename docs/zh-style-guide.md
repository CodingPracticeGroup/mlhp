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
- 署名行、BibTeX 条目、标准文献著录（如 "S. Truong, A. Haupt, and S. Koyejo. 2025. ..."）
- 人名、机构名、软件与数据集名、URL、DOI

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
4. 习题：`src/psets/pset1.qmd`–`pset3.qmd` 原文没有 YAML front matter，译稿加上带标题的头部，否则直接渲染出来是没有标题、没有书壳的裸页。曾尝试新增嵌套项目 `src/psets/_quarto.yml`，但它引用的 SCSS 字体路径相对于该目录解析，构建报 `lstat .../resources/fonts/et-book/roman-line-figures.ttf` 不存在而失败，因此删除；习题目前仍未接入构建，`src/teaching.qmd` 里的习题链接暂时指向 GitHub 上的源文件。`project.render` 里追加习题文件也无效（book 类型只渲染书内文件，实测仍只输出 11 页）。
5. `src/teaching.qmd`：习题 4 一行注明"上游仓库里的这个文件是空的，暂未提供内容"（`src/psets/pset4.qmd` 为 0 字节）。
6. `license.qmd`：删掉 hits.seeyoufarm 访客计数徽章（它统计的是 mlhp.stanford.edu 的访问量，放在译本上会误导读者），改为写明原作与本译本的授权归属。
7. `src/notation.qmd`：原英文那句"Introduced 列标明符号首次出现的章节"，表里其实没有这一列，因此译成"每一节标明这些记号主要出现在哪一章"。这是 upstream 自身的文实不符。
8. 上游正文有 3 处引用在 `src/references.bib` 里没有对应条目（`auer_cesa-bianchi_fischer_2002`、`kahneman_tversky_1979`、`mcfadden1981econometric`），渲染时显示为空。原文即如此，本分支未擅自补造条目。
9. `src/chap1.qmd`：原"本章视频导览"框里的 `{{< video animations/ch1/chapter1_narrated.mp4 >}}` 已删除，改为一句说明：该 mp4 被仓库 `.gitignore` 的 `*.html`/`*.mp4` 规则排除、未随仓库发布，且上游站点同一路径返回 404。
10. `src/chap1.qmd`：Metropolis-Hastings 那段原文有一句语法不完整的句子（`the distribution is a proposal $P$ for $x_{t+1}$ is made via sampling from ...`，其中 $P$ 在下文没有出现，公式里用的是 $\tilde Q$）。译文按上下文与公式译为"从概率核 $Q(\bullet | x_t)$ 采样得到提议分布 $\tilde Q(\bullet | x_t)$"，未保留悬空的 $P$（$x_{t+1}$ 与 $\tilde Q$ 均保留）。
11. `src/chap1.qmd`：一处把 `[@breiman2001statistical; @rudin2022interpretable]` 写成两条并排的 `@` 引用，渲染结果相同。

12. 正文个别地方变量漏写了数学定界符（例如 `src/chap2.qmd` 的 "one or more coordinates of (V)"）。译文按上下文补成 `$V$` 这种正常写法；这类新增的公式片段会在校验里显示为"新增"，属于有意修正排版疏漏，不改变含义。

13. `src/chap2.qmd` 交叉验证一节有一句正文直接印出了代码里的格式化占位符（`{cv_scores.mean():.4f} ± {cv_scores.std():.4f}`），没有代入数值。这是 upstream 的笔误。本分支不擅自填入数字（那是代码运行结果，不是原文内容），只在该句后补了一句说明，指出按原样保留。

## 5.1 校验脚本的输出怎么读

`scripts/check-translation.py` 有两类已知的假阳性，出现时要人工核对而不是直接改正文：

1. `inline_math`：脚本按行用 `$` 配对切分，中英混排时切分边界会偏移，导致若干条目"看似丢失/新增"（例如原文 `$k > 2$` 与译文 `$k>2$` 会被算成两条）。核对方法是把差异条目在译文里逐个搜索。第 1 章已逐条核对，5 处"丢失"均在正文中。
2. 有意偏离（见本节）产生的 `div_blocks`、`shortcodes` 差异。

其余项（标题、行间公式、代码块、引用键、标签、单元格选项、`\text{}` 等命令）必须完全一致。

## 6. 交付前自查

```bash
python3 scripts/check-translation.py index.qmd src/chap1.qmd   # 基线取 main
```

它比对的项：标题层级、行间/行内公式数量、代码围栏数量、`:::` 分块数量、引用键集合、标签集合、短代码调用、单元格选项、`\ref` 类命令、数学命令集合。任一不一致都会打印出具体是哪几处。允许的偏差只有两种，且必须在本文件第 5 节登记：译者为说明已有符号而新增的行内符号，以及登记过的结构改动。

除此之外，每章还需人工确认：术语命中上表、没有把"可能"写成"一定"、没有删掉任何限定条件。
