# Introduction | <mark>介绍</mark>

---

## Preface | <mark>前言</mark>

Welcome to "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems." As we look across the landscape of modern artificial intelligence, we see a clear evolution from simple, reactive programs to sophisticated, autonomous entities capable of understanding context, making decisions, and interacting dynamically with their environment and other systems. These are the intelligent agents and the agentic systems they comprise.

<mark>欢迎阅读《智能体设计模式：构建智能系统的实践指南》。当我们纵观现代人工智能的发展图景时，可以清楚地看到从简单的反应式程序向复杂、自主的实体的演进，这些实体能够理解上下文、做出决策，并与其环境和其他系统进行动态交互。这些就是智能体 (Intelligent Agent) 以及它们构成的智能体系统 (Agentic System)。</mark>

The advent of powerful large language models (LLMs) has provided unprecedented capabilities for understanding and generating human-like content such as text and media, serving as the cognitive engine for many of these agents. However, orchestrating these capabilities into systems that can reliably achieve complex goals requires more than just a powerful model. It requires structure, design, and a thoughtful approach to how the agent perceives, plans, acts, and interacts.

<mark>强大的大语言模型 (LLM) 的出现为理解和生成类人内容（如文本和媒体）提供了前所未有的能力，成为许多智能体的认知引擎。然而，将这些能力协调成能够可靠实现复杂目标的系统需要的不仅仅是一个强大的模型。它需要结构、设计，以及对智能体如何感知、规划、行动和交互的深思熟虑的方法。</mark>

Think of building intelligent systems as creating a complex work of art or engineering on a canvas. This canvas isn't a blank visual space, but rather the underlying infrastructure and frameworks that provide the environment and tools for your agents to exist and operate. It's the foundation upon which you'll build your intelligent application, managing state, communication, tool access, and the flow of logic.

<mark>将构建智能系统想象成在画布上创作复杂的艺术作品或工程项目。这个画布不是空白的视觉空间，而是为您的智能体提供存在和运作环境和工具的底层基础设施和框架。它是您构建智能应用程序的基础，管理状态、通信、工具访问和逻辑流程。</mark>

Building effectively on this agentic canvas demands more than just throwing components together. It requires understanding proven techniques – **patterns** – that address common challenges in designing and implementing agent behavior. Just as architectural patterns guide the construction of a building, or design patterns structure software, agentic design patterns provide reusable solutions for the recurring problems you'll face when bringing intelligent agents to life on your chosen canvas.

<mark>在这个智能体画布上有效构建需要的不仅仅是将组件简单拼凑在一起。它需要理解经过验证的技术——**模式 (Pattern)**——来解决设计和实现智能体行为时的常见挑战。就像建筑模式指导建筑的构建，或设计模式构建软件一样，智能体设计模式 (Agentic Design Pattern) 为您在选定的画布上赋予智能体生命时面临的重复问题提供可重用的解决方案。</mark>

---

## What are Agentic Systems? | <mark>什么是智能体系统？</mark>

At its core, an agentic system is a computational entity designed to perceive its environment (both digital and potentially physical), make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously. Unlike traditional software, which follows rigid, step-by-step instructions, agents exhibit a degree of flexibility and initiative.

<mark>从根本上讲，智能体系统是一个计算实体，旨在感知其环境（数字环境和潜在的物理环境），基于这些感知和一组预定义或学习的目标做出明智的决策，并自主执行行动来实现这些目标。与遵循严格、逐步指令的传统软件不同，智能体表现出一定程度的灵活性和主动性。</mark>

Imagine you need a system to manage customer inquiries. A traditional system might follow a fixed script. An agentic system, however, could perceive the nuances of a customer's query, access knowledge bases, interact with other internal systems (like order management), potentially ask clarifying questions, and proactively resolve the issue, perhaps even anticipating future needs. These agents operate on the canvas of your application's infrastructure, utilizing the services and data available to them.

<mark>想象一下，您需要一个系统来管理客户咨询。传统系统可能遵循固定的脚本。然而，智能体系统可以感知客户查询的细微差别，访问知识库，与其他内部系统（如订单管理）交互，可能询问澄清问题，并主动解决问题，甚至可能预测未来的需求。这些智能体在您应用程序基础设施的画布上运行，利用可用的服务和数据。</mark>

Agentic systems are often characterized by features like **autonomy**, allowing them to act without constant human oversight; **proactiveness**, initiating actions towards their goals; and **reactiveness**, responding effectively to changes in their environment. They are fundamentally **goal-oriented**, constantly working towards objectives. A critical capability is **tool use**, enabling them to interact with external APIs, databases, or services – effectively reaching out beyond their immediate canvas. They possess **memory**, retain information across interactions, and can engage in **communication** with users, other systems, or even other agents operating on the same or connected canvases.

