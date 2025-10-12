# Chapter 2: Routing | <mark>第二章：路由</mark>

## Routing Pattern Overview | <mark>路由模式概述</mark>

While sequential processing via prompt chaining is a foundational technique for executing deterministic, linear workflows with language models, its applicability is limited in scenarios requiring adaptive responses. Real-world agentic systems must often arbitrate between multiple potential actions based on contingent factors, such as the state of the environment, user input, or the outcome of a preceding operation. This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing.

<mark>提示链的顺序处理虽是执行确定性线性工作流的基础，但面对需要自适应响应的场景时适用性有限。</mark>

<mark>现实世界的智能体系统常需基于情境因素——环境状态、用户输入或前序操作结果——在多个行动方案间做出选择。路由（Routing）机制正是将控制流导向相应功能模块、工具或子流程的关键。</mark>

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.

<mark>路由为智能体引入条件判断逻辑，使其从固定流程转变为动态评估模式：根据具体情况选择最合适的后续动作，实现更灵活、更具上下文感知能力的系统行为。</mark>

For instance, an agent designed for customer inquiries, when equipped with a routing function, can first classify an incoming query to determine the user's intent. Based on this classification, it can then direct the query to a specialized agent for direct question-answering, a database retrieval tool for account information, or an escalation procedure for complex issues, rather than defaulting to a single, predetermined response pathway. Therefore, a more sophisticated agent using routing could:

<mark>以客户咨询智能体为例，集成路由功能后，它先对查询分类以判断用户意图，再根据结果将查询导向相应目标：专门的问答智能体、账户信息数据库检索工具，或复杂问题升级流程，而非固守单一响应路径。</mark>

<mark>因此，具有路由功能的智能体可以：</mark>

1. Analyze the user's query.

   <mark>分析用户的请求。</mark>

2. **Route** the query based on its *intent*:

    <mark>基于查询的意图将其<strong>路由</strong>到相应的处理路径：</mark>

   - If the intent is "check order status", route to a sub-agent or tool chain that interacts with the order database.

      <mark>如果意图是「检查订单状态」，转到能访问订单数据库的子智能体或工具链。</mark>

   - If the intent is "product information", route to a sub-agent or chain that searches the product catalog.

      <mark>如果意图是「产品信息」，转到负责检索产品目录的子智能体或工具链。</mark>

   - If the intent is "technical support", route to a different chain that accesses troubleshooting guides or escalates to a human.

      <mark>如果意图是「技术支持」，转到访问故障排除指南或升级至人工客服的流程。</mark>

   - If the intent is unclear, route to a clarification sub-agent or prompt chain.

      <mark>如果意图不清楚，转到专门用于澄清的子智能体或提示流程以获取更多信息。</mark>

The core component of the Routing pattern is a mechanism that performs the evaluation and directs the flow. This mechanism can be implemented in several ways:

<mark>路由模式的核心是评估与决策机制，它可通过多种方式实现：</mark>

**LLM-based Routing:** The language model itself can be prompted to analyze the input and output a specific identifier or instruction that indicates the next step or destination. For example, a prompt might ask the LLM to "Analyze the following user query and output only the category: 'Order Status', 'Product Info', 'Technical Support', or 'Other'." The agentic system then reads this output and directs the workflow accordingly.

<mark><strong>基于大语言模型的路由（LLM-based Routing）：</strong>通过提示让大语言模型分析输入并输出特定标识符或指令，指明下一步走向。例如，提示可要求大语言模型「分析以下用户请求，并只输出其类别：订单状态、产品信息、技术支持或其他」。系统读取输出后据此引导工作流。</mark>

**Embedding-based Routing:** The input query can be converted into a vector embedding (see RAG, Chapter 14). This embedding is then compared to embeddings representing different routes or capabilities. The query is routed to the route whose embedding is most similar. This is useful for semantic routing, where the decision is based on the meaning of the input rather than just keywords.

<mark><strong>基于嵌入的路由（Embedding-based Routing）：</strong>将输入请求转换为向量嵌入（详见第 14 章 RAG），再与代表不同路径或能力的嵌入比较，将请求路由至语义最相似的路径。这种方式非常适合语义路由（Semantic Routing），因为它基于输入含义而非仅靠关键词。</mark>

**Rule-based Routing:** This involves using predefined rules or logic (e.g., if-else statements, switch cases) based on keywords, patterns, or structured data extracted from the input. This can be faster and more deterministic than LLM-based routing, but is less flexible for handling nuanced or novel inputs.

