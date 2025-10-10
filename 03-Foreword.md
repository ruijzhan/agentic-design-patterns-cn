# Introduction | <mark>介绍</mark>

---

## Preface | <mark>前言</mark>

Welcome to "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems." As we look across the landscape of modern artificial intelligence, we see a clear evolution from simple, reactive programs to sophisticated, autonomous entities capable of understanding context, making decisions, and interacting dynamically with their environment and other systems. These are the intelligent agents and the agentic systems they comprise.

<mark>欢迎阅读《智能体设计模式：构建智能系统的实践指南》。纵观当代人工智能的版图，我们清晰地看见一条演进之路：从简单的响应式程序，迈向能够理解上下文、做出决策，并与环境及其他系统动态交互的复杂自主实体。这些正是智能体，及其所组成的智能体系统。</mark>

The advent of powerful large language models (LLMs) has provided unprecedented capabilities for understanding and generating human-like content such as text and media, serving as the cognitive engine for many of these agents. However, orchestrating these capabilities into systems that can reliably achieve complex goals requires more than just a powerful model. It requires structure, design, and a thoughtful approach to how the agent perceives, plans, acts, and interacts.

<mark>大语言模型的出现带来了前所未有的能力，能够理解并生成类人内容（如文本与多媒体），成为众多智能体的认知引擎。然而，要把这些能力编排成能够可靠达成复杂目标的系统，仅有强大的模型还不够；还需要结构化的设计，以及对智能体如何感知、规划、行动与交互的深思熟虑。</mark>

Think of building intelligent systems as creating a complex work of art or engineering on a canvas. This canvas isn't a blank visual space, but rather the underlying infrastructure and frameworks that provide the environment and tools for your agents to exist and operate. It's the foundation upon which you'll build your intelligent application, managing state, communication, tool access, and the flow of logic.

<mark>不妨把构建智能系统理解为在一套「技术底座」上搭建工程：这里的“底座”并非可视化空间，而是为智能体提供生存与运行环境的底层基础设施与框架。它是构建智能应用的基石，承担状态管理、通信、工具接入与逻辑流转。</mark>

Building effectively on this agentic canvas demands more than just throwing components together. It requires understanding proven techniques – **patterns** – that address common challenges in designing and implementing agent behavior. Just as architectural patterns guide the construction of a building, or design patterns structure software, agentic design patterns provide reusable solutions for the recurring problems you'll face when bringing intelligent agents to life on your chosen canvas.

<mark>要在这套智能体「技术底座」上有效构建，远不止把组件简单拼在一起；你需要理解那些行之有效的技术——也就是<strong>模式（Pattern）</strong>——以应对智能体行为设计与实现中的常见难题。正如建筑模式指导施工、设计模式塑造软件架构，智能体设计模式也为你在这一底座上反复遇到的问题提供可复用的解法。</mark>

---

## What are Agentic Systems? | <mark>什么是智能体系统？</mark>

At its core, an agentic system is a computational entity designed to perceive its environment (both digital and potentially physical), make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously. Unlike traditional software, which follows rigid, step-by-step instructions, agents exhibit a degree of flexibility and initiative.

<mark>从本质上讲，智能体系统是一种计算实体，它能够感知环境（包括数字环境和可能的物理环境），根据感知结果以及预设或学习到的目标做出决策，并自主执行行动以实现目标。与遵循严格逐步指令的传统软件不同，智能体展现出一定的灵活性和主动性。</mark>

Imagine you need a system to manage customer inquiries. A traditional system might follow a fixed script. An agentic system, however, could perceive the nuances of a customer's query, access knowledge bases, interact with other internal systems (like order management), potentially ask clarifying questions, and proactively resolve the issue, perhaps even anticipating future needs. These agents operate on the canvas of your application's infrastructure, utilizing the services and data available to them.

<mark>设想你需要一个系统来处理客户咨询。传统系统也许照本宣科地执行脚本；而智能体系统能够洞察咨询的细微差别，访问知识库，与其他内部系统（如订单管理）交互，并在必要时提出澄清问题，主动解决问题，甚至预判后续需求。这些智能体运行在你的应用基础设施「技术底座」之上，善用触手可及的服务与数据。</mark>

Agentic systems are often characterized by features like **autonomy**, allowing them to act without constant human oversight; **proactiveness**, initiating actions towards their goals; and **reactiveness**, responding effectively to changes in their environment. They are fundamentally **goal-oriented**, constantly working towards objectives. A critical capability is **tool use**, enabling them to interact with external APIs, databases, or services – effectively reaching out beyond their immediate canvas. They possess **memory**, retain information across interactions, and can engage in **communication** with users, other systems, or even other agents operating on the same or connected canvases.

