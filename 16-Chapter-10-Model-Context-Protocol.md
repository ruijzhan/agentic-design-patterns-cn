# Chapter 10: Model Context Protocol | <mark>第 10 章：模型上下文协议</mark>

To enable LLMs to function effectively as agents, their capabilities must extend beyond multimodal generation. Interaction with the external environment is necessary, including access to current data, utilization of external software, and execution of specific operational tasks. The Model Context Protocol (MCP) addresses this need by providing a standardized interface for LLMs to interface with external resources. This protocol serves as a key mechanism to facilitate consistent and predictable integration.

<mark>要使大语言模型（LLM）作为智能体有效运作，其能力必须超越多模态生成。与外部环境的交互是必需的，包括访问当前数据、利用外部软件以及执行特定操作任务。模型上下文协议（Model Context Protocol，MCP）通过为 LLM 提供与外部资源交互的标准化接口来满足这一需求。该协议是促进一致且可预测集成的关键机制。</mark>

------

## MCP Pattern Overview | <mark>MCP 模式概览</mark>

Imagine a universal adapter that allows any LLM to plug into any external system, database, or tool without a custom integration for each one. That's essentially what the Model Context Protocol (MCP) is. It's an open standard designed to standardize how LLMs like Gemini, OpenAI's GPT models, Mixtral, and Claude communicate with external applications, data sources, and tools. Think of it as a universal connection mechanism that simplifies how LLMs obtain context, execute actions, and interact with various systems.

<mark>想象一个通用适配器，它允许任何 LLM 接入任何外部系统、数据库或工具，而无需为每个系统定制集成。这就是模型上下文协议（MCP）的本质。它是一个开放标准，旨在规范化 Gemini、OpenAI GPT 模型、Mixtral 和 Claude 等 LLM 如何与外部应用程序、数据源和工具进行通信。可以将其视为一种通用连接机制，简化了 LLM 获取上下文、执行操作以及与各种系统交互的方式。</mark>

MCP operates on a client-server architecture. It defines how different elements—data (referred to as resources), interactive templates (which are essentially prompts), and actionable functions (known as tools)—are exposed by an MCP server. These are then consumed by an MCP client, which could be an LLM host application or an AI agent itself. This standardized approach dramatically reduces the complexity of integrating LLMs into diverse operational environments.

<mark>MCP 采用客户端-服务器架构。它定义了 MCP 服务器如何暴露不同元素——数据（称为资源）、交互模板（本质上是提示词）和可执行函数（称为工具）。这些元素随后由 MCP 客户端使用，客户端可以是 LLM 宿主应用程序或 AI 智能体本身。这种标准化方法显著降低了将 LLM 集成到多样化操作环境中的复杂性。</mark>

However, MCP is a contract for an "agentic interface," and its effectiveness depends heavily on the design of the underlying APIs it exposes. There is a risk that developers simply wrap pre-existing, legacy APIs without modification, which can be suboptimal for an agent. For example, if a ticketing system's API only allows retrieving full ticket details one by one, an agent asked to summarize high-priority tickets will be slow and inaccurate at high volumes. To be truly effective, the underlying API should be improved with deterministic features like filtering and sorting to help the non-deterministic agent work efficiently. This highlights that agents do not magically replace deterministic workflows; they often require stronger deterministic support to succeed.

<mark>然而，MCP 是「具智能体特性接口」的契约，其有效性在很大程度上取决于它所暴露的底层 API 的设计。存在一个风险，即开发者可能只是简单地封装现有的遗留 API 而不加修改，这对智能体来说可能不是最优的。例如，如果票务系统的 API 只允许逐个检索完整的票务详情，那么被要求总结高优先级票务的智能体在大量数据下将会缓慢且不准确。要真正有效，底层 API 应该通过添加过滤和排序等确定性功能来改进，以帮助非确定性智能体高效工作。这突显出智能体并不能神奇地替代确定性工作流；它们通常需要更强的确定性支持才能成功。</mark>

Furthermore, MCP can wrap an API whose input or output is still not inherently understandable by the agent. An API is only useful if its data format is agent-friendly, a guarantee that MCP itself does not enforce. For instance, creating an MCP server for a document store that returns files as PDFs is mostly useless if the consuming agent cannot parse PDF content. The better approach would be to first create an API that returns a textual version of the document, such as Markdown, which the agent can actually read and process. This demonstrates that developers must consider not just the connection, but the nature of the data being exchanged to ensure true compatibility.

<mark>此外，MCP 可能封装一个输入或输出仍然不被智能体固有理解的 API。只有当 API 的数据格式对智能体友好时，该 API 才有用，而这一点 MCP 本身并不强制保证。例如，如果使用方智能体无法解析 PDF 内容，那么为文档存储创建一个返回 PDF 文件的 MCP 服务器基本上是无用的。更好的方法是首先创建一个返回文档文本版本的 API，比如 Markdown，这样智能体才能真正读取和处理。这表明开发者必须考虑的不仅仅是连接，还要考虑正在交换的数据的性质，以确保真正的兼容性。</mark>

------

## MCP vs. Tool Function Calling | <mark>MCP 与工具函数调用</mark>

The Model Context Protocol (MCP) and tool function calling are distinct mechanisms that enable LLMs to interact with external capabilities (including tools) and execute actions. While both serve to extend LLM capabilities beyond text generation, they differ in their approach and level of abstraction.

<mark>模型上下文协议（MCP）和工具函数调用是不同的机制，它们使 LLM 能够与外部能力（包括工具）交互并执行操作。虽然两者都用于扩展 LLM 超越文本生成的能力，但它们在方法和抽象级别上有所不同。</mark>

Tool function calling can be thought of as a direct request from an LLM to a specific, pre-defined tool or function. Note that in this context we use the words "tool" and "function" interchangeably. This interaction is characterized by a one-to-one communication model, where the LLM formats a request based on its understanding of a user's intent requiring external action. The application code then executes this request and returns the result to the LLM. This process is often proprietary and varies across different LLM providers.

<mark>工具函数调用可以被认为是 LLM 对特定预定义工具或函数的直接请求。注意，在此语境中我们交替使用「工具」和「函数」这两个词。这种交互的特点是一对一通信模型，其中 LLM 根据其对需要外部操作的用户意图的理解来格式化请求。然后应用代码执行此请求并将结果返回给 LLM。这个过程通常是专有的，并且在不同的 LLM 提供商之间有所不同。</mark>