<mark><strong>基于规则的路由（Rule-based Routing）：</strong>使用预定义规则或逻辑（如 if-else 语句、switch 判断）依据输入中的关键词、模式或结构化数据做决策。相比大模型驱动路由更快、更确定，但面对复杂、细微或未见输入时灵活性不足。</mark>

**Machine Learning Model-Based Routing:** it employs a discriminative model, such as a classifier, that has been specifically trained on a small corpus of labeled data to perform a routing task. While it shares conceptual similarities with embedding-based methods, its key characteristic is the supervised fine-tuning process, which adjusts the model's parameters to create a specialized routing function. This technique is distinct from LLM-based routing because the decision-making component is not a generative model executing a prompt at inference time. Instead, the routing logic is encoded within the fine-tuned model's learned weights. While LLMs may be used in a pre-processing step to generate synthetic data for augmenting the training set, they are not involved in the real-time routing decision itself.

<mark><strong>基于机器学习模型的路由（Machine Learning Model-Based Routing）：</strong>使用判别模型（如分类器）在少量标注数据上专门训练来完成路由任务。虽与基于嵌入的方法概念相近，但其核心是通过监督微调调整模型参数，创建专门的路由功能。</mark>

<mark>这与基于大模型的路由不同：决策不靠推理时运行提示的生成模型，而是内嵌在微调后模型的权重中。虽可在预处理阶段用大语言模型生成合成数据扩充训练集，但实时路由决策中不再使用它们。</mark>

Routing mechanisms can be implemented at multiple junctures within an agent's operational cycle. They can be applied at the outset to classify a primary task, at intermediate points within a processing chain to determine a subsequent action, or during a subroutine to select the most appropriate tool from a given set.

<mark>路由机制可在智能体运作的多个阶段启用：初始阶段识别和分类主要任务，处理流程中段决定下一步动作，子程序中从可用工具中挑选最合适的一个。</mark>

Computational frameworks such as LangChain, LangGraph, and Google's Agent Developer Kit (ADK) provide explicit constructs for defining and managing such conditional logic. With its state-based graph architecture, LangGraph is particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system. Similarly, Google's ADK provides foundational components for structuring an agent's capabilities and interaction models, which serve as the basis for implementing routing logic. Within the execution environments provided by these frameworks, developers define the possible operational paths and the functions or model-based evaluations that dictate the transitions between nodes in the computational graph.

<mark>LangChain、LangGraph 和 Google 智能体开发套件（ADK）等框架提供了便捷的条件逻辑定义与管理能力。</mark>

<mark>LangGraph 基于状态图架构，尤其适合复杂路由场景——此时决策依赖于整个系统的累积状态。Google ADK 同样为构建智能体能力和交互模型提供了基础组件，是实现路由逻辑的基石。在这些框架中，开发者定义可选运行路径，以及决定图中节点转换的函数或模型评估逻辑。</mark>

The implementation of routing enables a system to move beyond deterministic sequential processing. It facilitates the development of more adaptive execution flows that can respond dynamically and appropriately to a wider range of inputs and state changes.

<mark>路由的实现让系统超越确定性顺序处理，开发出更具适应性的执行流程，能对更广泛的输入和状态变化做出动态且恰当的响应。</mark>

---

## Practical Applications & Use Cases | <mark>实际应用和用例</mark>

The routing pattern is a critical control mechanism in the design of adaptive agentic systems, enabling them to dynamically alter their execution path in response to variable inputs and internal states. Its utility spans multiple domains by providing a necessary layer of conditional logic.

<mark>路由模式是自适应型智能体系统中的重要控制机制，能让系统根据不同输入和内部状态动态调整执行流程。通过提供必要的条件逻辑层，其效用贯穿多个领域。</mark>

In human-computer interaction, such as with virtual assistants or AI-driven tutors, routing is employed to interpret user intent. An initial analysis of a natural language query determines the most appropriate subsequent action, whether it is invoking a specific information retrieval tool, escalating to a human operator, or selecting the next module in a curriculum based on user performance. This allows the system to move beyond linear dialogue flows and respond contextually.

<mark>在人机交互领域，如虚拟助手或 AI 辅导系统，路由用于识别用户意图。对自然语言查询的初步分析决定最合适的后续操作：调用信息检索工具、转接人工客服，或根据用户表现选择课程的下一模块。这让系统摆脱线性对话流程，做出更符合上下文的响应。</mark>

