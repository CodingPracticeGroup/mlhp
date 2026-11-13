#!/usr/bin/env python3
"""检查 div 的属性写法是否能被 Pandoc 正确解析。

只针对 `::: {.callout-note title="…"}` 这一类：title 的值必须是一段被引号包住、
后面直接跟 `}`（或 ` collapse="true|false"` 再跟 `}`）的内容。如果中文里用了半角引号，
属性会被提前截断，页面上标题就少了一半，而公式/分块数量都不变，其它脚本查不出来。

用法：python3 scripts/check-attributes.py [文件…]   不带参数时检查 src/ 与 index.qmd
"""
import re
import sys
import glob

OK = re.compile(r'title="[^"]*"(?:\s+collapse="(?:true|false)")?\s*\}')
LABEL = re.compile(r'(label|name|format)=\"[^\"]*\"\s*\}')


def check(path):
    bad = 0
    for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
        if "title=\"" not in line:
            continue
        if OK.search(line) or LABEL.search(line):
            continue
        print(f"{path}:{lineno}: 属性可能被截断：{line.strip()[:120]}")
        bad += 1
    return bad


def main():
    files = sys.argv[1:] or sorted(glob.glob("src/**/*.qmd", recursive=True)) + ["index.qmd"]
    total = sum(check(f) for f in files)
    print("未发现异常" if not total else f"共 {total} 处待修")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