In contrast, the Model Context Protocol (MCP) operates as a standardized interface for LLMs to discover, communicate with, and utilize external capabilities. It functions as an open protocol that facilitates interaction with a wide range of tools and systems, aiming to establish an ecosystem where any compliant tool can be accessed by any compliant LLM. This fosters interoperability, composability and reusability across different systems and implementations. By adopting a federated model, we significantly improve interoperability and unlock the value of existing assets. This strategy allows us to bring disparate and legacy services into a modern ecosystem simply by wrapping them in an MCP-compliant interface. These services continue to operate independently, but can now be composed into new applications and workflows, with their collaboration orchestrated by LLMs. This fosters agility and reusability without requiring costly rewrites of foundational systems.

<mark>相比之下,模型上下文协议（MCP）作为标准化接口运作，使 LLM 能够发现、通信和利用外部能力。它作为一个开放协议，促进与广泛的工具和系统的交互，旨在建立一个生态系统，让任何兼容工具都可以被任何兼容 LLM 访问。这促进了不同系统和实现之间的互操作性、可组合性和可重用性。通过采用联邦模型，我们显著提高了互操作性并释放了现有资产的价值。这一策略允许我们仅通过将异构和遗留服务封装在符合 MCP 的接口中，就能将它们带入现代生态系统。这些服务继续独立运行，但现在可以被组合成新的应用程序和工作流，它们的协作由 LLM 编排。这在不需要对基础系统进行昂贵重写的情况下促进了敏捷性和可重用性。</mark>

Here's a breakdown of the fundamental distinctions between MCP and tool function calling:

<mark>以下是 MCP 与工具函数调用之间基本区别的分解：</mark>

| Feature         | Tool Function Calling                                        | Model Context Protocol (MCP)                                 |
| :-------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Standardization | Proprietary and vendor-specific. The format and implementation differ across LLM providers. | An open, standardized protocol, promoting interoperability between different LLMs and tools. |
| Scope           | A direct mechanism for an LLM to request the execution of a specific, predefined function. | A broader framework for how LLMs and external tools discover and communicate with each other. |
| Architecture    | A one-to-one interaction between the LLM and the application's tool-handling logic. | A client-server architecture where LLM-powered applications (clients) can connect to and utilize various MCP servers (tools). |
| Discovery       | The LLM is explicitly told which tools are available within the context of a specific conversation. | Enables dynamic discovery of available tools. An MCP client can query a server to see what capabilities it offers. |
| Reusability     | Tool integrations are often tightly coupled with the specific application and LLM being used. | Promotes the development of reusable, standalone "MCP servers" that can be accessed by any compliant application. |

| <mark>特性</mark>     | <mark>工具函数调用</mark>                                    | <mark>模型上下文协议（MCP）</mark>                           |
| :-------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| <mark>标准化</mark>   | <mark>专有且特定于供应商。格式和实现在不同 LLM 提供商之间有所不同。</mark> | <mark>开放的标准化协议，促进不同 LLM 和工具之间的互操作性。</mark> |
| <mark>范围</mark>     | <mark>LLM 请求执行特定预定义函数的直接机制。</mark>          | <mark>LLM 和外部工具如何发现和相互通信的更广泛框架。</mark>  |
| <mark>架构</mark>     | <mark>LLM 与应用程序工具处理逻辑之间的一对一交互。</mark>    | <mark>客户端-服务器架构，其中 LLM 驱动的应用程序（客户端）可以连接并利用各种 MCP 服务器（工具）。</mark> |
| <mark>发现机制</mark> | <mark>在特定对话上下文中明确告知 LLM 哪些工具可用。</mark>   | <mark>支持可用工具的动态发现。MCP 客户端可以查询服务器以查看它提供哪些能力。</mark> |
| <mark>可重用性</mark> | <mark>工具集成通常与正在使用的特定应用程序和 LLM 紧密耦合。</mark> | <mark>促进可重用、独立的「MCP 服务器」的开发，可被任何兼容应用程序访问。</mark> |

Think of tool function calling as giving an AI a specific set of custom-built tools, like a particular wrench and screwdriver. This is efficient for a workshop with a fixed set of tasks. MCP (Model Context Protocol), on the other hand, is like creating a universal, standardized power outlet system. It doesn't provide the tools itself, but it allows any compliant tool from any manufacturer to plug in and work, enabling a dynamic and ever-expanding workshop.

<mark>可以将工具函数调用想象为给 AI 一套特定的定制工具，比如特定的扳手和螺丝刀。这对于具有固定任务集的工作坊来说很高效。而模型上下文协议（MCP）则像是创建一个通用的、标准化的电源插座系统。它本身不提供工具，但它允许来自任何制造商的任何兼容工具插入并工作，从而实现一个动态且不断扩展的工作坊。</mark>

In short, function calling provides direct access to a few specific functions, while MCP is the standardized communication framework that lets LLMs discover and use a vast range of external resources. For simple applications, specific tools are enough; for complex, interconnected AI systems that need to adapt, a universal standard like MCP is essential.

<mark>简而言之，函数调用提供对少数特定函数的直接访问，而 MCP 是标准化的通信框架，让 LLM 能够发现和使用广泛的外部资源。对于简单应用程序，特定工具就足够了；对于需要适应的复杂互联 AI 系统，像 MCP 这样的通用标准是必不可少的。</mark>

------

## Additional considerations for MCP | <mark>MCP 的其他考虑因素</mark>

While MCP presents a powerful framework, a thorough evaluation requires considering several crucial aspects that influence its suitability for a given use case. Let's see some aspects in more details:

<mark>虽然 MCP 提供了一个强大的框架，但全面评估需要考虑影响其在特定用例中适用性的几个关键方面。让我们更详细地看一些方面：</mark>

