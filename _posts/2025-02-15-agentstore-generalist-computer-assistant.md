---
title: "AgentStore：迈向通专融合的自动化计算机助手"
date: 2025-02-15 10:00:00 +0800
lang: zh
categories:
  - "Computer-Using Agents"
  - "LLM"
tags:
  - "GUI Agent"
  - "Multi-Agent"
  - "OS Agent"
cover: "/assets/blog/agentstore-generalist-computer-assistant/title.png"
excerpt: "[论文分享] AgentStore: Scalable Integration of Heterogeneous Agents as Specialized Generalist Computer Assistant。"
---
![Title](/assets/blog/agentstore-generalist-computer-assistant/title.png)



**论文题目**：AgentStore: Scalable Integration of Heterogeneous Agents as Specialized Generalist Computer Assistant

**论文地址**：https://arxiv.org/abs/2410.18603

**项目地址**：https://chengyou-jia.github.io/AgentStore-Home/


## 1 引言

随着操作系统的持续发展和应用程序数量的急剧增加，探索自动化计算机助手已成为一个关键的研究领域。尽管现有的通用智能体能够处理多样的任务，它们往往缺乏完成高度专业化任务（如Task_1）所需的深度知识和精确性。另一方面，专业智能体虽在其领域内表现优异，但其应用范围受限，难以承担超出专业领域的任务（如Task_2）。为了克服这些局限性，本文提出了一种通专融合的自动化计算机助手。该方法旨在拓宽智能体系统在泛化和专业化方面的能力边界，通过整合现有两类智能体的优势，以适应不断变化的操作系统环境和多样化的任务需求。这种方法不仅增强了智能体系统的适应性和灵活性，也为自动化助手技术的未来发展打开了新的可能性。

![Title](/assets/blog/agentstore-generalist-computer-assistant/intro.png)

## 2 可扩展智能体集成平台：AgentStore

AgentStore是一个创新的可扩展智能体集成平台。它能够动态地整合多种异构智能体，从通用智能体到高度专业化的智能体，以独立或协作的方式执行复杂的操作系统任务。AgentStore的核心特性包括其高度模块化的架构和灵活的智能体管理系统，这些设计使得它能够快速适应操作系统的变化。

AgentStore由两个主要组成部分构成：AgentPool和MetaAgent。AgentPool（见第2-1节）存储具有特定功能的智能体，并定义了添加新智能体的集成协议。MetaAgent（见第2-2节）从AgentPool中选择最合适的智能体，以独立或协作的方式完成任务。这两部分的设计使AgentStore能够灵活应对各种任务需求，提高任务处理的效率和质量。

![Title](/assets/blog/agentstore-generalist-computer-assistant/overview.png)

## 2-1 AgentPool 

AgentPool 是 AgentStore 中所有可用智能体的集合。开发者在创建新智能体并希望将其集成到 AgentStore 时，必须按照标准化的格式注册该智能体的信息。为了确保集成流程的一致性，我们设立了一个**集成协议**。在注册过程中，开发者需填写预定义表格，详述智能体的功能、限制、适用场景及其功能演示。

所有注册的智能体集合被形式化表示为:
$$
\mathcal{A} = \{(a_1,d_1), (a_2,d_2), ..., (a_n,d_n)\})
$$

其中每个智能体 $a_i$ 的填写表格构成一个文档 $d_i$。为了构建 AgentStore 的原型，我们创建了 20 个计算机应用智能体和 10 个移动应用智能体，分别处理其所在平台的任务。我们同时采用了手动和自动的智能体生成方法。

#### 手动生成计算机应用智能体

由于计算机应用间的操作不一致，统一的自动化智能体生成仍是一大挑战。因此，我们手动设计了适用于常见应用程序的计算机智能体。通过向基于 GUI 的 MMAgent 和基于 CLI 的 FridayAgent 注入领域特定知识文档，使这些智能体得以进化。这些智能体从单模态到多模态，从开源到闭源，从 GUI 到 CLI，形式各异。这种多样的组合为验证 AgentStore 概念的有效性提供了坚实基础。相关智能体列表如下表所示。![ENVISIONS-Title](/assets/blog/agentstore-generalist-computer-assistant/table1.png)

#### 自动生成移动应用智能体

移动应用的操作完全基于 GUI，具有更统一的设计，使我们能够自动化生成领域特定的智能体。遵循 APPAgent 的方法，我们最初开发了一个通用的基于 GUI 的 APPAgent。随后，我们通过自我探索引导其与九个常见移动应用进行导航和互动，最终将其发展为专门的移动平台智能体。这种方法大幅减少了人工工作，确保了为移动应用创建定制智能体的效率。

