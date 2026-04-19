---
title: "ViLT：图像-文本多模态Transformer"
date: 2022-08-11 18:49:23 +0800
lang: zh
categories:
  - "Multimodality"
tags:
  - "Multimodality"
  - "Transformer"
cover: "/assets/blog/vilt-vision-language-transformer/ViLT-Cover.jpg"
excerpt: "[论文导读] ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision。"
---
[论文导读] ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision



## 前言与背景

### 背景

ViLT是ICML 2021的一篇Oral Presentation，它提出了一个极其简单的多模态训练方法，大大减少了视觉-文本多模态任务中处理图像特征抽取部分的计算量，将主要的计算量都放在了模态融合上，显著提高了模型的推理的速度，把方法的建模做了相当程度的简化，算是多模态领域这两年来里程碑式的工作了。

### 主要贡献

ViLT把目标检测（Object Detection），也就是文章Title中提及的Region Supervision从多模态任务里面去掉了。天下苦目标检测久矣，回忆一下DETR就是因为把目标检测框架做的简单，不仅可以End2End（端到端）训练，而且支持后处理。而ViLT直接把目标检测这个高开销任务干掉了，让模型明显简化和推理加速。

![Visual Embedding Schema](/assets/blog/vilt-vision-language-transformer/ViLT-Visual-Embed-Schema.jpg "Visual Embedding Schema")

从上图可以概览一下前面的工作，文本的处理都很简单，通过word embedding生成向量，扔到Transformer里就可以了。但是视觉这边就不一样了，对于最流行的区域特征，先给一个图像，通过一个Backbone网络，然后RoI，相当于就是做了一次目标检测（抽取Bounding box），所以图像处理的结果就跟文本的单词一样，都是离散形式存在的（也就是一个序列），最后再把文本和图像的序列扔给Transformer进行处理。把图像化为和文本序列一样的离散化表示是一种理论上可行且实现方便的方法，这也就是为什么之前的工作都是把和文本一起训练的通过OD来建模。但是，整个模型的运行时间分配并不合理，用BERT类模型处理文本只占用约15ms，但是视觉OD部分占了810ms。过去这几年（ViLT出现之前）一直有各种各样的工作把视觉这部分的时间压缩，但并没有根本性解决这个问题的方案出现。

![Running Time Comparison](/assets/blog/vilt-vision-language-transformer/ViLT-Running-Time.jpg "Running Time Comparison")

而ViLT直接把这件事情反过来了，视觉部分只占据0.4ms，也就是说处理图像部分的时间开销反而只有文本的1/35了，获得了上千倍的运行时间的减少，这也是本文最大的卖点。但实际上，之前被诟病的高开销目标检测也并没有这么不堪，因为可以复用一些处理好的、静态的数据（抽取好的特征），而ViLT虽然推理很快，但是其训练依然是很昂贵的，需要64张32g V100训练三天，它甚至比之前的方法训练时间都要久，而且从上图也可以看出其性能和基于RoI的模型比并没有显著提升。因此，个人认为ViLT最大的贡献是开了“Without Convolution or Region Supervision”这个坑，而非是模型的性能。

接下来对paper本身进行分析

## 文章解读

### Title

ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision

解释一下这里的Conv和Region Supervision的具体含义

1. 卷积：指的就是预训练好的一个模型抽出的backbone，提供特征图。
2. 区域特征：简而言之就是目标检测的框框。

可以看出，作者最希望体现的卖点，就是既不用卷积带来监督信号，也不用区域特征带来监督信号，以此降低计算复杂度。

### Abstract

VLP（视觉文本预训练）在过去几年发展的很好，在各种downstream任务都有很好的效果，但是这些模型在图像处理部分花费的精力太多了。常理而言，视觉部分越复杂，开销越大，结果越好，因此之前的工作太过依赖于feature extraction，也就是看为一个目标检测，模型又有Backbone网络在工作，又有Region Supervision在工作。这篇文章针对这个点开始研究，指出了一下两个问题：

