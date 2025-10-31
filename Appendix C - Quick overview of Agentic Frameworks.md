# Appendix C - Quick overview of Agentic Frameworks | <mark>附录C: 智能体框架快速概览</mark>


## LangChain 

LangChain is a framework for developing applications powered by LLMs. Its core strength lies in its LangChain Expression Language (LCEL), which allows you to "pipe" components together into a chain. This creates a clear, linear sequence where the output of one step becomes the input for the next. It's built for workflows that are Directed Acyclic Graphs (DAGs), meaning the process flows in one direction without loops.

<mark>LangChain 是一个用于开发基于大语言模型 (LLM) 的应用程序框架。它的核心优势在于其 LangChain 表达式语言 (LCEL)，该语言允许您将组件“串联”成一个链。这创建了一个清晰的线性序列，其中一步的输出成为下一步的输入。它专为有向无环图 (DAG) 工作流而设计，这意味着流程沿一个方向流动，没有循环。</mark>

Use it for: <mark>用途：</mark>

●  Simple RAG: Retrieve a document, create a prompt, get an answer from an LLM.

<mark>简单 RAG：检索文档，创建提示，从 LLM 获取答案。</mark>

●  Summarization: Take user text, feed it to a summarization prompt, and return the output.

<mark>摘要：获取用户文本，将其输入摘要提示，并返回输出结果。</mark>

●  Extraction: Extract structured data (like JSON) from a block of text.

<mark>提取：从文本块中提取结构化数据（例如 JSON）。</mark>

Python



## LangGraph

LangGraph is a library built on top of LangChain to handle more advanced agentic systems. It allows you to define your workflow as a graph with nodes (functions or LCEL chains) and edges (conditional logic). Its main advantage is the ability to create cycles, allowing the application to loop, retry, or call tools in a flexible order until a task is complete. It explicitly manages the application state, which is passed between nodes and updated throughout the process.

<mark>LangGraph 是一个基于 LangChain 构建的库，用于处理更高级的智能体系统。它允许您将工作流定义为一个图，该图由节点（函数或 LCEL 链）和边（条件逻辑）组成。其主要优势在于能够创建循环，从而允许应用程序以灵活的顺序循环、重试或调用工具，直到任务完成。它显式地管理应用程序状态，该状态在节点之间传递并在整个过程中更新。</mark>

Use it for: <mark>用途：</mark>

●  Multi-agent Systems: A supervisor agent routes tasks to specialized worker agents, potentially looping until the goal is met.

<mark>多智能体系统：主管智能体将任务分配给专门的工作智能体，可能会循环执行，直到达到目标。</mark>

●  Plan-and-Execute Agents: An agent creates a plan, executes a step, and then loops back to update the plan based on the result.

<mark>计划执行智能体：智能体创建计划，执行步骤，然后循环返回并根据结果更新计划。</mark>

●  Human-in-the-Loop: The graph can wait for human input before deciding which node to go to next.

<mark>人机交互：该图可以等待人工输入，然后再决定下一步要访问哪个节点。</mark>

Feature	                   LangChain	                        LangGraph

Core Abstraction	      Chain (using LCEL)	                 Graph of Nodes

Workflow Type	      Linear (Directed Acyclic Graph)	     Cyclical (Graphs with loops)

State Management	  Generally stateless per run	        Explicit and persistent state object

Primary Use	      Simple, predictable sequences	      Complex, dynamic, stateful agents

Which One Should You Use? <mark>你应该使用哪一个？</mark>

●  Choose LangChain when your application has a clear, predictable, and linear flow of steps. If you can define the process from A to B to C without needing to loop back, LangChain with LCEL is the perfect tool.

<mark>如果您的应用流程清晰、可预测且呈线性发展，那么 LangChain 是您的理想之选。如果您可以定义从 A 到 B 到 C 的完整流程而无需循环，那么 LangChain 与 LCEL 结合使用将是您的完美选择。</mark>

●  Choose LangGraph when you need your application to reason, plan, or operate in a loop. If your agent needs to use tools, reflect on the results, and potentially try again with a different approach, you need the cyclical and stateful nature of LangGraph.

<mark>当您的应用程序需要进行推理、规划或循环操作时，请选择 LangGraph。如果您的智能体需要使用工具、反思结果，并可能尝试不同的方法，那么您就需要 LangGraph 的循环性和有状态特性。</mark>

Python


## Google's ADK

Google's Agent Development Kit, or ADK, provides a high-level, structured framework for building and deploying applications composed of multiple, interacting AI agents. It contrasts with LangChain and LangGraph by offering a more opinionated and production-oriented system for orchestrating agent collaboration, rather than providing the fundamental building blocks for an agent's internal logic.

