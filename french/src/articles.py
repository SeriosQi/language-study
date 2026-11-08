# -*- coding: utf-8 -*-
"""法语 v2（B1–B2）两篇文章的全部内容：句子、生词（词性、阴阳性、音标）、语法讲解、练习题。
题材和 v1 相同，句子更短、用词更常见。改文章内容只改这个文件，然后重新运行 build.py。

V(原句中要标出的片段, 词条原形, 词性, 音标, 中文释义, 补充说明)
G(原句中要标出的片段, 句型, 中文意思, 讲解, 法语例句, 例句中文)
词性代码：nm 阳性名词，nf 阴性名词，v 动词，adj 形容词，adv 副词，loc 短语。
撇号和标点前的空格在 build.py 里统一处理，这里直接用普通的 ' 和空格。
"""

def V(hl, word, pos, ipa, mean, extra=None):
    return dict(kind="v", hl=hl, word=word, pos=pos, ipa=ipa, mean=mean, extra=extra)

def G(hl, pat, gloss, exp, ex=None, ex_zh=None):
    return dict(kind="g", hl=hl, pat=pat, gloss=gloss, exp=exp, ex=ex, ex_zh=ex_zh)

A1 = dict(
    id="a1", no="文章一", genre="说明文 · 科学与健康",
    title="Dormir pour mieux apprendre",
    title_zh="睡好觉，学得更好",
    paras=[
        [
            ("Pendant longtemps, on a pensé que le sommeil était seulement un moment de repos.", [
                G("Pendant longtemps", "pendant + 时间", "在……期间；很长时间以来",
                  "pendant longtemps＝很长一段时间里。",
                  "J'ai habité à Lyon pendant deux ans.", "我在里昂住过两年。"),
                G("on a pensé", "on（泛指主语）", "人们",
                  "on 指\"人们、大家\"，动词用第三人称单数。口语里 on 也常代替 nous。",
                  "En France, on mange tard.", "在法国，人们晚饭吃得晚。"),
                V("sommeil", "sommeil", "nm", "/sɔ.mɛj/", "睡眠", "avoir sommeil＝困了"),
                G("était", "未完成过去时 imparfait", "（当时）是",
                  "描述过去的状态或看法。主句 on a pensé 用复合过去时，从句的 était 用未完成过去时，这是转述过去想法的常见搭配。",
                  "Il a dit qu'il était fatigué.", "他说他累了。"),
                V("seulement", "seulement", "adv", "/sœl.mɑ̃/", "只、仅仅", "近义 ne … que"),
                V("repos", "repos", "nm", "/ʁə.po/", "休息", "se reposer＝休息"),
            ]),
            ("Selon cette idée, le cerveau ne faisait presque rien pendant la nuit.", [
                G("Selon", "selon", "根据、按照",
                  "selon + 名词＝按照……的说法。",
                  "Selon la météo, il va pleuvoir.", "天气预报说要下雨。"),
                V("cerveau", "cerveau", "nm", "/sɛʁ.vo/", "大脑", "复数 cerveaux"),
                G("ne faisait presque rien", "ne … rien", "（几乎）什么也不做",
                  "ne … rien＝什么都不。presque＝几乎。faisait 是 faire 的未完成过去时。",
                  "Je n'ai rien compris.", "我什么也没听懂。"),
            ]),
            ("Aujourd'hui, les scientifiques savent que ce n'est pas vrai.", [
                V("Aujourd'hui", "aujourd'hui", "adv", "/o.ʒuʁ.dɥi/", "今天；如今"),
                V("scientifiques", "scientifique", "nm", "/sjɑ̃.ti.fik/", "科学家", "也可作形容词：科学的"),
                G("savent que", "savoir que + 句子", "知道……",
                  "savoir 的现在时：je sais, nous savons, ils savent。"),
                G("ce n'est pas vrai", "ne … pas", "这不对",
                  "否定句用 ne … pas 夹住动词：c'est → ce n'est pas。"),
            ]),
            ("Quand nous dormons, notre cerveau continue à travailler : il trie les informations de la journée et garde les plus importantes.", [
                G("Quand nous dormons", "quand + 现在时", "当……的时候",
                  "quand 引出时间从句。dormir 的现在时：je dors, nous dormons。",
                  "Quand il pleut, je reste à la maison.", "下雨的时候我待在家里。"),
                G("continue à travailler", "continuer à + 不定式", "继续做……",
                  "continuer à 和 continuer de 都可以。",
                  "Elle continue à étudier le soir.", "她晚上继续学习。"),
                V("trie", "trier", "v", "/tʁi.je/", "分类、整理", "le tri des déchets＝垃圾分类"),
                V("informations", "information", "nf", "/ɛ̃.fɔʁ.ma.sjɔ̃/", "信息", "-tion 结尾的名词都是阴性"),
                V("garde", "garder", "v", "/ɡaʁ.de/", "保留、留下"),
                G("les plus importantes", "最高级 le / la / les plus + 形容词", "最重要的（那些）",
                  "最高级要和所指的名词性数一致：这里指 les informations（阴性复数），所以是 les plus importantes。",
                  "C'est la ville la plus grande du pays.", "这是这个国家最大的城市。"),
            ]),
        ],
        [
            ("Le sommeil se compose de plusieurs phases qui se répètent environ toutes les quatre-vingt-dix minutes.", [
                G("se compose de", "se composer de", "由……组成",
                  "代词式动词，意思和 être composé de 一样。",
                  "L'équipe se compose de cinq personnes.", "这个团队由五个人组成。"),
                V("phases", "phase", "nf", "/faz/", "阶段", "英 phase"),
                G("qui se répètent", "关系代词 qui", "……的（在从句里作主语）",
                  "qui 代替前面的 phases，在从句里作主语。se répéter＝重复。"),
                V("environ", "environ", "adv", "/ɑ̃.vi.ʁɔ̃/", "大约"),
                G("toutes les quatre-vingt-dix minutes", "tous / toutes les + 时间", "每隔……",
                  "toutes les heures＝每小时，tous les jours＝每天。minutes 是阴性，所以用 toutes。",
                  "Le bus passe toutes les dix minutes.", "公交车每十分钟一班。"),
            ]),
            ("Pendant le sommeil profond, le cerveau « rejoue » ce que nous avons vécu dans la journée.", [
                V("profond", "profond", "adj", "/pʁɔ.fɔ̃/", "深的", "le sommeil profond＝深度睡眠"),
                V("rejoue", "rejouer", "v", "/ʁə.ʒwe/", "重放、重演", "re- 表示\"再\"；加引号表示比喻"),
                G("ce que nous avons vécu", "ce que", "……的事情（作宾语）",
                  "ce que＝……的东西、……的事情。vécu 是 vivre 的过去分词。",
                  "Je ne comprends pas ce que tu dis.", "我听不懂你说的话。"),
                V("journée", "journée", "nf", "/ʒuʁ.ne/", "一天（白天）", "jour 多指日期，journée 强调一整天的时间"),
            ]),
            ("C'est ce qui nous aide à transformer ces souvenirs récents en souvenirs durables.", [
                G("C'est ce qui", "c'est ce qui", "正是这个……",
                  "ce qui 在从句里作主语。c'est ce qui nous aide＝正是这个帮助我们。"),
                G("nous aide à", "aider qqn à + 不定式", "帮助某人做……",
                  "宾语代词 nous 放在动词前面。",
                  "Il m'aide à porter mes valises.", "他帮我提行李。"),
                G("transformer", "transformer A en B", "把A变成B",
                  "en 后面接变成的结果。"),
                V("souvenirs", "souvenir", "nm", "/su.və.niʁ/", "记忆、回忆", "易混：英语 souvenir 是\"纪念品\""),
                V("récents", "récent", "adj", "/ʁe.sɑ̃/", "最近的"),
                V("durables", "durable", "adj", "/dy.ʁabl/", "持久的", "le développement durable＝可持续发展"),
            ]),
            ("Pendant le sommeil paradoxal, celui des rêves, le cerveau crée aussi des liens entre des idées différentes.", [
                V("paradoxal", "sommeil paradoxal", "loc", "/sɔ.mɛj pa.ʁa.dɔk.sal/", "快速眼动睡眠（REM）", "大脑活跃、身体放松，大部分梦出现在这个阶段"),
                G("celui des rêves", "指示代词 celui", "……的那个",
                  "celui 代替前面的阳性单数名词 le sommeil：celui des rêves＝做梦的那种睡眠。le rêve＝梦。"),
                V("crée", "créer", "v", "/kʁe.e/", "创造、建立"),
                V("liens", "lien", "nm", "/ljɛ̃/", "联系", "un lien entre A et B＝A和B之间的联系"),
                V("différentes", "différent", "adj", "/di.fe.ʁɑ̃/", "不同的", "阴性 différente"),
            ]),
            ("C'est peut-être pour cela qu'on trouve parfois, au réveil, la solution d'un problème difficile.", [
                G("C'est peut-être pour cela qu'on", "c'est pour cela que", "这（也许）就是为什么……",
                  "意思和 c'est pourquoi 一样。peut-être＝也许。",
                  "Il était malade, c'est pour cela qu'il n'est pas venu.", "他病了，所以没来。"),
                V("parfois", "parfois", "adv", "/paʁ.fwa/", "有时"),
                V("au réveil", "au réveil", "loc", "/o ʁe.vɛj/", "醒来时", "se réveiller＝醒来"),
                V("solution", "solution", "nf", "/sɔ.ly.sjɔ̃/", "解决办法", "la solution d'un problème"),
            ]),
        ],
        [
            ("Ces découvertes ont des conséquences très concrètes pour les étudiants.", [
                V("découvertes", "découverte", "nf", "/de.ku.vɛʁt/", "发现", "découvrir＝发现"),
                V("conséquences", "conséquence", "nf", "/kɔ̃.se.kɑ̃s/", "后果、影响"),
                V("concrètes", "concret", "adj", "/kɔ̃.kʁɛ/", "具体的、实际的", "阴性 concrète"),
            ]),
            ("Un étudiant qui ne dort pas la nuit avant un examen pense gagner du temps, mais en réalité, il risque d'oublier une partie de ce qu'il a appris.", [
                V("examen", "examen", "nm", "/ɛɡ.za.mɛ̃/", "考试", "passer un examen＝参加考试，réussir un examen＝考过"),
                G("pense gagner du temps", "penser + 不定式", "以为能节省时间",
                  "主语相同时，penser 后面直接接不定式。gagner du temps＝节省时间。",
                  "Il pense partir demain.", "他打算明天走。"),
                G("en réalité", "en réalité", "实际上",
                  "和前面的想法形成对比。"),
                G("risque d'oublier", "risquer de + 不定式", "可能会……（坏结果）",
                  "表示有可能发生不好的事。",
                  "Dépêche-toi, tu risques de rater le train.", "快点，不然你会赶不上火车。"),
                V("partie", "partie", "nf", "/paʁ.ti/", "部分", "une partie de＝……的一部分"),
                G("ce qu'il a appris", "ce que + 复合过去时", "他学过的东西",
                  "appris 是 apprendre 的过去分词。"),
            ]),
            ("À l'inverse, une courte sieste après une séance de travail peut améliorer la mémoire.", [
                G("À l'inverse", "à l'inverse", "相反地",
                  "引出相反的情况。"),
                V("sieste", "sieste", "nf", "/sjɛst/", "午睡、小睡", "faire la sieste＝睡午觉"),
                V("séance", "séance", "nf", "/se.ɑ̃s/", "（一段）时间、一次", "une séance de travail＝一段学习时间"),
                G("peut améliorer", "pouvoir + 不定式", "能够……、可以……",
                  "pouvoir 后面直接接不定式。améliorer＝改善。"),
            ]),
            ("Bien dormir n'est donc pas une perte de temps : c'est une partie importante de l'apprentissage.", [
                G("Bien dormir", "不定式作主语", "睡好觉（这件事）",
                  "动词不定式可以直接作主语，相当于中文的\"……这件事\"。",
                  "Apprendre une langue demande du temps.", "学一门语言需要时间。"),
                G("donc", "donc", "所以、因此",
                  "放在动词后面，总结前文。"),
                V("perte", "perte", "nf", "/pɛʁt/", "损失、浪费", "une perte de temps＝浪费时间；perdre＝失去"),
                V("apprentissage", "apprentissage", "nm", "/a.pʁɑ̃.ti.saʒ/", "学习（过程）", "-age 结尾的名词大多是阳性"),
            ]),
        ],
    ],
    quiz=[
        dict(no=1, q="Quelle est l'idée principale du texte ?", opts=[
            "Le cerveau ne travaille pas pendant la nuit.",
            "Le sommeil aide le cerveau à apprendre et à se souvenir.",
            "Il faut dormir plus de dix heures par nuit.",
            "Les rêves n'ont aucune importance."],
            ans=2, why="第4句说睡觉时大脑继续工作，最后一句说睡好觉是学习的重要部分。A 是作者否定的旧看法；C 文中没提；D 和第8句相反。"),
        dict(no=2, q="Vrai ou faux ? Justifiez votre réponse avec une phrase du texte.",
             ctx="Selon le texte, ne pas dormir avant un examen aide à mieux réussir.",
             opts=["Vrai", "Faux"],
             ans=2, why="Faux。依据第11句：il risque d'oublier une partie de ce qu'il a appris。DELF 判断题要抄出原文作依据，只写 Vrai/Faux 不得分。"),
        dict(no=3, q="Dans la phrase 13, « une perte de temps » veut dire :", opts=[
            "du temps gagné", "du temps inutile", "un moment de repos", "un examen difficile"],
            ans=2, why="perte 来自 perdre（失去），une perte de temps＝浪费时间。"),
    ],
)

