#!/usr/bin/env python3
"""按行号批量替换译文：python3 scripts/apply-line-translations.py <文件> <映射.json>

映射是 {"行号": "新内容"}，行号从 1 开始，对应原文件。新内容里可以用 \n 拆成多行。
安全闸（不满足就整份不写盘）：
  1. 目标行不能是代码围栏、行间公式、图片、callout、属性行；
  2. 每行（同一行号对应的整段）里的 `$…$` 行内公式多重集合必须与原文一致；
  3. 不能改动 `{#label}`、`{.class}`、`:::`、`![...]`、`{python ...}` 等结构标记。
自下而上应用，所以行号不会因为前面的插入而错位。
"""
import json
import re
import sys

path, mapfile = sys.argv[1], sys.argv[2]
lines = open(path, encoding="utf-8").read().split("\n")
mapping = {int(k): v for k, v in json.load(open(mapfile, encoding="utf-8")).items()}

STRUCT = re.compile(r"^\s*(:::|\{\.|\{#|!\[|```|\$\$)")


def math_spans(text):
    return sorted(re.findall(r"\$[^$\n]*\$", text))


def structural_tokens(text):
    return re.findall(r"\{#[^}]*\}|\{\.[^}]*\}|\{#[^}]* [^}]*\}|\{[a-z]+ [^}]*\}", text)


# 逐行核对，先把问题全部收集起来再报错，避免改一处试一次
problems = []
infence = {}
fence = False
for i, line in enumerate(lines, 1):
    if re.match(r"^\s*```", line):
        fence = not fence
    infence[i] = fence

for n, new in sorted(mapping.items()):
    if n < 1 or n > len(lines):
        problems.append(f"行 {n} 超出文件范围（{len(lines)} 行）")
        continue
    old = lines[n - 1]
    if not old.strip():
        problems.append(f"行 {n} 是空行")
        continue
    if infence[n]:
        problems.append(f"行 {n} 在代码围栏内")
        continue
    if STRUCT.match(old):
        problems.append(f"行 {n} 是结构行：{old.strip()[:50]}")
        continue
    joined_old = old
    joined_new = new.replace("\r", "")
    if math_spans(joined_old) != math_spans(joined_new):
        a, b = math_spans(joined_old), math_spans(joined_new)
        problems.append(f"行 {n} 公式不一致：原 {a} → 新 {b}")
        continue
    if sorted(structural_tokens(joined_old)) != sorted(structural_tokens(joined_new)):
        problems.append(
            f"行 {n} 结构标记不一致：原 {structural_tokens(joined_old)} → 新 {structural_tokens(joined_new)}"
        )
        continue

if problems:
    print("未应用，先修这些问题：")
    for p in problems:
        print("  -", p)
    sys.exit(1)

for n in sorted(mapping, reverse=True):
    lines[n - 1 : n] = mapping[n].replace("\r", "").split("\n")

open(path, "w", encoding="utf-8").write("\n".join(lines))
print(f"已应用 {len(mapping)} 行到 {path}")
