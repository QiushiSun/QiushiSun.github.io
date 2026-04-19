---
title: "Code预训练语言模型学习指南（原理/分析/代码）Part1"
date: 2022-07-06 20:00:03 +0800
lang: zh
categories:
  - "NLP"
  - "CodeRep"
tags:
  - "PTMs"
  - "CodeRep"
cover: "/assets/blog/codeptms-review-part1/sesame-street-code-long-1.jpg"
excerpt: "Code 预训练语言模型学习指南（原理 / 分析 / 代码）Part 1。"
---
Code预训练语言模型学习指南（原理/分析/代码）Part1



## Introduction

自从2020年CodeBERT开了代码表征预训练模型（本文称之为CodePTM）这个新坑后，在短短两年的时间内出现了若干个程序设计语言（Programming Language，称之为PL，与Natural Language，也就是NL对应）语言模型。它们的共同特点是大部分用于处理PL（或Source Code）时所采用的技术是从NLP中的Transformer-based模型迁移而来，但这些CodePTMs又各有特点，从训练的角度出发即不同的预训练/微调策略，从数据的角度出发，比如是否使用了代码的结构信息，即抽象语法树（Abstract Syntax Tree，本文将其简称为AST）及其变体。而从架构出发，这些Code预训练模型大致可以被分为以下这三类：

1. encoder-only：CuBERT、CodeBERT、GraphCodeBERT等
2. decoder-only：CodeGPT、GPT-C等
3. encoder-decoder：PLBART、CodeT5等

本文对各个CodePTM建模编程语言的思想进行回顾，并简要分析了一下它们的特色。对文中提到的所有CodePTMs的描述主要从背景、预训练策略、微调策略以及下游任务这几个角度出发进行分析，考虑到这些模型之间都存在一些共性以及文章篇幅原因，文中略去了一些通用的处理手段和细节，因此对各部分的分析讲解详略不一，不过都保留了建模编程语言最核心的思想。阅读前需要对Transformer有一定的了解，考虑到单篇博客的长度，这些模型分在两篇博客中讲完。

## CuBERT

