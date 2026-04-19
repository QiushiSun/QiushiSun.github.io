---
title: "快速为 Hexo-Icarus 配置 MathJax（2022）"
date: 2022-07-17 21:00:03 +0800
lang: zh
categories:
  - "Blog"
tags:
  - "Blog"
excerpt: "如何让自己的博客能可靠地渲染数学公式？快速为 Hexo-Icarus 配置 MathJax。"
---
如何让自己的博客能可靠地渲染数学公式？这是个问题。



## 前言

前几天在将hugo博客迁移到Hexo-Icarus后，发现了MathJax无法正常工作的问题。在搜索引擎搜索的话，会得到一些类似的答案，尤其是csdn上的答案，不仅不完全正确，而且因博主们持续不断地互相抄袭，这些答案早就不适合2022年的hexo-icarus了，真正可靠的答案很少，而且都被淹没在了这些垃圾信息中。

 ## 解决方案

大多数人刚配置好Hexo-Icarus后会出现LaTeX Error，典型的情况如下图所示

![LaTeX Error](/assets/blog/hexo-icarus-mathjax/mathjax-error.png "LaTeX Error")

还有一些个别情况，会出现公式直接被吞无法显示的情况，一般是有些LaTeX符号在Hexo生成页面时，被识别成Markdown语法而被渲染成HTML标签导致的，这也不用急，先尝试排查一下npm modules看一下自己装了哪些包，然后卸载掉安装好Icarus主题后再安装的公式package，Icarus自带行间公式的渲染。

如果发现自己有hexo-math，还需要卸载这个package

```bash
$ npm uninstall hexo-math
```

使用以下命令，换装hexo-filter-mathjax，在Hexo端渲染MathJax

```bash
$ npm install hexo-filter-mathjax
$ hexo clean
```

在编辑博客md文件时，在header区域加上 `mathjax: true`，如下所示

```tex
title: "快速为 Hexo-Icarus 配置 MathJax（2022）"
date: 2022-07-17 21:00:03
mathjax: true
categories:
- Blog
tags:
- Blog
keywords:
- Blog
```

然后重新使用 hexo g 命令生成博客页面，再使用 hexo s 进行预览，会发现问题解决了。

## 效果

### 行内公式

CodeBERT的输入形式为 $[CLS], w_1, w_2, ...w_n, [SEP], c_1, c_2, ..., c_m, [EOS]$，第一段为自然语言文本，第二段为代码，训练的数据可分为两种，即bimodal data，即NL-PL Pairs和unimodal data，也就是纯代码。

### 行间公式

行间公式使用`{raw}...{endraw}`进行包裹，如下

```tex
{% raw %}
$$
\begin{equation}M_{i j}= \begin{cases}0 & \text { if } q_{i} \in\{[C L S],[S E P]\} \text { or } q_{i}, k_{j} \in W \cup C \text { or }\left\langle q_{i}, k_{j}\right\rangle \in E \cup E^{\prime} \\ -\infty & \text { otherwise }\end{cases}\end{equation}
$$
{% endraw %}
```

{% raw %}
$$
\begin{equation}M_{i j}= \begin{cases}0 & \text { if } q_{i} \in\{[C L S],[S E P]\} \text { or } q_{i}, k_{j} \in W \cup C \text { or }\left\langle q_{i}, k_{j}\right\rangle \in E \cup E^{\prime} \\ -\infty & \text { otherwise }\end{cases}\end{equation}
$$
{% endraw %}

以上就是在为Icarus配置MathJax时的一些经验分享，有时候直接去这些主题仓库的issue中寻找答案，会比用搜索引擎的效率高很多，希望能有所帮助。
