#!/usr/bin/env python3
"""把文件里的 ::: 开合序列修成与基线（默认 main）一致。

做法：把两边的 ::: 抽成 +1/-1 序列，用 difflib 对齐。
基线多出的"闭"就是漏写的闭合，补在它应当出现的位置；
当前多出的"闭"就是多写的，删掉。每次只修一处，反复直到一致（最多 40 轮）。

用法：
    python3 scripts/fix-blocks.py src/chap3.qmd [基线ref]
"""
import difflib
import subprocess
import sys

path = sys.argv[1]
base_ref = sys.argv[2] if len(sys.argv) > 2 else "main"


def events(text):
    """[(行号(1基), ±1)]，跳过代码围栏。"""
    out, fence = [], False
    for i, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        s = line.strip()
        if s.startswith(":::"):
            out.append((i, -1 if s == ":::" else 1))
    return out


base_text = subprocess.run(
    ["git", "show", f"{base_ref}:{path}"], capture_output=True, text=True
).stdout
b_lines = base_text.split("\n")

for round_no in range(1, 41):
    lines = open(path, encoding="utf-8").read().split("\n")
    b, c = events(base_text), open(path, encoding="utf-8").read()
    b, c = events(base_text), events(c)
    bd = [d for _, d in b]
    cd = [d for _, d in c]
    if bd == cd:
        print(f"OK  {path}: 第 {round_no} 轮检查，结构与基线一致")
        sys.exit(0)
    fixed = False
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=bd, b=cd, autojunk=False).get_opcodes():
        if tag == "delete":  # 基线有、当前缺：在"上一个匹配事件"之后补闭合
            anchor = c[j1 - 1][0] if j1 > 0 else 0
            for k in range(i2 - i1):
                lines.insert(anchor + k, ":::")
            print(f"  第 {round_no} 轮：在 {anchor + 1} 行后补 {i2 - i1} 个闭合（基线行 {b[i1][0]}）")
            fixed = True
            break
        if tag == "insert":  # 当前多出来的事件：删掉
            for ln in sorted((c[j][0] for j in range(j1, j2)), reverse=True):
                del lines[ln - 1]
            print(f"  第 {round_no} 轮：删除多余事件行 {[c[j][0] for j in range(j1, j2)]}")
            fixed = True
            break
        if tag == "replace":
            print(f"  第 {round_no} 轮：开/闭类型不一致，需要人工看：基线行 {b[i1][0]} vs 当前行 {c[j1][0]}")
            sys.exit(1)
    if not fixed:
        print("  无法自动修复，请人工检查")
        sys.exit(1)
    open(path, "w", encoding="utf-8").write("\n".join(lines))

print("超过 40 轮仍未收敛")
sys.exit(1)