A2 = dict(
    id="a2", no="文章二", genre="论说文 · 社会与文化",
    title="Lire à l'époque des écrans",
    title_zh="屏幕时代的阅读",
    paras=[
        [
            ("On dit souvent que les jeunes ne lisent plus.", [
                G("On dit souvent que", "on dit que", "人们常说……",
                  "on 是泛指主语，表示\"人们\"。"),
                V("jeunes", "jeune", "nm", "/ʒœn/", "年轻人", "les jeunes 可以指男女；作形容词是\"年轻的\""),
                G("ne lisent plus", "ne … plus", "不再……",
                  "lire 的现在时：ils lisent。这里的 plus 读 [ply]。",
                  "Il ne fume plus.", "他不再抽烟了。"),
            ]),
            ("Pourtant, nous lisons beaucoup chaque jour : des messages, des articles, des publications sur les réseaux sociaux.", [
                V("Pourtant", "pourtant", "adv", "/puʁ.tɑ̃/", "然而、可是", "比 mais 正式，常放在句首"),
                V("chaque", "chaque", "adj", "/ʃak/", "每一个", "后面接单数名词：chaque jour＝每天"),
                V("publications", "publication", "nf", "/py.bli.ka.sjɔ̃/", "发布的内容、帖子"),
                V("réseaux sociaux", "réseau social", "nm", "/ʁe.zo sɔ.sjal/", "社交网络", "-al 结尾的形容词复数变成 -aux"),
            ]),
            ("La vraie question n'est donc pas de savoir si nous lisons, mais comment nous lisons.", [
                V("vraie", "vrai", "adj", "/vʁɛ/", "真正的", "阴性 vraie，读音不变"),
                G("de savoir si", "la question est de savoir si", "问题在于是否……",
                  "si 在这里是\"是否\"，不是\"如果\"。",
                  "Je ne sais pas si elle viendra.", "我不知道她会不会来。"),
                G("mais comment", "ne … pas … mais …", "不是……而是……",
                  "否定前一项，肯定后一项。"),
            ]),
        ],
        [
            ("Sur un écran, nous lisons souvent très vite.", [
                V("écran", "écran", "nm", "/e.kʁɑ̃/", "屏幕"),
                V("vite", "vite", "adv", "/vit/", "快", "形容词是 rapide"),
            ]),
            ("Nous passons d'un texte à l'autre et, parfois, nous lisons seulement les titres.", [
                G("passons d'un texte à l'autre", "passer d'un … à l'autre", "从一个……换到另一个",
                  "表示不停地换来换去。"),
                V("seulement", "seulement", "adv", "/sœl.mɑ̃/", "只"),
                V("titres", "titre", "nm", "/titʁ/", "标题"),
            ]),
            ("D'après certains chercheurs, cette habitude peut rendre plus difficile la lecture de textes longs.", [
                G("D'après", "d'après", "根据……",
                  "意思和 selon 一样。"),
                V("chercheurs", "chercheur", "nm", "/ʃɛʁ.ʃœʁ/", "研究者", "阴性 chercheuse"),
                V("habitude", "habitude", "nf", "/a.bi.tyd/", "习惯", "h 不发音，所以 cette habitude 要连起来读"),
                G("rendre plus difficile", "rendre + 形容词", "使……变得（更难）",
                  "rendre qqch difficile＝使……变难。宾语很长时，形容词可以放到宾语前面：rendre plus difficile la lecture。",
                  "Le froid rend la route dangereuse.", "寒冷让路面变得危险。"),
                V("lecture", "lecture", "nf", "/lɛk.tyʁ/", "阅读", "易混：英语 lecture 是\"讲座\""),
            ]),
            ("En effet, pour lire un livre, il faut rester concentré pendant longtemps.", [
                G("En effet", "en effet", "确实；因为",
                  "用来解释或证实前一句。"),
                G("pour lire", "pour + 不定式", "为了……",
                  "表示目的。",
                  "Je travaille pour gagner de l'argent.", "我工作是为了挣钱。"),
                G("il faut rester", "il faut + 不定式", "必须……、需要……",
                  "无人称结构，主语永远是 il。rester＝保持。",
                  "Il faut boire de l'eau.", "要多喝水。"),
                V("concentré", "concentré", "adj", "/kɔ̃.sɑ̃.tʁe/", "专注的", "se concentrer＝集中注意力"),
            ]),
            ("C'est une capacité qui s'apprend et qui se travaille, un peu comme un muscle.", [
                V("capacité", "capacité", "nf", "/ka.pa.si.te/", "能力"),
                G("qui s'apprend", "代词式动词表被动", "可以学会的",
                  "主语是事物时，代词式动词常带被动意思：s'apprendre＝能学会，se travailler＝能练出来。"),
                G("un peu comme", "un peu comme", "有点像……",
                  "用来打比方。"),
                V("muscle", "muscle", "nm", "/myskl/", "肌肉"),
            ]),
            ("Si on ne l'utilise pas, elle devient plus faible.", [
                G("Si on ne l'utilise pas", "si + 现在时，主句也用现在时", "如果……就……",
                  "说一般规律时，si 从句和主句都用现在时。l' 是宾语代词 la 的省音，指 la capacité。",
                  "Si on chauffe la glace, elle fond.", "冰一加热就会化。"),
                G("devient plus faible", "比较级 plus + 形容词", "变得更弱",
                  "devenir＝变成，现在时 il / elle devient。faible＝弱的。"),
            ]),
        ],
        [
            ("Faut-il pour autant arrêter de lire sur écran ?", [
                G("Faut-il", "疑问倒装", "是否应该……？",
                  "il faut 倒装成 faut-il，t 要连读：[fo.til]。"),
                G("pour autant", "pour autant", "（难道）因此就……",
                  "常用在疑问句和否定句里：\"难道因此就要……吗？\""),
                G("arrêter de lire", "arrêter de + 不定式", "停止做……",
                  "arrêter de faire＝不再做。",
                  "Il a arrêté de fumer.", "他戒烟了。"),
            ]),
            ("Je ne le crois pas, car Internet permet à beaucoup de gens d'accéder facilement au savoir.", [
                G("Je ne le crois pas", "宾语代词 le 指代整句", "我不这么认为",
                  "le 代替上一句的整个意思。"),
                G("car", "car", "因为",
                  "书面语，放在两个分句中间说明原因，不能放在句首。"),
                G("permet à beaucoup de gens d'accéder", "permettre à qqn de + 不定式", "让某人能够……",
                  "accéder à＝获得、进入，à + le 缩合成 au。",
                  "Ce travail me permet de voyager.", "这份工作让我能去旅行。"),
                V("facilement", "facilement", "adv", "/fa.sil.mɑ̃/", "容易地"),
                V("savoir", "savoir", "nm", "/sa.vwaʁ/", "知识", "这里是名词，不是动词\"知道\""),
            ]),
            ("À mon avis, il vaut mieux apprendre à utiliser les deux : l'écran pour s'informer rapidement, le papier pour lire en profondeur.", [
                G("À mon avis", "à mon avis", "我认为",
                  "表达个人观点，写作题常用。"),
                G("il vaut mieux", "il vaut mieux + 不定式", "最好……",
                  "用来提建议。",
                  "Il vaut mieux partir tôt.", "最好早点出发。"),
                G("apprendre à utiliser", "apprendre à + 不定式", "学着做……",
                  "apprendre à faire＝学做某事；apprendre qqch＝学某样东西。"),
                V("s'informer", "s'informer", "v", "/sɛ̃.fɔʁ.me/", "了解信息"),
                V("en profondeur", "en profondeur", "loc", "/ɑ̃ pʁɔ.fɔ̃.dœʁ/", "深入地", "profond＝深的"),
            ]),
            ("Pour cela, il faut aussi savoir éteindre son téléphone de temps en temps.", [
                G("Pour cela", "pour cela", "为此",
                  "cela 指前一句说的事。"),
                G("savoir", "savoir + 不定式", "会、懂得（做）",
                  "savoir faire 表示\"会做、懂得做\"。"),
                V("éteindre", "éteindre", "v", "/e.tɛ̃dʁ/", "关掉（电器）", "反义 allumer＝打开"),
                V("de temps en temps", "de temps en temps", "loc", "/də tɑ̃ zɑ̃ tɑ̃/", "时不时、偶尔"),
            ]),
        ],
    ],
    quiz=[
        dict(no=4, q="Quelle est l'opinion de l'auteur ?", opts=[
            "Il faut arrêter d'utiliser Internet.",
            "Les jeunes ne lisent plus du tout.",
            "Il faut savoir utiliser l'écran et le papier selon ce qu'on veut faire.",
            "Lire sur papier est toujours plus rapide."],
            ans=3, why="依据第12句。A 被第11句否定：作者认为网络让更多人获得知识；B 被第2句否定；D 文中没提。"),
        dict(no=5, q="Vrai ou faux ? Justifiez votre réponse avec une phrase du texte.",
             ctx="D'après le texte, la capacité à rester concentré peut devenir plus faible si on ne l'utilise pas.",
             opts=["Vrai", "Faux"],
             ans=1, why="Vrai。依据第9句：Si on ne l'utilise pas, elle devient plus faible。"),
        dict(no=6, q="Dans la phrase 12, « il vaut mieux » a le même sens que :", opts=[
            "il est préférable de", "il est interdit de", "il est impossible de", "il est rare de"],
            ans=1, why="il vaut mieux faire＝最好做……，和 il est préférable de 意思相同。"),
    ],
)
