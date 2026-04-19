---
title: "SEA：基于大模型的自动评审框架"
date: 2024-07-30 10:00:00 +0800
lang: zh
categories:
  - "LLM"
  - "Research Methodology"
tags:
  - "LLM"
  - "Peer Review"
  - "Evaluation"
cover: "/assets/blog/sea-automated-peer-reviewing/paper.png"
excerpt: "[论文分享] Automated Peer Reviewing in Paper SEA: Standardization, Evaluation, and Analysis。"
---
![ENVISIONS-Title](/assets/blog/sea-automated-peer-reviewing/paper.png)

**论文题目**：Automated Peer Reviewing in Paper SEA: Standardization, Evaluation, and Analysis

**主页地址**: https://ecnu-sea.github.io/

**论文地址**：https://arxiv.org/abs/2407.12857

**Github地址**：https://github.com/ecnu-sea/sea


## 1 引言

当前，学术论文数量的激增对传统评审机制造成了严重冲击，导致出版物质量参差不齐，不仅加大了同行评审的压力，也对科研环境产生了负面影响。现有的方法通过Prompt工程诱导大语言模型（LLM）进行评审，但这些模型往往倾向于讨好人类，输出的内容较为圆滑；另一类方法使用同行评审数据进行微调，但由于微调时仅使用一个评审标签，生成的意见往往是片面和不完整的。（如下图所示）

![SEA-Motivation](/assets/blog/sea-automated-peer-reviewing/motivation.png)

因此，本研究的核心是：**如何让大型语言模型生成高质量且全面的评审内容，从而帮助作者提升论文质量？**


## 2 自动化论文评审框架：SEA

![SEA-Model](/assets/blog/sea-automated-peer-reviewing/method.png)

本文提出一个新颖的自动化论文评审框架SEA，包括三个模块：标准化，评估和分析。如上图所示。

### 2-1 SEA-S（标准化模块）： 
为了使大型语言模型（LLMs）具备审稿能力，高质量的SFT（监督微调）数据集至关重要。然而，现有的同行评审数据集的评审标签存在以下两个问题：
1. 每篇文章对应多条评审，不同的评审基于其领域或知识提供片面的意见。
2. 不同领域以及不同年份的评审格式各异，直接进行SFT会造成不一致性。

为了解决这些问题，本文提出将一篇文章的所有评审整合为一个评审。这种整合后的评审不仅内容丰富，还统一了格式。具体来说，本文尝试使用不同的闭源和开源模型基于特定指令进行整合，发现只有GPT-4能够达到理想效果。然而，GPT-4的成本高且缺乏扩展性。因此，作者随机抽取20%的评审数据，用GPT-4进行整合，并将整合后的评审作为标签，原始的多条评审作为输入，构建SFT数据集来微调开源模型Mistral-7B。通过这种方法，将GPT-4的整合能力蒸馏到Mistral-7B中，形成数据标准化模型SEA-S。最后，作者利用SEA-S对同行评审数据集的评审标签进行整合，生成高质量的评审标签。


### 2-2 SEA-E（评估模块）：

本文采用Nougat对原论文PDF进行解析。Nougat是一款专门的学术文档PDF解析器，能够将公式转换为LaTeX代码。随后，将SEA-S的输出与解析后的PDF结合，构建了一个高质量的同行评审指令微调数据集，并用其对Mistral-7B进行微调，最终得到一个能够生成全面且高质量审稿意见的评审模型SEA-E。

### 2-3 SEA-A（分析模块）：

为了分析SEA-E生成的意见与原始文章的一致性，本文训练了一个回归模型SEA-A。该模型基于原始文章和SEA-E生成的评审内容，预测这些内容与文章的一致性得分。本文利用训练集中的论文的Reviewer confidence作为权重，来计算平均的Rating分数作为ground truth： 

![SEA-Formula](/assets/blog/sea-automated-peer-reviewing/eq1.png)

随后，SEA-A的输入为经过表征模型得到的文章表征和评审表征。

![SEA-Formula](/assets/blog/sea-automated-peer-reviewing/eq2.png)
![SEA-Formula](/assets/blog/sea-automated-peer-reviewing/eq3.png)


SEA-A的最终输出作为mismatch score，分数越接近0，生成的评审内容与原文更一致。基于此，本文引入了一个自我修正机制，当SEA-E生成的意见与原始文章不一致时，SEA-A会提供反馈，指导SEA-E重新生成更一致的审稿意见。


## 3 主要实验