Within automated data and document processing pipelines, routing serves as a classification and distribution function. Incoming data, such as emails, support tickets, or API payloads, is analyzed based on content, metadata, or format. The system then directs each item to a corresponding workflow, such as a sales lead ingestion process, a specific data transformation function for JSON or CSV formats, or an urgent issue escalation path.

<mark>在自动化数据与文档处理流水线中，路由扮演分类与分发角色。系统根据内容、元数据或格式分析传入数据（如邮件、支持工单或 API 请求），并将其导向对应工作流：销售线索导入、JSON 或 CSV 数据转换，或紧急问题升级处理。</mark>

In complex systems involving multiple specialized tools or agents, routing acts as a high-level dispatcher. A research system composed of distinct agents for searching, summarizing, and analyzing information would use a router to assign tasks to the most suitable agent based on the current objective. Similarly, an AI coding assistant uses routing to identify the programming language and user's intent—to debug, explain, or translate—before passing a code snippet to the correct specialized tool.

<mark>在涉及多个专业工具或智能体的复杂系统中，路由扮演高级调度员角色。由搜索、总结、分析等独立智能体组成的研究系统，会使用路由器根据当前目标将任务分配给最合适的智能体。AI 编程助手同样利用路由识别编程语言和用户意图（如调试、解释或翻译），再将代码片段交给对应专用工具处理。</mark>

Ultimately, routing provides the capacity for logical arbitration that is essential for creating functionally diverse and context-aware systems. It transforms an agent from a static executor of pre-defined sequences into a dynamic system that can make decisions about the most effective method for accomplishing a task under changing conditions.

<mark>路由赋予系统逻辑判断能力，这对构建功能多样、具备上下文感知的系统至关重要。它让智能体从按预设步骤执行的静态执行器，演变为能在环境变化时动态选择最有效方式完成任务的动态系统。</mark>

---

## Hands-On Code Example (LangChain) | <mark>使用 LangChain 的实战代码</mark>

Implementing routing in code involves defining the possible paths and the logic that decides which path to take. Frameworks like LangChain and LangGraph provide specific components and structures for this. LangGraph's state-based graph structure is particularly intuitive for visualizing and implementing routing logic.

<mark>在代码中实现路由，需要定义所有可能的路径和决策逻辑。LangChain 和 LangGraph 等框架为此提供了专门的组件和结构。LangGraph 基于状态的图结构在可视化和实现路由逻辑方面尤为直观。</mark>

This code demonstrates a simple agent-like system using LangChain and Google's Generative AI. It sets up a "coordinator" that routes user requests to different simulated "sub-agent" handlers based on the request's intent (booking, information, or unclear). The system uses a language model to classify the request and then delegates it to the appropriate handler function, simulating a basic delegation pattern often seen in multi-agent architectures.

<mark>以下代码使用 LangChain 和 Google Gemini 模型演示一个简单的智能体系统。它设置了一个「协调员」，根据请求意图（预订、信息查询或意图不明）将用户请求路由到不同的模拟「子智能体」。整个流程：先由语言模型进行意图分类，再将任务交给对应处理模块，模拟了多智能体架构中常见的任务委派模式。</mark>

First, ensure you have the necessary libraries installed:

<mark>首先，确保你安装了必要的库：</mark>

```bash path=null start=null
pip install langchain langgraph google-cloud-aiplatform langchain-google-genai google-adk deprecated pydantic
```

You will also need to set up your environment with your API key for the language model you choose (e.g., OpenAI, Google Gemini, Anthropic).

<mark>你还需要在环境中设置所选语言模型（如 OpenAI、Google Gemini、Anthropic）的 API 密钥。</mark>