<mark>谷歌智能体开发工具包（ADK）提供了一个高级的结构化框架，用于构建和部署由多个交互的AI智能体组成的应用程序。与LangChain和LangGraph不同，ADK提供了一个更具规范性和面向生产环境的系统来协调智能体之间的协作，而不是提供智能体内部逻辑的基本构建模块。</mark>

LangChain operates at the most foundational level, offering the components and standardized interfaces to create sequences of operations, such as calling a model and parsing its output. LangGraph extends this by introducing a more flexible and powerful control flow; it treats an agent's workflow as a stateful graph. Using LangGraph, a developer explicitly defines nodes, which are functions or tools, and edges, which dictate the path of execution. This graph structure allows for complex, cyclical reasoning where the system can loop, retry tasks, and make decisions based on an explicitly managed state object that is passed between nodes. It gives the developer fine-grained control over a single agent's thought process or the ability to construct a multi-agent system from first principles.

<mark>LangChain 在最基础的层面上运行，提供创建操作序列所需的组件和标准化接口，例如调用模型并解析其输出。LangGraph 在此基础上扩展了功能，引入了更灵活、更强大的控制流；它将智能体的工作流程视为一个有状态图。使用 LangGraph，开发者可以显式地定义节点（即函数或工具）和边（即执行路径）。这种图结构支持复杂的循环推理，系统可以循环执行、重试任务，并基于在节点之间传递的显式管理的状态对象做出决策。它使开发者能够对单个智能体的思维过程进行细粒度控制，或者从零开始构建多智能体系统。</mark>

Google's ADK abstracts away much of this low-level graph construction. Instead of asking the developer to define every node and edge, it provides pre-built architectural patterns for multi-agent interaction. For instance, ADK has built-in agent types like SequentialAgent or ParallelAgent, which manage the flow of control between different agents automatically. It is architected around the concept of a "team" of agents, often with a primary agent delegating tasks to specialized sub-agents. State and session management are handled more implicitly by the framework, providing a more cohesive but less granular approach than LangGraph's explicit state passing. Therefore, while LangGraph gives you the detailed tools to design the intricate wiring of a single robot or a team, Google's ADK gives you a factory assembly line designed to build and manage a fleet of robots that already know how to work together.

<mark>Google ADK 抽象化了许多底层图构建工作。它无需开发者定义每个节点和边，而是提供了预构建的多智能体交互架构模式。例如，ADK 内置了 SequentialAgent 或 ParallelAgent 等智能体类型，可以自动管理不同智能体之间的控制流。它的架构围绕着智能体“团队”的概念展开，通常由一个主智能体将任务委派给专门的子智能体。框架以更隐式的方式处理状态和会话管理，提供了一种比 LangGraph 的显式状态传递更统一但粒度更低的方法。因此，LangGraph 提供了设计单个机器人或团队复杂线路的详细工具，而 Google 的 ADK 则提供了一条工厂装配线，用于构建和管理一支已经知道如何协同工作的机器人集群。</mark>

Python


This code creates a search-augmented agent. When this agent receives a question, it will not just rely on its pre-existing knowledge. Instead, following its instructions, it will use the Google Search tool to find relevant, real-time information from the web and then use that information to construct its answer.

<mark>这段代码创建了一个搜索增强型智能体。当该智能体接收到问题时，它不会仅仅依赖其已有的知识。相反，它会按照指令，使用谷歌搜索工具从网络上查找相关的实时信息，然后利用这些信息构建答案。</mark>


## Crew.AI

CrewAI offers an orchestration framework for building multi-agent systems by focusing on collaborative roles and structured processes. It operates at a higher level of abstraction than foundational toolkits, providing a conceptual model that mirrors a human team. Instead of defining the granular flow of logic as a graph, the developer defines the actors and their assignments, and CrewAI manages their interaction.

<mark>CrewAI 提供了一个编排框架，用于构建多智能体系统，其核心在于协作角色和结构化流程。与基础工具包相比，CrewAI 的抽象层次更高，提供了一个类似于人类团队的概念模型。开发者无需将细粒度的逻辑流程定义为图，只需定义参与者及其任务，CrewAI 便会负责管理它们之间的交互。</mark>