<mark>智能体系统通常具备以下特征：<strong>自主性（Autonomy）</strong>——无需持续人工监督亦能行动；<strong>主动性（Proactiveness）</strong>——会主动朝着目标发起行动；<strong>反应性（Reactiveness）</strong>——能有效应对环境变化。它们以<strong>目标</strong>为导向，持续推进任务。关键能力还包括<strong>工具使用（Tool Use）</strong>，使之能够与外部 API、数据库或服务交互，将触角伸出自身运行环境；具备<strong>记忆（Memory）</strong>，能在交互中保留信息；以及<strong>沟通（Communication）</strong>，可与用户、其他系统，乃至同一或相连画布上的智能体进行交流。</mark>

Effectively realizing these characteristics introduces significant complexity. How does the agent maintain state across multiple steps on its canvas? How does it decide *when* and *how* to use a tool? How is communication between different agents managed? How do you build resilience into the system to handle unexpected outcomes or errors?

<mark>要把这些特性真正落地，复杂性随之而来：智能体如何在多步流程中维持状态？如何判断<em>何时</em>、<em>如何</em>使用工具？多个智能体之间的沟通怎样编排？系统该如何具备韧性，以应对意外结果或错误？</mark>

---

## Why Patterns Matter in Agent Development | <mark>为什么模式在智能体开发中很重要</mark>

This complexity is precisely why agentic design patterns are indispensable. They are not rigid rules, but rather battle-tested templates or blueprints that offer proven approaches to standard design and implementation challenges in the agentic domain. By recognizing and applying these design patterns, you gain access to solutions that enhance the structure, maintainability, reliability, and efficiency of the agents you build on your canvas.

<mark>复杂性正是智能体设计模式不可或缺的原因。它们不是刻板的教条，而是经受实战考验的模板与蓝图，为智能体领域的通用设计与实现难题提供可靠路径。识别并应用这些模式，能显著提升你在这一底座上构建的智能体之结构性、可维护性、可靠性与效率。</mark>

Using design patterns helps you avoid reinventing fundamental solutions for tasks like managing conversational flow, integrating external capabilities, or coordinating multiple agent actions. They provide a common language and structure that makes your agent's logic clearer and easier for others (and yourself in the future) to understand and maintain. Implementing patterns designed for error handling or state management directly contributes to building more robust and reliable systems. Leveraging these established approaches accelerates your development process, allowing you to focus on the unique aspects of your application rather than the foundational mechanics of agent behavior.

<mark>采用设计模式，可避免在对话流管理、外部能力集成或多智能体协同等任务上重复造轮子。它们提供通用语言与结构，使智能体的逻辑更清晰，也更便于他人（以及未来的你）理解与维护。将专为错误处理或状态管理设计的模式纳入实现，可显著增强系统的健壮性与可靠性。借助这些成熟方法，你能加快开发，把精力投入到应用的独特价值，而非智能体行为的底层机理。</mark>

This book extracts 21 key design patterns that represent fundamental building blocks and techniques for constructing sophisticated agents on various technical canvases. Understanding and applying these patterns will significantly elevate your ability to design and implement intelligent systems effectively.

<mark>本书提炼出 21 个关键设计模式，构成了在不同「技术底座」上构建复杂智能体的基本积木与方法。理解并运用这些模式，将显著提升你设计与实现智能系统的能力。</mark>

---

## Overview of the Book and How to Use It | <mark>本书简介及使用方法</mark>

This book, "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems," is crafted to be a practical and accessible resource. Its primary focus is on clearly explaining each agentic pattern and providing concrete, runnable code examples to demonstrate its implementation. Across 21 dedicated chapters, we will explore a diverse range of design patterns, from foundational concepts like structuring sequential operations (Prompt Chaining) and external interaction (Tool Use) to more advanced topics like collaborative work (Multi-Agent Collaboration) and self-improvement (Self-Correction).

<mark>本书旨在成为一部实用且易读的参考。核心在于清晰讲解每一种智能体模式，并配以可运行的代码示例展示其实现。全书用 21 个专章覆盖多种设计模式：从结构化顺序操作（提示链）、外部交互（工具使用）等基础概念，到协同工作（多智能体协作）、自我改进（自我纠正）等进阶主题。</mark>

The book is organized chapter by chapter, with each chapter delving into a single agentic pattern. Within each chapter, you will find:

<mark>本书按章节组织，每章聚焦一种智能体模式。每章均包含：</mark>

- A detailed **Pattern Overview** providing a clear explanation of the pattern and its role in agentic design.

- <mark>详细的<strong>模式概述</strong>，清晰解释模式及其在智能体设计中的作用。</mark>

- A section on **Practical Applications & Use Cases** illustrating real-world scenarios where the pattern is invaluable and the benefits it brings.

- <mark><strong>实际应用和用例</strong>部分，说明模式发挥重要作用的实际场景及其带来的好处。</mark>

- A **Hands-On Code Example** offering practical, runnable code that demonstrates the pattern's implementation using prominent agent development frameworks. This is where you'll see how to apply the pattern within the context of a technical canvas.