```python path=null start=null
# Copyright (c) 2025 Marco Fago
#
# This code is licensed under the MIT License.
# See the LICENSE file in the repository for the full license text.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch

# --- Configuration ---
# Ensure your API key environment variable is set (e.g., GOOGLE_API_KEY)
# 确保你的 API 密钥环境变量已设置 (如 GOOGLE_API_KEY)
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    print(f"Language model initialized: {llm.model}")
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None

# --- Define Simulated Sub-Agent Handlers (equivalent to ADK sub_agents) ---
# --- 定义模拟的子智能体处理器 (等同于 ADK 中的 sub_agents) ---

def booking_handler(request: str) -> str:
    """Simulates the Booking Agent handling a request."""
    print("\n--- DELEGATING TO BOOKING HANDLER ---")
    return f"Booking Handler processed request: '{request}'. Result: Simulated booking action."

def info_handler(request: str) -> str:
    """Simulates the Info Agent handling a request."""
    print("\n--- DELEGATING TO INFO HANDLER ---")
    return f"Info Handler processed request: '{request}'. Result: Simulated information retrieval."

def unclear_handler(request: str) -> str:
    """Handles requests that couldn't be delegated."""
    print("\n--- HANDLING UNCLEAR REQUEST ---")
    return f"Coordinator could not delegate request: '{request}'. Please clarify."

# --- Define Coordinator Router Chain (equivalent to ADK coordinator's instruction) ---
# This chain decides which handler to delegate to.
# --- 定义协调员的路由链 (等同于 ADK 协调员的指令) ---
# 这个链负责决定将任务委派给哪个处理器。
coordinator_router_prompt = ChatPromptTemplate.from_messages([
    ("system", """Analyze the user's request and determine which specialist handler should process it.
     - If the request is related to booking flights or hotels, output 'booker'.
     - For all other general information questions, output 'info'.
     - If the request is unclear or doesn't fit either category, output 'unclear'.
     ONLY output one word: 'booker', 'info', or 'unclear'."""),
    ("user", "{request}")
])

if llm:
    coordinator_router_chain = coordinator_router_prompt | llm | StrOutputParser()

# --- Define the Delegation Logic (equivalent to ADK's Auto-Flow based on sub_agents) ---
# Use RunnableBranch to route based on the router chain's output.
# --- 定义委派逻辑 (等同于 ADK 基于 sub_agents 的自动流) ---
# 使用 RunnableBranch 根据路由链的输出进行路由。

# Define the branches for the RunnableBranch
# 为 RunnableBranch 定义分支
branches = {
    "booker": RunnablePassthrough.assign(output=lambda x: booking_handler(x['request']['request'])),
    "info": RunnablePassthrough.assign(output=lambda x: info_handler(x['request']['request'])),
    "unclear": RunnablePassthrough.assign(output=lambda x: unclear_handler(x['request']['request'])),
}

# Create the RunnableBranch. It takes the output of the router chain
# and routes the original input ('request') to the corresponding handler.
# 创建 RunnableBranch。它会接收路由链的输出，
# 并将原始输入 ('request') 路由到相应的处理器。
delegation_branch = RunnableBranch(
    (lambda x: x['decision'].strip() == 'booker', branches["booker"]), # Added .strip()
    (lambda x: x['decision'].strip() == 'info', branches["info"]),     # Added .strip()
    branches["unclear"] # Default branch for 'unclear' or any other output
)

# Combine the router chain and the delegation branch into a single runnable
# The router chain's output ('decision') is passed along with the original input ('request')
# to the delegation_branch.
# 将路由链和委派分支组合成一个可执行单元
# 路由链的输出 ('decision') 会连同原始输入 ('request') 一起
# 传递给 delegation_branch。
coordinator_agent = {
    "decision": coordinator_router_chain,
    "request": RunnablePassthrough()
} | delegation_branch | (lambda x: x['output']) # Extract the final output

# --- Example Usage ---
# --- 使用示例 ---
def main():
    if not llm:
        print("\nSkipping execution due to LLM initialization failure.")
        return

    print("--- Running with a booking request ---")
    request_a = "Book me a flight to London."
    result_a = coordinator_agent.invoke({"request": request_a})
    print(f"Final Result A: {result_a}")

    print("\n--- Running with an info request ---")
    request_b = "What is the capital of Italy?"
    result_b = coordinator_agent.invoke({"request": request_b})
    print(f"Final Result B: {result_b}")

    print("\n--- Running with an unclear request ---")
    request_c = "Tell me about quantum physics."
    result_c = coordinator_agent.invoke({"request": request_c})
    print(f"Final Result C: {result_c}")

if __name__ == "__main__":
    main()
```