The core components of this framework are Agents, Tasks, and the Crew. An Agent is defined not just by its function but by a persona, including a specific role, a goal, and a backstory, which guides its behavior and communication style. A Task is a discrete unit of work with a clear description and expected output, assigned to a specific Agent. The Crew is the cohesive unit that contains the Agents and the list of Tasks, and it executes a predefined Process. This process dictates the workflow, which is typically either sequential, where the output of one task becomes the input for the next in line, or hierarchical, where a manager-like agent delegates tasks and coordinates the workflow among other agents.

<mark>该框架的核心组成部分包括智能体（Agent）、任务（Task）和团队（Crew）。智能体的定义不仅取决于其功能，还取决于其角色，包括具体角色、目标和背景故事，这些因素共同指导其行为和沟通方式。任务是一个独立的工作单元，具有清晰的描述和预期输出，并分配给特定的智能体。团队是一个包含所有智能体和任务列表的凝聚单元，它执行预定义的流程。该流程决定了工作流程，通常分为顺序式和层级式两种。顺序式工作流程中，一个任务的输出成为下一个任务的输入；层级式工作流程中，一个类似经理的智能体负责分配任务并协调其他智能体之间的工作流程。</mark>

When compared to other frameworks, CrewAI occupies a distinct position. It moves away from the low-level, explicit state management and control flow of LangGraph, where a developer wires together every node and conditional edge. Instead of building a state machine, the developer designs a team charter. While Googlés ADK provides a comprehensive, production-oriented platform for the entire agent lifecycle, CrewAI concentrates specifically on the logic of agent collaboration and for simulating a team of specialists.

<mark>与其他框架相比，CrewAI 占据着独特的地位。它摒弃了 LangGraph 那种底层、显式的状态管理和控制流——在 LangGraph 中，开发者需要将每个节点和条件边连接起来。CrewAI 的开发者无需构建状态机，而是设计团队章程。虽然 Google ADK 为整个智能体生命周期提供了一个全面、面向生产的平台，但 CrewAI 则专注于智能体协作逻辑以及专家团队的模拟。</mark>

Python

This code sets up a sequential workflow for a team of AI agents, where they tackle a list of tasks in a specific order, with detailed logging enabled to monitor their progress.




<mark>该平台支持创建和部署专门的人工智能体，这些智能体可以执行复杂任务并实现流程自动化。这些智能体不仅仅是聊天机器人；它们可以自主推理、规划和执行多步骤操作。例如，智能体可以研究某个主题，编写包含引文的报告，甚至生成音频摘要。</mark>

To achieve this, AgentSpace constructs an enterprise knowledge graph, mapping the relationships between people, documents, and data. This allows the AI to understand context and deliver more relevant and personalized results. The platform also includes a no-code interface called Agent Designer for creating custom agents without requiring deep technical expertise.

<mark>为了实现这一点，AgentSpace 构建了一个企业知识图谱，映射了人员、文档和数据之间的关系。这使得人工智能够理解上下文并提供更相关、更个性化的结果。该平台还包含一个名为 Agent Designer 的无代码界面，无需深厚的技术专业知识即可创建自定义智能体。</mark>

Furthermore, AgentSpace supports a multi-agent system where different AI agents can communicate and collaborate through an open protocol known as the Agent2Agent (A2A) Protocol. This interoperability allows for more complex and orchestrated workflows. Security is a foundational component, with features like role-based access controls and data encryption to protect sensitive enterprise information. Ultimately, AgentSpace aims to enhance productivity and decision-making by embedding intelligent, autonomous systems directly into an organization's operational fabric.

<mark>此外，AgentSpace 支持多智能体系统，不同的 AI 智能体可以通过Agent2Agent (A2A) 协议的开放协议进行通信和协作。这种互操作性支持更复杂、更协调的工作流程。安全性是其基础组件，它还提供基于角色的访问控制和数据加密等功能来保护敏感的企业信息。AgentSpace 的最终目标是通过将智能自主系统直接嵌入到组织的运营结构中来提高生产力和决策能力。</mark>

How to build an Agent with AgentSpace UI

<mark>如何使用 AgentSpace UI 构建智能体</mark>

Figure 1 illustrates how to access AgentSpace by selecting AI Applications from the Google Cloud Console.

<mark>图 1 展示了如何通过从 Google Cloud Console 选择“AI Appcalition”来访问 AgentSpace。</mark>

![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140597818-455d7428-484f-4bf5-858f-7495fd418bbd.png)

Fig. 1:  How to use Google Cloud Console to access AgentSpace

<mark>图 1：如何使用 Google Cloud Console 访问 AgentSpace</mark>

Your agent can be connected to various services, including Calendar, Google Mail, Workaday, Jira, Outlook, and Service Now (see Fig. 2).

