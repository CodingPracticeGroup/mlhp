#!/usr/bin/env python3
"""按行号把文件里的一段替换成标准输入给出的新内容。

用法：
    python3 scripts/splice.py <文件> <起始行> <结束行> [--expect 前缀] <<'EOF'
    ...新的中文内容...
    EOF

行号从 1 开始，两端都含。--expect 用来核对起始行内容（防止行号看错后替换错位置）；
只提供一小段起始行文字即可，不匹配就报错退出、不改动文件。
"""
import re
import sys

args = sys.argv[1:]
if len(args) < 3:
    sys.exit(__doc__)

path, start, end = args[0], int(args[1]), int(args[2])
expect = None
if "--expect" in args:
    i = args.index("--expect")
    expect = args[i + 1]
    del args[i:i + 2]

new = sys.stdin.read()
lines = open(path, encoding="utf-8").read().split("\n")

if not (1 <= start <= end <= len(lines)):
    sys.exit(f"行号越界：文件共 {len(lines)} 行，要求 {start}-{end}")
if expect is not None:
    got = lines[start - 1]
    # 写 here-doc 时容易顺手把 markdown 特殊字符转义（\* \$ \{ …），这里容忍这类多余的转义；
    # 只去掉紧挨 markdown 特殊字符的反斜杠，像 \theta 这样的 LaTeX 命令保持原样。
    relaxed = re.sub(r"\\(?=[*$\\{}[\]()#|])", "", expect)
    if not got.startswith(expect) and not got.startswith(relaxed):
        sys.exit(f"起始行不匹配，未做任何修改。\n实际: {got[:120]}\n期望前缀: {expect}")

lines[start - 1:end] = new.rstrip("\n").split("\n")
open(path, "w", encoding="utf-8").write("\n".join(lines))
print(f"ok: {path} 第 {start}-{end} 行 -> {len(new.rstrip(chr(10)).splitlines())} 行")
