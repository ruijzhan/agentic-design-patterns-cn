# Introduction | <mark>介绍</mark>

---

## Preface | <mark>前言</mark>

Welcome to "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems." As we look across the landscape of modern artificial intelligence, we see a clear evolution from simple, reactive programs to sophisticated, autonomous entities capable of understanding context, making decisions, and interacting dynamically with their environment and other systems. These are the intelligent agents and the agentic systems they comprise.

<mark>欢迎阅读《智能体设计模式：构建智能系统的实践指南》。纵观现代人工智能的发展图景，我们可以清楚地看到一条演进之路：从简单的响应式程序，到能够理解上下文、做出决策，并与环境及其他系统动态交互的复杂自主实体。这些就是智能体及其构成的智能体系统。</mark>

The advent of powerful large language models (LLMs) has provided unprecedented capabilities for understanding and generating human-like content such as text and media, serving as the cognitive engine for many of these agents. However, orchestrating these capabilities into systems that can reliably achieve complex goals requires more than just a powerful model. It requires structure, design, and a thoughtful approach to how the agent perceives, plans, acts, and interacts.

<mark>大语言模的的出现带来了前所未有的能力，能够理解和生成类人内容（如文本和多媒体），成为许多智能体的认知引擎。然而，要将这些能力编排成能够可靠实现复杂目标的系统，仅有强大的模型还不够，还需要结构化设计，以及对智能体如何感知、规划、行动和交互的深思熟虑。</mark>

Think of building intelligent systems as creating a complex work of art or engineering on a canvas. This canvas isn't a blank visual space, but rather the underlying infrastructure and frameworks that provide the environment and tools for your agents to exist and operate. It's the foundation upon which you'll build your intelligent application, managing state, communication, tool access, and the flow of logic.

<mark>将构建智能系统想象成在画布上创作复杂的艺术作品或工程项目。这个画布不是空白的视觉空间，而是为智能体提供运行环境的底层基础设施和框架。它是构建智能应用的基石，负责管理状态、通信、工具使用和逻辑流程。</mark>

Building effectively on this agentic canvas demands more than just throwing components together. It requires understanding proven techniques – **patterns** – that address common challenges in designing and implementing agent behavior. Just as architectural patterns guide the construction of a building, or design patterns structure software, agentic design patterns provide reusable solutions for the recurring problems you'll face when bringing intelligent agents to life on your chosen canvas.

<mark>在智能体画布上有效构建，绝不只是将组件简单拼凑在一起，而需要理解那些经过验证的技术——也就是<strong>模式（Pattern）</strong>——来应对设计和实现智能体行为时的常见挑战。正如建筑模式指导建筑施工，设计模式规范软件结构，智能体设计模式也为您在画布上构建智能体时反复遇到的问题提供可复用的解决方案。</mark>

---

## What are Agentic Systems? | <mark>什么是智能体系统？</mark>

At its core, an agentic system is a computational entity designed to perceive its environment (both digital and potentially physical), make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously. Unlike traditional software, which follows rigid, step-by-step instructions, agents exhibit a degree of flexibility and initiative.

<mark>从本质上讲，智能体系统是一种计算实体，它能够感知环境（包括数字环境和可能的物理环境），根据感知结果以及预设或学习到的目标做出决策，并自主执行行动以实现目标。与遵循严格逐步指令的传统软件不同，智能体展现出一定的灵活性和主动性。</mark>

Imagine you need a system to manage customer inquiries. A traditional system might follow a fixed script. An agentic system, however, could perceive the nuances of a customer's query, access knowledge bases, interact with other internal systems (like order management), potentially ask clarifying questions, and proactively resolve the issue, perhaps even anticipating future needs. These agents operate on the canvas of your application's infrastructure, utilizing the services and data available to them.

<mark>想象一下，您需要一个系统来管理客户咨询。传统系统可能遵循固定脚本，而智能体系统则能感知客户查询的细微差别，访问知识库，与其他内部系统（如订单管理）交互，可能提出澄清问题，主动解决问题，甚至预测未来需求。这些智能体在应用程序基础设施的画布上运行，利用可用的服务和数据。</mark>

Agentic systems are often characterized by features like **autonomy**, allowing them to act without constant human oversight; **proactiveness**, initiating actions towards their goals; and **reactiveness**, responding effectively to changes in their environment. They are fundamentally **goal-oriented**, constantly working towards objectives. A critical capability is **tool use**, enabling them to interact with external APIs, databases, or services – effectively reaching out beyond their immediate canvas. They possess **memory**, retain information across interactions, and can engage in **communication** with users, other systems, or even other agents operating on the same or connected canvases.

<mark>智能体系统通常具有以下特征：<strong>自主性（Autonomy）</strong>，能在无需持续人工监督的情况下行动；<strong>主动性（Proactiveness）</strong>，主动发起朝向目标的行动；<strong>反应性（Reactiveness）</strong>，有效响应环境变化。它们以<strong>目标</strong>为导向，持续努力达成任务。一项关键能力是<strong>工具使用（Tool Use）</strong>，使它们能够与外部 API、数据库或服务交互，超出自身运行环境进行操作。它们拥有<strong>记忆（Memory）</strong>，在交互中保留信息，并能与用户、其他系统，甚至同一或连接画布上的其他智能体进行<strong>沟通（Communication）</strong>。</mark>