- <mark><strong>实践代码示例</strong>：用主流智能体开发框架给出可运行示例，在具体「技术底座」中演示如何应用该模式。</mark>

- **Key Takeaways** summarizing the most crucial points for quick review.

- <mark><strong>关键要点</strong>，总结最关键的内容以便快速回顾。</mark>

- **References** for further exploration, providing resources for deeper learning on the pattern and related concepts.

- <mark><strong>参考资料</strong>，为模式和相关概念的深入学习提供扩展资源。</mark>

While the chapters are ordered to build concepts progressively, feel free to use the book as a reference, jumping to chapters that address specific challenges you face in your own agent development projects. The appendices provide a comprehensive look at advanced prompting techniques, principles for applying AI agents in real-world environments, and an overview of essential agentic frameworks. To complement this, practical online-only tutorials are included, offering step-by-step guidance on building agents with specific platforms like AgentSpace and for the command-line interface. The emphasis throughout is on practical application; we strongly encourage you to run the code examples, experiment with them, and adapt them to build your own intelligent systems on your chosen canvas.

<mark>虽然章节循序铺陈、层层递进，但你也可以将其当作参考手册，直达与你当前挑战相关的章节。附录囊括高级提示技巧、在真实环境中应用 AI 智能体的原则，以及主流智能体框架的概览。为便于上手，还配有仅在线提供的实操教程，手把手演示如何在特定平台（如 AgentSpace）与命令行界面上构建智能体。全书强调「可操作性」：我们鼓励你运行示例、尽情试验，并按需调整，在你选定的「技术底座」上搭建自己的智能系统。</mark>

A great question I hear is, 'With AI changing so fast, why write a book that could be quickly outdated?' My motivation was actually the opposite. It's precisely because things are moving so quickly that we need to step back and identify the underlying principles that are solidifying. Patterns like RAG, Reflection, Routing, Memory and the others I discuss, are becoming fundamental building blocks. This book is an invitation to reflect on these core ideas, which provide the foundation we need to build upon. Humans need these reflection moments on foundation patterns.

<mark>我常被问到：「AI 日新月异，为何还要写一本可能很快过时的书？」我的动机恰恰相反：正因演进太快，我们更需要退后一步，辨识那些正在定型的底层原则。诸如 RAG、反思、路由、记忆等模式，正成为基础积木。本书邀请你回望这些核心观念，它们构成我们得以继续搭建的地基。对于基础模式，人类需要这样的「反思时刻」。</mark>

---

## Introduction to the Frameworks Used | <mark>所用框架简介</mark>

To provide a tangible "canvas" for our code examples (see also Appendix), we will primarily utilize three prominent agent development frameworks. **LangChain**, along with its stateful extension **LangGraph**, provides a flexible way to chain together language models and other components, offering a robust canvas for building complex sequences and graphs of operations. **Crew AI** provides a structured framework specifically designed for orchestrating multiple AI agents, roles, and tasks, acting as a canvas particularly well-suited for collaborative agent systems. The **Google Agent Developer Kit (Google ADK)** offers tools and components for building, evaluating, and deploying agents, providing another valuable canvas, often integrated with Google's AI infrastructure.

<mark>为了给代码示例提供具体的「承载底座」（亦可参阅附录），本书主要采用三类代表性智能体开发框架。<strong>LangChain</strong> 与其有状态扩展 <strong>LangGraph</strong>，可灵活串联语言模型与各类组件，适于构建复杂的序列与有向图；<strong>Crew AI</strong> 提供专为多智能体、角色与任务编排而设的结构化框架，尤其适合协作型系统；<strong>Google Agent Developer Kit (Google ADK)</strong> 则提供构建、评估与部署智能体的工具与部件，常与 Google 的 AI 基础设施协同作为另一类「技术底座」。</mark>

These frameworks represent different facets of the agent development canvas, each with its strengths. By showing examples across these tools, you will gain a broader understanding of how the patterns can be applied regardless of the specific technical environment you choose for your agentic systems. The examples are designed to clearly illustrate the pattern's core logic and its implementation on the framework's canvas, focusing on clarity and practicality.

<mark>这些框架呈现了智能体开发「技术底座」的不同切面，各有所长。跨工具对照示例，有助于你理解模式如何在不同技术语境中落地。示例专注呈现模式的核心逻辑与在框架上的实现，强调清晰与实用。</mark>

By the end of this book, you will not only understand the fundamental concepts behind 21 essential agentic patterns but also possess the practical knowledge and code examples to apply them effectively, enabling you to build more intelligent, capable, and autonomous systems on your chosen development canvas. Let's begin this hands-on journey!

<mark>通读全书后，你不仅将理解 21 种关键智能体设计模式的基本理念，还将收获足以落地的实践知识与代码示例，助你在所选「技术底座」上高效应用这些模式，构建更智能、更强大、更具自主性的系统。让我们开始这段动手之旅！</mark>

---
