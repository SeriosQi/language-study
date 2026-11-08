# -*- coding: utf-8 -*-
"""法语 B1–B2 精读跟读页面（当前为 v2），精读 / 通读 / 跟读三种模式。

用法：在这个文件夹里运行  python build.py
默认读取同目录的 template.html，生成上一级文件夹里的 index.html。
也可以指定路径：python build.py 模板.html 输出.html
"""
import html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from articles import A1, A2
from shadow_data import CHUNKS, PRON, RULES

TPL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "template.html")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "index.html")

E = html.escape
NB, NNB = " ", " "

def fix(s):
    """French typography: curly apostrophe, no-break space before ; : ? ! and inside « »."""
    s = s.replace("'", "’")
    for p in (" ;", " :", " ?", " !"):
        s = s.replace(p, NNB + p[1])
    return s.replace("« ", "«" + NB).replace(" »", NB + "»")

def norm(x):
    if isinstance(x, str):
        return fix(x)
    if isinstance(x, list):
        return [norm(i) for i in x]
    if isinstance(x, tuple):
        return tuple(norm(i) for i in x)
    if isinstance(x, dict):
        return {k: (v if k in ("ipa", "kind", "pos", "id") else norm(v)) for k, v in x.items()}
    return x

A1, A2 = norm(A1), norm(A2)
CHUNKS = {k: fix(v) for k, v in CHUNKS.items()}
PRON = {k: [(fix(w), ipa, rules, fix(note)) for (w, ipa, rules, note) in v] for k, v in PRON.items()}
RULES = [(k, s, n1, n2, fix(exp)) for (k, s, n1, n2, exp) in RULES]
RULE = {r[0]: r for r in RULES}

POS = {"nm": ("阳性名词", "n.m."), "nf": ("阴性名词", "n.f."), "v": ("动词", ""), "adj": ("形容词", ""),
       "adv": ("副词", ""), "loc": ("短语", ""), "conj": ("连词", "")}

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

LETTERS = "ABCD"
EXAMPLES = {k: [] for k in RULE}

def rule_chips(keys):
    return "".join(f'<a class="rc" href="#rule-{k}">{E(RULE[k][1])}</a>' for k in keys)

def base_html(span):
    """Display form of an annotated span: ‿ = link these words, | = no liaison here."""
    out = []
    for ch in span:
        if ch == "‿":
            out.append('<span class="lk" aria-hidden="true">‿</span>')
        elif ch == "|":
            out.append('<span class="nl" title="这里不能连" aria-hidden="true"> ǀ </span>')
        else:
            out.append(E(ch))
    return "".join(out)

