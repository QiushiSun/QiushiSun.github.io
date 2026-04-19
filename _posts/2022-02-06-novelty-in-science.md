---
title: "The Value of Research & Novelty in Science"
date: 2022-02-06 09:12:37 +0800
lang: zh
categories:
  - "research"
tags:
  - "research"
cover: "/assets/blog/novelty-in-science/novelty.jpg"
excerpt: "学习笔记：判断研究工作的价值，以及研究新意度（Novelty）的五大误解。"
---
学习笔记：判断研究工作的价值，以及研究新意度（Novelty）的五大误解



<!-- ![Hugo-logo-wide](/assets/blog/novelty-in-science/novelty.jpg "The Value of Research & Novelty in Science") -->

本篇博客是基于李沐老师的视频：

1. [如何判断（你自己的）研究工作的价值](https://www.bilibili.com/video/BV1oL411c7Us)
2. [你（被）吐槽过论文不够 novel 吗？](https://www.bilibili.com/video/BV1ea41127Bq?share_source=copy_web)

总结的学习笔记

## 研究工作的价值

### **核心思想**：用有新意的方法有效地解决一个研究问题

1. 问题
   1. 工程问题
      1. 如算法很占内存，代码是否能优化，实现方式是否能优化
      2. 如模型精度不高，那是否能多采样点数据
   2. 研究问题
2. 有效（相对地有效性）
   1. 相对之前的工作，你一般无法彻底解决一个问题，相对之前的工作我是否能做提升
3. 新意（Novelty）：对你的研究社区中的其他研究者而言，你用的方法别人没想到

### 研究工作的价值

新意度 x 有效性 x 问题大小 = 价值

每一项都可以分为三个级别：1，10，100

| 新意度                                      | 有效性                                  | 问题大小                            |
| ------------------------------------------- | --------------------------------------- | ----------------------------------- |
| 1（说了你的方法，后面的文章结果都不用看了） | 1（好那么一点点，多重复几次就差不多了） | 1（对前面的工作在不好一个的点改进） |
| 10（某一方面用了聪明的技术）                | 10（中等，可见的提升）                  | 10（比如一个计算机视觉的子任务）    |
| 100（之前的工作没用过，打开了新世界的大门） | 100（一个工作就能向前推5-10个点）       | 100（可以大到解决通用的人工智能）   |

如果一个工作能拿到两个10，那么值得一写，如果能拿到10，10，10就很不错，两个方向拉满就非常困难，三个方向都拉满即功成名就。



## 研究新意度（Novelty）的五大误解

文章链接：[Novelty in Science](https://perceiving-systems.blog/en/news/novelty-in-science)，这篇文章是用来教育reviewer的。

作者背景：德国马普所智能系统研究院的创始人之一，研究方向是计算机视觉、计算机图形学等。

用来评价论文价值的公式对强理论性的工作并不适用，因为对一个理论问题来说，你很难判断他这个领域的大小，有效性也不是很好判断，因为一个定理总是正确的。所以理论研究者对一个文章的判断，作者经常用两个词：

1. 深刻：你是不是揭示了一些本质的一些东西
2. 优美：你的定理的本身和你证明，是不是有美感（与个人品味相关）

优美这个词的好处是他把**技术性**和**复杂性**从指标中剥夺出来了

参考：毕加索和伦勃朗，我们都能欣赏出美来，即使创作过程作品的复杂度有区别，创作的艰难度上有区别。

### 1. Novelty as Complexity：用复杂度衡量Novelty

The simplicity of an idea is often confused with a lack of novelty when exactly the opposite is often true.  A common review critique is

*The idea is very simple. It just changes one term in the loss and everything else is the same as prior work.*

If nobody thought to change that one term, then it is *ipso facto* novel. The inventive insight is to realize that a small change could have a big effect and to formulate the new loss.

典型：只修改了损失函数

### 2. Novelty as Difficulty：用困难度衡量Novelty

Formulating a simple idea means stripping away the unnecessary to reveal the core of something. This is one of the most useful things that a scientist can do.

典型：Ian Goodfellow的GAN，着重解释对抗的思想，而不是为了效果堆砌复杂技术（比如把文中的MLP替换为CNN）

### 3. Novelty as Surprise：用惊讶来衡量Novelty

完全使用**Surprise**来衡量，那么会认为一个新的工作自然而然，人的思维就是这样的。

*The idea is obvious because the authors just combined two well known ideas.*

在你没有听到前，你大概率没想到过！

典型：MAE，就是简单的技术拼在一起，但是在这之前并没有人想到，所以它拥有Novelty。

### 4. Novelty as Technical Novelty：用技术新意来等价新意

典型：ImageNet，大家都是晚上抓图片然后人工标注，但是ImageNet大啊，大才能支撑深度学习中的各种算法。

此外，如果你把一个复杂的算法替换为简单的算法，而且能提供一些Insight，那当然也是有效的。

### 5. Novelty as Usefulness or value：用有效性等价新意

Lack of utility is indeed an issue but it is very hard to assess with a new idea. Reviewers should be careful here and aware that we all have limited imagination.

实用性的缺少不能代表新意度低，它的确是个问题，但是后面可能会被其他研究者玩出花来

### 总结：Novelty≠ Complexity, Difficulty, Surprise, Technical Novelty, Usefulness.

文章作者认为新意度，更多的是关于这个想法是不是优美的。
