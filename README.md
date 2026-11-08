# 外语学习 · language-study

韩语和法语的精读跟读网页。每句单独成行，生词和语法按出现顺序紧跟在句子下面；跟读模式按意群断句，每句一条进度条，标出连读和音变。

**在线打开：** https://seriosqi.github.io/language-study/

| 页面 | 难度 | 内容 |
| --- | --- | --- |
| [韩语：TOPIK 5–6级精读跟读](https://seriosqi.github.io/language-study/korean/) | TOPIK II 5–6 级 | 「인공지능 진단, 의사를 대체할 수 있을까」（说明文）、「보고 싶은 것만 보는 시대」（论说文） |
| [法语：B1–B2 精读跟读](https://seriosqi.github.io/language-study/french/) | DELF B1–B2 | «Dormir pour mieux apprendre»（说明文）、«Lire à l'époque des écrans»（论说文） |

## 功能

- **精读**：每句下面按出现顺序列出生词和语法。韩语汉字词标繁体汉字；法语生词标词性、阴阳性和国际音标。每个词和例句都能点喇叭听。
- **通读**：收起所有讲解，只剩原文，适合限时阅读。
- **跟读**：
  - 句子按意群用 / 分开，读音和拼写不同的地方在上方标出实际读音。
  - 每句一条进度条，可以暂停、继续、点击或拖动跳转；点句子里任意一块，从这块读到句尾。
  - 「跟读这句」分三步：听整句 → 逐块跟读（每块后留出停顿）→ 再听整句。
- **练习题**：韩语仿照 TOPIK II，法语仿照 DELF，附答案和解析。

## 使用

- 直接打开上面的网址，手机和电脑都可以。
- 也可以下载仓库，双击 `index.html` 在本地打开，不需要联网，也不需要安装任何东西。
- 朗读用的是浏览器自带的语音，Edge 的 Natural 语音效果最好。Chrome 也能用，但进度条只能按时间估算。没有网络时，字体和在线语音会换成系统自带的，功能不受影响。

## 目录

```
index.html          首页
korean/index.html   韩语页面（由 korean/src 生成）
french/index.html   法语页面（由 french/src 生成）
*/src/
  articles.py       文章、生词、语法、练习题
  shadow_data.py    意群断句、读音标注、发音规则
  build.py          生成页面的脚本
  template.html     页面样式和交互代码
```

## 修改

需要 Python 3，不用装其他东西。改 `src/` 里的文件后，在该 `src/` 文件夹里运行：

```
python build.py
```

就会重新生成上一级的 `index.html`。如果某处标注在原句里找不到，或者意群拼不回原句，脚本会报错并指出是哪一句。

## 版本

用 git 标签记录每个版本，在仓库的 Tags 页可以看到并下载任意一版。

- `korean-v4`：韩语第 4 版，跟读模式加进度条。
- `french-v2`：法语第 2 版，难度从 B2–C1 降到 B1–B2。

更早的版本保存在作者的本地存档里。
