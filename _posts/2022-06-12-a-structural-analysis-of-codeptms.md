---
title: "A Structural Analysis of CodePTMs"
date: 2022-06-12 20:00:03 +0800
lang: zh
categories:
  - "NLP"
  - "CodeRep"
tags:
  - "PTMs"
  - "CodeRep"
  - "Interpretability"
cover: "/assets/blog/a-structural-analysis-of-codeptms/CPTM-capture-paper-logo-long.png"
excerpt: "[论文导读] A Structural Analysis of Pre-Trained Language Model for Source Code (ICSE 2022)。"
---
[论文导读] What Do They Capture? - A Structural Analysis of Pre-Trained Language Models for Source Code



## 简述

这篇发表在ICSE 2022的文章来自华中科大，主要研究代码表征预训练模型（Code PTM）的可解释性。通读后发现其中的相当一部分参考了ICLR 2021的一篇对蛋白质Transformer（如TapeBert、ProtBert以及ProtXLNet等，挖个坑之后补）进行注意力机制分析的文章：

[BERTOLOGY MEETS BIOLOGY: INTERPRETING ATTENTION IN PROTEIN LANGUAGE MODELS]( https://arxiv.org/abs/2006.15222)

其中的可视化代码，以及Attention Analysis部分，几乎是照搬了蛋白质文章的代码和公式（设置threshold来过滤低注意力值，并计算各个类的注意力分布）

本文大量内容是参考了前人在NLP和生信领域的工作，将它们直接迁移到了Code上。但不失为一种入门Code PTM可解释性这个小领域的渠道。

## 摘要与要点

本文进行了透彻的结构性分析，以期为CPTM提供可解释性，分为以下三个方面

1. attention analysis: Attention aligns strongly with the syntax structure of code
2. probing on the word embedding: Pre-training language models of code can preserve the syntax structure of code in the intermediate representations of each Transformer layer
3. syntax tree induction: The pre-trained models of code have the ability of inducing syntax trees of code.

这些发现可能代表着将code的语法结构融入预训练会帮助得到更好的代码表征

## 导言

本文将当前的代码表征研究方案分为了两类

1. 监督学习模型：任务特定模型，也就是一个编码器网络 (e.g. LSTM, CNN, and **Transformer**) 为程序生成一个表征向量。
2. 无监督/自监督学习模型：utilize word embedding techniques to represent source code，学习全局词向量，如基于AST的Code2Vec

**We try to answer the following question: Can the existing pre-trained language models learn the syntactical structure of source code written in programming languages?**

核心问题：现在的CPTM能否学习到源码中的句法结构，重申了三点contribution

1. Analyze the self-attention weights and align the weights with the syntax structure，即给定一个代码片段，如果二者有neighborhood关系，那么分配给他们的注意力会比较高，研究揭示了注意力可以捕获源代码的高维结构属性，比如**motif structure**
2. Design a structural probing approach to investigate whether the syntax structure is embedded in the linear-transformed contextual word embedding of pre-trained code models. 证明了代码的句法结构隐式地嵌入在了模型所学习到的向量中
3. Investigate whether the pretrained language models for source code provide the ability of inducing the syntax tree without training 说明了预训练模型的确能够在一定程度上学习到源代码的句法结构

作者还提到，本工作和其他以设计更好的网络以获得更好的源代码表示的工作是互补关系。

## 研究背景

### Transformers的概述

主要是对Transformer的一般架构和计算方式做了简介，包括投影、注意力分数计算、Scaled Dot-Product Attention以及通过positional encodings为输入添加位置信息，没有提出新的概念，对这部分不了解的朋友可以参考下HarvardNLP的[The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)这篇文章

### Pre-Training Language Model

在代码表征领域，最先开这个坑的就是MSRA提出CodeBERT，随后出现了GraphCodeBERT、CodeT5以及PLBART等诸多预训练模型，最近比较新的是ICLR提出的UniXcoder（以后再讲，挖个坑）

值得一提的是这部分是对BERT模型的简介，提及的输入和训练任务都直接照搬了BERT的原文，但代码表征预训练模型的输入和训练任务与BERT有很大不同，以CodeBERT为例，其输入为代码片段和自然语言拼接而成，训练任务为ELECTRA。而GraphCodeBERT基于CodeBERT，在预训练阶段融入了Data-flow信息（通过AST提供）

{% raw %}
$$
s=[\mathrm{CLS}], \underbrace{w_{1}, w_{2}, \ldots, w_{n}}_{c_{1}},[\mathrm{SEP}], \underbrace{u_{1}, u_{2}, \ldots, u_{m}}_{c_{2}},[\mathrm{EOS}]
$$
{% endraw %}

## 研究动机

早期的NLP工作指出了Transformer的自注意力机制能够帮助捕获一定的自然语言句法信息

![Visualization of self-attention distribution](/assets/blog/a-structural-analysis-of-codeptms/CPTM-capture-paper-logo-long.png "Visualization of self-attention distribution")

上图为经过CodeBERT模型编码的一个代码片段的注意力可视化，（a）图展示了相应的注意力，（b）图展示了Transformer第五层的各注意力头的注意力分数平均值（c）图是这层第12个头的注意力权重，其中标注了一些红色的点为相应ast中有motif structure

本文作者对motif structure的定义是：AST树中包含非叶子节点和叶子节点的结构，可见示例图中（a）图中用深色标注的AST局部结构

示例图中的（b）图展示了自注意力分布的热力图，作者从其中挑选了一些“长方形”，将其归为一个group，结合AST的信息可以发现此热力图所反馈的信息可以和AST相对应，比如tokens在AST的同一个分支。最后（c）图挑选了一个Transformer层中的一个Head做了case study，根据我的经验应该是使用BertViz完成的绘图。

这里有一个重要的概念：motif structure，也就是作者为AST定义了一个特殊的语法结构，它包含了非叶子结点及其子节点，如上图的 (a) 中的if_statement部分。

## CodePTMs的结构性分析

这部分在文章的第四章，使用了三个不同的结构分析方法，以解释CodeBERT和GraphCodeBERT两个模型，下图为三个方法的示例

### 注意力分析

每个Transformer层中都能获得一套输入的代码的注意力，设计了一个indicator函数𝑓 (𝑤𝑖, 𝑤 𝑗 )，判断两个输入token是否有syntactic relation（句法关联），作者定义了syntactic relation，即 𝑤𝑖 和 𝑤𝑗 在AST中有相同父节点。

{% raw %}
$$
\begin{equation}p_{\alpha}(f)=\frac{\sum_{c \in C} \sum_{i=1}^{|c|} \sum_{j=1}^{|c|} \mathcal{1}_{\alpha_{i, j}(c)>\theta} \cdot f\left(w_{i}, w_{j}\right)}{\sum_{c \in C} \sum_{i=1}^{|c|} \sum_{j=1}^{|c|} 1_{\alpha_{i, j}(c)>\theta}}\end{equation}
$$
{% endraw %}

公式中的theta为一个阈值，用于过滤掉注意力权重较低（低置信）的token pairs，上面这个公式中相应的注意力仅仅取决于权重的绝对值。因为这些head注意在前一个或是后一个code token，它并不会考虑到code token的内容，因此不会和整个代码片段的句法结构匹配。

（这块的分析简直和BERTOLOGY MEETS BIOLOGY一模一样）

所以进一步调研了注意力的变化性（attention variability），用来衡量对于不同的输入，注意力怎么变化，公式如下

{% raw %}
$$
\begin{equation}\text { Variability }_{\alpha}=\frac{\sum_{c \in C} \sum_{i=1}^{|c|} \sum_{j=1}^{|i|}\left|\alpha_{i, j}(c)-\bar{\alpha}_{i, j}\right|}{2 \cdot \sum_{c \in C} \sum_{i=1}^{|c|} \sum_{j=1}^{|i|} \alpha_{i, j}(c)}\end{equation}
$$
{% endraw %}

（我觉得这部分完全参考了 Analyzing the Structure of Attention in a Transformer Language Model）

使用单个token pair的注意力分数减去所有注意力分数的均值，只选取了前10个token来保证每个position有足够多的数据，这些位置信息在整个序列中（看起来）是一致的，作者认为变化性的较高则为content-dependent head，较低变化性则为content-independent head

### Structural Probing on Word Embedding

![An illustration of attention analysis, probing on word embedding, and syntax tree induction](/assets/blog/a-structural-analysis-of-codeptms/Capture-Paper-Structural-Analysis-CPTM.png "An illustration of attention analysis, probing on word embedding, and syntax tree induction")

这部分使用了Structural Probing的分析方法来检查预训练模型是否把句法结构嵌入在上下文中的word embedding中（白话讲就是训练出来的word/code embedding中是否含有句法信息）。该方法的核心概念是（AST的）树状结构在被嵌入一个新的空间后，两个词向量之间的欧氏距离和两个词在语法树之间的边数量对应。

上图的简介图（a）和（c）演示了对代码的Word Embedding的Structural probing

此处学习了一个mapping function，使用代码序列作为输入，模型的每个层生成词向量，然后计算二者在高维空间中的distance。作者认为，如果Vf和Vi的欧式平方距离接近2，那么语法树的结构被较好地保留

{% raw %}
$$
\begin{equation}d_{B}\left(\mathbf{h}*{i}, \mathbf{h}*{j}\right)^{2}=\left(B\left(\mathbf{h}*{i}-\mathbf{h}*{j}\right)\right)^{T}\left(B\left(\mathbf{h}*{i}-\mathbf{h}*{j}\right)\right)\end{equation}
$$
{% endraw %}

参数训练的loss function，两个distance，第一个表示AST中code token的距离，第二个表示词向量的距离，第一个sigma为所有训练序列的平均distance，第二个sigma为代码序列中所有可能的二元组组合，训练目标就是通过误差反向传播更新映射函数B

{% raw %}
$$
\begin{equation}\min *{B} \sum*{c \in C} \frac{1}{|c|^{2}} \sum_{i, j}\left|d_{T^{c}}\left(w_{i}^{c}, w_{j}^{c}\right)-d_{B}\left(\mathbf{h}*{i}^{c}, \mathbf{h}*{j}^{c}\right)^{2}\right|\end{equation}
$$
{% endraw %}

### Syntax Tree Induction

这一部分研究预训练模型在不训练的情况下引导句法结构的能力

两个code tokens之间的“距离”接近（如注意力分布类似或是表示类似），那么它们应该在语法树中较为接近，比如有公共父节点。此处的假设是，如果源于预训练模型的语法树与gold standard的语法树很相似，我们可以合理的推导出预训练模型保留了句法结构信息这个结论

这里有一个概念，文章没有讲清楚，那就是Gold Standard指代的是什么

我个人的理解：预训练模型得到的token embedding的距离关系和实际AST里两个token之间的距离关系是一致的

通过保证token embedding的距离关系来验证没有通过树结构就学到语法了

![Visualization of attention heads in CodeBERT](/assets/blog/a-structural-analysis-of-codeptms/Capture-Paper-Vis-of-att-heads-in-CodeBERT.png "Visualization of attention heads in CodeBERT")





## 实验设计和结果

作者在这里以三个Research Question的形式展示了实验的效果

![Consistency between the attention and AST for the CodeBERT and GraphCodeBERT](/assets/blog/a-structural-analysis-of-codeptms/Capture-Paper-attention-consistency.png "Consistency between the attention and AST for the CodeBERT and GraphCodeBERT")

### RQ1: Attention Analysis

这张图展示了CodeBERT和GraphCodeBERT的注意力是如何与AST对应的，其中的色块是AST中连接了motif structure高置信度的注意力权重的proportion，柱状图展示了每个层的最大值



### RQ2: Probing on Word Embedding

probing中的python语言的斯皮尔曼系数



![The heatmaps of gold-standard distance and predicted distance based on pre-trained CodeBERT and GraphCodeBERT models in Python.](/assets/blog/a-structural-analysis-of-codeptms/gold-standard-distance.png "The heatmaps of gold-standard distance and predicted distance based on pre-trained CodeBERT and GraphCodeBERT models in Python.")



### RQ3: Syntax Tree Induction



![A case study of syntax tree induction based on CodeBERT for a given Python code snippet.](/assets/blog/a-structural-analysis-of-codeptms/Syntax-Tree-Induction.png "A case study of syntax tree induction based on CodeBERT for a given Python code snippet")

上图为一个针对CodeBERT模型的Case study，比较了是否注入了bias，从图中可以看到CodeBERT能捕获多个motif structure，说明了syntax tree induction的有效性

本节小结：

1. 代码的语法树可以由代码表征预训练模型induce得到
2. 从注意力信息中抽取语法树比从CodePTM的上下文表示中抽取更有效



## Limitations and Future Work

进一步的研究

**预训练的另外几个方面**

1. Control-flow graphs (CFGs)
2. Data-flow graphs (DFGs)

**更多预训练模型**

本文只研究了CodeBERT and GraphCodeBERT的表征，言下之意：这两个模型都是Encoder-only的模型，其他架构的模型如PLBART，CodeT5也可以整一发，还有一些经典模型，比如把LSTM和CNN + 注意力模型应用在代码的处理上也可以使用类似的分析方法。

**Structural Analysis**

本文的Structural probing相对简单，用一个更深的网络也许可以获得更好的映射

**树结构**

所涉及的Right-skewness bias是用于NLP的，或许可以使用AST结构来补充

回顾一下，本文从三个角度对代码表征预训练模型进行了分析，把一些NLP中的可解释性分析方法迁移到了Code领域，并且融合了生信领域的一些工作。不过本文并没有基于这些发现改进模型（比如给Code的各种下游任务提点）

## 后记

补充一下注意力权重的可视化策略，之前提到过这篇文章的注意力可视化可能用了[BertViz](https://github.com/jessevig/bertviz)，我个人也觉得BertViz非常的好用，Github给的demo可以支持交互效果，而且如果报告/文章版面够大的话，还可以这么玩（选择neuron view）

![BertViz](/assets/blog/a-structural-analysis-of-codeptms/attn-roberta-code-vis.png "BertViz Demo")