1. 效率不行，抽特征花了太多的时间，花费的时间已经超过了模态融合，对下游任务不友好。
2. 如果只用一个预训练好的模型去抽取特征，模型的表示能力肯定有问题，比如用一个目标检测器，因为目标检测的数据集规模都不大，不能涵盖问题的边边角角，因此如果只是抽特征，大概率就不是最优解。而且深度学习时代，总得想办法做End2end的学习。

因此，ViLT提出了极简化的方案，图像预处理做的和文本预处理一样，都通过linear embedding就结束了，正是因为这种设计，ViLT的速度快了很多，但是性能依旧保持竞争力。

### Introduction

模态学习近几年很火，进步也很快，因为也采用了PT-FT的方式。不论是nlp还是视觉，大家现在都这么干，当把它拓展到多模态的时候，效果也不错。作者指出在这个条件下，预训练阶段的学习比较重要，它不仅能够为模型提供一个好的初始化，甚至还可以帮助模型Zero-Shot做下游任务，催生了多模态的视觉文本联合预训练模型。

在文章的导言部分，作者罗列了2019-2021年间出现的若干引用过百的文章（显然，背后还有上千篇跟进性质的工作），可见这个东西过去几年发展的速度多快，19年Vilbert、VisualBert、VLBert三篇文章名字很像。因此多模态虽然听起来还是挺新的，但实际上竞争很激烈，需要拼手速。

作者认为，一般来说上述模型都是图像文本对来训练的，他们的目标函数都是imgae-text matching为主导的，也就是计算匹配loss和nlp专用的掩码学习，作者在footnote中指出了，虽然还有其他的目标形式，但是imgae-text matching和mlm基本是所有模型都要使用的。同样的，ViLT也是用了这两个任务。下游任务涉及到自然语言和视觉这两个模态，不过要注意图像和文本的数量关系并不是一一对应的，可能是一对多，也可能是多对一。从宏观上看过以后，我们看看ViLT的具体内容：

**首先，如何去处理文本？**

这个问题的解决方案比较统一，17年开始学界就是用Transformer处理文本了，而且也早早一统江湖，文本可发挥的地方不大。

**重要的是，是如何处理视觉部分**

视觉部分就有很多可以发挥的地方了，你的图像的像素，必须被转化为某一种形式，比如离散化，能够跟language tokens去匹配起来，然后才能和文本一起喂给Transformer去玩Self-Attention。你可能会问为什么不能用Pixel？ViT已经指出了这个问题，就是长度太长了，Transformer接受不了，因此ViT把图像分割为16*16的patches，用patch构建的特征喂给Transformer。因此，就是这类问题的核心就可以抽象为像素 → 语义特征的处理方法如何优化了。

作者指出了，大部分这种VLP都依赖一个目标检测器，原因归纳如下

1. 想要一个离散化的特征，目标检测的框就是天然的离散特征，给你图，返回我框，而且这些框有明确的语义信息，直接用RoI抽取特征即可。思路打开，可以把每个这样的Bounding Box理解为一个词语。
2. 下游任务，因为对于Vision-Language的任务而言，要么是VQA，要么是Captioning，他们和物体的联系太紧密了，对于Visual Reassign/Retrieval来说也是，其实你只要正确地识别出了物体，就有了很大的概率来匹配到相应的文字

目前的VLP都是用了预训练好的目标检测器（Visual Genome数据集，1600个类别和400个属性），就是看中了覆盖类别数量多。如果是coco的80类，很有可能就超出匹配的空间了，总而言之类别越多越好。此外，各个工作也都需要在同数据集比较，因此都选择了这个VG训练的目标检测器，但是它非常昂贵。