- **Tool vs. Resource vs. Prompt:** It's important to understand the specific roles of these components. A resource is static data (e.g., a PDF file, a database record). A tool is an executable function that performs an action (e.g., sending an email, querying an API). A prompt is a template that guides the LLM in how to interact with a resource or tool, ensuring the interaction is structured and effective.
- <mark><strong>工具 vs. 资源 vs. 提示词：</strong>理解这些组件的特定角色很重要。资源是静态数据（例如 PDF 文件、数据库记录）。工具是执行操作的可执行函数（例如发送电子邮件、查询 API）。提示词是指导 LLM 如何与资源或工具交互的模板，确保交互是结构化和有效的。</mark>
- **Discoverability:** A key advantage of MCP is that an MCP client can dynamically query a server to learn what tools and resources it offers. This "just-in-time" discovery mechanism is powerful for agents that need to adapt to new capabilities without being redeployed.
- <mark><strong>可发现性：</strong>MCP 的一个关键优势是 MCP 客户端可以动态查询服务器以了解它提供哪些工具和资源。这种「即时」发现机制对于需要适应新能力而无需重新部署的智能体来说非常强大。</mark>
- **Security:** Exposing tools and data via any protocol requires robust security measures. An MCP implementation must include authentication and authorization to control which clients can access which servers and what specific actions they are permitted to perform.
- <mark><strong>安全性：</strong>通过任何协议暴露工具和数据都需要强大的安全措施。MCP 实现必须包括身份验证和授权，以控制哪些客户端可以访问哪些服务器以及它们被允许执行哪些特定操作。</mark>
- **Implementation:** While MCP is an open standard, its implementation can be complex. However, providers are beginning to simplify this process. For example, some model providers like Anthropic or FastMCP offer SDKs that abstract away much of the boilerplate code, making it easier for developers to create and connect MCP clients and servers.
- <mark><strong>实现：</strong>虽然 MCP 是开放标准，但其实现可能很复杂。然而，提供商正在开始简化这一过程。例如，像 Anthropic 或 FastMCP 这样的一些模型提供商提供 SDK，抽象出大量样板代码，使开发者更容易创建和连接 MCP 客户端和服务器。</mark>
- **Error Handling:** A comprehensive error-handling strategy is critical. The protocol must define how errors (e.g., tool execution failure, unavailable server, invalid request) are communicated back to the LLM so it can understand the failure and potentially try an alternative approach.
- <mark><strong>错误处理：</strong>全面的错误处理策略至关重要。协议必须定义如何将错误（例如工具执行失败、服务器不可用、无效请求）传达回 LLM，以便它能够理解失败并可能尝试替代方法。</mark>
- **Local vs. Remote Server:** MCP servers can be deployed locally on the same machine as the agent or remotely on a different server. A local server might be chosen for speed and security with sensitive data, while a remote server architecture allows for shared, scalable access to common tools across an organization.
- <mark><strong>本地 vs. 远程服务器：</strong>MCP 服务器可以部署在与智能体相同的机器上（本地），也可以部署在不同的服务器上（远程）。本地服务器可能因速度和敏感数据的安全性而被选择，而远程服务器架构则允许组织内对公共工具的共享、可扩展访问。</mark>
- **On-demand vs. Batch:** MCP can support both on-demand, interactive sessions and larger-scale batch processing. The choice depends on the application, from a real-time conversational agent needing immediate tool access to a data analysis pipeline that processes records in batches.
- <mark><strong>按需 vs. 批处理：</strong>MCP 可以支持按需交互式会话和大规模批处理。选择取决于应用程序，从需要即时工具访问的实时对话智能体到批量处理记录的数据分析管道。</mark>
- **Transportation Mechanism:** The protocol also defines the underlying transport layers for communication. For local interactions, it uses JSON-RPC over STDIO (standard input/output) for efficient inter-process communication. For remote connections, it leverages web-friendly protocols like Streamable HTTP and Server-Sent Events (SSE) to enable persistent and efficient client-server communication.
- <mark><strong>传输机制：</strong>该协议还定义了用于通信的底层传输层。对于本地交互，它使用基于 STDIO（标准输入/输出）的 JSON-RPC 来实现高效的进程间通信。对于远程连接，它利用 Streamable HTTP 和服务器发送事件（SSE）等 Web 友好协议来实现持久且高效的客户端-服务器通信。</mark>

The Model Context Protocol uses a client-server model to standardize information flow. Understanding component interaction is key to MCP's advanced agentic behavior:

<mark>模型上下文协议使用客户端-服务器模型来标准化信息流。理解组件交互是理解 MCP 高级智能体行为的关键：</mark>

1. **Large Language Model (LLM):** The core intelligence. It processes user requests, formulates plans, and decides when it needs to access external information or perform an action.
2. <mark><strong>大语言模型（LLM）：</strong>核心智能。它处理用户请求、制定计划，并决定何时需要访问外部信息或执行操作。</mark>
3. **MCP Client:** This is an application or wrapper around the LLM. It acts as the intermediary, translating the LLM's intent into a formal request that conforms to the MCP standard. It is responsible for discovering, connecting to, and communicating with MCP Servers.
4. <mark><strong>MCP 客户端：</strong>这是 LLM 周围的应用程序或包装器。它充当中介，将 LLM 的意图转换为符合 MCP 标准的正式请求。它负责发现、连接和与 MCP 服务器通信。</mark>
5. **MCP Server:** This is the gateway to the external world. It exposes a set of tools, resources, and prompts to any authorized MCP Client. Each server is typically responsible for a specific domain, such as a connection to a company's internal database, an email service, or a public API.
6. <mark><strong>MCP 服务器：</strong>这是通往外部世界的网关。它向任何授权的 MCP 客户端暴露一组工具、资源和提示词。每个服务器通常负责特定领域，例如连接到公司内部数据库、电子邮件服务或公共 API。</mark>
7. **Optional Third-Party (3P) Service:** This represents the actual external tool, application, or data source that the MCP Server manages and exposes. It is the ultimate endpoint that performs the requested action, such as querying a proprietary database, interacting with a SaaS platform, or calling a public weather API.
8. <mark><strong>可选第三方（3P）服务：</strong>这代表 MCP 服务器管理和暴露的实际外部工具、应用程序或数据源。它是执行请求操作的最终端点，例如查询专有数据库、与 SaaS 平台交互或调用公共天气 API。</mark>

The interaction flows as follows:

<mark>交互流程如下：</mark>