## 2-2 MetaAgent with AgentToken  

MetaAgent 在 AgentStore 中扮演着至关重要的角色，它负责从 AgentPool 中选择最适合的智能体来独立或协作完成任务。这一过程的核心是 AgentToken 机制，它为智能体的选择和任务分配提供了一种高效可靠的方法。

#### 2-2-1 AgentToken推理

为了提高智能体集成和管理的效率与可扩展性，我们提出了 **AgentToken** 策略。AgentToken通过在MetaAgent 的词汇表中添加token来注册智能体。添加的token被参数化为嵌入矩阵 $W{\mathcal{A}} \in \mathbb{R}^{|\mathcal{A}| \times d}$，并附加到原始词表头$W{\nu} \in \mathbb{R}^{|\mathcal{V}| \times d}$。假设智能体token $W_{\mathcal{A}}$  已经训练并可用，连接后的结果形成了 MetaAgent 的新语言模型头。MetaAgent 预测下一个token的概率为：

$$
P_M(t_i | t_{<i}) = \text{softmax}([W_{\nu}; W_{\mathcal{A}}] \cdot h_{i-1}),
$$
其中下一个token可以是词token或智能体token，即$t_i \in \mathcal{V} \cup \mathcal{A}$。这样，MetaAgent 通过以下两种主要功能实现高效的智能体管理：

##### MetaAgent as Router

MetaAgent 作为一个高效的Router，通过最大化条件概率来预测最可能的下一个token：
$$
t_i^* = \operatorname{arg\,max}_{t \in \mathcal{V} \cup \mathcal{A}} \left(P_{M}(t_i | t_{<i}) \right).
$$
一旦预测出智能体token，即 $t_i^* \in \mathcal{A}$，MetaAgent 停止解码，并调用相应的智能体来执行任务。

##### MetaAgent as Manager

在处理需要多智能体协作的复杂任务时，MetaAgent 表现出哈希Manager的功能。训练过的智能体token常出现在下一个token预测的Top-K候选中，使 MetaAgent 能够预测对任务最相关的 $K$ 个智能体：
$$
T_i^* = \operatorname{TopK}_{t \in \mathcal{A}} \left( P_M(t_i | t_{<i}),\ K \right),\\
$$
这些预测token代表与此任务最相关的 $K$ 个智能体。MetaAgent 则通过使用包含这些选定智能体的在上下文文档的新提示，指导如何为复杂任务生成子任务并将其分配给相应的智能体。这种设计与哈希方法类似，将任意大小的输入转换为固定大小的输出，以便进行有效的检索和任务分配。

#### 2-2-2 AgentToken训练

为了提高智能体的适应性并减轻训练负担，我们采用了自我指导（self-instruct）的自动化过程来训练 AgentToken。这一过程主要涉及智能体token $W_{\mathcal{A}}$ 的训练，这些token是系统中唯一需要训练的参数。然而，训练这些智能体token需要大量的任务描述和初始操作系统状态的演示，但我们的场景中，开发者仅提供有关智能体的文档，无法提供大量的演示数据。 

为了解决这个问题，我们设计了一种迭代算法，这个算法从有限的原始演示开始，引导生成额外的演示数据。首先，我们使用现有的演示和智能体描述$S_i, c_i$来激活 MetaAgent，生成一组新的演示：
$$
S'_i = M(S_i, c_i),
$$
然后，为了确保生成输出的质量，我们应用 BERTScore 来评估新生成的输出，确保它们的一致性和多样性：
$$
\tau_1 \leq \text{BETRScore}(y_k, y_j) \leq \tau_2, \\
\forall y_k, y_j \in S_i \cup S_i^{new} \text{ and } k \neq j.
$$
最后，我们使用贪婪算法迭代筛选生成的演示，最终得到一组经过精炼的演示，这组演示在相似性和多样性之间达到平衡，满足预定的标准。算法细节展示如下：

![ENVISIONS-Title](/assets/blog/agentstore-generalist-computer-assistant/alg1.png)

整个过程是自动化的，MetaAgent 将持续生成额外的示例，直到收集到足够的演示以满足训练需求。在训练阶段，每个任务描述和初始状态都作为输入前缀，特殊智能体token作为预测的下一个token。这种方法不仅简化了训练流程，还确保了语言模型在智能体token被激活时不受影响，从而可以无缝地应用到不同的智能体调用中，极大地提高了系统的灵活性和扩展性。




## 3 主要实验

### 3-1 实验设定