<mark>智能体系统通常具有以下特征：**自主性 (Autonomy)**，允许它们在没有持续人工监督的情况下行动；**主动性 (Proactiveness)**，主动发起朝向目标的行动；以及**反应性 (Reactiveness)**，有效地响应环境中的变化。它们从根本上是**面向目标的 (Goal-oriented)**，不断朝着目标努力。一个关键能力是**工具使用 (Tool Use)**，使它们能够与外部 API、数据库或服务交互——有效地超越其直接画布的范围。它们拥有**记忆 (Memory)**，在交互中保留信息，并可以与用户、其他系统，甚至在同一或连接画布上运行的其他智能体进行**通信 (Communication)**。</mark>

Effectively realizing these characteristics introduces significant complexity. How does the agent maintain state across multiple steps on its canvas? How does it decide *when* and *how* to use a tool? How is communication between different agents managed? How do you build resilience into the system to handle unexpected outcomes or errors?

<mark>有效实现这些特征会带来显著的复杂性。智能体如何在其画布上的多个步骤中维持状态？它如何决定*何时*和*如何*使用工具？如何管理不同智能体之间的通信？如何在系统中构建韧性以处理意外结果或错误？</mark>

---

## Why Patterns Matter in Agent Development | <mark>为什么模式在智能体开发中很重要</mark>

This complexity is precisely why agentic design patterns are indispensable. They are not rigid rules, but rather battle-tested templates or blueprints that offer proven approaches to standard design and implementation challenges in the agentic domain. By recognizing and applying these design patterns, you gain access to solutions that enhance the structure, maintainability, reliability, and efficiency of the agents you build on your canvas.

<mark>这种复杂性正是智能体设计模式不可或缺的原因。它们不是严格的规则，而是经过实战检验的模板或蓝图，为智能体领域的标准设计和实现挑战提供经过验证的方法。通过识别和应用这些设计模式，您可以获得增强在画布上构建的智能体的结构、可维护性、可靠性和效率的解决方案。</mark>

Using design patterns helps you avoid reinventing fundamental solutions for tasks like managing conversational flow, integrating external capabilities, or coordinating multiple agent actions. They provide a common language and structure that makes your agent's logic clearer and easier for others (and yourself in the future) to understand and maintain. Implementing patterns designed for error handling or state management directly contributes to building more robust and reliable systems. Leveraging these established approaches accelerates your development process, allowing you to focus on the unique aspects of your application rather than the foundational mechanics of agent behavior.

<mark>使用设计模式帮助您避免为管理对话流程、集成外部能力或协调多个智能体行动等任务重新发明基础解决方案。它们提供一种通用语言和结构，使您的智能体逻辑更加清晰，更容易让他人（以及未来的您自己）理解和维护。实现专为错误处理或状态管理设计的模式直接有助于构建更加稳健和可靠的系统。利用这些已建立的方法加速您的开发过程，让您能够专注于应用程序的独特方面，而不是智能体行为的基础机制。</mark>

This book extracts 21 key design patterns that represent fundamental building blocks and techniques for constructing sophisticated agents on various technical canvases. Understanding and applying these patterns will significantly elevate your ability to design and implement intelligent systems effectively.

<mark>本书提取了 21 个关键设计模式，这些模式代表了在各种技术画布上构建复杂智能体的基础构建块和技术。理解和应用这些模式将显著提升您有效设计和实现智能系统的能力。</mark>

---

## Overview of the Book and How to Use It | <mark>本书概述和使用方法</mark>

This book, "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems," is crafted to be a practical and accessible resource. Its primary focus is on clearly explaining each agentic pattern and providing concrete, runnable code examples to demonstrate its implementation. Across 21 dedicated chapters, we will explore a diverse range of design patterns, from foundational concepts like structuring sequential operations (Prompt Chaining) and external interaction (Tool Use) to more advanced topics like collaborative work (Multi-Agent Collaboration) and self-improvement (Self-Correction).

<mark>本书《智能体设计模式：构建智能系统的实践指南》被精心设计为一个实用且易于理解的资源。其主要重点是清楚地解释每个智能体模式，并提供具体的、可运行的代码示例来演示其实现。在 21 个专门的章节中，我们将探索各种设计模式，从基础概念如结构化顺序操作（提示链）和外部交互（工具使用）到更高级的主题如协作工作（多智能体协作）和自我改进（自我纠正）。</mark>

The book is organized chapter by chapter, with each chapter delving into a single agentic pattern. Within each chapter, you will find:

<mark>本书按章节组织，每章深入探讨单一智能体模式。在每章中，您将找到：</mark>

- A detailed **Pattern Overview** providing a clear explanation of the pattern and its role in agentic design.

<mark>- 详细的**模式概述**，清楚地解释模式及其在智能体设计中的作用。</mark>

- A section on **Practical Applications & Use Cases** illustrating real-world scenarios where the pattern is invaluable and the benefits it brings.

<mark>- 关于**实际应用和用例**的部分，说明模式非常有价值的现实场景以及它带来的好处。</mark>

- A **Hands-On Code Example** offering practical, runnable code that demonstrates the pattern's implementation using prominent agent development frameworks. This is where you'll see how to apply the pattern within the context of a technical canvas.