1. **Discovery:** The MCP Client, on behalf of the LLM, queries an MCP Server to ask what capabilities it offers. The server responds with a manifest listing its available tools (e.g., send_email), resources (e.g., customer_database), and prompts.
2. <mark><strong>发现：</strong>MCP 客户端代表 LLM 查询 MCP 服务器以询问它提供哪些能力。服务器响应一个清单，列出其可用的工具（例如 <code>send_email</code>）、资源（例如 <code>customer_database</code>）和提示词。</mark>
3. **Request Formulation:** The LLM determines that it needs to use one of the discovered tools. For instance, it decides to send an email. It formulates a request, specifying the tool to use (send_email) and the necessary parameters (recipient, subject, body).
4. <mark><strong>请求制定：</strong>LLM 确定它需要使用其中一个已发现的工具。例如，它决定发送电子邮件。它制定一个请求，指定要使用的工具（<code>send_email</code>）和必要的参数（收件人、主题、正文）。</mark>
5. **Client Communication:** The MCP Client takes the LLM's formulated request and sends it as a standardized call to the appropriate MCP Server.
6. <mark><strong>客户端通信：</strong>MCP 客户端获取 LLM 制定的请求，并将其作为标准化调用发送到相应的 MCP 服务器。</mark>
7. **Server Execution:** The MCP Server receives the request. It authenticates the client, validates the request, and then executes the specified action by interfacing with the underlying software (e.g., calling the send() function of an email API).
8. <mark><strong>服务器执行：</strong>MCP 服务器接收请求。它对客户端进行身份验证、验证请求，然后通过与底层软件交互（例如调用电子邮件 API 的 <code>send()</code> 函数）来执行指定的操作。</mark>
9. **Response and Context Update:** After execution, the MCP Server sends a standardized response back to the MCP Client. This response indicates whether the action was successful and includes any relevant output (e.g., a confirmation ID for the sent email). The client then passes this result back to the LLM, updating its context and enabling it to proceed with the next step of its task.
10. <mark><strong>响应和上下文更新：</strong>执行后，MCP 服务器将标准化响应发送回 MCP 客户端。该响应指示操作是否成功，并包含任何相关输出（例如已发送电子邮件的确认 ID）。然后客户端将此结果传递回 LLM，更新其上下文并使其能够继续执行任务的下一步。</mark>

------

## Practical Applications & Use Cases | <mark>实际应用与用例</mark>

MCP significantly broadens AI/LLM capabilities, making them more versatile and powerful. Here are nine key use cases:

<mark>MCP 显著扩展了 AI/LLM 的能力，使它们更加通用和强大。以下是九个关键用例：</mark>

- **Database Integration:** MCP allows LLMs and agents to seamlessly access and interact with structured data in databases. For instance, using the MCP Toolbox for Databases, an agent can query Google BigQuery datasets to retrieve real-time information, generate reports, or update records, all driven by natural language commands.
- <mark><strong>数据库集成：</strong>MCP 允许 LLM 和智能体无缝访问和与数据库中的结构化数据交互。例如，使用 MCP Toolbox for Databases，智能体可以查询 Google BigQuery 数据集以检索实时信息、生成报告或更新记录，所有这些都由自然语言命令驱动。</mark>
- **Generative Media Orchestration:** MCP enables agents to integrate with advanced generative media services. Through MCP Tools for Genmedia Services, an agent can orchestrate workflows involving Google's Imagen for image generation, Google's Veo for video creation, Google's Chirp 3 HD for realistic voices, or Google's Lyria for music composition, allowing for dynamic content creation within AI applications.
- <mark><strong>生成式媒体编排：</strong>MCP 使智能体能够与高级生成式媒体服务集成。通过 MCP Tools for Genmedia Services，智能体可以编排涉及 Google Imagen（图像生成）、Google Veo（视频创建）、Google Chirp 3 HD（逼真语音）或 Google Lyria（音乐作曲）的工作流，从而在 AI 应用程序中实现动态内容创建。</mark>
- **External API Interaction:** MCP provides a standardized way for LLMs to call and receive responses from any external API. This means an agent can fetch live weather data, pull stock prices, send emails, or interact with CRM systems, extending its capabilities far beyond its core language model.
- <mark><strong>外部 API 交互：</strong>MCP 为 LLM 提供了调用和接收来自任何外部 API 响应的标准化方式。这意味着智能体可以获取实时天气数据、拉取股票价格、发送电子邮件或与 CRM 系统交互，将其能力扩展到远超其核心语言模型。</mark>
- **Reasoning-Based Information Extraction:** Leveraging an LLM's strong reasoning skills, MCP facilitates effective, query-dependent information extraction that surpasses conventional search and retrieval systems. Instead of a traditional search tool returning an entire document, an agent can analyze the text and extract the precise clause, figure, or statement that directly answers a user's complex question.
- <mark><strong>基于推理的信息提取：</strong>利用 LLM 强大的推理能力，MCP 促进了有效的、依赖查询的信息提取，超越了传统的搜索和检索系统。传统搜索工具会返回整个文档，而智能体可以分析文本并提取直接回答用户复杂问题的精确条款、数字或陈述。</mark>
- **Custom Tool Development:** Developers can build custom tools and expose them via an MCP server (e.g., using FastMCP). This allows specialized internal functions or proprietary systems to be made available to LLMs and other agents in a standardized, easily consumable format, without needing to modify the LLM directly.
- <mark><strong>自定义工具开发：</strong>开发者可以构建自定义工具并通过 MCP 服务器暴露它们（例如使用 FastMCP）。这允许将专门的内部函数或专有系统以标准化、易于使用的格式提供给 LLM 和其他智能体，而无需直接修改 LLM。</mark>
- **Standardized LLM-to-Application Communication:** MCP ensures a consistent communication layer between LLMs and the applications they interact with. This reduces integration overhead, promotes interoperability between different LLM providers and host applications, and simplifies the development of complex agentic systems.
- <mark><strong>标准化 LLM 到应用程序的通信：</strong>MCP 确保 LLM 与其交互的应用程序之间有一致的通信层。这减少了集成开销，促进了不同 LLM 提供商和宿主应用程序之间的互操作性，并简化了复杂智能体系统的开发。</mark>
- **Complex Workflow Orchestration:** By combining various MCP-exposed tools and data sources, agents can orchestrate highly complex, multi-step workflows. An agent could, for example, retrieve customer data from a database, generate a personalized marketing image, draft a tailored email, and then send it, all by interacting with different MCP services.
- <mark><strong>复杂工作流编排：</strong>通过组合各种 MCP 暴露的工具和数据源，智能体可以编排高度复杂的多步骤工作流。例如，智能体可以从数据库中检索客户数据、生成个性化营销图像、起草定制电子邮件，然后发送它，所有这些都通过与不同的 MCP 服务交互来完成。</mark>
- **IoT Device Control:** MCP can facilitate LLM interaction with Internet of Things (IoT) devices. An agent could use MCP to send commands to smart home appliances, industrial sensors, or robotics, enabling natural language control and automation of physical systems.
- <mark><strong>物联网设备控制：</strong>MCP 可以促进 LLM 与物联网（IoT）设备的交互。智能体可以使用 MCP 向智能家居设备、工业传感器或机器人发送命令，实现物理系统的自然语言控制和自动化。</mark>
- **Financial Services Automation:** In financial services, MCP could enable LLMs to interact with various financial data sources, trading platforms, or compliance systems. An agent might analyze market data, execute trades, generate personalized financial advice, or automate regulatory reporting, all while maintaining secure and standardized communication.
- <mark><strong>金融服务自动化：</strong>在金融服务中，MCP 可以使 LLM 与各种金融数据源、交易平台或合规系统交互。智能体可能分析市场数据、执行交易、生成个性化财务建议或自动化监管报告，同时保持安全和标准化的通信。</mark>