def render_shadow(aid, sno, fr):
    chunks = [c.strip() for c in CHUNKS[(aid, sno)].split(" / ")]
    if " ".join(chunks) != fr:
        sys.exit(f"[{aid} s{sno}] chunks do not rebuild the sentence")
    starts, pos = [], 0
    for c in chunks:
        starts.append(pos)
        pos += len(c) + 1
    spans, cur = [], 0
    for marked, ipa, rules, note in PRON.get((aid, sno), []):
        word = marked.replace("‿", " ").replace("|", " ")
        p = fr.find(word, cur)
        if p < 0:
            sys.exit(f"[{aid} s{sno}] pron span not found: {word!r}")
        ci = max(i for i, s in enumerate(starts) if s <= p)
        if p + len(word) > starts[ci] + len(chunks[ci]):
            sys.exit(f"[{aid} s{sno}] pron span crosses a chunk: {word!r}")
        for r in rules:
            if r not in RULE:
                sys.exit(f"unknown rule {r}")
            if len(EXAMPLES[r]) < 6 and word not in [w for w, _ in EXAMPLES[r]]:
                EXAMPLES[r].append((marked, ipa))
        spans.append((p, p + len(word), marked, word, ipa, rules, note))
        cur = p + len(word)
    parts = []
    for i, c in enumerate(chunks):
        s0, s1 = starts[i], starts[i] + len(c)
        out, k = [], s0
        for (a, b, marked, word, ipa, rules, note) in spans:
            if a >= s0 and b <= s1:
                out.append(E(fr[k:a]))
                out.append(f'<ruby class="pr"><rb>{base_html(marked)}</rb><rt>{E(ipa)}</rt></ruby>')
                k = b
        out.append(E(fr[k:s1]))
        if i:
            parts.append('<span class="sep" aria-hidden="true">/</span>')
        parts.append(f'<span class="ck" role="button" tabindex="0" data-t="{E(c)}" data-start="{s0}" '
                     f'title="从这一块开始读到句尾">{"".join(out)}</span>')
    items = "".join(
        f'<li><span class="pw" lang="fr">{base_html(marked)}</span>{say(word, "朗读 " + word, "sm")}'
        f'<span class="pp">[{E(ipa)}]</span><span class="rcs">{rule_chips(rules)}</span>'
        f'<span class="pn">{E(note)}</span></li>'
        for (_, _, marked, word, ipa, rules, note) in spans)
    plist = (f'<div class="pron"><p class="pron-h">本句发音要点</p><ul class="pron-list">{items}</ul></div>'
             if items else '<div class="pron"><p class="pron-h">本句没有需要特别注意的连读</p></div>')
    return (f'<div class="sh">'
            f'<p class="sh-text" lang="fr">{"".join(parts)}</p>'
            f'<div class="pl">'
            f'<button class="pl-btn" type="button" aria-label="播放这句">{PLAY}{PAUSE}</button>'
            f'<div class="pl-track" role="slider" tabindex="0" aria-label="播放位置" aria-valuemin="1">'
            f'<span class="pl-rail"></span></div>'
            f'<span class="pl-pos" aria-hidden="true"></span></div>'
            f'<div class="sh-ctl">'
            f'<button class="btn sm sh-go" type="button">{PLAY}<span class="lbl">跟读这句</span></button>'
            f'<span class="sh-stage" aria-live="polite"></span></div>'
            f'{plist}</div>')

def render_sentence(aid, sno, fr, notes):
    placed = []
    for n in notes:
        pos = fr.find(n["hl"])
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
        out.append(E(fr[cur:s]))
        out.append(f'<mark class="hl {n["kind"]}" data-k="{k}">{E(fr[s:e])}</mark>')
        cur = e
        items.append(render_note(k, n))
    out.append(E(fr[cur:]))
    return (f'<div class="s" id="{aid}-s{sno}" data-text="{E(fr)}">'
            f'<div class="s-side"><span class="s-no" aria-hidden="true">{sno}</span>'
            f'<button class="say say-s" type="button" aria-label="朗读第{sno}句" title="朗读这句">{SPK}</button></div>'
            f'<p class="s-text" lang="fr">{"".join(out)}</p>'
            f'{render_shadow(aid, sno, fr)}'
            f'<ul class="notes">{"".join(items)}</ul></div>')

def render_note(k, n):
    if n["kind"] == "v":
        zh, abbr = POS[n["pos"]]
        g = " g-" + n["pos"][1] if n["pos"] in ("nm", "nf") else ""
        chip = f'<span class="pos{g}">{E(zh)}{(" " + E(abbr)) if abbr else ""}</span>'
        extra = f'<p class="extra">{E(n["extra"])}</p>' if n["extra"] else ""
        return (f'<li class="note v" data-k="{k}"><span class="tag">词</span><div class="nb">'
                f'<p class="head"><span class="w" lang="fr">{E(n["word"])}</span>'
                f'{say(n["word"], "朗读 " + n["word"], "sm")}'
                f'<span class="ipa">{E(n["ipa"])}</span>{chip}'
                f'<span class="mean">{E(n["mean"])}</span></p>{extra}</div></li>')
    ex = ""
    if n["ex"]:
        ex = (f'<p class="ex"><span class="ex-ko" lang="fr">{E(n["ex"])} {say(n["ex"], "朗读例句", "sm")}</span>'
              f'<span class="ex-zh">{E(n["ex_zh"])}</span></p>')
    return (f'<li class="note g" data-k="{k}"><span class="tag">语法</span><div class="nb">'
            f'<p class="head"><span class="w pat" lang="fr">{E(n["pat"])}</span>'
            f'<span class="mean">{E(n["gloss"])}</span></p>'
            f'<p class="exp">{E(n["exp"])}</p>{ex}</div></li>')

