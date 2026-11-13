#!/usr/bin/env python3
"""列出一个 .qmd 里仍然像英文正文的行段（跳过代码围栏与 YAML 头），供逐段翻译定位用。

用法：
    python3 scripts/find-english.py src/chap2.qmd [--max 40]

判定办法：去掉行内公式、行内代码、引用键、HTML 标签与链接目标之后，
连续出现 5 个以上由 ASCII 字母组成的单词，就认为这一行还是英文。
输出的是行号区间（含两端），可以直接喂给 scripts/splice.py。
"""
import re
import sys

path = sys.argv[1]
limit = 999
if "--max" in sys.argv:
    limit = int(sys.argv[sys.argv.index("--max") + 1])

lines = open(path, encoding="utf-8").read().split("\n")
in_fence = in_yaml = False
hits = []
for i, line in enumerate(lines, 1):
    stripped = line.lstrip()
    if i == 1 and stripped == "---":
        in_yaml = True
        continue
    if in_yaml:
        if stripped == "---":
            in_yaml = False
        continue
    if stripped.startswith("```"):
        in_fence = not in_fence
        continue
    if in_fence or not line.strip():
        continue
    if stripped.startswith(("{{<", ":::", "<", "#|", "!", "|")):
        continue
    t = line
    t = re.sub(r"\$[^$]*\$", " ", t)              # 行内公式
    t = re.sub(r"`[^`]*`", " ", t)                # 行内代码
    t = re.sub(r"!</?[^>]+>", " ", t)             # HTML
    t = re.sub(r"\(https?://[^)]*\)", " ", t)      # 链接目标
    t = re.sub(r"@[\w:.-]+", " ", t)               # 引用键与交叉引用
    words = re.findall(r"[A-Za-z]{2,}", t)
    if len(words) >= 5:
        hits.append(i)

# 合并相邻行段（中间只允许隔空行）
groups = []
for ln in hits:
    if groups and ln - groups[-1][1] <= 2:
        groups[-1][1] = ln
    else:
        groups.append([ln, ln])

for a, b in groups[:limit]:
    print(f"{a}-{b}" if a != b else str(a))
print(f"# 共 {len(groups)} 段", file=sys.stderr)
