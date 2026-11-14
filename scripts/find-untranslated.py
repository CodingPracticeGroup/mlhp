#!/usr/bin/env python3
"""找出**应该翻译却还是英文**的正文行。

做法：跳过代码围栏、`:::` 伪代码环境里的算法描述之外的行、HTML 注释、行间公式（`$$` 包裹的整块）、
行内公式、行内代码、引用键（`@key`）、标签与属性块、URL；剩下的行里如果还连着出现若干个英文单词，
就当作漏译报出来。

判定不只看词数：还要求这一行里出现至少 3 个英文虚词（the / this / you / with …）。
这样"IIA Gumbel Bradley Terry"这类术语与专名连排（我们有意保留英文）不会被报出来，
报出的基本都是真正的英文句子。仍可能有误报（图中的英文坐标名、命令式代码说明等），需要人工过一遍。

用法：python3 scripts/find-untranslated.py <文件…>
"""
import re
import sys

MIN_WORDS = 6          # 连续英文单词数达到这个数才算候选
# 只有真正的散文才算漏译：术语、人名、模型名连排（例如 "IIA Gumbel Bradley Terry"）不是。
# 所以除了词数，还要求这一行里出现若干个常见英文虚词。
STOPWORDS = {"the", "this", "that", "these", "those", "and", "for", "with", "from", "into",
             "you", "your", "we", "our", "they", "it", "its", "is", "are", "was", "were",
             "be", "can", "could", "should", "would", "will", "have", "has", "do", "does",
             "of", "in", "on", "by", "as", "at", "to", "if", "then", "when", "which",
             "what", "how", "why", "there", "their", "not", "but", "so", "such", "each"}
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
        low = [w.lower() for w in words]
        stops = sum(1 for w in low if w in STOPWORDS)
        if len(words) >= MIN_WORDS and stops >= 3:
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
