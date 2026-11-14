#!/usr/bin/env python3
"""按"英文原句的片段"定位整行并按行号替换，自动从文件后面往前改。

这样就不用手工推算行号（前面的替换会移动后面的行号）。
每段新内容从 here-doc 读入，格式：

    python3 scripts/replace-by-key.py src/chap3.qmd <<'PYEOF'
    @ 要查找的英文片段（唯一即可，不必写整行）
    替换后的中文内容（可以多行）
    @@
    @ 下一个片段
    ...
    @@
    PYEOF

规则：命中的那一行到"下一条空行之前的最后一行"会被整段替换？——不会，
这里只替换匹配到的**那一行**，所以给出的新内容必须是这一行的完整内容。
同一段里的两个片段若落到同一行，会互相覆盖——脚本会跳过第二段并提醒。
"""
import sys


def main() -> int:
    path = sys.argv[1]
    spec = sys.stdin.read()
    blocks, cur = [], None
    for raw in spec.split("\n"):
        if raw.startswith("@@"):
            if cur is not None:
                blocks.append(cur)
            cur = None
            continue
        if raw.startswith("@ "):
            if cur is not None:
                blocks.append(cur)
            cur = [raw[2:], []]
            continue
        if cur is not None:
            cur[1].append(raw)
    if cur is not None:
        blocks.append(cur)

    lines = open(path, encoding="utf-8").read().split("\n")
    todo, seen = [], {}
    for key, body in blocks:
        hits = [i for i, ln in enumerate(lines) if key in ln]
        if not any(line.strip() for line in body):  # 空正文会直接删掉整行，容易出事
            print(f"!! 新内容为空（会删掉整行），跳过；确实要删请用 splice.py：{key[:40]}")
            continue
        if len(hits) != 1:
            print(f"!! 匹配到 {len(hits)} 处，跳过：{key[:60]}")
            continue
        if hits[0] in seen:  # 两段新内容落到同一行会互相覆盖，必须避免
            print(f"!! 与「{seen[hits[0]][:40]}」落在同一行 {hits[0] + 1}，跳过：{key[:40]}")
            continue
        seen[hits[0]] = key
        todo.append((hits[0], body, key))
    for idx, body, key in sorted(todo, reverse=True):
        lines[idx : idx + 1] = body
        print(f"ok 第 {idx + 1} 行 -> {len(body)} 行（{key[:40]}）")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return 0


sys.exit(main())