def render_quiz(qs):
    parts = []
    for q in qs:
        ctx = f'<p class="q-ctx" lang="fr">{E(q["ctx"])}</p>' if q.get("ctx") else ""
        opts = "".join(f'<li><span class="o-no">{LETTERS[i]}</span><span lang="fr">{E(o)}</span></li>'
                       for i, o in enumerate(q["opts"]))
        parts.append(
            f'<div class="q"><p class="q-head"><span class="q-no">{q["no"]}.</span>'
            f'<span lang="fr">{E(q["q"])}</span></p>{ctx}<ol class="opts">{opts}</ol>'
            f'<details><summary>看答案与解析</summary><p class="ans"><b>答案 {LETTERS[q["ans"]-1]}</b>'
            f'{E(q["why"])}</p></details></div>')
    return "".join(parts)

def render_article(a):
    sno, nv, ng, body = 0, 0, 0, []
    for pi, para in enumerate(a["paras"], 1):
        sents = []
        for fr, notes in para:
            sno += 1
            nv += sum(n["kind"] == "v" for n in notes)
            ng += sum(n["kind"] == "g" for n in notes)
            sents.append(render_sentence(a["id"], sno, fr, notes))
        body.append(f'<section class="para"><p class="p-label">第{pi}段</p>'
                    f'<div class="p-body">{"".join(sents)}</div></section>')
    meta = f'{a["genre"]} · {len(a["paras"])}段 {sno}句 · 生词{nv} · 语法{ng}'
    return (f'<article class="art" id="{a["id"]}">'
            f'<header class="a-head"><p class="eyebrow">{a["no"]}</p>'
            f'<h2 lang="fr">{E(a["title"])}</h2><p class="a-zh">{E(a["title_zh"])}</p>'
            f'<p class="a-meta">{E(meta)}</p>'
            f'<button class="btn play-all" type="button" data-art="{a["id"]}">{SPK}<span class="lbl">朗读全文</span></button></header>'
            f'{"".join(body)}'
            f'<section class="quiz"><h3>练习</h3>{render_quiz(a["quiz"])}</section></article>')

def render_rules():
    cards = []
    for key, short, fr_name, zh_name, exp in RULES:
        ex = "".join(f'<li><span lang="fr">{base_html(w)}</span><span class="pp">[{E(p)}]</span></li>'
                     for w, p in EXAMPLES[key])
        exlist = f'<ul class="rule-ex">{ex}</ul>' if ex else ""
        cards.append(f'<div class="rule" id="rule-{key}"><h4>{E(zh_name)} <span lang="fr">{E(fr_name)}</span></h4>'
                     f'<p>{E(exp)}</p>{exlist}</div>')
    return (f'<section class="rules" id="rules"><h2>发音规则速查</h2>'
            f'<p class="rules-lead">两篇文章里出现的发音现象共 {len(RULES)} 类，例子都取自本文。读音用国际音标标注，. 是音节分界。</p>'
            f'{"".join(cards)}</section>')

tpl = open(TPL, encoding="utf-8").read()
articles = render_article(A1) + render_article(A2)
page = tpl.replace("<!--ARTICLES-->", articles).replace("<!--RULES-->", render_rules())
open(OUT, "w", encoding="utf-8").write(page)
n_pron = sum(len(v) for v in PRON.values())
print("ok", len(page), "pron entries:", n_pron)