作者认为之前大部分工作还是集中在提升视觉编码器上，学术界关注效率没有关注性能这么火，尤其是多模态，都不把它当回事，因为在训练的时候可以抽取好目标检测的特征，放在硬盘上，需要的时候从里面拿，因此可以发现抽特征可以在线下完成，真的训练没想象中这么贵。但是！真实世界中，你的数据每时每秒在新生成，你每个时刻都要去抽取特征，这个时间就不能忽略了，这就是前面工作最大的局限性。

### 对先前工作的归纳

这篇文章比较神奇的地方就是：它的背景知识介绍比自己的方法长得多，作者把抽取图像的技术路线写了一整页，重新定义了vision-language model，并按照以下策略进行分类。

1. 图像和文本的表达是否平衡：使用参数量和计算量来衡量
2. 模态之间如何交互与融合

![Categories of Vision-Language Models](/assets/blog/vilt-vision-language-transformer/ViLT-Categorization.jpg "Categorization")

先对Abbreviation进行一下简单的解释

1. VE：Visual Embedding
2. TE：Textual Embedding
3. MI：模态融合

对于这四张子图而言而言

1. 文本轻量，视觉很贵，融合轻量（点积 or 浅层网络），其代表为Visual Semantic Embedding (VSE)
2. 二者开销基本等价，但融合轻量（点积），其代表为CLIP
3. 最主流的方法，基本80%的工作都是这个形式，文本处理便宜，目标检测非常昂贵，但是性能还不错，其代表为Visual-BERT和UNITER
4. 作者提出方法，认为在多模态任务中，两个模态的融合比较重要，和特征关系最好不要这么大，希望二者的特征抽取都能便宜一点

### ViLT的模型结构

模型的输入细节：：

1. Word：L*H
2. 图像（Patch Embedding）：N*H

![ViLT Model overview](/assets/blog/vilt-vision-language-transformer/ViLT-Model.jpg "ViLT Model")

灰色指代模态，0就是文本，1就是图像，这是因为concatenate后，模型并不知道谁是谁，不利于学习。因此你要告诉模型哪块是文本，哪块是图像，模型的输入和输出等长度。

其中的✳分别代表文本和图片的[CLS] Token

注意：图像中的灰色-绿色-浅绿/灰色-紫色-浅紫，也就是文本/图像的Model-type Embedding，Token Pos Embedding和文本/图像本身的Embeddeding看起来是拼接起来的，实际上是加法加在一起的。

### 训练的策略与细节

1. Image Text Matching：人为设计的任务，故意把和文本匹配的图片随机替换掉，实际上做二分类，让模型判断一张图是否被替换为了另一张图片。
2. MLM：NLP经典任务，都懂的。
3. Word Patch Alignment：文本和图像的相似度如何？OT是把几何和概率联系起来的一个工具。可以理解为在计算文本和图像概率分布的distance

![Word-Patch Alignment](/assets/blog/vilt-vision-language-transformer/ViLT-Word-Patch-Alignment.jpg "Word-Patch Alignment")

看到这里可能有个问题：为啥不给图像也来个MLM？当时ViT已经有了，但是MAE还没出来，不过MAE现在（22年）已经很火了，就前面的模型架构图来看，把图片中的紫色部分遮住，似乎就是个BERT，把蓝色部分遮住，似乎就是个ViT，因此在图片的Caption中也说了是受到了ViT的启发。

**Whole Word Masking：**作者举了个例子，这个giraffe，被劈成小的词根（token）以后，你mask了中间一部分后，由gi和raff开头结尾的单词并不多，很容易就能猜出来是giraffe，根本就不学了。这就导致了你做多模态的时候我压根不借助图像信息了（short cut），一部分loss就失去了意义，因此还不如全部mask掉，让模型一定要借助图像信息。

**Image Augmentation：**之前的多模态任务里没办法用数据增强的，因为特征都已经抽取好了，只要一增强，特征就要全部重抽。作者这里既然已经end2end了，直接就上了修改版的random augment，用了ra的policy，但是去掉了color gitter和cutout，让文本能够和图片对应起来。

