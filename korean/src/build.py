# -*- coding: utf-8 -*-
"""韩语 TOPIK 5–6 级精读跟读页面（当前为 v4：每句进度条、点语块从该处读到句尾）。

用法：在这个文件夹里运行  python build.py
默认读取同目录的 template.html，生成上一级文件夹里的 index.html。
也可以指定路径：python build.py 模板.html 输出.html
"""
import html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from articles import A1, A2
from shadow_data import CHUNKS, PRON, RULES

E = html.escape
TPL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "template.html")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "index.html")

RULE = {r[0]: r for r in RULES}

SPK = ('<svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">'
       '<path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/>'
       '<path d="M16 8.5a4.5 4.5 0 0 1 0 7M18.5 6a8 8 0 0 1 0 12" fill="none" stroke="currentColor" '
       'stroke-width="1.8" stroke-linecap="round"/></svg>')
PLAY = ('<svg viewBox="0 0 24 24" width="13" height="13" aria-hidden="true">'
        '<path d="M7 5v14l12-7z" fill="currentColor"/></svg>')
PAUSE = ('<svg class="ic-pause" viewBox="0 0 24 24" width="13" height="13" aria-hidden="true">'
         '<path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z" fill="currentColor"/></svg>')

def say(text, label, cls=""):
    return (f'<button class="say {cls}" type="button" data-say="{E(text)}" '
            f'aria-label="{E(label)}" title="{E(label)}">{SPK}</button>')

CIRC = "①②③④"
EXAMPLES = {k: [] for k in RULE}

def rule_chips(keys):
    return "".join(f'<a class="rc" href="#rule-{k}">{E(RULE[k][1])}</a>' for k in keys)

def render_shadow(aid, sno, ko):
    raw = CHUNKS[(aid, sno)]
    chunks = [c.strip() for c in raw.split(" / ")]
    if " ".join(chunks) != ko:
        sys.exit(f"[{aid} s{sno}] chunks do not rebuild the sentence")
    starts, pos = [], 0
    for c in chunks:
        starts.append(pos)
        pos += len(c) + 1
    # place pronunciation spans, left to right
    spans, cur = [], 0
    for word, pron, rules, note in PRON.get((aid, sno), []):
        p = ko.find(word, cur)
        if p < 0:
            sys.exit(f"[{aid} s{sno}] pron span not found: {word!r}")
        ci = max(i for i, s in enumerate(starts) if s <= p)
        if p + len(word) > starts[ci] + len(chunks[ci]):
            sys.exit(f"[{aid} s{sno}] pron span crosses a chunk: {word!r}")
        for r in rules:
            if r not in RULE:
                sys.exit(f"unknown rule {r}")
            if len(EXAMPLES[r]) < 6 and word not in [w for w, _ in EXAMPLES[r]]:
                EXAMPLES[r].append((word, pron))
        spans.append((p, p + len(word), word, pron, rules, note))
        cur = p + len(word)
    # chunk html with ruby
    parts = []
    for i, c in enumerate(chunks):
        s0, s1 = starts[i], starts[i] + len(c)
        out, k = [], s0
        for (a, b, word, pron, rules, note) in spans:
            if a >= s0 and b <= s1:
                out.append(E(ko[k:a]))
                out.append(f'<ruby class="pr"><rb>{E(word)}</rb><rt>{E(pron)}</rt></ruby>')
                k = b
        out.append(E(ko[k:s1]))
        if i:
            parts.append('<span class="sep" aria-hidden="true">/</span>')
        parts.append(f'<span class="ck" role="button" tabindex="0" data-t="{E(c)}" data-start="{s0}" '
                     f'title="从这一块开始读到句尾">{"".join(out)}</span>')
    items = "".join(
        f'<li><span class="pw" lang="ko">{E(word)}</span>{say(word, "朗读 " + word, "sm")}'
        f'<span class="pp" lang="ko">[{E(pron)}]</span><span class="rcs">{rule_chips(rules)}</span>'
        f'<span class="pn">{E(note)}</span></li>'
        for (_, _, word, pron, rules, note) in spans)
    plist = (f'<div class="pron"><p class="pron-h">本句音变</p><ul class="pron-list">{items}</ul></div>'
             if items else '<div class="pron"><p class="pron-h">本句没有需要特别注意的音变</p></div>')
    return (f'<div class="sh">'
            f'<p class="sh-text" lang="ko">{"".join(parts)}</p>'
            f'<div class="pl">'
            f'<button class="pl-btn" type="button" aria-label="播放这句">{PLAY}{PAUSE}</button>'
            f'<div class="pl-track" role="slider" tabindex="0" aria-label="播放位置" aria-valuemin="1">'
            f'<span class="pl-rail"></span></div>'
            f'<span class="pl-pos" aria-hidden="true"></span></div>'
            f'<div class="sh-ctl">'
            f'<button class="btn sm sh-go" type="button">{PLAY}<span class="lbl">跟读这句</span></button>'
            f'<span class="sh-stage" aria-live="polite"></span></div>'
            f'{plist}</div>')

