"""校验译文与英文原文的"机器内容"是否一致。

用法:
    python3 scripts/check-translation.py index.qmd src/chap1.qmd
    CHECK_BASE=upstream/main python3 scripts/check-translation.py ...

基线默认取 main 分支（= upstream 纯镜像）的版本，对比对象是当前工作区文件。
允许的偏差种类见 docs/zh-style-guide.md 第 5、6 节。
"""
import re
import subprocess
import sys

import os

BASE = os.environ.get("CHECK_BASE", "main")


def feats(t: str):
    f = {}
    f["headings"] = sorted(re.findall(r"^(#{1,6})\s", t, flags=re.M))
    f["display_math"] = len(re.findall(r"\$\$", t)) // 2
    f["inline_math"] = len(re.findall(r"(?<!\$)\$(?!\$)(?:[^$\n]|\\.)+?\$(?!\$)", t))
    f["code_fences"] = len(re.findall(r"^```", t, flags=re.M))
    f["div_blocks"] = len(re.findall(r"^:::", t, flags=re.M))
    f["cite_keys"] = sorted(
        k.rstrip(".") for k in re.findall(r"@([A-Za-z0-9_:.-]+)", t)
    )
    f["labels"] = sorted(set(re.findall(r"\{#[^}]+\}", t)))
    f["ref_cmds"] = sorted(set(re.findall(r"\\(?:ref|eqref|autoref|cref)\{[^}]*\}", t)))
    f["shortcodes"] = sorted(re.findall(r"\{\{<\s*([A-Za-z0-9_.-]+)", t))
    f["cell_opts"] = sorted(re.findall(r"^#\|\s*([A-Za-z0-9_.-]+)", t, flags=re.M))
    f["html_attrs"] = sorted(re.findall(r"\{\\.([A-Za-z0-9_#.\-=\s]+)\}", t))
    f["math_cmds"] = sorted(set(re.findall(r"\\[A-Za-z]+\{", t)))
    # 代码围栏内的内容必须逐字符一致（代码注释也不翻译）
    f["code_blocks"] = re.findall(r"^```(?:\{[^}]*\})?\n(.*?)^```", t, flags=re.S | re.M)
    f["_items"] = {
        "display_math": re.findall(r"\$\$(?:.*?)\$\$", t, flags=re.S),
        "inline_math": math_spans(t),
    }
    return f


def math_spans(t: str):
    """按行取 $...$ 之间的内容（跳过代码围栏）。用奇偶配对，不受相邻中文引号影响。"""
    # 先去掉行间公式，避免一行里出现成对的 $$ 打乱奇偶
    t = re.sub(r"\$\$(?:.|\n)*?\$\$", " ", t)
    out, in_fence = [], False
    for line in t.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or "$" not in line:
            continue
        parts = line.split("$")
        for i in range(1, len(parts), 2):
            span = parts[i]
            if span and "\n" not in span:
                out.append(span)
    return out


def item_diff(key, base, new):
    """计数不一致时，列出到底多/少了哪几处数学式。"""
    from collections import Counter

    b, z = Counter(base["_items"][key]), Counter(new["_items"][key])
    for x in (z - b).elements():
        print(f"       + 新增 {x[:70]!r}")
    for x in (b - z).elements():
        print(f"       - 丢失 {x[:70]!r}")


def get_base(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{BASE}:{path}"], capture_output=True, text=True, check=True
    )
    return r.stdout


ok_all = True
for path in sys.argv[1:]:
    base = feats(get_base(path))
    new = feats(open(path, encoding="utf-8").read())
    print(f"=== {path}")
    for k in base:
        if k.startswith("_"):
            continue
        if base[k] == new[k]:
            n = len(base[k]) if isinstance(base[k], list) else base[k]
            print(f"  OK   {k:<14} n={n}")
        else:
            ok_all = False
            print(f"  DIFF {k:<14} base={base[k]!r}")
            print(f"       {'':<14} zh  ={new[k]!r}")
            if k in base.get("_items", {}):
                item_diff(k, base, new)
print("ALL_OK" if ok_all else "HAS_DIFF")