**ViLT所使用的数据集**

![ViLT: Dataset](/assets/blog/vilt-vision-language-transformer/ViLT-Dataset.jpg "ViLT: Dataset")

1. MS-COCO：每个图对应5个Caption，标题较长（平均超过十个词）
2. VG：10w图，对应500w文字描述，但是标题比较短
3. GCC：一对一
4. SBU：一对一

一般将他们称为4-million，很多人沿用了这个设定，但实际上每个数据集有自己的特性，比如一对多和多对一关系。因此在衡量数据集大小的时候，我们一般是用图片的数量来衡量数据集的大小，而非是有多少个pair。注意：GCC和SBU现在下不完整了，有很多url失效了。

### 实验效果

**分类任务**

![Comparison of ViLT-B/32 with other models on downstream classification tasks](/assets/blog/vilt-vision-language-transformer/ViLT-Classification-Comp.jpg "Comparison on Classification tasks")

时间：ViLT最大的卖点，之前都是900ms，即使Grid feature也有100ms，但是ViLT直接降低到了15ms

结果：依然是基于目标检测（区域特征）的模型效果最好，但ViLT的速度和精确度结合比较好（成功Tradeoff）

**Retrieval**

![Comparison of ViLT-B/32 on Zero-Shot Retrieval Tasks](/assets/blog/vilt-vision-language-transformer/ViLT-Zero-shot.jpg "Comparison on Zero-Shot")

![Comparison of ViLT-B/32 on Eetrieval Tasks](/assets/blog/vilt-vision-language-transformer/ViLT-Retrieval-Comp.jpg "Comparison on retrieval tasks")

上面是Zero-Shot的性能，下面是经过Fine-Tuning的性能，总而言之，ViLT的性能还差一点点（这样才有坑可填），但性能并不是它的卖点，所以也不用太过在意。

### 消融实验

作者就训练步数对模型性能的提升和前面提到的训练技巧进行了消融。

![ViLT: Ablation Study](/assets/blog/vilt-vision-language-transformer/ViLT-Ablation.jpg "ViLT: Ablation Study")

**问题1：训练时间**

很多自监督的工作，都说自己训练越长越好，比如MoCo，SimCLR，MAE（1600epochs），作者尝试了下这个东西的steps对性能是否有影响。得出的结论是有提升，但是提升很少，消融应该就是在25k做的，但是刷分肯定挑了更好的模型。

**问题2：前面的技巧**

证明了ViLT所使用的图像数据增强非常有效，而且注意，作者在这里让图像也简单的做了下完形填空，但是效果不怎么样（当时MAE还没出来）。

### 拓展方向

1. Scalability：Transformer都是越大越好的，数据越多越好，来个ViLT-H
2. 图像的遮蔽语言建模：今天看来，已经被MAE做掉了，而且有超级多的跟进工作
3. 更先进的数据增强：消融就能发现，数据增强很管用，而且能提高Data Efficiency

## 总结

本文的写作有些非主流，背景知识写出了文献综述的味道，而且是自己方法的两倍长度。不过个人觉得本文对之前工作做的Taxonomy很好，重新定义了vision-language model，来彰显自己方案的可靠性。从文章真正的贡献而言：

1. 模型既没有贵的Embedding，又能保住性能，简单且有效（也让后面人有坑可以填）
2. 证明了不再需要Conv或者Region，任务一样可以做好

不过需要注意，ViLT是用PyTorch-Lightening写的代码，和原生PyTorch有区别，而且需要64个V100训练三天，似乎99%的从业者都不能承担。

总而言之，ViLT算是一个多模态领域开创性的工作，成功地平衡了训练/推理时间开销和下游任务的性能，因此也出现了若干跟进性质的工作，在之后的文章导读中应该还会继续涉及这个话题。
