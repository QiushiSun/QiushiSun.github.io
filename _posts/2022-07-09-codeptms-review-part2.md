---
title: "Code预训练语言模型学习指南（原理/分析/代码）Part2"
date: 2022-07-09 20:00:03 +0800
lang: zh
categories:
  - "NLP"
  - "CodeRep"
tags:
  - "PTMs"
  - "CodeRep"
cover: "/assets/blog/codeptms-review-part2/sesame-street-code-long-2.jpg"
excerpt: "Code 预训练语言模型学习指南（原理 / 分析 / 代码）Part 2。"
---
Code预训练语言模型学习指南（原理/分析/代码）Part2



这个主题的上一篇文章 [Code预训练语言模型学习指南（原理/分析/代码）Part1](https://qiushisun.github.io/2022/07/06/2022-7-CodePTMs-Review1/) 讲解了几个典型的Code预训练语言模型（CodePTMs），这篇文章顺延这个话题，继续讨论21年及以后出现的CodePTMs，并且补充一些代码。

## PLBART
NAACL 2021 [Unified Pre-training for Program Understanding and Generation](https://aclanthology.org/2021.naacl-main.211/)

顾名思义，就是应用于编程语言的BART，参考了ACL 2020的文章：[BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461.pdf)

先简单说下BART，它吸收了BERT模型的双向编码器和GPT中的单向left-to-right解码器这二者的优点，因此比BERT更适合文本生成的场景（BERT因Pre-training阶段和生成式下游任务差异比较大，因此被认为不适合做NLG相关任务），而它相比GPT，也多了双向上下文语境信息（GPT是单向建模）。除此之外，相比BERT的Token Masking，BART对Encoder端采用了更加复杂的Noise。

基于对BART的知识，理解PLBART并不算困难，其使用了和BART-base相同的架构，唯一结构上的不同的是它在Encoder和Decoder的顶部添加了一个额外的LayerNorm。在Noise策略方面，PLBART使用了token masking, token deletion和token infilling这三种策略，与BART相比少了Sentence Permutation和Document Rotation这两个任务，这些任务的细节都可以参考BART原文。

在微调下游任务方面，作者将PLBART的下游任务分为两块

首先是Sequence Generation，又可细分为三个任务，可参考下图

![PLBART: Sequence Generation](/assets/blog/codeptms-review-part2/PLBART-Seq-Gen.png "PLBART: Sequence Generation")

其次是Sequence Classification：将序列尾部的special token喂给线性分类器用于预测，与BERT等模型的分类区别不大。

实验与比较方面，作者先指定了baseline模型，并将其分成了两种

Training from Scratch，作者用下游任务的数据集从零开始训练了LSTM+Attention以及一个Transformer
Pre-trained Models，作者挑选了RoBERTa、CodeBERT、GraphCodeBERT、GPT-2、CodeGPT(-adapted)
具体的实验部分做了Code Summarization、Code Generation、Code Translation这三个生成式任务，效果自然是好的，在Classification方面做了两个任务：clone detection和vulnerability detection，在后者上PLBART不如基于AST的模型。

## CodeT5
EMNLP 2021 [CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation](https://aclanthology.org/2021.emnlp-main.685/)

文中对CodeT5的描述是：a unified pre-trained encoder-decoder Transformer model that better leverages the code semantics conveyed from the developer-assigned identifiers，即一个能更好地利用代码语法信息（形式是identifier，即标识符）的统一预训练Transformer模型。在开始之前，和PLBART一样，先简单说下Google T5模型。T5的名字来源是Text-To-Text Transfer Transformer，顾名思义T5把所有的NLP问题统一归纳为了Text2Text任务，用来做NMT、QA、文本摘要和文本分类任务。

![T5-Illustration](/assets/blog/codeptms-review-part2/T5-Illustration.png "T5-Illustration")

对比下T5原文，可以发现二者的核心思想还是非常类似的，作者将CodeT5归纳为a pre-trained encoder-decoder model that considers the token type information in code，细心的玩家可能发现了，前面提到的CodeBERT为首的BERT类模型和CodeGPT为首的GPT类模型，仅含有Encoder或Decoder，而非完整利用一个Transformer架构来处理代码。因此CodeT5最大的卖点即第一个unified encoder-decoder CodePTM，可以理解为完全使用了Transformer的两个部分。

![CodeT5-Illustration](/assets/blog/codeptms-review-part2/CodeT5-Illustration.png "CodeT5-Illustration")

此外，除了使用T5的架构外，作者使用了以下两个方案来更好地利用代码结构特性：

使用了代码的标识符信息，提出了Identifier-aware Pre-training，是一个与T5中Masked Span类似的目标，简而言之就是随机mask掉任意长度的Span，然后让decoder去预测。
利用了代码地Comments（自然语言注释）信息，作者称之为Bimodel Dual Generation，让自然语言和源代码的表征可以对齐，帮助缓和Pre-training和Fine-Tuning阶段的差距。

![Identifier-aware Pre-training](/assets/blog/codeptms-review-part2/CodeT5-pretraining-task.png "CodeT5-pretraining")

文章发表时在CodeXGLUE Benchmark的若干任务上取得了SOTA效果。

## UniXcoder
ACL 2022 [UniXcoder: Unified Cross-Modal Pre-training for Code Representation](https://aclanthology.org/2022.acl-long.499/)

这是当今（2022.7）的SOTA模型，参考了NIPS2019: Unified Language Model Pre-training for Natural Language Understanding and Generation

文章选择了五个任务，分为以下三类

代码理解任务：Clone Detection和Code Search
代码生成任务：Code Summary和Code Generation
自回归任务：Code Completion
本文很重要的一个卖点就是更全面地利用了AST提供的代码结构信息。文章开头讲过，AST一般会被表示为一个Tree结构，不能直接作为Transformer类模型的输入，回忆一下前面提到的GraphCodeBERT，作者在以损失相当一部分信息的情况下让模型学习AST的数据流。为了能更加有效地利用AST，因此UniXcoder地作者构建了一个one-to-one的mapping function，将AST转为一个序列结构（flattened token sequence），然后和Code Comments一同编码，对这个mapping function的有效性的证明在文章的附录中。

模型结构方面，UniXcoder的一个卖点就是一个统一的，可以同时兼容Encoder-Only，Decoder-Only和Encoder-Decoder三种模式的CodePTM，相当于给模型添加了“开关”，来决定采用什么模式处理任务，用白话讲，就是通过使用三种不同类型的自注意力Mask策略来控制模型的行为。

![UniXcoder的架构](/assets/blog/codeptms-review-part2/unixcoder-arch.png "UniXcoder's Architecture")

既然同时能拥有三种模式，那么自然会有更多预训练任务，如下所示：

Masked Language Modeling（MLM），算是基本操作了。
Unidirectional Language Modeling（ULM），用于训练decoder-only模式，帮助完成自回归任务，对应的是右上三角masking。
Denoising Objective DeNoiSing (DNS)，可参考BART和T5，用于训练encoder-decoder模式，帮助完成生成任务，参考架构图中的encoder-decoder部分。
除了上面这些任务以外，作者还提出了Code Fragment Representation Learning

![Code Fragment Representation Learning](/assets/blog/codeptms-review-part2/unixcoder-Code-fragment-representation-learning.png "Code Fragment Representation Learning")

其中包含了Multi-modal Contrastive Learning (MCL) 和 Cross-Modal Generation (CMG)这两个任务。前者采用了一个对比学习损失，后者是使用了一个统一的自然语言描述（comment），文中使用了fulcrum，即支点这个词，让模型学习到的代码表征在不同语言之间的对齐。

还需注意的一点就是，UniXcoder在预训练和微调这两个阶段中的输入形式有所不同，由于引入了Flattened AST，AST展开后的序列中被引入了大量额外的tokens（70% longer）会导致额外的开销。因此，在微调阶段UniXcoder仅使用AST的叶子节点，为了缓解这个gap，在预训练阶段作者设置了0.5的概率随机丢弃输入序列中的非叶子节点。

除了Clone Detection、Code Search、Code Summarization和Code Completion等任务上表现较好外，UniXcoder还提供了一个新任务：zero-shot code-to-code search，即在zero-shot的情境下，通过一个源代码的query在candidates集合中寻找语义相同的源代码，该任务使用的数据集是[CodeNet](https://arxiv.org/abs/2105.12655v1)，2021年的一篇数据集文章，用来衡量训练所得的code fragment embeddings的效果。

![zero-shot code-to-code search](/assets/blog/codeptms-review-part2/unixcoder-zero-shot-code2code-search.png "zero-shot code-to-code search")


## 相关代码整理

### CuBERT

[https://github.com/google-research/google-research/tree/master/cubert](https://github.com/google-research/google-research/tree/master/cubert)

### CodeBERT、GraphCodeBERT和UniXCoder

MSRA提供了CodeBERT、GraphCodeBERT和UniXCoder在下游任务微调时可用的代码，在仓库[https://github.com/microsoft/](github.com/microsoft/CodeBERT)CodeBERT，但没有提供预训练阶段的实现（CodeBERT和UniXCoder在预训练阶段都使用了16 张 32GB NVIDIA Tesla V100实现），使用时通过transformers加载checkpoints就可使用。此外，huggingface还提供了一个经济适用版的CodeBERT模型：[huggingface/CodeBERTa-small-v1](https://huggingface.co/huggingface/CodeBERTa-small-v1)

### CodeGPT

与上述三个MSRA提供的模型一样，CodeGPT仍然是提供了可通过transformers加载checkpoints，即[CodeGPT-small-java-adaptedGPT2](https://huggingface.co/microsoft/CodeGPT-small-java-adaptedGPT2)

### CodeT5

[https://github.com/salesforce/codet5](https://github.com/salesforce/codet5)

### PLBART

[https://github.com/wasiahmad/PL](https://github.com/wasiahmad/PL)

## 总结
上述对CodePTMs相关的内容大致上是六月中下旬赶一个文章时调研文献后总结的笔记，然后补充了点链接和细节，实验部分写的比较简略，是因为如果每个模型的实验都要全讲的话篇幅就太长了，而且这些任务都大差不差，每个模型都讲一遍冗余会比较多，之后可能会在其他文章补充。此外，有一些影响力比较小或者Task-specific的工作可能没完全覆盖到。总而言之，不论是CodeBERT开的新坑还是今天的SOTA模型UniXcoder，MSRA在这个领域还是完全dominant的存在。对于CodeBERT和GraphCodeBERT为首的大模型，复现预训练阶段的成本很高，不适合平民玩家，而且今年五月的IJCAI 22 Survey Track连CodePTMs的Survey工作都已经出了（Deep Learning Meets Software Engineering: A Survey on Pre-Trained Models of Source Code），可能短时间内出革命性的新模型的可能性不大，而且Code领域使用的这些方法终究还是跟着NLP走的，需要NLP提出新技术后Code领域才有跟进的可能。个人感觉接下来在这个相对较小但很卷的领域的研究热点可能会慢慢向可解释性和模型分析（Analysis of Models & Interpretability）方面转移，最近还研读了一些22年新出的Probing CodePTMs的文章，之后再补充。

希望本文对想熟悉代码表征预训练模型这块的朋友有所帮助。