In short, the Model Context Protocol (MCP) enables agents to access real-time information from databases, APIs, and web resources. It also allows agents to perform actions like sending emails, updating records, controlling devices, and executing complex tasks by integrating and processing data from various sources. Additionally, MCP supports media generation tools for AI applications.

<mark>简而言之，模型上下文协议（MCP）使智能体能够从数据库、API 和 Web 资源访问实时信息。它还允许智能体通过集成和处理来自各种来源的数据来执行发送电子邮件、更新记录、控制设备和执行复杂任务等操作。此外，MCP 支持 AI 应用程序的媒体生成工具。</mark>

------

## Hands-On Code Example with ADK | <mark>使用 ADK 的实战代码示例</mark>

This section outlines how to connect to a local MCP server that provides file system operations, enabling an ADK agent to interact with the local file system.

<mark>本节概述了如何连接到提供文件系统操作的本地 MCP 服务器，使 ADK 智能体能够与本地文件系统交互。</mark>

### Agent Setup with MCPToolset | <mark>使用 MCPToolset 设置智能体</mark>

To configure an agent for file system interaction, an `agent.py` file must be created (e.g., at `./adk_agent_samples/mcp_agent/agent.py`). The `MCPToolset` is instantiated within the `tools` list of the `LlmAgent` object. It is crucial to replace `"/path/to/your/folder"` in the `args` list with the absolute path to a directory on the local system that the MCP server can access. This directory will be the root for the file system operations performed by the agent.

<mark>要配置智能体进行文件系统交互，必须创建一个 <code>agent.py</code> 文件（例如在 <code>./adk_agent_samples/mcp_agent/agent.py</code>）。<code>MCPToolset</code> 在 <code>LlmAgent</code> 对象的 <code>tools</code> 列表中实例化。至关重要的是，将 <code>args</code> 列表中的 <code>"/path/to/your/folder"</code> 替换为 MCP 服务器可以访问的本地系统上目录的绝对路径。该目录将成为智能体执行的文件系统操作的根目录。</mark>

```
pythonimport os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# Create a reliable absolute path to a folder named 'mcp_managed_files'
# within the same directory as this agent script.
# This ensures the agent works out-of-the-box for demonstration.
# For production, you would point this to a more persistent and secure location.
TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_managed_files")

# Ensure the target directory exists before the agent needs it.
os.makedirs(TARGET_FOLDER_PATH, exist_ok=True)

root_agent = LlmAgent(
   model='gemini-2.0-flash',
   name='filesystem_assistant_agent',
   instruction=(
       'Help the user manage their files. You can list files, read files, and write files. '
       f'You are operating in the following directory: {TARGET_FOLDER_PATH}'
   ),
   tools=[
       MCPToolset(
           connection_params=StdioServerParameters(
               command='npx',
               args=[
                   "-y",  # Argument for npx to auto-confirm install
                   "@modelcontextprotocol/server-filesystem",
                   # This MUST be an absolute path to a folder.
                   TARGET_FOLDER_PATH,
               ],
           ),
           # Optional: You can filter which tools from the MCP server are exposed.
           # For example, to only allow reading:
           # tool_filter=['list_directory', 'read_file']
       )
   ],
)
```

`npx` (Node Package Execute), bundled with npm (Node Package Manager) versions 5.2.0 and later, is a utility that enables direct execution of Node.js packages from the npm registry. This eliminates the need for global installation. In essence, `npx` serves as an npm package runner, and it is commonly used to run many community MCP servers, which are distributed as Node.js packages.

<mark><code>npx</code>（Node Package Execute）与 npm（Node Package Manager）5.2.0 及更高版本捆绑在一起，是一个实用程序，可以直接从 npm 注册表执行 Node.js 包。这消除了全局安装的需要。本质上，<code>npx</code> 充当 npm 包运行器，它通常用于运行许多社区 MCP 服务器，这些服务器作为 Node.js 包分发。</mark>

Creating an **init**.py file is necessary to ensure the agent.py file is recognized as part of a discoverable Python package for the Agent Development Kit (ADK). This file should reside in the same directory as agent.py.

<mark>创建 <code>**init**.py</code> 文件是必要的，以确保 <code>agent.py</code> 文件被识别为智能体开发套件（ADK）可发现的 Python 包的一部分。该文件应与 <code>agent.py</code> 位于同一目录中。</mark>

```
python# ./adk_agent_samples/mcp_agent/__init__.py
from . import agent
```

Certainly, other supported commands are available for use. For example, connecting to python3 can be achieved as follows:

<mark>当然，还有其他支持的命令可供使用。例如，可以按如下方式连接到 <code>python3</code>：</mark>

```
pythonconnection_params = StdioConnectionParams(
 server_params={
     "command": "python3",
     "args": ["./agent/mcp_server.py"],
     "env": {
       "SERVICE_ACCOUNT_PATH":SERVICE_ACCOUNT_PATH,
       "DRIVE_FOLDER_ID": DRIVE_FOLDER_ID
     }
 }
)
```

