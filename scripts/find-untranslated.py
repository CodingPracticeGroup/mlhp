#!/usr/bin/env python3
"""找出**应该翻译却还是英文**的正文行。

做法：跳过代码围栏、`:::` 伪代码环境里的算法描述之外的行、HTML 注释、行间公式（`$$` 包裹的整块）、
行内公式、行内代码、引用键（`@key`）、标签与属性块、URL；剩下的行里如果还连着出现若干个英文单词，
就当作漏译报出来。

这是给人看的辅助工具，会有误报（图中坐标名、专有名词连写等），需要人工判断。

用法：python3 scripts/find-untranslated.py <文件…>
"""
import re
import sys

MIN_WORDS = 6          # 连续英文单词数达到这个数才算漏译
SKIP_STARTS = ("```", "    ::: ", ":::: ")   # 代码围栏等


def scan(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    in_fence = in_math = in_comment = False
    for no, raw in enumerate(lines, 1):
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if in_math:
            if "$$" in line:
                in_math = False
            continue
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if "<!--" in line:
            in_comment = "-->" not in line
            continue
        if line == "$$":
            in_math = True
            continue
        if line.startswith("$$") and line.endswith("$$") and line.count("$$") >= 2:
            continue
        text = re.sub(r"\$\$.*?\$\$", " ", raw)          # 同一行里的行间公式
        text = re.sub(r"\$[^$]*\$", " ", text)           # 行内公式
        text = re.sub(r"`[^`]*`|@[\w:.-]+|\{#[^}]*\}|\{[^}]*\}|https?://\S+|\\\\[\w*{}]+", " ", text)
        words = re.findall(r"[A-Za-z]{2,}", text)
        if len(words) >= MIN_WORDS:
            out.append((no, " ".join(words[:12]), line[:90]))
    return out


def main():
    bad = 0
    for path in sys.argv[1:]:
        hits = scan(path)
        print(f"== {path}: 疑似漏译 {len(hits)} 行")
        for no, words, _ in hits:
            print(f"  {no}: {words}")
        bad += len(hits)
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
