#!/usr/bin/env python3
"""删除紧挨着的重复 `:::` 闭合标记（替换正文时容易把闭合框多写一遍）。"""
import sys

for path in sys.argv[1:]:
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    removed = 0
    for i, ln in enumerate(lines):
        if ln.strip() == ":::" and out and out[-1].strip() == ":::":
            removed += 1
            continue
        out.append(ln)
    if removed:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    print(f"{path}: 删除 {removed} 处重复闭合")