UVX, in the context of Python, refers to a command-line tool that utilizes uv to execute commands in a temporary, isolated Python environment. Essentially, it allows you to run Python tools and packages without needing to install them globally or within your project's environment. You can run it via the MCP server.

<mark>在 Python 上下文中，UVX 指的是一个命令行工具，它利用 uv 在临时隔离的 Python 环境中执行命令。本质上，它允许你运行 Python 工具和包，而无需全局安装它们或在项目环境中安装。你可以通过 MCP 服务器运行它。</mark>

```
pythonconnection_params = StdioConnectionParams(
 server_params={
   "command": "uvx",
   "args": ["mcp-google-sheets@latest"],
   "env": {
     "SERVICE_ACCOUNT_PATH":SERVICE_ACCOUNT_PATH,
     "DRIVE_FOLDER_ID": DRIVE_FOLDER_ID
   }
 }
)
```

Once the MCP Server is created, the next step is to connect to it.

<mark>一旦创建了 MCP 服务器，下一步就是连接到它。</mark>

### Connecting the MCP Server with ADK Web | <mark>使用 ADK Web 连接 MCP 服务器</mark>

To begin, execute 'adk web'. Navigate to the parent directory of mcp_agent (e.g., adk_agent_samples) in your terminal and run:

<mark>首先，执行「adk web」。在终端中导航到 <code>mcp_agent</code> 的父目录（例如 <code>adk_agent_samples</code>）并运行：</mark>

```
bashcd ./adk_agent_samples # Or your equivalent parent directory
adk web
```

Once the ADK Web UI has loaded in your browser, select the `filesystem_assistant_agent` from the agent menu. Next, experiment with prompts such as:

<mark>一旦 ADK Web UI 在浏览器中加载，从智能体菜单中选择 <code>filesystem_assistant_agent</code>。接下来，尝试如下提示：</mark>

- "Show me the contents of this folder."
- "Read the `sample.txt` file." (This assumes `sample.txt` is located at `TARGET_FOLDER_PATH`.)
- "What's in `another_file.md`?"
- <mark>「显示此文件夹的内容。」</mark>
- <mark>「读取 <code>sample.txt</code> 文件。」（假设 <code>sample.txt</code> 位于 <code>TARGET_FOLDER_PATH</code>。）</mark>
- <mark>「<code>another_file.md</code> 里有什么？」</mark>

------

## Creating an MCP Server with FastMCP | <mark>使用 FastMCP 创建 MCP 服务器</mark>

FastMCP is a high-level Python framework designed to streamline the development of MCP servers. It provides an abstraction layer that simplifies protocol complexities, allowing developers to focus on core logic.

<mark>FastMCP 是一个高级 Python 框架，旨在简化 MCP 服务器的开发。它提供了一个抽象层，简化了协议复杂性，使开发者能够专注于核心逻辑。</mark>

The library enables rapid definition of tools, resources, and prompts using simple Python decorators. A significant advantage is its automatic schema generation, which intelligently interprets Python function signatures, type hints, and documentation strings to construct necessary AI model interface specifications. This automation minimizes manual configuration and reduces human error.

<mark>该库支持使用简单的 Python 装饰器快速定义工具、资源和提示词。一个显著优势是其自动模式生成，它智能地解释 Python 函数签名、类型提示和文档字符串，以构建必要的 AI 模型接口规范。这种自动化最大限度地减少了手动配置并减少了人为错误。</mark>

Beyond basic tool creation, FastMCP facilitates advanced architectural patterns like server composition and proxying. This enables modular development of complex, multi-component systems and seamless integration of existing services into an AI-accessible framework. Additionally, FastMCP includes optimizations for efficient, distributed, and scalable AI-driven applications.

<mark>除了基本工具创建之外，FastMCP 还促进了服务器组合和代理等高级架构模式。这使得能够模块化开发复杂的多组件系统，并将现有服务无缝集成到 AI 可访问的框架中。此外，FastMCP 包含对高效、分布式和可扩展 AI 驱动应用程序的优化。</mark>

### Server setup with FastMCP | <mark>使用 FastMCP 设置服务器</mark>

To illustrate, consider a basic "greet" tool provided by the server. ADK agents and other MCP clients can interact with this tool using HTTP once it is active.

<mark>为了说明，考虑服务器提供的一个基本「问候」工具。一旦激活，ADK 智能体和其他 MCP 客户端可以使用 HTTP 与该工具交互。</mark>

```
python# fastmcp_server.py
# This script demonstrates how to create a simple MCP server using FastMCP.
# It exposes a single tool that generates a greeting.

# 1. Make sure you have FastMCP installed:
# pip install fastmcp
from fastmcp import FastMCP, Client

# Initialize the FastMCP server.
mcp_server = FastMCP()

# Define a simple tool function.
# The `@mcp_server.tool` decorator registers this Python function as an MCP tool.
# The docstring becomes the tool's description for the LLM.
@mcp_server.tool
def greet(name: str) -> str:
    """
    Generates a personalized greeting.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}! Nice to meet you."

# Or if you want to run it from the script:
if __name__ == "__main__":
    mcp_server.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )
```

This Python script defines a single function called greet, which takes a person's name and returns a personalized greeting. The @tool() decorator above this function automatically registers it as a tool that an AI or another program can use. The function's documentation string and type hints are used by FastMCP to tell the Agent how the tool works, what inputs it needs, and what it will return.

<mark>这个 Python 脚本定义了一个名为 <code>greet</code> 的单一函数，它接受一个人的姓名并返回个性化的问候。函数上方的 <code>@tool()</code> 装饰器自动将其注册为 AI 或其他程序可以使用的工具。FastMCP 使用函数的文档字符串和类型提示来告诉智能体工具如何工作、需要什么输入以及将返回什么。</mark>

When the script is executed, it starts the FastMCP server, which listens for requests on localhost:8000. This makes the greet function available as a network service. An agent could then be configured to connect to this server and use the greet tool to generate greetings as part of a larger task. The server runs continuously until it is manually stopped.