<mark>- **实践代码示例**，提供使用著名智能体开发框架演示模式实现的实用、可运行代码。这是您将看到如何在技术画布环境中应用模式的地方。</mark>

- **Key Takeaways** summarizing the most crucial points for quick review.

<mark>- **关键要点**，总结最重要的点以便快速回顾。</mark>

- **References** for further exploration, providing resources for deeper learning on the pattern and related concepts.

<mark>- 供进一步探索的**参考资料**，为模式和相关概念的深入学习提供资源。</mark>

While the chapters are ordered to build concepts progressively, feel free to use the book as a reference, jumping to chapters that address specific challenges you face in your own agent development projects. The appendices provide a comprehensive look at advanced prompting techniques, principles for applying AI agents in real-world environments, and an overview of essential agentic frameworks. To complement this, practical online-only tutorials are included, offering step-by-step guidance on building agents with specific platforms like AgentSpace and for the command-line interface. The emphasis throughout is on practical application; we strongly encourage you to run the code examples, experiment with them, and adapt them to build your own intelligent systems on your chosen canvas.

<mark>虽然章节按顺序排列以逐步构建概念，但请随意将本书用作参考，跳转到解决您在自己智能体开发项目中面临的特定挑战的章节。附录提供了高级提示技术、在现实世界环境中应用 AI 智能体的原则，以及基本智能体框架概述的全面介绍。为了补充这一点，还包括了仅在线的实用教程，为使用 AgentSpace 等特定平台和命令行界面构建智能体提供逐步指导。整个过程的重点都是实际应用；我们强烈鼓励您运行代码示例，进行实验，并适应它们来在您选择的画布上构建自己的智能系统。</mark>

A great question I hear is, 'With AI changing so fast, why write a book that could be quickly outdated?' My motivation was actually the opposite. It's precisely because things are moving so quickly that we need to step back and identify the underlying principles that are solidifying. Patterns like RAG, Reflection, Routing, Memory and the others I discuss, are becoming fundamental building blocks. This book is an invitation to reflect on these core ideas, which provide the foundation we need to build upon. Humans need these reflection moments on foundation patterns.

<mark>我经常听到一个很好的问题，"随着 AI 变化如此之快，为什么要写一本可能很快就过时的书？"我的动机实际上相反。正是因为事物发展如此迅速，我们需要退一步，识别正在固化的底层原则。我讨论的 RAG、反思、路由、记忆等模式正在成为基本构建块。这本书是对这些核心思想的反思邀请，这些思想为我们需要构建的基础提供了支撑。人类需要这些对基础模式的反思时刻。</mark>

---

## Introduction to the Frameworks Used | <mark>使用框架介绍</mark>

To provide a tangible "canvas" for our code examples (see also Appendix), we will primarily utilize three prominent agent development frameworks. **LangChain**, along with its stateful extension **LangGraph**, provides a flexible way to chain together language models and other components, offering a robust canvas for building complex sequences and graphs of operations. **Crew AI** provides a structured framework specifically designed for orchestrating multiple AI agents, roles, and tasks, acting as a canvas particularly well-suited for collaborative agent systems. The **Google Agent Developer Kit (Google ADK)** offers tools and components for building, evaluating, and deploying agents, providing another valuable canvas, often integrated with Google's AI infrastructure.

<mark>为了为我们的代码示例提供有形的"画布"（另见附录），我们将主要使用三个著名的智能体开发框架。**LangChain**，连同其有状态扩展 **LangGraph**，提供了一种灵活的方式来链接语言模型和其他组件，为构建复杂的操作序列和图提供了强大的画布。**Crew AI** 提供了一个专门为编排多个 AI 智能体、角色和任务而设计的结构化框架，充当特别适合协作智能体系统的画布。**Google 智能体开发工具包 (Google ADK)** 提供了用于构建、评估和部署智能体的工具和组件，提供了另一个有价值的画布，通常与 Google 的 AI 基础设施集成。</mark>

These frameworks represent different facets of the agent development canvas, each with its strengths. By showing examples across these tools, you will gain a broader understanding of how the patterns can be applied regardless of the specific technical environment you choose for your agentic systems. The examples are designed to clearly illustrate the pattern's core logic and its implementation on the framework's canvas, focusing on clarity and practicality.

<mark>这些框架代表了智能体开发画布的不同方面，各有其优势。通过展示这些工具的示例，您将更广泛地了解无论您为智能体系统选择什么特定的技术环境，如何应用这些模式。这些示例旨在清楚地说明模式的核心逻辑及其在框架画布上的实现，重点关注清晰度和实用性。</mark>

By the end of this book, you will not only understand the fundamental concepts behind 21 essential agentic patterns but also possess the practical knowledge and code examples to apply them effectively, enabling you to build more intelligent, capable, and autonomous systems on your chosen development canvas. Let's begin this hands-on journey!

<mark>在本书结束时，您不仅将理解 21 个基本智能体模式背后的基本概念，还将拥有有效应用它们的实用知识和代码示例，使您能够在选定的开发画布上构建更智能、更有能力和更自主的系统。让我们开始这个实践之旅吧！</mark>

---