译者注：[Colab 代码](https://colab.research.google.com/drive/1Yh3eUcvajJfgTFKhEQga6bJ3yyKodAmg) 已维护在[此处](/codes/Chapter-02-Routing-LangChain-Example.py)。

**运行输出（译者添加）：**

```text
Language model initialized: models/gemini-2.5-flash
--- Running with a booking request ---

--- DELEGATING TO BOOKING HANDLER ---
Final Result A: Booking Handler processed request: 'Book me a flight to London.'. Result: Simulated booking action.

--- Running with an info request ---

--- DELEGATING TO INFO HANDLER ---
Final Result B: Info Handler processed request: 'What is the capital of Italy?'. Result: Simulated information retrieval.

--- Running with an unclear request ---

--- DELEGATING TO INFO HANDLER ---
Final Result C: Info Handler processed request: 'Tell me about quantum physics.'. Result: Simulated information retrieval.
```

As mentioned, this Python code constructs a simple agent-like system using the LangChain library and Google's Generative AI model, specifically gemini-2.5-flash. In detail, It defines three simulated sub-agent handlers: booking_handler, info_handler, and unclear_handler, each designed to process specific types of requests.

<mark>如前所述，这段 Python 代码使用 LangChain 库和 Google 的 gemini-2.5-flash 模型构建了一个简单的类智能体系统。它定义了三个模拟的子智能体处理器：booking_handler、info_handler 和 unclear_handler，分别用于处理特定类型的请求。</mark>

A core component is the coordinator_router_chain, which utilizes a ChatPromptTemplate to instruct the language model to categorize incoming user requests into one of three categories: 'booker', 'info', or 'unclear'. The output of this router chain is then used by a RunnableBranch to delegate the original request to the corresponding handler function. The RunnableBranch checks the decision from the language model and directs the request data to either the booking_handler, info_handler, or unclear_handler. The coordinator_agent combines these components, first routing the request for a decision and then passing the request to the chosen handler. The final output is extracted from the handler's response.

<mark>核心组件是 coordinator_router_chain，它通过 ChatPromptTemplate 指示模型将用户请求分为三类：'booker'、'info' 或 'unclear'。随后 RunnableBranch 使用路由链的输出将原始请求委派给相应的处理函数。RunnableBranch 根据模型的判断，将请求数据发送到 booking_handler、info_handler 或 unclear_handler。coordinator_agent 将这些部分组合在一起：先进行路由决策，然后把请求转给选定的处理器，最后从处理器的响应中提取并返回最终结果。</mark>

The main function demonstrates the system's usage with three example requests, showcasing how different inputs are routed and processed by the simulated agents. Error handling for language model initialization is included to ensure robustness. The code structure mimics a basic multi-agent framework where a central coordinator delegates tasks to specialized agents based on intent.

<mark>主函数通过三个示例请求展示了系统的实际用法，说明不同的输入如何被路由并由各个模拟智能体处理。为了保证稳定性，代码还包含了语言模型初始化的错误处理。整体代码结构类似一个简化的多智能体框架：中央协调器根据意图把任务分配给各个专长不同的智能体。</mark>

---

## Hands-On Code Example (Google ADK) | <mark>使用 Google ADK 的实战代码</mark>

The Agent Development Kit (ADK) is a framework for engineering agentic systems, providing a structured environment for defining an agent's capabilities and behaviours. In contrast to architectures based on explicit computational graphs, routing within the ADK paradigm is typically implemented by defining a discrete set of "tools" that represent the agent's functions. The selection of the appropriate tool in response to a user query is managed by the framework's internal logic, which leverages an underlying model to match user intent to the correct functional handler.

<mark>Google 智能体开发套件（ADK）是用于构建智能体系统的框架，提供了一个用于定义智能体能力与行为的结构化环境。与基于显式计算图的架构相比，ADK 中的路由通常是通过定义一组独立的「工具」来实现，这些工具对应智能体的各项功能。框架的内部逻辑会在用户发起查询时选择合适的工具，借助底层模型将用户意图匹配到相应的功能处理器。</mark>

This Python code demonstrates an example of an Agent Development Kit (ADK) application using Google's ADK library. It sets up a "Coordinator" agent that routes user requests to specialized sub-agents ("Booker" for bookings and "Info" for general information) based on defined instructions. The sub-agents then use specific tools to simulate handling the requests, showcasing a basic delegation pattern within an agent system.

<mark>这段 Python 代码演示了如何使用 Google ADK 构建应用。它设置了一个「协调员」智能体，根据预设指令将用户请求分发给两个专门的子智能体：负责预订的「Booker」和提供通用信息的「Info」。各子智能体再调用各自的工具来模拟处理请求，展示了智能体系统中基本的任务委派模式。</mark>

```python path=null start=null
# Copyright (c) 2025 Marco Fago
#
# This code is licensed under the MIT License.
# See the LICENSE file in the repository for the full license text.

import uuid
from typing import Dict, Any, Optional

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool
from google.genai import types
from google.adk.events import Event

# Colab 代码链接: https://colab.research.google.com/drive/10wxRlPyDJ70pPEtWWA3Aa3tjvfobrB3m

# 安装依赖
# pip install google-genai google-adk

# --- Define Tool Functions ---
# These functions simulate the actions of the specialist agents.
# --- 定义工具函数 ---
# 这些函数模拟了专业智能体的具体行动。

def booking_handler(request: str) -> str:
    """
    Handles booking requests for flights and hotels.
    Args:
        request: The user's request for a booking.
    Returns:
        A confirmation message that the booking was handled.
    """
    print("-------------------------- Booking Handler Called ----------------------------")
    return f"Booking action for '{request}' has been simulated."

def info_handler(request: str) -> str:
    """
    Handles general information requests.
    Args:
        request: The user's question.
    Returns:
        A message indicating the information request was handled.
    """
    print("-------------------------- Info Handler Called ----------------------------")
    return f"Information request for '{request}'. Result: Simulated information retrieval."

def unclear_handler(request: str) -> str:
    """Handles requests that couldn't be delegated."""
    return f"Coordinator could not delegate request: '{request}'. Please clarify."

# --- Create Tools from Functions ---
# --- 从函数创建工具 ---
booking_tool = FunctionTool(booking_handler)
info_tool = FunctionTool(info_handler)

# Define specialized sub-agents equipped with their respective tools
# --- 定义配备了各自工具的专业子智能体 ---
booking_agent = Agent(
    name="Booker",
    model="gemini-2.0-flash",
    description="A specialized agent that handles all flight and hotel booking requests by calling the booking tool.",
    tools=[booking_tool]
)

info_agent = Agent(
    name="Info",
    model="gemini-2.0-flash",
    description="A specialized agent that provides general information and answers user questions by calling the info tool.",
    tools=[info_tool]
)

# Define the parent agent with explicit delegation instructions
# --- 定义带有明确委派指令的父智能体 ---
coordinator = Agent(
    name="Coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "You are the main coordinator. Your only task is to analyze incoming user requests "
        "and delegate them to the appropriate specialist agent. Do not try to answer the user directly.\n"
        "- For any requests related to booking flights or hotels, delegate to the 'Booker' agent.\n"
        "- For all other general information questions, delegate to the 'Info' agent."
    ),
    description="A coordinator that routes user requests to the correct specialist agent.",
    # The presence of sub_agents enables LLM-driven delegation (Auto-Flow) by default.
    # 定义了 sub_agents 默认就会启用由大语言模型驱动的委派。
    sub_agents=[booking_agent, info_agent]
)

# --- Execution Logic ---
# --- 执行逻辑 ---
def run_coordinator(runner: InMemoryRunner, request: str):
    """Runs the coordinator agent with a given request and delegates."""
    """用给定的请求运行协调员智能体并进行委派。"""
    print(f"\n--- Running Coordinator with request: '{request}' ---")
    final_result = ""
    try:
        user_id = "user_123"
        session_id = str(uuid.uuid4())
        runner.session_service.create_session(
            app_name=runner.app_name, user_id=user_id, session_id=session_id
        )

        for event in runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role='user',
                parts=[types.Part(text=request)]
            ),
        ):
            if event.is_final_response() and event.content:
                # Try to get text directly from event.content to avoid iterating parts
                if hasattr(event.content, 'text') and event.content.text:
                     final_result = event.content.text
                elif event.content.parts:
                    # Fallback: Iterate through parts and extract text (might trigger warning)
                    text_parts = [part.text for part in event.content.parts if part.text]
                    final_result = "".join(text_parts)
                # Assuming the loop should break after the final response
                break

        print(f"Coordinator Final Response: {final_result}")
        return final_result
    except Exception as e:
        print(f"An error occurred while processing your request: {e}")
        return f"An error occurred while processing your request: {e}"

def main():
    """Main function to run the ADK example."""
    """运行 ADK 示例的主函数。"""
    print("--- Google ADK Routing Example (ADK Auto-Flow Style) ---")
    print("Note: This requires Google ADK installed and authenticated.")

    runner = InMemoryRunner(coordinator)
    # Example Usage
    # 使用示例
    result_a = run_coordinator(runner, "Book me a hotel in Paris.")
    print(f"Final Output A: {result_a}")
    result_b = run_coordinator(runner, "What is the highest mountain in the world?")
    print(f"Final Output B: {result_b}")
    result_c = run_coordinator(runner, "Tell me a random fact.") # Should go to Info
    print(f"Final Output C: {result_c}")
    result_d = run_coordinator(runner, "Find flights to Tokyo next month.") # Should go to Booker
    print(f"Final Output D: {result_d}")


if __name__ == "__main__":
    main()
```

译者注：[Colab 代码](https://colab.research.google.com/drive/10wxRlPyDJ70pPEtWWA3Aa3tjvfobrB3m) 已维护在[此处](/codes/Chapter-02-Routing-ADK-Example.py)。

This script consists of a main Coordinator agent and two specialized sub_agents: Booker and Info. Each specialized agent is equipped with a FunctionTool that wraps a Python function simulating an action. The booking_handler function simulates handling flight and hotel bookings, while the info_handler function simulates retrieving general information. The unclear_handler is included as a fallback for requests the coordinator cannot delegate, although the current coordinator logic doesn't explicitly use it for delegation failure in the main run_coordinator function.

<mark>该脚本包含一个主协调员和两个专职子智能体：Booker 和 Info。每个子智能体都配有一个 FunctionTool，用于封装模拟操作的 Python 函数。booking_handler 用来模拟处理航班和酒店预订，info_handler 用来模拟查询信息。脚本中还包含一个 unclear_handler，作为协调器在无法委派请求时的备用处理，不过在当前的 run_coordinator 主流程中，并没有明确使用它来处理委派失败的情况。</mark>

The Coordinator agent's primary role, as defined in its instruction, is to analyze incoming user messages and delegate them to either the Booker or Info agent. This delegation is handled automatically by the ADK's Auto-Flow mechanism because the Coordinator has sub_agents defined. The run_coordinator function sets up an InMemoryRunner, creates a user and session ID, and then uses the runner to process the user's request through the coordinator agent. The runner.run method processes the request and yields events, and the code extracts the final response text from the event.content.

<mark>协调员的主要职责是分析收到的用户消息，并将其分派给 Booker 或 Info 子智能体。因为协调员定义了子智能体，ADK 的流程会自动完成这种分派。run_coordinator 函数会初始化一个 InMemoryRunner，创建用户和会话 ID，然后用该 runner 将用户请求提交给协调员来处理。runner.run 方法会处理请求并生成事件，代码从这些事件的 event.content 中提取最终的响应文本。</mark>

The main function demonstrates the system's usage by running the coordinator with different requests, showcasing how it delegates booking requests to the Booker and information requests to the Info agent.

<mark>主函数通过用不同的请求来演示，展示了协调员如何把预订类请求交给负责预订的子智能体，把查询类信息请求交给信息查询子智能体。</mark>

---

## At a Glance | <mark>要点速览</mark>

**What:** Agentic systems must often respond to a wide variety of inputs and situations that cannot be handled by a single, linear process. A simple sequential workflow lacks the ability to make decisions based on context. Without a mechanism to choose the correct tool or sub-process for a specific task, the system remains rigid and non-adaptive. This limitation makes it difficult to build sophisticated applications that can manage the complexity and variability of real-world user requests.

<mark><strong>问题所在：</strong> 智能体系统往往需要应对各种各样的输入和情境，单一的线性流程无法满足这一需求。简单的顺序工作流缺乏根据上下文做出决策的能力。如果没有一个机制来为特定任务选择正确的工具或子流程，系统就会显得死板，缺乏适应性，难以构建能够管理真实世界复杂多变请求的成熟应用。</mark>

**Why:** The Routing pattern provides a standardized solution by introducing conditional logic into an agent's operational framework. It enables the system to first analyze an incoming query to determine its intent or nature. Based on this analysis, the agent dynamically directs the flow of control to the most appropriate specialized tool, function, or sub-agent. This decision can be driven by various methods, including prompting LLMs, applying predefined rules, or using embedding-based semantic similarity. Ultimately, routing transforms a static, predetermined execution path into a flexible and context-aware workflow capable of selecting the best possible action.

<mark><strong>解决之道：</strong>路由模式通过在智能体操作框架中引入条件判断，提供标准化解决方案。它使系统先分析传入请求以判断其意图或性质，然后将控制流动态导向最合适的专业工具、函数或子智能体。决策可由多种方法驱动：提示大语言模型、应用预定义规则或使用基于嵌入的语义相似度。最终，路由将静态预定的执行路径转变为灵活、具备上下文感知的工作流，能为任务选择最佳行动方案。</mark>

**Rule of Thumb:** Use the Routing pattern when an agent must decide between multiple distinct workflows, tools, or sub-agents based on the user's input or the current state. It is essential for applications that need to triage or classify incoming requests to handle different types of tasks, such as a customer support bot distinguishing between sales inquiries, technical support, and account management questions.

<mark><strong>经验法则：</strong>当智能体必须根据用户输入或当前状态在多个不同的工作流、工具或子智能体之间做出选择时，就应使用路由模式。对于那些需要对传入请求进行分类以处理不同类型任务的应用来说，它是必不可少的，例如需要区分销售咨询、技术支持和账户管理问题的客户支持机器人。</mark>

**Visual summary** | <mark>可视化总结</mark>

![可视化总结](/images/chapter02_fig1.jpg)

Fig.1: Router pattern, using an LLM as a Router

<mark>路由模式 —— 利用一个大语言模型作为路由器</mark>

---

## Key Takeaways | <mark>核心要点</mark>

- Routing enables agents to make dynamic decisions about the next step in a workflow based on conditions.

   <mark>路由使智能体能够根据条件，动态决定工作流的下一步。</mark>

- It allows agents to handle diverse inputs and adapt their behavior, moving beyond linear execution.

   <mark>它允许智能体处理多样化的输入并适应其行为，超越了线性的执行方式。</mark>

- Routing logic can be implemented using LLMs, rule-based systems, or embedding similarity.

   <mark>路由逻辑可以使用大语言模型、基于规则的系统或嵌入相似度来实现。</mark>

- Frameworks like LangGraph and Google ADK provide structured ways to define and manage routing within agent workflows, albeit with different architectural approaches.

   <mark>像 LangGraph 和 Google ADK 这样的框架，为在智能体工作流中定义和管理路由提供了结构化的方法，尽管它们的架构方式有所不同。</mark>

---

## Conclusion | <mark>结语</mark>

The Routing pattern is a critical step in building truly dynamic and responsive agentic systems. By implementing routing, we move beyond simple, linear execution flows and empower our agents to make intelligent decisions about how to process information, respond to user input, and utilize available tools or sub-agents.

<mark>路由模式是构建真正动态、响应迅速的智能体系统的关键。通过实现路由，我们超越简单线性执行流程，赋予智能体智能决策能力，使其知道如何处理信息、响应用户输入以及利用可用工具或子智能体。</mark>

We've seen how routing can be applied in various domains, from customer service chatbots to complex data processing pipelines. The ability to analyze input and conditionally direct the workflow is fundamental to creating agents that can handle the inherent variability of real-world tasks.

<mark>我们看到路由如何应用于从客户服务聊天机器人到复杂数据处理流水线的多个领域。分析输入并有条件地引导工作流的能力，是创建能处理现实世界任务固有多变性的智能体的基础。</mark>

The code examples using LangChain and Google ADK demonstrate two different, yet effective, approaches to implementing routing. LangGraph's graph-based structure provides a visual and explicit way to define states and transitions, making it ideal for complex, multi-step workflows with intricate routing logic. Google ADK, on the other hand, often focuses on defining distinct capabilities (Tools) and relies on the framework's ability to route user requests to the appropriate tool handler, which can be simpler for agents with a well-defined set of discrete actions.

<mark>LangChain 和 Google ADK 的代码示例展示了两种不同但同样有效的路由实现方法。LangGraph 的图结构提供可视化、显式定义状态和转换的方式，非常适合具有复杂路由逻辑的多步工作流。Google ADK 则侧重定义离散能力(工具),依赖框架将用户请求路由到合适工具处理程序,对于职责清晰、相互独立的子智能体来说更为简洁高效。</mark>

Mastering the Routing pattern is essential for building agents that can intelligently navigate different scenarios and provide tailored responses or actions based on context. It's a key component in creating versatile and robust agentic applications.

<mark>掌握路由模式对于构建能根据不同场景和上下文智能选择响应或执行操作的智能体至关重要，是打造灵活可靠的智能体应用的核心要素。</mark>

---

## References | <mark>参考文献</mark>

1. LangGraph Documentation: [https://www.langchain.com/](https://www.langchain.com/)

   <mark>LangGraph 官方文档：[https://www.langchain.com/](https://www.langchain.com/)</mark>

2. Google Agent Developer Kit Documentation: [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)

   <mark>谷歌智能体开发套件官方文档：[https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)</mark>
