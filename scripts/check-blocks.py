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
    """返回 ([(行号, +1/-1, 该行内容)], 收尾层数)。跳过代码围栏。

    围栏的定界符是 3 个或更多冒号，闭合必须数同样的冒号（pandoc 语义，
    已用一个 `:::: outer` / `::: inner` / `:::` / `::::` 的最小例子实测确认：
    两个 div 都正确闭合）。所以这里按冒号个数配对，而不是把"恰好三个冒号"
    当成唯一合法的闭合写法——早先版本把 `::::` 一律算作开框，导致第 4 章
    的 `:::: algorithm` 被误报成 12 个未闭合。
    """
    out, stack, fence = [], [], False
    for i, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        s = line.strip()
        if not s.startswith(":"):
            continue
        run = len(s) - len(s.lstrip(":"))
        if run < 3:
            continue
        if stack and stack[-1][1] == run:
            _, _, ln, _ = stack.pop()
            out.append((i, -1, f"闭合 {run} 冒号（对应第 {ln} 行）"))
        elif any(w == run for _, w, _, _ in stack):
            while stack and stack[-1][1] != run:
                out.append((stack.pop()[0] + 0, 0, "★被外层闭合吞掉的块★"))
            _, _, ln, _ = stack.pop()
            out.append((i, -1, f"闭合 {run} 冒号（对应第 {ln} 行）"))
        else:
            stack.append((i, run, i, s[:56]))
            out.append((i, +1, s[:56]))
    for i, w, _, txt in stack:
        out.append((i, +9, f"★未闭合：第 {i} 行 {w} 冒号 {txt[:40]}★"))
    return out, sum(1 for _, d, _ in out if d == +9)


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
    if len(b) != len(c):
        more, fewer = (len(c) - len(b), "译稿多"), (len(b) - len(c), "译稿少")
        print(f"  事件个数不同：译稿比基线{'多' if more > 0 else '少'} {abs(more)} 个"
              "（多半是新增或删除了 callout，需在风格指南第 5 节登记）")
    else:
        print("  开合序列一致，但收尾层数不为 0（有块没有闭合）")
sys.exit(1)
