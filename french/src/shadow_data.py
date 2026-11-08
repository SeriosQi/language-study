# -*- coding: utf-8 -*-
"""法语 v2 跟读模式的数据：意群断句和发音标注。

CHUNKS[(文章, 句号)] = 原句，用 " / " 隔开意群（节奏组）。
PRON[(文章, 句号)] = [(原文片段, 实际读音, [规则代码], 说明), ...]，按句中顺序排列。
片段里用 ‿ 代替空格表示要连起来读，用 | 代替空格表示这里不能连。
读音用国际音标，. 是音节分界，(ə) (z) (t) 表示可读可不读。
RULES 只列文中用到的规则。
"""

RULES = [
    ("lo", "必须联诵", "liaison obligatoire", "必须联诵",
     "词尾本来不发音的辅音，碰到下一个词开头的元音或哑音 h，要读出来并连到下一个词上。必须连的地方：限定词＋名词（les‿informations、mon‿avis），代词＋动词（nous‿avons），en 后面（en‿effet），固定说法（de temps‿en temps），疑问倒装（faut-il）。s、x 连读成 [z]，d 连读成 [t]。"),
    ("lf", "可选联诵", "liaison facultative", "可连可不连",
     "动词后、多音节副词和介词后可以连，也可以不连。正式朗读和新闻播报多连，日常说话多不连。音标里写成 (z)、(t)。"),
    ("en", "连音", "enchaînement", "连音",
     "词尾本来就发音的辅音，直接连到下一个词开头的元音上，组成新的音节：lire‿un → [li.ʁœ̃]。和联诵的区别是，这个辅音单独说的时候也发音。"),
    ("el", "省音", "élision", "省音",
     "le、la、de、que、ne、se、ce、je 等单音节词碰到元音或哑音 h 开头的词，省掉元音写成撇号（l'utilise、qu'on），和后面的词读成一个音节。"),
    ("ec", "哑音e", "e caduc", "哑音 e 脱落",
     "不带重音符号的 e [ə] 在正常语速下常常不发音，尤其是 se、de、ne、le 这类小词和词中间的 e（seulement → [sœl.mɑ̃]）。音标里写成 (ə)。慢速朗读时一般都读出来。"),
    ("mu", "不发音", "lettres muettes", "不发音的字母",
     "词尾的 s、t、d、x、p 和 e 一般不发音。动词第三人称复数的 -ent 也不发音（lisent → [liz]），但副词里的 -ent 读 [ɑ̃]（souvent → [su.vɑ̃]）。"),
    ("sp", "特殊读音", "cas particuliers", "特殊读音",
     "少数词的读音要单独记：faisait 里的 ai 读 [ə]；dix 在辅音前读 [di]；ne … plus 里的 plus 读 [ply]；ex- 在元音前读 [ɛɡz]（examen → [ɛɡ.za.mɛ̃]）。"),
]