ICML 2020 [Learning and Evaluating Contextual Embedding of Source Code](https://arxiv.org/abs/2001.00059)

CuBERT，即Code Understanding BERT，和后面提到的CodeBERT可被归为同一个时期的工作，虽是首个提出Code预训练模型的工作，但和CodeBERT相比，其影响力较小（我在写这篇文章的时候CuBERT引用还没过百），具体原因个人认为是它仅对Python语言进行建模（CodeBERT同时对6种编程语言建模），且它的下游任务和CodeBERT相比不太丰富，主要是以代码理解任务为主。

作者通过GitHub采集了7.4M Python语言编写的程序用于CuBERT的预训练，将基于Transformer类模型处理自然语言的手段迁移到了编程语言上，使用的模型架构和训练方式直接照搬了BERT-Large（24层16个注意力头），然后使用了一个处理过的[ETH Py150](https://github.com/google-research-datasets/eth_py150_open)数据集进行微调。

与此同时，作者还训练了一组Word2Vec embeddings、Bi-LSTM模型和Transformer模型用于比较。

就任务而言，作者构建了一个Benchmark，其中包含了：

1. 五个分类任务（具体细节和描述可参考原文附录）
    1. Variable-Misuse Classification
    2. Wrong Binary Operator
    3. Swapped Operand
    4. Function-Docstring Mismatch
    5. Exception Type
2. 一个定位+修复任务（Variable-Misuse Localization and Repair），也是本文唯一一个非分类任务

就这几个下游任务而言，可以看到CuBERT主要还是在做代码理解领域的判别式任务，与后续出现的CodeXGLUE Benchmark比其在任务的数量和类型上都有局限性。而且，由于它仅采用了Python语言，和后面出现的各种CodePTMs比局限性比较大，因此仅做简单的科普。

## CodeBERT

Findings of EMNLP 2020 [CodeBERT: A Pre-Trained Model for Programming and Natural Languages](https://aclanthology.org/2020.findings-emnlp.139/)

相比前面提到同期工作的CuBERT，CodeBERT的影响力比它大很多。一方面是因为它是多语言（multi-programming-lingual）模型，纳入了6个编程语言，另一方面是它和MSRA自己的CodeXGLUE Benchmark配套后在各个下游任务上被广泛使用。

除了预训练阶段的任务有变化外，CodeBERT的其他方面与自然语言中的BERT模型训练基本无异（其本质上的一个RoBERTa），CodeBERT使用了bimodal data（即PL-NL Pairs）进行了预训练，预训练数据的来源为CodeSearchNet数据集，其中有Python, Java, JavaScript, PHP, Ruby和Go这六种编程语言的2.1M bimodal data和6.4M unimodal codes（也就是没有对应comments的纯代码），这些数据的来源都是GitHub中的开源仓库，并且后续的很多工作也在预训练阶段用了CodeSearchNet数据集。

![CodeSearchNet](/assets/blog/codeptms-review-part1/codesearchnet-data.png "codesearchnet-data")

CodeBERT的输入形式为 $[CLS], w_1, w_2, ...w_n, [SEP], c_1, c_2, ..., c_m, [EOS]$，第一段为自然语言文本，第二段为代码，训练的数据可分为两种，即bimodal data，即NL-PL Pairs和unimodal data，也就是纯代码。

![Bomodal Data](/assets/blog/codeptms-review-part1/codebert-code-with-NL.png "Bomodal Data")

**Masked Language Modeling (MLM)**，算是Transformer类模型的预训练中最老生常谈的任务了，作者将其应用于基于bimodal data的训练


![Masked Language Modeling](/assets/blog/codeptms-review-part1/codebert-mlm.png "Masked Language Modeling")

**Replaced Token Detection (RTD)**，迁移自ELECTRA，既可以利用bimodal data进行训练，还可以进一步利用unimodal data（比如是没有对应自然语言文本的code），具体细节可以参考ELECTRA原文。


![Replaced Token Detection](/assets/blog/codeptms-review-part1/codebert-rtd.png "Replaced Token Detection")

实验部分做了Natural Language Code Search，个人认为文中没有添加更多下游任务是受到EMNLP的篇幅限制，使用CodeBERT可以在多个下游任务，如Clone detection（克隆检测）、Defect detection（缺陷检测）、Code summarization等上得到出色的结果，具体可参考CodeXGLUE，如下图所示

![CodeXGLUE Benchmark](/assets/blog/codeptms-review-part1/CodeXGLUE-benchmark.jpg "CodeXGLUE Benchmark")

从CodeBERT开始，后续的CodePTMs就全部继承了对多个PL的支持，不过CodeBERT完全使用了建模自然语言的手段来为Code（或是说NL-PL Pairs）做预训练，忽视了代码的一个很大的特性，那就是结构信息，具体而言就是在编译器进行语法分析阶段生成的抽象语法树（Abstract Syntax Tree，本文称之为AST），紧跟着CodeBERT的GraphCodeBERT立刻填上了这个坑。

## GraphCodeBERT
ICLR2021 [GRAPHCODEBERT: PRE-TRAINING CODE REPRESENTATIONS WITH DATA FLOW](https://iclr.cc/Conferences/2021/Schedule?showEvent=2598)

看名字就知道这是CodeBERT的后续工作，主要想法就是为CodeBERT添加代码的语法信息，使CodePTM可以显式学习代码的结构信息。

GraphCodeBERT基于数据流学习代码的表征，如下图所示

![GraphCodeBERT所使用的数据流](/assets/blog/codeptms-review-part1/graphcodebert-extracting-data-flow.png "Extracting Data Flow")

数据流的获得分为以下几个步骤

1. 通过语法分析工具获得AST，原文中使用的工具是tree-sitter
2. 从AST中提出变量，构成一个由变量组成的序列
3. 从AST中抽取变量之间的依赖关系，文中称之为“value comes from”，构造数据流图

![GraphCodeBERT的预训练](/assets/blog/codeptms-review-part1/graphcodebert-pt.png "GCB Pretraining")

GraphCodeBERT在模型预训练阶段额外提出了两个在当时较为新颖的训练任务

1. Edge Prediction，即数据流图边预测，通过预测数据流图的边学习代码的结构信息
2. Node Alignment，即变量对齐，具体而言是学习数据流图中的某个node来自输入代码中的哪个code token
    将它们和从CodeBERT（或是BERT or RoBERTa）继承下来的MLM任务一起优化。考虑到AST是一种图结构，为了让Transformer能适应其与一般序列结构的差异，作者修改了其注意力机制，主要是通过调整Attention Mask缩小感受野。

{% raw %}
$$
\begin{equation}M_{i j}= \begin{cases}0 & \text { if } q_{i} \in\{[C L S],[S E P]\} \text { or } q_{i}, k_{j} \in W \cup C \text { or }\left\langle q_{i}, k_{j}\right\rangle \in E \cup E^{\prime} \\ -\infty & \text { otherwise }\end{cases}\end{equation}
$$
{% endraw %}

作者将其称为Graph-Guided Masked Attention，其中E代表的是数据流图的边，E'代表的是数据流图的节点和代码的对应关系边。

就下游任务而言，GraphCodeBERT文中主要完成了Natural Language Code Search、Clone Detection、Code Translation和Code Refinement这几个任务，它同样适用CodeXGLUE Benchmark中的其他任务，比如Code Summarization等。

GraphCodeBERT相较于前作CodeBERT解决了CodePTM只学习自然语义，而不学代码结构/语法的问题。但细心的读者或许能发现，学习数据流相较于学习AST本身有相当的信息损失，这也为之后的UniXcoder挖了一个小坑。

## GPT-C

FSE/ESEC 2020 [IntelliCode Compose: Code Generation using Transformer](https://dl.acm.org/doi/10.1145/3368089.3417058)

GPT-C是为了代码补全（Code Completion）这个任务而设计的，作者认为之前的的代码补全工作有两点不同

1. 根据上文的token来预测下个token，没有将代码的全文环境纳入考虑
2. 多语言效果不佳

![Code Completion](/assets/blog/codeptms-review-part1/GPT-C-Code-Completion.png "GPT-C Code Completion")

作者提出的GPT-C是GPT-2模型的变体，在一个大规模、无监督、多语言的数据集上从零开始训练。基于GPT-C，作者构建了一个代码补全Framework，称之为IntelliCode Compose，并对多种编程语言进行建模。作者将Sequence decoding的过程视为对树的搜索，搜到出现目标token为止。

![Sequence decoding](/assets/blog/codeptms-review-part1/GPT-C-code-snippet.png "GPT-C Sequence decoding")

虽说是多语言，但是使用的是Python, C#, JavaScript 和 TypeScript，和CodeXGLUE不同且少了两个语言。

就多语言模型的训练而言，作者提出了四个训练的策略

1. Language-agnostic baseline，即忽略掉编程语言的不同构建一个baseline多语言模型。
2. Language-type embedding，即加入一个向量来表示每种编程语言，和token embedding等相加。
3. Language specific control codes，每个输入的训练样本前拼接一个"lang ∗ remaining token sequence”字符串，∗即为编程语言
4. add a programming language classification task during model pretraining，即在预训练阶段加入一个分类编程语言的任务

关于IntelliCode Compose：作者将Sequence decoding的过程视为对树的搜索，搜到出现目标token为止

![multilingual modeling approaches based on GPT-C](/assets/blog/codeptms-review-part1/GPT-C-ablation.png "GPT-C Ablation")

在文末，作者考虑到了模型的推理开销问题，还上了一个知识蒸馏，并且还讨论了一下模型基于K8S和VS Code的部署问题。

## Code-GPT

Code-GPT是在CodeXGLUE中被提出的，没有单独成文，不要和GPT-C搞混了。作者实现它的目的是为了code completion 和 text-to-code generation任务。它就是一个由Code训练，与GPT-2完全同架构的12层Transformer Decoder模型，不过MSRA的研究者实现了两个版本

1. Pretrained from scratch：随机初始化，从零训练
2. CodeGPT-adapted：先使用一个GPT-2作为起始点，再持续使用Code进行训练，作者将这个方法称为“domain-adaptive”

更详细的内容可以参考CodeXGLUE原文的4.2节，作者在Huggingface提供了[CodeGPT-small-java](https://huggingface.co/microsoft/CodeGPT-small-java) 和 [CodeGPT-small-java-adaptedGPT2](https://huggingface.co/microsoft/CodeGPT-small-java-adaptedGPT2) 这两个checkpoints，正常地使用transformers库加载就能使用了。

以上是5个代码表征领域的预训练模型的简介与简要分析，还有若干模型会在下一篇博客中继续讨论。
