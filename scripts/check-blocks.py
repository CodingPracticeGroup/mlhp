#!/usr/bin/env python3
"""比较译稿与基线（默认 main 分支）里的 ::: 结构。

翻译只该改文字，不该改变 ::: 的开合序列。这里把两个文件里的 ::: 抽成
一串 +1/-1，逐个对比；不一致就打印出两边各自的位置和内容。

用法：
    python3 scripts/check-blocks.py src/chap3.qmd [基线ref]
"""
import subprocess
import sys

path = sys.argv[1]
base_ref = sys.argv[2] if len(sys.argv) > 2 else "main"


def events(text):
    """返回 ([(行号, +1/-1, 该行内容)], 收尾层数)。跳过代码围栏。"""
    out, depth, fence = [], 0, False
    for i, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        s = line.strip()
        if s.startswith(":::"):
            d = -1 if s == ":::" else 1
            if d < 0 and depth == 0:
                out.append((i, d, "★此处闭合时没有打开的块★"))
            else:
                depth += d
                out.append((i, d, s[:56]))
    return out, depth


base_text = subprocess.run(
    ["git", "show", f"{base_ref}:{path}"], capture_output=True, text=True
).stdout
cur_text = open(path, encoding="utf-8").read()

b, bd = events(base_text)
c, cd = events(cur_text)
if [d for _, d, _ in b] == [d for _, d, _ in c] and bd == cd == 0:
    print(f"OK  {path}: ::: 结构与基线一致（{len(b)} 个开合，两端平衡）")
    sys.exit(0)

print(f"DIFF {path}: 基线 {len(b)} 个事件、收尾 {bd} 层；当前 {len(c)} 个、收尾 {cd} 层")
for n, (eb, ec) in enumerate(zip(b, c)):
    if eb[1] != ec[1] or "★" in ec[2]:
        print(f"  从第 {n} 个事件开始不一致：")
        for k in range(max(0, n - 2), min(len(b), n + 3)):
            print(f"    基线 行{b[k][0]:>5} {'开' if b[k][1] > 0 else '闭'}  {b[k][2]}")
        print("    ---")
        for k in range(max(0, n - 2), min(len(c), n + 3)):
            print(f"    当前 行{c[k][0]:>5} {'开' if c[k][1] > 0 else '闭'}  {c[k][2]}")
        break
else:
    print("  开合序列一致，但收尾层数不为 0（有块没有闭合）")
sys.exit(1)