CHUNKS = {
    ("a1", 1): "Pendant longtemps, / on a pensé que le sommeil / était seulement un moment de repos.",
    ("a1", 2): "Selon cette idée, / le cerveau ne faisait presque rien / pendant la nuit.",
    ("a1", 3): "Aujourd'hui, / les scientifiques savent / que ce n'est pas vrai.",
    ("a1", 4): "Quand nous dormons, / notre cerveau continue à travailler : / il trie les informations de la journée / et garde les plus importantes.",
    ("a1", 5): "Le sommeil se compose / de plusieurs phases / qui se répètent / environ toutes les quatre-vingt-dix minutes.",
    ("a1", 6): "Pendant le sommeil profond, / le cerveau « rejoue » / ce que nous avons vécu / dans la journée.",
    ("a1", 7): "C'est ce qui nous aide / à transformer ces souvenirs récents / en souvenirs durables.",
    ("a1", 8): "Pendant le sommeil paradoxal, / celui des rêves, / le cerveau crée aussi des liens / entre des idées différentes.",
    ("a1", 9): "C'est peut-être pour cela / qu'on trouve parfois, / au réveil, / la solution d'un problème difficile.",
    ("a1", 10): "Ces découvertes / ont des conséquences très concrètes / pour les étudiants.",
    ("a1", 11): "Un étudiant / qui ne dort pas la nuit avant un examen / pense gagner du temps, / mais en réalité, / il risque d'oublier / une partie de ce qu'il a appris.",
    ("a1", 12): "À l'inverse, / une courte sieste / après une séance de travail / peut améliorer la mémoire.",
    ("a1", 13): "Bien dormir / n'est donc pas une perte de temps : / c'est une partie importante / de l'apprentissage.",

    ("a2", 1): "On dit souvent / que les jeunes ne lisent plus.",
    ("a2", 2): "Pourtant, / nous lisons beaucoup chaque jour : / des messages, des articles, / des publications sur les réseaux sociaux.",
    ("a2", 3): "La vraie question / n'est donc pas de savoir / si nous lisons, / mais comment nous lisons.",
    ("a2", 4): "Sur un écran, / nous lisons souvent très vite.",
    ("a2", 5): "Nous passons d'un texte à l'autre / et, parfois, / nous lisons seulement les titres.",
    ("a2", 6): "D'après certains chercheurs, / cette habitude peut rendre plus difficile / la lecture de textes longs.",
    ("a2", 7): "En effet, / pour lire un livre, / il faut rester concentré / pendant longtemps.",
    ("a2", 8): "C'est une capacité / qui s'apprend et qui se travaille, / un peu comme un muscle.",
    ("a2", 9): "Si on ne l'utilise pas, / elle devient plus faible.",
    ("a2", 10): "Faut-il pour autant / arrêter de lire sur écran ?",
    ("a2", 11): "Je ne le crois pas, / car Internet permet à beaucoup de gens / d'accéder facilement au savoir.",
    ("a2", 12): "À mon avis, / il vaut mieux apprendre à utiliser les deux : / l'écran pour s'informer rapidement, / le papier pour lire en profondeur.",
    ("a2", 13): "Pour cela, / il faut aussi savoir / éteindre son téléphone / de temps en temps.",
}

