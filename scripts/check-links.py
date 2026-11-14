#!/usr/bin/env python3
"""检查 _book 里所有页面的链接是否可用。

用法：python3 scripts/check-links.py [_book]

对每个 .html 文件，解析真实的 a/img/script/link/iframe/source 标签（不解析正文里的
代码文本），把引用分成几类并逐条判定：

  站内相对链接  解析到 _book 下的路径（支持 foo -> foo.html / foo/index.html 的
                clean-url 形式），文件或目录不存在即报错；跳出 _book 的也报错。
  纯锚点 #x     检查同一页面里有没有 id/name 等于 x。
  本站绝对链接  按路径解析回 _book 后同样判定存在性。
  外部绝对链接  按域名归类统计；mlhp.stanford.edu 单独列出（本站是译本，指向上游
                站点的跳转要逐条确认是不是有意保留）。
  data:/mailto/ 只统计，不判定。

另附：指向 .qmd/.md 的链接（源码链接，允许）、带 .html 后缀但站内没有该文件的链接。
脚本不联网，外部链接只做归类不做请求。
"""
import os
import re
import sys
import posixpath
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

BOOK = sys.argv[1] if len(sys.argv) > 1 else "_book"
SELF_HOST_HINTS = ("codingpracticegroup.github.io",)
UPSTREAM_HOSTS = ("mlhp.stanford.edu",)

ATTR_BY_TAG = {
    "a": ["href"],
    "img": ["src", "data-src"],
    "script": ["src"],
    "link": ["href"],
    "iframe": ["src"],
    "source": ["src"],
    "use": ["href", "xlink:href"],
    "form": ["action"],
}


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []   # (tag, attr, value, line)
        self.ids = set()
        self.in_pre = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("pre", "code"):
            self.in_pre += 1
        d = dict(attrs)
        for name in ("id", "name"):
            if d.get(name):
                self.ids.add(d[name])
        if tag in ATTR_BY_TAG and not self.in_pre:
            for attr in ATTR_BY_TAG[tag]:
                v = d.get(attr)
                if v:
                    self.refs.append((tag, attr, v, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in ("pre", "code") and self.in_pre:
            self.in_pre -= 1


def html_files(root):
    out = []
    for dirpath, _dirs, names in os.walk(root):
        if "site_libs" in dirpath.split(os.sep):
            continue
        for n in sorted(names):
            if n.endswith(".html"):
                out.append(os.path.join(dirpath, n))
    return sorted(out)


def web_path(fs_path):
    """_book/src/chap1.html -> src/chap1.html"""
    rel = os.path.relpath(fs_path, BOOK).replace(os.sep, "/")
    return rel


def resolve(base_web, target):
    """把站内相对路径解析成 _book 下的规范 web 路径（带 .html）。"""
    joined = posixpath.normpath(posixpath.join(posixpath.dirname(base_web), target))
    joined = joined.lstrip("./")
    if joined.startswith("../"):
        return None  # 跳出站点根
    if joined.endswith("/"):
        joined += "index.html"
    if joined == "":
        joined = "index.html"
    for cand in (joined, joined + ".html", posixpath.join(joined, "index.html")):
        if os.path.isfile(os.path.join(BOOK, cand)):
            return cand.replace(os.sep, "/")
    return joined  # 未找到，原样返回以便报错


def main():
    files = html_files(BOOK)
    if not files:
        print(f"没找到 HTML：{BOOK}/")
        return 1
    parsed = {}
    for f in files:
        c = Collector()
        with open(f, encoding="utf-8", errors="ignore") as fh:
            c.feed(fh.read())
        parsed[web_path(f)] = c

    broken, outside, upstream, ext_hosts, mailish, src_links = [], [], [], {}, [], []
    total = 0
    for page, c in parsed.items():
        for tag, attr, val, line in c.refs:
            raw = val.strip()
            if not raw or raw.startswith(("data:", "javascript:", "blob:")):
                continue
            total += 1
            where = f"{page}:{line}"
            u = urlparse(raw)
            host = (u.hostname or "").lower()
            if u.scheme == "mailto":
                mailish.append((where, raw))
                continue
            if u.scheme in ("http", "https"):
                if any(h in host for h in UPSTREAM_HOSTS):
                    upstream.append((where, raw, u.fragment))
                elif any(h in host for h in SELF_HOST_HINTS):
                    target = unquote(u.path)
                    target = re.sub(r"^/mlhp/", "/", target)
                    rp = resolve("index.html", target.lstrip("/"))
                    if rp is None or not os.path.isfile(os.path.join(BOOK, rp)):
                        broken.append((where, raw, "站内绝对链接指向的页面不存在"))
                else:
                    ext_hosts[host] = ext_hosts.get(host, 0) + 1
                continue
            if u.scheme:
                continue
            frag = u.fragment
            if raw.startswith("#"):
                if frag and frag not in c.ids and not frag.startswith(("~1", "/")):
                    broken.append((where, raw, "锚点在本页没有对应 id/name"))
                continue
            path = unquote(u.path)
            if not path:
                continue
            rp = resolve(page, path)
            if rp is None:
                outside.append((where, raw, "解析后跳出站点根目录"))
                continue
            if not os.path.isfile(os.path.join(BOOK, rp)):
                broken.append((where, raw, f"目标不存在（解析为 {rp}）"))
                continue
            if frag:
                tpath = os.path.join(BOOK, rp)
                tids = parsed.get(rp)
                if tids is None:
                    cc = Collector()
                    with open(tpath, encoding="utf-8", errors="ignore") as fh:
                        cc.feed(fh.read())
                    tids = cc
                    parsed[rp] = cc
                if frag not in tids.ids:
                    broken.append((where, raw, f"目标页 {rp} 里没有锚点 #{frag}"))
            if re.search(r"\.(qmd|md|ipynb|bib|py|ipynb)$", path):
                src_links.append((where, raw))

    print(f"扫描页面 {len(files)} 个，引用 {total} 条")
    print(f"  站内引用解析通过：{total - len(broken) - len(outside)} 条（含指向本站自身的绝对链接）")
    print(f"  跳出站点根：{len(outside)} 条")
    print(f"  断链/锚点缺失：{len(broken)} 条")
    print(f"  指向上游 mlhp.stanford.edu：{len(upstream)} 条")
    print(f"  指向本站源码文件（.qmd/.md 等）：{len(src_links)} 条")
    print(f"  mailto：{len(mailish)} 条")
    print("  外部域名分布：")
    for h, n in sorted(ext_hosts.items(), key=lambda kv: -kv[1]):
        print(f"      {n:>4}  {h}")

    def show(title, items, extra=lambda r: ""):
        print(f"\n### {title}（{len(items)} 条）")
        for it in items[:60]:
            print("  " + " | ".join(str(x) for x in it) + extra(it))
        if len(items) > 60:
            print(f"  ……另有 {len(items) - 60} 条，用 --all 查看完整列表" if "--all" in sys.argv else
                  f"  ……另有 {len(items) - 60} 条")

    if broken:
        show("断链 / 锚点缺失", broken)
    if outside:
        show("跳出站点根目录", outside)
    if upstream:
        show("指向上游站点", upstream)
    return 0 if not broken and not outside else 2


if __name__ == "__main__":
    sys.exit(main())
