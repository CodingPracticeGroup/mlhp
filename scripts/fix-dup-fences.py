#!/usr/bin/env python3
"""删除多余的重复 `:::` 闭合标记。

只在文件整体"闭合多于开始"时才删，并且从文件末尾往回删，
这样嵌套调用（连续两个合法闭合）不会被误删。
"""
import sys


def balance(lines):
    depth, fence = 0, False
    for ln in lines:
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        s = ln.strip()
        if s.startswith(":::"):
            depth += -1 if s == ":::" else 1
    return depth


for path in sys.argv[1:]:
    lines = open(path, encoding="utf-8").read().split("\n")
    removed = 0
    while balance(lines) < 0:
        for i in range(len(lines) - 1, 0, -1):
            if lines[i].strip() == ":::" and lines[i - 1].strip() == ":::":
                del lines[i]
                removed += 1
                break
        else:
            break
    if removed:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"{path}: 删除 {removed} 处多余闭合（当前平衡 {balance(lines)}）")