<mark>您的智能体可以连接到各种服务，包括日历、Google Mail、Workaday、Jira、Outlook 和 Service Now（见图 2）。</mark>

![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140597872-5c91627d-6ad6-4f13-a72e-82888c0b0eee.png)

Fig. 2: Integrate with diverse services, including Google and third-party platforms.

<mark>图 2：与包括 Google 和第三方平台在内的各种服务集成。</mark>

The Agent can then utilize its own prompt, chosen from a gallery of pre-made prompts provided by Google, as illustrated in Fig. 3.

<mark>然后，智能体可以使用自己的提示，这些提示可以从 Google 提供的预制提示库中选择，如图 3 所示。</mark>

![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598084-0db2871e-1251-44d1-8bcd-ab4c9b13d6f1.png)

Fig.3: Google's Gallery of Pre-assembled  prompts

<mark>图 3：Google 预置提示库</mark>

In alternative you can create your own prompt as in Fig.4, which will be then used by your agent

<mark>或者，您可以像图 4 所示那样创建自己的提示，供您的智能体使用</mark>

![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598048-09bf9f3c-c8bd-4ff9-9514-fc76840344c5.png)

Fig.4: Customizing the Agent's Prompt

<mark>图 4：自定义智能体提示</mark>

AgentSpace offers a number of advanced features such as integration with datastores to store your own data, integration with Google Knowledge Graph or with your private Knowledge Graph, Web interface for exposing your agent to the Web, and Analytics to monitor usage, and more (see Fig. 5) 

<mark>AgentSpace 提供许多高级功能，例如与数据存储集成以存储您自己的数据、与 Google 知识图谱或您的私有知识图谱集成、用于将您的智能体公开到Web界面以及用于监控使用情况的 Analytics 等等（参见图 5）。</mark>

![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598223-8f7249bf-931c-42c2-8f33-a916c0a4bdcb.png)

Fig. 5: AgentSpace advanced capabilities 

<mark>图 5：AgentSpace 高级功能</mark>

Upon completion, the AgentSpace chat interface (Fig. 6) will be accessible.

<mark>完成后，即可访问 AgentSpace 聊天界面（图 6）。</mark>

![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598253-264347cb-f46d-468c-abcc-a87eb21ef909.png)

Fig. 6: The AgentSpace User Interface for initiating a chat with your Agent.

<mark>图 6：用于与您的智能体发起聊天的 AgentSpace 用户界面。</mark>

## Conclusion | <mark>结语</mark>

In conclusion, AgentSpace provides a functional framework for developing and deploying AI agents within an organization's existing digital infrastructure. The system's architecture links complex backend processes, such as autonomous reasoning and enterprise knowledge graph mapping, to a graphical user interface for agent construction. Through this interface, users can configure agents by integrating various data services and defining their operational parameters via prompts, resulting in customized, context-aware automated systems.

<mark>总而言之，AgentSpace 提供用于在组织现有的数字基础架构内开发和部署AI智能体的功能框架。该系统的架构将复杂的后端流程（例如自主推理和企业知识图谱映射）链接到用于构建智能体的图形用户界面。通过该界面，用户可以通过集成各种数据服务并通过提示定义其操作参数来配置智能体，从而构建定制的、情境感知的自动化系统。</mark>

This approach abstracts the underlying technical complexity, enabling the construction of specialized multi-agent systems without requiring deep programming expertise. The primary objective is to embed automated analytical and operational capabilities directly into workflows, thereby increasing process efficiency and enhancing data-driven analysis. For practical instruction, hands-on learning modules are available, such as the "Build a Gen AI Agent with Agentspace" lab on Google Cloud Skills Boost, which provides a structured environment for skill acquisition.

<mark>这种方法抽象了底层的技术复杂性，无需深厚的编程专业知识即可构建专用的多智能体系统。其主要目标是将自动化分析和操作功能直接嵌入到工作流中，从而提高流程效率并增强数据驱动的分析能力。在实践教学方面，我们提供动手学习模块，例如 Google Cloud Skills Boost 上的“Build a Gen AI Agent with Agentspace”实验，它为技能学习提供结构化的环境。</mark>

## References | <mark>参考文献</mark>

1. Create a no-code agent with Agent Designer, [https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer](https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer)

     <mark>使用 Agent Designer 创建无代码智能体，[https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer](https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer)

2. Google Cloud Skills Boost,[https://www.cloudskillsboost.google/](https://www.cloudskillsboost.google/)

      <mark>Google Cloud Skills Boost,[https://www.cloudskillsboost.google/](https://www.cloudskillsboost.google/)</mark>