为了评估 AgentStore 的有效性和多功能性，我们在多种任务上进行了全面的实验。首先，我们在三个实际操作系统基准测试中展示了其卓越的性能，这些测试验证了 AgentStore 在实际环境中的应用效果。我们还提供了一些实际运行案例进行定性分析，通过这些案例展示 AgentStore 在解决复杂任务时的策略和效果。

### 3-2 OSworld Benchmark

![ENVISIONS-Title](/assets/blog/agentstore-generalist-computer-assistant/table2.png)

上表展示了我们的方法与当前最优的通用智能体在 OSworld 上的性能比较。虽然更先进的基础模型可以提高性能（例如，GPT-4o 在CogAgent中表现优于 GogVLM），但即便是最好的基础模型仍面临重大挑战。值得注意的是，这些方法不仅整体表现不佳，而且在特定任务类别中还存在明显的弱点。例如，MMAgent 和 CRADLE在处理 Excel 计算任务时因缺乏知识和操作能力而表现不佳，而基于 CLI 的Friday 和 Open-Interpreter 在执行 Chrome 或 Thunderbird 等 GUI 操作任务时也未能有效执行。

相比之下，AgentStore 通过集成多种专业智能体克服了这些限制，每个智能体被指派执行特定擅长的软件和操作。 “AgentStore(GT)” 指的是每个任务都被分配给最合适的智能体，代表了当前 AgentStore 实现的性能上限。如数据所示，使用专业智能体在其各自领域处理任务，使得整个系统在所有领域中都没有显著的性能短板。这强调了多样化能力的重要性。

### 3-3 OSWorld-Multi Benchmark

我们基于 OSWorld 开发了一个全新的基准 OSWorld-Multi，包括超过 100 个需要多个智能体协作的多样化任务。这个新提出的基准测试使我们能够在真实世界环境中评估任务分解和子任务处理的准确性。此外，我们提出了三个指标：AgentMatch、SubtaskAcc 和 ExecutionAcc，分别用来测量多智能体预测的准确性、子任务分解的准确性以及执行成功率。

如下表所示，单一通用智能体 MMAgent 在这个基准测试中表现不佳，这是因为它缺乏智能体预测和任务分解能力。由于智能体组合的无限可能性，Fine-Tuning方法在此场景中不适用，因为其无法预先组织训练所需的数据。此外，尽管 In-context learning 方法在某种程度上是有效的，过长的上下文和庞大的组合空间的限制也导致了次优的结果。相比之下，AgentToken 利用其固有的任务感知能力，显著缩小了选择的智能体范围。它在所有指标上展示了出色的性能。

![ENVISIONS-Title](/assets/blog/agentstore-generalist-computer-assistant/table3.png)

### 3-4 APPAgent Benchmark

我们还使用了APPAgent基准测试来验证 AgentStore 是否可以泛化到移动操作系统平台。该基准包括 9 个流行的移动应用程序，每个应用程序都服务于不同的目的，共同构成了 45 个任务。

下表比较了 AgentStore 与 APPAgent单一通用智能体的性能。如数据所示，通用智能体由于缺乏对每个应用的具体知识，在许多应用中的表现都不尽人意。相比之下，AgentStore 构建了针对各自应用程序的专用智能体，有效解决了某些应用中的性能不足，并显示出从 26.7% 到 57.8% 的显著性能提升。这突显了 AgentStore 概念适用于其他操作系统平台的可能性。

![ENVISIONS-Title](/assets/blog/agentstore-generalist-computer-assistant/table4.png)



## 4 可视化运行实例

在下图中，我们提供了运行示例，以展示 AgentStore 如何增强整个系统的能力。在任务一中，智能体的任务是设置自动邮件转发，这涉及频繁的 GUI 交互并需要理解 Thunderbird 设置。MetaAgent 指派专业的 MailAgent 来处理这一任务，它精确地导航配置转发设置的具体步骤。特别是在第三步中，它执行一系列操作以准确填写所需的表格和选项，展示了其在邮件领域的高级理解能力。同样，在任务二中，需要处理复杂的电子表格处理，MetaAgent 从 AgentPool 中选择 SheetAgent 来处理任务，避免了过于复杂的 GUI 交互。SheetAgent 掌握了 openpyxl 库的知识，并深入理解操作表格所需的步骤，有效完成了这一任务。此外，任务三展示了一个需要多个智能体协作的系统级任务。MetaAgent 成功地将任务分解为子任务，并指派合适的智能体完成每一个子任务。这些案例突出了 AgentStore 在处理领域特定和系统级任务方面的专业通才能力。

![ENVISIONS-Title](/assets/blog/agentstore-generalist-computer-assistant/case1.png)
