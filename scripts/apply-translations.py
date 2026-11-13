#!/usr/bin/env python3
"""按"前缀 → 新行"的成对文本替换文件内容，并核对行内公式是否一致。

输入格式（标准输入或一个文本文件）：

    @ <原文某行的唯一前缀>
    <替换后的整行内容>（可以是一行，也可以是若干行）
    @@

规则：
- 前缀必须在文件中**恰好匹配一行**，否则整份输入拒绝写入并报告；
- 每对替换前后 `$…$` 公式集合（不计顺序）必须相同，否则同样拒绝——
  这条能挡住"顺手补了个 $x$"或"漏掉一个 $y$"这类最容易破坏校验的错。
  确实需要增删公式时，改用 scripts/splice.py 并把变化登记到风格指南第 5 节。

用法：python3 scripts/apply-translations.py <目标 .qmd> < 替换说明.txt
"""
import re
import sys


def spans(line):
    return sorted(re.findall(r"\$([^$]+)\$", line))


def parse(text):
    pairs, start, body = [], None, []
    for line in text.split("\n"):
        if line.startswith("@ ") and start is None:
            start = line[2:]
        elif line == "@@":
            if start is None:
                raise SystemExit("出现 @@ 但没有对应的 @ 开头")
            while body and not body[-1].strip():
                body.pop()
            pairs.append((start, "\n".join(body)))
            start, body = None, []
        elif start is not None:
            body.append(line)
    if start is not None:
        raise SystemExit(f"这一段没有用 @@ 结束：{start[:40]}")
    return pairs


def main():
    target = sys.argv[1]
    pairs = parse(sys.stdin.read())
    lines = open(target, encoding="utf-8").read().split("\n")
    problems = []
    for start, new in pairs:
        hits = [i for i, l in enumerate(lines) if l.startswith(start)]
        if len(hits) != 1:
            problems.append(f"匹配 {len(hits)} 行：{start[:50]}")
            continue
        i = hits[0]
        if spans(new) != spans(lines[i]):
            problems.append(f"公式不一致（第 {i + 1} 行）：原 {spans(lines[i])} 新 {spans(new)}")
    if problems:
        print("未做任何修改：")
        for p in problems:
            print("  " + p)
        return 1
    # 从后往前替换，避免前面的替换改变后面的行号
    for start, new in sorted(pairs, key=lambda p: -[i for i, l in enumerate(lines) if l.startswith(start)][0]):
        i = [k for k, l in enumerate(lines) if l.startswith(start)][0]
        lines[i : i + 1] = new.split("\n")
    open(target, "w", encoding="utf-8").write("\n".join(lines))
    print(f"已替换 {len(pairs)} 处")
    return 0


if __name__ == "__main__":
    sys.exit(main())