Effectively realizing these characteristics introduces significant complexity. How does the agent maintain state across multiple steps on its canvas? How does it decide *when* and *how* to use a tool? How is communication between different agents managed? How do you build resilience into the system to handle unexpected outcomes or errors?

<mark>要实现这些特性会变得相当复杂。智能体如何在画布上的多个步骤中维持状态？它如何决定<em>何时</em>和<em>如何</em>使用工具？多个代理之间的通信应如何协调？又如何为系统设计容错和恢复机制，以应对意外结果或错误？</mark>

---

## Why Patterns Matter in Agent Development | <mark>为什么模式在智能体开发中很重要</mark>

This complexity is precisely why agentic design patterns are indispensable. They are not rigid rules, but rather battle-tested templates or blueprints that offer proven approaches to standard design and implementation challenges in the agentic domain. By recognizing and applying these design patterns, you gain access to solutions that enhance the structure, maintainability, reliability, and efficiency of the agents you build on your canvas.

<mark>正因为复杂性存在，智能体设计模式才显得至关重要。它们不是死板的规则，而是经过实战检验的模板或蓝图，为智能体领域的标准设计和实现挑战提供可靠的解决方案。识别并应用这些设计模式，能提升您在画布上构建的代理的结构性、可维护性、可靠性和效率。</mark>

Using design patterns helps you avoid reinventing fundamental solutions for tasks like managing conversational flow, integrating external capabilities, or coordinating multiple agent actions. They provide a common language and structure that makes your agent's logic clearer and easier for others (and yourself in the future) to understand and maintain. Implementing patterns designed for error handling or state management directly contributes to building more robust and reliable systems. Leveraging these established approaches accelerates your development process, allowing you to focus on the unique aspects of your application rather than the foundational mechanics of agent behavior.

<mark>使用设计模式帮助您避免为管理对话流程、集成外部能力或协调多智能体行动等任务重新发明解决方案。它们提供通用语言和结构，使智能体逻辑更清晰，更易于他人（以及未来的自己）理解和维护。把专门用于错误处理或状态管理的模式纳入实现，能显著提高系统的健壮性与可靠性。采用这些成熟方法还能加快开发速度，让你把更多精力放在应用的独特价值上，而不是代理行为的底层机制。</mark>

This book extracts 21 key design patterns that represent fundamental building blocks and techniques for constructing sophisticated agents on various technical canvases. Understanding and applying these patterns will significantly elevate your ability to design and implement intelligent systems effectively.

<mark>本书总结了 21 个核心设计模式，构成了在不同技术环境中构建复杂智能代理的基本要素和方法。掌握并运用这些模式能够大幅提升你设计与实现智能系统的能力。</mark>

---

## Overview of the Book and How to Use It | <mark>本书简介及使用方法</mark>

This book, "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems," is crafted to be a practical and accessible resource. Its primary focus is on clearly explaining each agentic pattern and providing concrete, runnable code examples to demonstrate its implementation. Across 21 dedicated chapters, we will explore a diverse range of design patterns, from foundational concepts like structuring sequential operations (Prompt Chaining) and external interaction (Tool Use) to more advanced topics like collaborative work (Multi-Agent Collaboration) and self-improvement (Self-Correction).

<mark>本书《智能体设计模式：构建智能系统的实践指南》旨在成为一个实用且易于理解的资源。它的主要重点是清晰解释每个智能体模式，并提供具体可运行的代码示例来演示其实现。在 21 个专门章节中，我们将探索各种设计模式，从基础概念如结构化顺序操作（提示链）、外部交互（工具使用），到更高级的主题如协作工作（多智能体协作）、自我改进（自我纠正）。</mark>

The book is organized chapter by chapter, with each chapter delving into a single agentic pattern. Within each chapter, you will find:

<mark>本书按章节组织，每章深入探讨单一智能体模式。在每章中，您将找到：</mark>

- A detailed **Pattern Overview** providing a clear explanation of the pattern and its role in agentic design.

- <mark>详细的<strong>模式概述</strong>，清晰解释模式及其在智能体设计中的作用。</mark>

- A section on **Practical Applications & Use Cases** illustrating real-world scenarios where the pattern is invaluable and the benefits it brings.

- <mark><strong>实际应用和用例</strong>部分，说明模式发挥重要作用的实际场景及其带来的好处。</mark>

- A **Hands-On Code Example** offering practical, runnable code that demonstrates the pattern's implementation using prominent agent development frameworks. This is where you'll see how to apply the pattern within the context of a technical canvas.

- <mark><strong>实践代码示例</strong>，提供使用主流智能体开发框架演示模式实现的可运行代码。这里会在具体的技术场景中演示如何应用该模式并提供实用代码。</mark>