def render_sentence(aid, sno, ko, notes):
    placed = []
    for n in notes:
        pos = ko.find(n["hl"])
        if pos < 0:
            sys.exit(f"[{aid} s{sno}] highlight not found: {n['hl']!r}")
        placed.append((pos, pos + len(n["hl"]), n))
    placed.sort(key=lambda t: t[0])
    for (a0, a1, na), (b0, b1, nb) in zip(placed, placed[1:]):
        if b0 < a1:
            sys.exit(f"[{aid} s{sno}] overlap: {na['hl']!r} / {nb['hl']!r}")
    out, cur, items = [], 0, []
    for i, (s, e, n) in enumerate(placed, 1):
        k = f"{aid}-{sno}-{i}"
        out.append(E(ko[cur:s]))
        out.append(f'<mark class="hl {n["kind"]}" data-k="{k}">{E(ko[s:e])}</mark>')
        cur = e
        items.append(render_note(k, n))
    out.append(E(ko[cur:]))
    return (f'<div class="s" id="{aid}-s{sno}" data-text="{E(ko)}">'
            f'<div class="s-side"><span class="s-no" aria-hidden="true">{sno}</span>'
            f'<button class="say say-s" type="button" aria-label="朗读第{sno}句" title="朗读这句">{SPK}</button></div>'
            f'<p class="s-text" lang="ko">{"".join(out)}</p>'
            f'{render_shadow(aid, sno, ko)}'
            f'<ul class="notes">{"".join(items)}</ul></div>')

def render_note(k, n):
    if n["kind"] == "v":
        hj = (f'<span class="hj native">固有词</span>' if n["hanja"] is None
              else f'<span class="hj" lang="ko">{E(n["hanja"])}</span>')
        extra = f'<p class="extra">{E(n["extra"])}</p>' if n["extra"] else ""
        return (f'<li class="note v" data-k="{k}"><span class="tag">词</span><div class="nb">'
                f'<p class="head"><span class="w" lang="ko">{E(n["word"])}</span>{say(n["word"], "朗读 " + n["word"], "sm")}{hj}'
                f'<span class="mean">{E(n["mean"])}</span></p>{extra}</div></li>')
    ex = ""
    if n["ex_ko"]:
        ex = (f'<p class="ex"><span class="ex-ko" lang="ko">{E(n["ex_ko"])} {say(n["ex_ko"], "朗读例句", "sm")}</span>'
              f'<span class="ex-zh">{E(n["ex_zh"])}</span></p>')
    return (f'<li class="note g" data-k="{k}"><span class="tag">语法</span><div class="nb">'
            f'<p class="head"><span class="w pat" lang="ko">{E(n["pat"])}</span>'
            f'<span class="mean">{E(n["gloss"])}</span></p>'
            f'<p class="exp">{E(n["exp"])}</p>{ex}</div></li>')

def render_quiz(qs):
    parts = []
    for q in qs:
        ctx = ""
        if q.get("ctx"):
            a, u, b = q["ctx"]
            ctx = f'<p class="q-ctx" lang="ko">{E(a)}<u>{E(u)}</u>{E(b)}</p>'
        opts = "".join(f'<li><span class="o-no">{CIRC[i]}</span><span lang="ko">{E(o)}</span></li>'
                       for i, o in enumerate(q["opts"]))
        parts.append(
            f'<div class="q"><p class="q-head"><span class="q-no">{q["no"]}.</span>'
            f'<span lang="ko">{E(q["q"])}</span></p>{ctx}<ol class="opts">{opts}</ol>'
            f'<details><summary>看答案与解析</summary><p class="ans"><b>答案 {CIRC[q["ans"]-1]}</b>'
            f'{E(q["why"])}</p></details></div>')
    return "".join(parts)

def render_article(a):
    sno, nv, ng, body = 0, 0, 0, []
    for pi, para in enumerate(a["paras"], 1):
        sents = []
        for ko, notes in para:
            sno += 1
            nv += sum(n["kind"] == "v" for n in notes)
            ng += sum(n["kind"] == "g" for n in notes)
            sents.append(render_sentence(a["id"], sno, ko, notes))
        body.append(f'<section class="para"><p class="p-label">第{pi}段</p>'
                    f'<div class="p-body">{"".join(sents)}</div></section>')
    meta = f'{a["genre"]} · {len(a["paras"])}段 {sno}句 · 生词{nv} · 语法{ng}'
    return (f'<article class="art" id="{a["id"]}">'
            f'<header class="a-head"><p class="eyebrow">{a["no"]}</p>'
            f'<h2 lang="ko">{E(a["title"])}</h2><p class="a-zh">{E(a["title_zh"])}</p>'
            f'<p class="a-meta">{E(meta)}</p>'
            f'<button class="btn play-all" type="button" data-art="{a["id"]}">{SPK}<span class="lbl">朗读全文</span></button></header>'
            f'{"".join(body)}'
            f'<section class="quiz"><h3>练习</h3>{render_quiz(a["quiz"])}</section></article>')

def render_rules():
    cards = []
    for key, short, ko_name, zh_name, exp in RULES:
        ex = "".join(f'<li><span lang="ko">{E(w)}</span><span class="pp" lang="ko">[{E(p)}]</span></li>'
                     for w, p in EXAMPLES[key])
        exlist = f'<ul class="rule-ex">{ex}</ul>' if ex else ""
        cards.append(f'<div class="rule" id="rule-{key}"><h4>{E(zh_name)} <span lang="ko">{E(ko_name)}</span></h4>'
                     f'<p>{E(exp)}</p>{exlist}</div>')
    return (f'<section class="rules" id="rules"><h2>音变速查</h2>'
            f'<p class="rules-lead">两篇文章里出现的音变共 {len(RULES)} 类，例词都取自本文。读音以《标准国语大辞典》为准。</p>'
            f'{"".join(cards)}</section>')

tpl = open(TPL, encoding="utf-8").read()
articles = render_article(A1) + render_article(A2)
page = tpl.replace("<!--ARTICLES-->", articles).replace("<!--RULES-->", render_rules())
open(OUT, "w", encoding="utf-8").write(page)
n_pron = sum(len(v) for v in PRON.values())
print("ok", len(page), "pron entries:", n_pron)