<mark>当执行脚本时，它启动 FastMCP 服务器，该服务器在 localhost:8000 上监听请求。这使得 <code>greet</code> 函数作为网络服务可用。然后可以配置智能体连接到此服务器并使用 <code>greet</code> 工具生成问候，作为更大任务的一部分。服务器持续运行，直到手动停止。</mark>

### Consuming the FastMCP Server with an ADK Agent | <mark>使用 ADK 智能体消费 FastMCP 服务器</mark>

An ADK agent can be set up as an MCP client to use a running FastMCP server. This requires configuring HttpServerParameters with the FastMCP server's network address, which is usually [http://localhost:8000](http://localhost:8000/).

<mark>可以将 ADK 智能体设置为 MCP 客户端以使用正在运行的 FastMCP 服务器。这需要使用 FastMCP 服务器的网络地址配置 <code>HttpServerParameters</code>，通常是 [http://localhost:8000。](http://localhost:8000。/)</mark>

A tool_filter parameter can be included to restrict the agent's tool usage to specific tools offered by the server, such as 'greet'. When prompted with a request like "Greet John Doe," the agent's embedded LLM identifies the 'greet' tool available via MCP, invokes it with the argument "John Doe," and returns the server's response. This process demonstrates the integration of user-defined tools exposed through MCP with an ADK agent.

<mark>可以包含 <code>tool_filter</code> 参数，以将智能体的工具使用限制为服务器提供的特定工具，例如「greet」。当收到类似「问候 John Doe」的请求时，智能体的嵌入式 LLM 识别通过 MCP 可用的「greet」工具，使用参数「John Doe」调用它，并返回服务器的响应。这个过程演示了通过 MCP 暴露的用户定义工具与 ADK 智能体的集成。</mark>

To establish this configuration, an agent file (e.g., agent.py located in ./adk_agent_samples/fastmcp_client_agent/) is required. This file will instantiate an ADK agent and use HttpServerParameters to establish a connection with the operational FastMCP server.

<mark>要建立此配置，需要一个智能体文件（例如位于 <code>./adk_agent_samples/fastmcp_client_agent/</code> 的 <code>agent.py</code>）。该文件将实例化一个 ADK 智能体，并使用 <code>HttpServerParameters</code> 与运行中的 FastMCP 服务器建立连接。</mark>

```
python# ./adk_agent_samples/fastmcp_client_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, HttpServerParameters

# Define the FastMCP server's address.
# Make sure your fastmcp_server.py (defined previously) is running on this port.
FASTMCP_SERVER_URL = "http://localhost:8000"

root_agent = LlmAgent(
   model='gemini-2.0-flash', # Or your preferred model
   name='fastmcp_greeter_agent',
   instruction='You are a friendly assistant that can greet people by their name. Use the "greet" tool.',
   tools=[
       MCPToolset(
           connection_params=HttpServerParameters(
               url=FASTMCP_SERVER_URL,
           ),
           # Optional: Filter which tools from the MCP server are exposed
           # For this example, we're expecting only 'greet'
           tool_filter=['greet']
       )
   ],
)
```

The script defines an Agent named fastmcp_greeter_agent that uses a Gemini language model. It's given a specific instruction to act as a friendly assistant whose purpose is to greet people. Crucially, the code equips this agent with a tool to perform its task. It configures an MCPToolset to connect to a separate server running on localhost:8000, which is expected to be the FastMCP server from the previous example. The agent is specifically granted access to the greet tool hosted on that server. In essence, this code sets up the client side of the system, creating an intelligent agent that understands its goal is to greet people and knows exactly which external tool to use to accomplish it.

<mark>该脚本定义了一个名为 <code>fastmcp_greeter_agent</code> 的智能体，它使用 Gemini 语言模型。它被赋予一个特定指令，即充当友好的助手，其目的是问候人们。至关重要的是，代码为该智能体配备了执行其任务的工具。它配置 <code>MCPToolset</code> 连接到运行在 localhost:8000 上的独立服务器，该服务器应该是前面示例中的 FastMCP 服务器。智能体被特别授予访问该服务器上托管的 <code>greet</code> 工具的权限。本质上，该代码设置了系统的客户端，创建了一个智能体，它理解其目标是问候人们，并确切知道使用哪个外部工具来完成它。</mark>

Creating an **init**.py file within the fastmcp_client_agent directory is necessary. This ensures the agent is recognized as a discoverable Python package for the ADK.

<mark>在 <code>fastmcp_client_agent</code> 目录中创建 <code>**init**.py</code> 文件是必要的。这确保智能体被识别为 ADK 的可发现 Python 包。</mark>

To begin, open a new terminal and run `python fastmcp_server.py` to start the FastMCP server. Next, go to the parent directory of `fastmcp_client_agent` (for example, `adk_agent_samples`) in your terminal and execute `adk web`. Once the ADK Web UI loads in your browser, select the `fastmcp_greeter_agent` from the agent menu. You can then test it by entering a prompt like "Greet John Doe." The agent will use the `greet` tool on your FastMCP server to create a response.

<mark>首先，打开一个新终端并运行 <code>python fastmcp_server.py</code> 来启动 FastMCP 服务器。接下来，在终端中转到 <code>fastmcp_client_agent</code> 的父目录（例如 <code>adk_agent_samples</code>）并执行 <code>adk web</code>。一旦 ADK Web UI 在浏览器中加载，从智能体菜单中选择 <code>fastmcp_greeter_agent</code>。然后你可以通过输入类似「问候 John Doe」的提示来测试它。智能体将使用你的 FastMCP 服务器上的 <code>greet</code> 工具来创建响应。</mark>

------

## At a Glance | <mark>要点速览</mark>

**What:** To function as effective agents, LLMs must move beyond simple text generation. They require the ability to interact with the external environment to access current data and utilize external software. Without a standardized communication method, each integration between an LLM and an external tool or data source becomes a custom, complex, and non-reusable effort. This ad-hoc approach hinders scalability and makes building complex, interconnected AI systems difficult and inefficient.

<mark><strong>问题所在：</strong>要作为有效的智能体运作，LLM 必须超越简单的文本生成。它们需要与外部环境交互以访问当前数据并利用外部软件的能力。如果没有标准化的通信方法，LLM 与外部工具或数据源之间的每次集成都会成为定制的、复杂的、不可重用的工作。这种临时方法阻碍了可扩展性，并使构建复杂、互联的 AI 系统变得困难和低效。</mark>

**Why:** The Model Context Protocol (MCP) offers a standardized solution by acting as a universal interface between LLMs and external systems. It establishes an open, standardized protocol that defines how external capabilities are discovered and used. Operating on a client-server model, MCP allows servers to expose tools, data resources, and interactive prompts to any compliant client. LLM-powered applications act as these clients, dynamically discovering and interacting with available resources in a predictable manner. This standardized approach fosters an ecosystem of interoperable and reusable components, dramatically simplifying the development of complex agentic workflows.

<mark><strong>解决之道：</strong>模型上下文协议（MCP）通过充当 LLM 与外部系统之间的通用接口提供了标准化解决方案。它建立了一个开放的标准化协议，定义了如何发现和使用外部能力。MCP 采用客户端-服务器模型运作，允许服务器向任何兼容客户端暴露工具、数据资源和交互式提示词。LLM 驱动的应用程序充当这些客户端，以可预测的方式动态发现和与可用资源交互。这种标准化方法培育了一个可互操作和可重用组件的生态系统，极大地简化了复杂智能体工作流的开发。</mark>

**Rule of thumb:** Use the Model Context Protocol (MCP) when building complex, scalable, or enterprise-grade agentic systems that need to interact with a diverse and evolving set of external tools, data sources, and APIs. It is ideal when interoperability between different LLMs and tools is a priority, and when agents require the ability to dynamically discover new capabilities without being redeployed. For simpler applications with a fixed and limited number of predefined functions, direct tool function calling may be sufficient.

<mark><strong>经验法则：</strong>在构建需要与多样化且不断发展的外部工具、数据源和 API 集交互的复杂、可扩展或企业级智能体系统时使用模型上下文协议（MCP）。当不同 LLM 和工具之间的互操作性是优先事项，并且当智能体需要在不重新部署的情况下动态发现新能力的能力时，它是理想的选择。对于具有固定且有限数量的预定义函数的更简单应用程序，直接工具函数调用可能就足够了。</mark>

**Visual summary**

<mark><strong>可视化总结</strong></mark>

Fig.1: Model Context protocol

<mark><strong>图 1：</strong>模型上下文协议</mark>

------

## Key Takeaways | <mark>核心要点</mark>

These are the key takeaways:

<mark>以下是核心要点：</mark>

- The Model Context Protocol (MCP) is an open standard facilitating standardized communication between LLMs and external applications, data sources, and tools.
- <mark>模型上下文协议（MCP）是一个开放标准，促进 LLM 与外部应用程序、数据源和工具之间的标准化通信。</mark>
- It employs a client-server architecture, defining the methods for exposing and consuming resources, prompts, and tools.
- <mark>它采用客户端-服务器架构，定义暴露和使用资源、提示词和工具的方法。</mark>
- The Agent Development Kit (ADK) supports both utilizing existing MCP servers and exposing ADK tools via an MCP server.
- <mark>智能体开发套件（ADK）支持使用现有 MCP 服务器和通过 MCP 服务器暴露 ADK 工具。</mark>
- FastMCP simplifies the development and management of MCP servers, particularly for exposing tools implemented in Python.
- <mark>FastMCP 简化了 MCP 服务器的开发和管理，特别是对于暴露用 Python 实现的工具。</mark>
- MCP Tools for Genmedia Services allows agents to integrate with Google Cloud's generative media capabilities (Imagen, Veo, Chirp 3 HD, Lyria).
- <mark>MCP Tools for Genmedia Services 允许智能体与 Google Cloud 的生成式媒体能力（Imagen、Veo、Chirp 3 HD、Lyria）集成。</mark>
- MCP enables LLMs and agents to interact with real-world systems, access dynamic information, and perform actions beyond text generation.
- <mark>MCP 使 LLM 和智能体能够与真实世界系统交互、访问动态信息并执行超越文本生成的操作。</mark>

------

## Conclusion | <mark>结语</mark>

The Model Context Protocol (MCP) is an open standard that facilitates communication between Large Language Models (LLMs) and external systems. It employs a client-server architecture, enabling LLMs to access resources, utilize prompts, and execute actions through standardized tools. MCP allows LLMs to interact with databases, manage generative media workflows, control IoT devices, and automate financial services. Practical examples demonstrate setting up agents to communicate with MCP servers, including filesystem servers and servers built with FastMCP, illustrating its integration with the Agent Development Kit (ADK). MCP is a key component for developing interactive AI agents that extend beyond basic language capabilities.

<mark>模型上下文协议（MCP）是一个开放标准，促进大语言模型（LLM）与外部系统之间的通信。它采用客户端-服务器架构，使 LLM 能够通过标准化工具访问资源、利用提示词并执行操作。MCP 允许 LLM 与数据库交互、管理生成式媒体工作流、控制物联网设备以及自动化金融服务。实际示例演示了设置智能体与 MCP 服务器通信，包括文件系统服务器和使用 FastMCP 构建的服务器，说明了其与智能体开发套件（ADK）的集成。MCP 是开发扩展到基本语言能力之外的交互式 AI 智能体的关键组件。</mark>

------

## References | <mark>参考文献</mark>

1. Model Context Protocol (MCP) Documentation. (Latest). Model Context Protocol (MCP). https://google.github.io/adk-docs/mcp/

<mark>1. 模型上下文协议（MCP）文档。（最新）。模型上下文协议（MCP）。https://google.github.io/adk-docs/mcp/</mark>

1. FastMCP Documentation. FastMCP. https://github.com/jlowin/fastmcp

<mark>2. FastMCP 文档。FastMCP。https://github.com/jlowin/fastmcp</mark>

1. MCP Tools for Genmedia Services. MCP Tools for Genmedia Services. https://google.github.io/adk-docs/mcp/#mcp-servers-for-google-cloud-genmedia

<mark>3. MCP Tools for Genmedia Services。MCP Tools for Genmedia Services。https://google.github.io/adk-docs/mcp/#mcp-servers-for-google-cloud-genmedia</mark>

1. MCP Toolbox for Databases Documentation. (Latest). MCP Toolbox for Databases. https://google.github.io/adk-docs/mcp/databases/

<mark>4. MCP Toolbox for Databases 文档。（最新）。MCP Toolbox for Databases。https://google.github.io/adk-docs/mcp/databases/</mark>