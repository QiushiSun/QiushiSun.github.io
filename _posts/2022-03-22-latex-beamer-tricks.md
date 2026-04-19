---
title: "配置LaTeX Beamer的小技巧"
date: 2022-03-22 12:11:36 +0800
lang: zh
categories:
  - "TeX"
tags:
  - "TeX"
cover: "/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-cover.png"
excerpt: "配置 LaTeX Beamer 的小技巧合集。"
---
分享一些在配置LaTeX Beamer时发现的小技巧



最近为了答辩，魔改了一个有些年份但是自己很喜欢的Beamer模版，因此分享一些在配置中不容易发现的小技巧。

## 1. 控制封面页的Subtitle

如题所示，LaTeX Beamer往往只支持两级标题，但是如果确有需要，可以在subtitle命令内部设置另一个大小字体的文本并且换行达成。可以使用以下命令

```tex
\subtitle{\tiny{Knowledge Distillation based on Programming Languages Pre-Trained models and Its Application}\\[0.8em] \scriptsize{中期进度汇报}}
```

效果预览

![Beamer Cover Subtitle](/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-subtitle.png "Beamer Cover Subtitle")

## 2. 优雅地在BibTeX中引用网页

一般技术博客或网页不会像Research Gate这样的Paper Repositories一样为你生成Bibtex，因此很多时候需要自己动手。

```tex
@misc{T-NLG,
    author = "Corby Rosset",
    title = "Turing-NLG: A 17-billion-parameter language model by Microsoft",
    howpublished = "Website",
    year = {2020},
    month = {3},
    note = {\url{https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/}}
}
```

**How do you get nicely formatted URLs in the bibliography?**

更多参考：[https://www.kronto.org/thesis/tips/url-formatting.html](https://www.kronto.org/thesis/tips/url-formatting.html)

## 3. 如何让caption换行再居中

有时候为了美观，在遇到Caption太长需要换行的时候可能会考虑让未填充完一整行的内容居中，但因为Beamer中不常见太长的Caption，因此以Article来举例（二者的使用方法是一样的）

![Original Caption](/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-caption.png "Original Caption")

上图为默认的换行方式，可以仿照下面的命令来调整居中，但是因为centering和换行符的优先级问题，因此换行符需要protect

```tex
\bicaption{\centering 教师模型在POJ-104数据集和Big Clone Bench数据集微调克隆检测任务的过程}{Performance on the POJ-104 \& Big Clone Bench Dataset, by Fine-Tuning Teacher Nets on \protect\\ \centering Clone Detection Task}
```

![Centered Caption](/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-caption-center.png "Centered Caption")

## 4. Beamer 分栏环境下使用脚注

在Beamer中使用columns环境进行分栏的话，需要特别注意footnote的位置，为了搞清楚这个footnote到底是属于某个column还是整个page，需要显示标注，以下是一个错误示例（在column中单单使用了\footnote命令）

![Beamer Footnote](/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-column-ftnote.png "Beamer Footnote")

使用以下命令显式声明footnote所对应的内容在整张slide的底部出现

```tex
\caption{\scriptsize CNN vs RNN vs Self-Attention vs Fully Connected\footnotemark}

\end{columns}  %分栏环境结束
\footnotetext[1]{$N$代表序列长度，$D$为维度，$K$为卷积核大小}
\end{frame}
```

![Beamer Footnote with footnotetext](/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-column-ftnote-divided.png "Beamer Footnote")

## 5. 调整Beamer插图Caption的大小

有时候想要调整一下Caption的大小，但由于大部分页面都会统一Caption比字符小2号，因此一个个修改似乎是治标不治本，而且在caption命令的内部调整偶尔会导致奇怪的错误。查阅手册后发现Beamer和Article一样支持全局修改。

因此，直接使用下面这个全局命令调整吧

```tex
\captionsetup{font={scriptsize}}
```

看下将默认大小调整为scriptsize的效果。

![Scriptsize Caption](/assets/blog/latex-beamer-tricks/2022-3-latex-beamer-tricks-cpt2script.png "Scriptsize Caption")