- **Key Takeaways** summarizing the most crucial points for quick review.

- <mark><strong>关键要点</strong>，总结最关键的内容以便快速回顾。</mark>

- **References** for further exploration, providing resources for deeper learning on the pattern and related concepts.

- <mark><strong>参考资料</strong>，为模式和相关概念的深入学习提供扩展资源。</mark>

While the chapters are ordered to build concepts progressively, feel free to use the book as a reference, jumping to chapters that address specific challenges you face in your own agent development projects. The appendices provide a comprehensive look at advanced prompting techniques, principles for applying AI agents in real-world environments, and an overview of essential agentic frameworks. To complement this, practical online-only tutorials are included, offering step-by-step guidance on building agents with specific platforms like AgentSpace and for the command-line interface. The emphasis throughout is on practical application; we strongly encourage you to run the code examples, experiment with them, and adapt them to build your own intelligent systems on your chosen canvas.

<mark>虽然章节按顺序编排以逐步构建概念，但您也可以将本书作为参考手册使用，直接跳转到能解决您在智能体开发项目中遇到的特定挑战的章节。附录提供了高级提示技术、在真实环境中应用 AI 智能体的原则，以及核心智能体框架的全面概览。为了补充内容，还提供了实用的在线教程，逐步演示如何在特定平台（如 AgentSpace）和命令行界面上构建代理。全书的重点是实践应用；我们强烈建议您运行书中的代码示例、进行实验并根据需要调整，以在您选择的平台上构建自己的智能系统。</mark>

A great question I hear is, 'With AI changing so fast, why write a book that could be quickly outdated?' My motivation was actually the opposite. It's precisely because things are moving so quickly that we need to step back and identify the underlying principles that are solidifying. Patterns like RAG, Reflection, Routing, Memory and the others I discuss, are becoming fundamental building blocks. This book is an invitation to reflect on these core ideas, which provide the foundation we need to build upon. Humans need these reflection moments on foundation patterns.

<mark>我经常听到一个很好的问题：「AI 变化如此之快，为什么还要写一本可能很快就过时的书？」实际上，我的动机恰恰相反。正是因为事物发展如此迅速，我们才需要退一步，识别那些正在凝固的底层原则。我讨论的 RAG、反思、路由、记忆等模式，正在成为基础构件。本书旨在引导我们反思这些核心思想，它们为我们的构建提供了必要的基础。人类需要这样对基础模式的反思时刻。</mark>

---

## Introduction to the Frameworks Used | <mark>所用框架简介</mark>

To provide a tangible "canvas" for our code examples (see also Appendix), we will primarily utilize three prominent agent development frameworks. **LangChain**, along with its stateful extension **LangGraph**, provides a flexible way to chain together language models and other components, offering a robust canvas for building complex sequences and graphs of operations. **Crew AI** provides a structured framework specifically designed for orchestrating multiple AI agents, roles, and tasks, acting as a canvas particularly well-suited for collaborative agent systems. The **Google Agent Developer Kit (Google ADK)** offers tools and components for building, evaluating, and deploying agents, providing another valuable canvas, often integrated with Google's AI infrastructure.

<mark>为了给代码示例提供具体的「画布」（另见附录），我们将主要使用三个主流的智能体开发框架。<strong>LangChain</strong> 及其有状态扩展 <strong>LangGraph</strong>，能灵活地将语言模型与其他组件串联起来，是构建复杂序列和操作图的理想选择。<strong>Crew AI</strong> 则提供了一个专为协调多个 AI 代理、角色与任务而设计的结构化框架，特别适合用于协作型代理系统。<strong>Google Agent Developer Kit (Google ADK)</strong> 则包含用于构建、评估和部署代理的工具组件，常与 Google 的 AI 基础设施结合使用，作为另一种重要的实现平台。</mark>

These frameworks represent different facets of the agent development canvas, each with its strengths. By showing examples across these tools, you will gain a broader understanding of how the patterns can be applied regardless of the specific technical environment you choose for your agentic systems. The examples are designed to clearly illustrate the pattern's core logic and its implementation on the framework's canvas, focusing on clarity and practicality.

<mark>这些框架代表了智能体开发画布的不同侧面，各有所长。通过展示这些工具的示例，您将更全面地理解如何应用这些模式，无论您为智能体系统选择何种特定技术环境。示例的设计旨在清楚地呈现每种模式的核心逻辑以及在相应框架中的实现，注重可读性和实用性。</mark>

By the end of this book, you will not only understand the fundamental concepts behind 21 essential agentic patterns but also possess the practical knowledge and code examples to apply them effectively, enabling you to build more intelligent, capable, and autonomous systems on your chosen development canvas. Let's begin this hands-on journey!

<mark>读完本书，您不仅能掌握 21 种关键代理设计模式的基本概念，还会获得实用知识和代码示例，帮助您在所选开发平台上有效应用这些模式，构建更智能、更强大、更具自主性的系统。让我们开始这段动手学习之旅吧！</mark>

---