PRON = {
    ("a1", 1): [
        ("longtemps", "lɔ̃.tɑ̃", ["mu"], "g、p、s 都不发音"),
        ("on‿a", "ɔ̃.na", ["lo"], "代词＋动词，n 连到 a"),
        ("était", "e.tɛ", ["mu"], "-ait 读 [ɛ]，t 不发音"),
        ("seulement", "sœl.mɑ̃", ["ec"], "中间的 e 不发音"),
        ("repos", "ʁə.po", ["mu"], "s 不发音"),
    ],
    ("a1", 2): [
        ("Selon", "s(ə).lɔ̃", ["ec"], "e 可以脱落"),
        ("cette‿idée", "sɛ.ti.de", ["en"], "cette 的 t 连到 idée"),
        ("faisait", "f(ə).zɛ", ["sp"], "fai- 读 [fə]，不读 [fɛ]"),
    ],
    ("a1", 3): [
        ("Aujourd'hui", "o.ʒuʁ.dɥi", ["el"], "写法里有撇号，读成一个词"),
        ("savent", "sav", ["mu"], "-ent 不发音"),
        ("ce n'est pas", "s(ə).nɛ.pa", ["ec", "el"], "ce 的 e 可以脱落；ne 省音成 n'"),
    ],
    ("a1", 4): [
        ("Quand nous", "kɑ̃.nu", ["mu"], "d 在辅音前不发音"),
        ("les‿informations", "le.zɛ̃.fɔʁ.ma.sjɔ̃", ["lo"], "限定词＋名词，s 读 [z]"),
        ("les plus‿importantes", "le.ply.zɛ̃.pɔʁ.tɑ̃t", ["lo"], "plus 在元音前要连，s 读 [z]"),
    ],
    ("a1", 5): [
        ("se compose", "s(ə).kɔ̃.poz", ["ec"], "se 的 e 可以脱落；s 读 [z]"),
        ("se répètent", "s(ə).ʁe.pɛt", ["ec", "mu"], "-ent 不发音"),
        ("quatre-vingt-dix minutes", "ka.tʁə.vɛ̃.di.mi.nyt", ["sp"], "vingt 的 t 不发音；dix 在辅音前读 [di]"),
    ],
    ("a1", 6): [
        ("profond", "pʁɔ.fɔ̃", ["mu"], "d 不发音"),
        ("rejoue", "ʁ(ə).ʒu", ["ec"], "re 的 e 可以脱落"),
        ("nous‿avons", "nu.za.vɔ̃", ["lo"], "代词＋动词，s 读 [z]"),
    ],
    ("a1", 7): [
        ("nous‿aide", "nu.zɛd", ["lo"], "宾语代词＋动词，s 读 [z]"),
        ("souvenirs", "su.v(ə).niʁ", ["ec", "mu"], "中间的 e 可以脱落；s 不发音"),
    ],
    ("a1", 8): [
        ("des‿idées", "de.zi.de", ["lo"], "限定词＋名词，s 读 [z]"),
        ("différentes", "di.fe.ʁɑ̃t", ["mu"], "词尾的 s 不发音"),
    ],
    ("a1", 9): [
        ("peut-être", "pø.tɛtʁ", ["lo"], "peut 的 t 要连到 être"),
        ("qu'on", "kɔ̃", ["el"], "que 省音"),
        ("d'un", "dœ̃", ["el"], "de 省音"),
    ],
    ("a1", 10): [
        ("concrètes", "kɔ̃.kʁɛt", ["mu"], "词尾的 s 不发音"),
        ("les‿étudiants", "le.ze.ty.djɑ̃", ["lo"], "限定词＋名词，s 读 [z]"),
    ],
    ("a1", 11): [
        ("Un‿étudiant", "œ̃.ne.ty.djɑ̃", ["lo"], "un＋名词，n 连读"),
        ("dort", "dɔʁ", ["mu"], "t 不发音"),
        ("avant‿un‿examen", "a.vɑ̃.(t)œ̃.nɛɡ.za.mɛ̃", ["lf", "lo", "sp"], "avant 后可连；un＋名词必须连；ex- 读 [ɛɡz]"),
        ("mais‿en", "mɛ.(z)ɑ̃", ["lf"], "mais 后可连可不连"),
        ("d'oublier", "du.bli.je", ["el"], "de 省音"),
        ("qu'il‿a appris", "ki.la.a.pʁi", ["en", "mu"], "il 的 l 连到 a；appris 的 s 不发音"),
    ],
    ("a1", 12): [
        ("l'inverse", "lɛ̃.vɛʁs", ["el"], "la 省音"),
        ("après‿une", "a.pʁɛ.(z)yn", ["lf"], "après 后可连可不连"),
        ("peut‿améliorer", "pø.(t)a.me.ljɔ.ʁe", ["lf"], "动词后 t 可连可不连"),
    ],
    ("a1", 13): [
        ("perte de temps", "pɛʁt.də.tɑ̃", ["mu"], "temps 的 p、s 不发音"),
        ("c'est‿une", "sɛ.tyn", ["el", "lf"], "ce 省音；c'est 后面常连"),
        ("l'apprentissage", "la.pʁɑ̃.ti.saʒ", ["el"], "le 省音"),
    ],

    ("a2", 1): [
        ("dit", "di", ["mu"], "t 不发音"),
        ("souvent", "su.vɑ̃", ["mu"], "副词的 -ent 读 [ɑ̃]"),
        ("ne lisent plus", "n(ə).liz.ply", ["ec", "mu", "sp"], "-ent 不发音；ne … plus 里的 plus 读 [ply]"),
    ],
    ("a2", 2): [
        ("Pourtant", "puʁ.tɑ̃", ["mu"], "t 不发音"),
        ("des‿articles", "de.zaʁ.tikl", ["lo"], "限定词＋名词，s 读 [z]"),
        ("réseaux sociaux", "ʁe.zo.sɔ.sjo", ["mu"], "x 不发音"),
    ],
    ("a2", 3): [
        ("vraie", "vʁɛ", ["mu"], "阴性的 e 不发音，和 vrai 读音一样"),
        ("de savoir", "d(ə).sa.vwaʁ", ["ec"], "de 的 e 可以脱落"),
        ("comment nous", "kɔ.mɑ̃.nu", ["mu"], "comment 的 t 不发音"),
    ],
    ("a2", 4): [
        ("Sur‿un‿écran", "sy.ʁœ̃.ne.kʁɑ̃", ["en", "lo"], "r 连到 un；un＋名词，n 连读"),
        ("très vite", "tʁɛ.vit", ["mu"], "très 的 s 在辅音前不发音"),
    ],
    ("a2", 5): [
        ("d'un texte‿à l'autre", "dœ̃.tɛks.ta.lotʁ", ["el", "en"], "de 省音；texte 的 t 连到 à"),
        ("seulement", "sœl.mɑ̃", ["ec"], "中间的 e 不发音"),
    ],
    ("a2", 6): [
        ("D'après", "da.pʁɛ", ["el"], "de 省音"),
        ("cette‿habitude", "sɛ.ta.bi.tyd", ["en"], "哑音 h，t 连到 a"),
        ("plus difficile", "ply.di.fi.sil", ["mu"], "plus 在辅音前读 [ply]"),
        ("textes longs", "tɛkst.lɔ̃", ["mu"], "longs 的 g、s 不发音"),
    ],
    ("a2", 7): [
        ("En‿effet", "ɑ̃.ne.fɛ", ["lo", "mu"], "en 后面必须连；effet 的 t 不发音"),
        ("lire‿un", "li.ʁœ̃", ["en"], "r 连到 un"),
        ("il faut", "il.fo", ["mu"], "t 不发音"),
        ("longtemps", "lɔ̃.tɑ̃", ["mu"], "g、p、s 都不发音"),
    ],
    ("a2", 8): [
        ("C'est‿une", "sɛ.tyn", ["el", "lf"], "ce 省音；c'est 后面常连"),
        ("se travaille", "s(ə).tʁa.vaj", ["ec"], "se 的 e 可以脱落"),
        ("comme‿un", "kɔ.mœ̃", ["en"], "m 连到 un"),
    ],
    ("a2", 9): [
        ("l'utilise", "ly.ti.liz", ["el"], "la 省音成 l'"),
        ("devient", "də.vjɛ̃", ["mu"], "t 不发音"),
    ],
    ("a2", 10): [
        ("Faut-il", "fo.til", ["lo"], "倒装时 t 必须连"),
        ("pour‿autant", "pu.ʁo.tɑ̃", ["en"], "r 连到 autant"),
        ("sur‿écran", "sy.ʁe.kʁɑ̃", ["en"], "r 连到 écran"),
    ],
    ("a2", 11): [
        ("Je ne le", "ʒən.lə", ["ec"], "ne 的 e 常脱落"),
        ("crois", "kʁwa", ["mu"], "s 不发音"),
        ("car‿Internet", "ka.ʁɛ̃.tɛʁ.nɛt", ["en"], "r 连到 Internet；Internet 的 t 发音"),
        ("permet‿à", "pɛʁ.mɛ.(t)a", ["lf"], "动词后 t 可连可不连"),
        ("d'accéder", "dak.se.de", ["el"], "de 省音；cc 读 [ks]"),
    ],
    ("a2", 12): [
        ("mon‿avis", "mɔ̃.na.vi", ["lo", "mu"], "限定词＋名词，n 连读；avis 的 s 不发音"),
        ("vaut mieux", "vo.mjø", ["mu"], "t、x 不发音"),
        ("apprendre‿à", "a.pʁɑ̃.dʁa", ["en"], "dr 连到 à"),
        ("les deux", "le.dø", ["mu"], "x 不发音"),
        ("s'informer", "sɛ̃.fɔʁ.me", ["el"], "se 省音"),
    ],
    ("a2", 13): [
        ("faut‿aussi", "fo.(t)o.si", ["lf"], "动词后 t 可连可不连"),
        ("temps‿en temps", "tɑ̃.zɑ̃.tɑ̃", ["lo"], "固定说法，s 要连读成 [z]"),
    ],
}