### 3-1 实验设定
本文爬取了OpenReview上NeurIPS-2023和ICLR-2024数据，其中90%的数据作为训练数据，剩下的10%作为测试集。此外测试集还包括REVIEWER2、PeerRead、NLPeer的数据。

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/dataset.png)

Baseline模型包括原始的Mistral-7B，随机挑选review进行SFT得到的Mistral-7B-R，GPT-3.5整合数据进行SFT得到的Mistral-7B-3.5。本文方法的模型包括SEA-E和SEA-EA，其中SEA-EA是将自我修复机制与SEA-E相结合的增强模型。评估指标采用BLEU，ROUGE和BERTScore。


### 3-2 主要实验结果
可以看到SEA在所有数据集上都远远超出别的baseline模型，无论是in-domain还是cross-domain。此外，SEA-EA也在所有的结果上超过了SEA-E，凸显出自我纠正机制在生成与原始文章更一致的评审的有效性。M-7B-R表现不佳可能是因为只用一条评审作为SFT的数据，导致生成的内容不够丰富；M-7B生成的内容虽然长度长，但是未能与人类评审对齐，质量不佳。M-7B-3.5表现不如SEA-E是因为数据标准化质量不够。
                        

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/main_results.png)

### 3-3 标准化结果分析

1. 内容分析:
由于整合后的评审内容没有ground truth，无法直接使用主试验的评估指标进行评估。为了解决这个问题，本文设计了一种巧妙的方法来评估不同模型的评审整合能力。具体来说，本文将SEA-S整合的评审内容作为参考（references），而其他模型整合的评审内容作为候选（candidates）。接着，计算候选与参考之间ROUGE值的召回率（recall）和精准率（precision）。通过这两个指标，可以推断出两个评论中重叠和独立语义信息的百分比。从信息量的角度来看，这有助于评估哪个模型整合的评审内容更为丰富，从而间接说明其整合能力更强。结果如下：

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/sea-s.png)

2. 格式分析：
相较于Mistral-7B和GPT-3.5，SEA-S整合的内容更为丰富，这进一步验证了SEA-S在标准化评审并提供更丰富信息方面的优越性。此外，研究还发现，SEA-S整合的内容甚至略优于GPT-4，因为GPT-4在整合过程中，有时会因未能完全遵循指令而生成低质量的评审内容。


![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/sea-s_format.png)


### 3-4 SEA-A中的不匹配度分数

本小节分析了不同模型生成的评审内容与原始文章之间的一致性。将不同模型在测试集上生成的评审内容输入SEA-A，计算每个模型在不同数据集上的mismatch score。结果显示，SEA-EA在所有数据集上保持最低的mismatch score，其次是SEA-E，这证明了SEA能够生成与原始文章更一致的评审意见。Mistral-7B由于没有经过SFT，未能学习到生成评审与原始文章一致的内容，因此表现最差。

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/mms_metric.png)


### 3-5 定量分数分析

本文还对生成评审中的评分部分进行了分析，包括Soundness、Presentation、Contribution和Rating。基于原数据中confidence的加权均分作为ground truth，并采用均方误差（MSE）作为度量标准。括号中的百分比表示生成内容能够准确生成有效分数的比例。结果显示：

1. SEA确保了输出格式的有效性。
2. MSE度量表明，SEA在所有情况下都优于基线模型。
3. SEA-EA在大多数情况下表现优于SEA-E，进一步验证了自我修正机制能够使生成结果与人类反馈在定量评估结果上高度一致。

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/score.png)


### 3-6 定性决策分析

本小节分析了生成的Decision和Reason部分，即类似于Meta-review的内容。结果如下表所示：

1. SEA-EA的准确率和BERTScore最高，后者表明生成内容与meta-review更加贴近。
2. NeurIPS-23数据集由于数据本身的问题（95%都是Accept），没有太大的参考价值。
3. ICLR-24数据集中，SEA-EA的准确率超过SEA-E多达4%，进一步表明自我纠正策略的有效性。
4. Mistral-7B的Recall高达97.65%，但Precision较低，这表明它倾向于迎合人类偏好，接受大部分论文。
5. SEA在Precision和F1上表现更好，这表明本文的方法可以更有效地识别不同质量的论文。

总体而言，SEA生成的评审内容更接近实际的审稿决策，并且不偏向于接受决策。

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/decision.png)


## SEA生成的实例展示

![SEA-Exp](/assets/blog/sea-automated-peer-reviewing/sea_new.png)
