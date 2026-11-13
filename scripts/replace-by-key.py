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
这里只替换匹配到的**那一行**；需要一次替换多行时，把起止行写清楚用 splice.py。
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
    todo = []
    for key, body in blocks:
        hits = [i for i, ln in enumerate(lines) if key in ln]
        if len(hits) != 1:
            print(f"!! 匹配到 {len(hits)} 处，跳过：{key[:60]}")
            continue
        todo.append((hits[0], body, key))
    for idx, body, key in sorted(todo, reverse=True):
        lines[idx : idx + 1] = body
        print(f"ok 第 {idx + 1} 行 -> {len(body)} 行（{key[:40]}）")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return 0


sys.exit(main())
