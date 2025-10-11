# Chapter 2: Routing | <mark>第二章：路由</mark>

## Routing Pattern Overview | <mark>路由模式概述</mark>

While sequential processing via prompt chaining is a foundational technique for executing deterministic, linear workflows with language models, its applicability is limited in scenarios requiring adaptive responses. Real-world agentic systems must often arbitrate between multiple potential actions based on contingent factors, such as the state of the environment, user input, or the outcome of a preceding operation. This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing.

<mark>虽然通过提示链进行顺序处理是使用语言模型执行确定性、线性工作流的基础技术，但在需要自适应响应的场景中，其适用性有限。现实世界的智能体系统往往需要基于多种情境因素——如环境状态、用户输入或前序操作的结果——在多个可能的行动之间做出选择。这种动态决策能力可以将控制流导向不同的专门功能、工具或子流程，而实现这一能力的机制，就是「路由」。</mark>

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.

<mark>路由在智能体的操作框架中引入了条件逻辑，使系统从固定执行路径转向一种新模式：智能体根据特定标准动态评估，从一组可能的后续行动中做出选择。这样，系统行为就变得更加灵活，也更具上下文感知能力。</mark>

For instance, an agent designed for customer inquiries, when equipped with a routing function, can first classify an incoming query to determine the user's intent. Based on this classification, it can then direct the query to a specialized agent for direct question-answering, a database retrieval tool for account information, or an escalation procedure for complex issues, rather than defaulting to a single, predetermined response pathway. Therefore, a more sophisticated agent using routing could:

<mark>以客户咨询智能体为例，当它配备了路由功能后，可以先对传入的查询进行分类，判断用户意图。根据分类结果，它可以将查询导向：专门的问答智能体、用于账户信息的数据库检索工具，或处理复杂问题的升级流程，而不会被限制在单一预设的响应路径上。因此，一个配备路由功能的成熟智能体可以：</mark>

1. Analyze the user's query.

1. <mark>分析用户的查询。</mark>

2. **Route** the query based on its *intent*:

2. <mark>基于查询的<em>意图</em>进行<strong>路由</strong>：</mark>

   - If the intent is "check order status", route to a sub-agent or tool chain that interacts with the order database.

   <mark>- 若意图为「检查订单状态」，则路由至与订单数据库交互的子智能体或工具链</mark>

   - If the intent is "product information", route to a sub-agent or chain that searches the product catalog.

   <mark>- 若意图为「产品信息」，则路由至搜索产品目录的子智能体或链</mark>

   - If the intent is "technical support", route to a different chain that accesses troubleshooting guides or escalates to a human.

   <mark>- 若意图为「技术支持」，则路由至访问故障排除指南或转接人工的处理链</mark>

   - If the intent is unclear, route to a clarification sub-agent or prompt chain.

   <mark>- 若意图不明确，则路由至澄清子智能体或提示链</mark>

The core component of the Routing pattern is a mechanism that performs the evaluation and directs the flow. This mechanism can be implemented in several ways:

<mark>路由模式的核心在于一个评估机制，它负责判断并引导流程走向。这一机制有多种实现方式：</mark>

### Routing Implementation Methods | <mark>路由实现方法</mark>

**LLM-based Routing:** The language model itself can be prompted to analyze the input and output a specific identifier or instruction that indicates the next step or destination. For example, a prompt might ask the LLM to "Analyze the following user query and output only the category: 'Order Status', 'Product Info', 'Technical Support', or 'Other'." The agentic system then reads this output and directs the workflow accordingly.

<mark><strong>基于 LLM 的路由：</strong>通过提示词让语言模型分析输入，并输出指示下一步或目标的标识符或指令。例如，提示词可以要求 LLM：「分析以下用户查询，并仅输出类别：『订单状态』、『产品信息』、『技术支持』或『其他』。」智能体系统随后读取这个输出，并据此引导工作流。</mark>

**Embedding-based Routing:** The input query can be converted into a vector embedding (see RAG, Chapter 14). This embedding is then compared to embeddings representing different routes or capabilities. The query is routed to the route whose embedding is most similar. This is useful for semantic routing, where the decision is based on the meaning of the input rather than just keywords.

<mark><strong>基于嵌入的路由：</strong>输入查询可以转换为向量嵌入（参见第 14 章 RAG）。然后将该嵌入与代表不同路由或能力的嵌入进行比较，系统会将查询路由到最相似的路径。这种方式对语义路由很有用，因为它根据输入的实际含义做决策，而非仅仅依赖关键字。</mark>

**Rule-based Routing:** This involves using predefined rules or logic (e.g., if-else statements, switch cases) based on keywords, patterns, or structured data extracted from the input. This can be faster and more deterministic than LLM-based routing, but is less flexible for handling nuanced or novel inputs.

<mark><strong>基于规则的路由：</strong>这种方法使用预定义的规则或逻辑（如 if-else 语句、switch 分支），依据从输入中提取的关键字、模式或结构化数据进行判断。与基于 LLM 的路由相比，它速度更快、结果更确定，但在处理微妙差异或新颖输入时灵活性较差。</mark>

**Machine Learning Model-Based Routing:** it employs a discriminative model, such as a classifier, that has been specifically trained on a small corpus of labeled data to perform a routing task. While it shares conceptual similarities with embedding-based methods, its key characteristic is the supervised fine-tuning process, which adjusts the model's parameters to create a specialized routing function. This technique is distinct from LLM-based routing because the decision-making component is not a generative model executing a prompt at inference time. Instead, the routing logic is encoded within the fine-tuned model's learned weights. While LLMs may be used in a pre-processing step to generate synthetic data for augmenting the training set, they are not involved in the real-time routing decision itself.

<mark><strong>基于机器学习模型的路由：</strong>这种方法采用判别模型（如分类器），在小规模标注数据上进行专门训练来执行路由任务。虽然它在概念上与基于嵌入的方法相似，但其关键特征在于监督式微调过程——通过调整模型参数来创建专用的路由功能。这项技术与基于 LLM 的路由截然不同：它的决策组件并非在推理时执行提示词的生成模型，而是将路由逻辑直接编码在微调后模型学习到的权重之中。虽然 LLM 可能在预处理阶段用于生成合成数据以扩充训练集，但在实时路由决策时，LLM 并不直接参与。</mark>

Routing mechanisms can be implemented at multiple junctures within an agent's operational cycle. They can be applied at the outset to classify a primary task, at intermediate points within a processing chain to determine a subsequent action, or during a subroutine to select the most appropriate tool from a given set.

<mark>路由机制可以部署在智能体操作周期的多个时机点上：在任务开始时对主任务进行分类，在处理链的中间环节决定后续行动，或在子程序中从给定工具集里选择最合适的一个。</mark>

Computational frameworks such as LangChain, LangGraph, and Google's Agent Developer Kit (ADK) provide explicit constructs for defining and managing such conditional logic. With its state-based graph architecture, LangGraph is particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system. Similarly, Google's ADK provides foundational components for structuring an agent's capabilities and interaction models, which serve as the basis for implementing routing logic. Within the execution environments provided by these frameworks, developers define the possible operational paths and the functions or model-based evaluations that dictate the transitions between nodes in the computational graph.

<mark>LangChain、LangGraph 和 Google Agent Developer Kit（ADK）等计算框架，为定义和管理此类条件逻辑提供了明确的结构。LangGraph 凭借其基于状态的图架构，特别适合决策依赖于整个系统累积状态的复杂路由场景。同样，Google ADK 为构建智能体的能力和交互模型提供了基础组件，是实现路由逻辑的重要基础。在这些框架提供的执行环境中，开发者可以定义可能的操作路径，以及决定计算图节点间如何转换的函数或基于模型的评估逻辑。</mark>

The implementation of routing enables a system to move beyond deterministic sequential processing. It facilitates the development of more adaptive execution flows that can respond dynamically and appropriately to a wider range of inputs and state changes.

<mark>路由的实现让系统得以超越确定性的顺序处理，促进更具适应性的执行流程的发展，使系统能够对更广泛的输入和状态变化做出动态而恰当的响应。</mark>

---

## Practical Applications & Use Cases | <mark>实际应用和用例</mark>

The routing pattern is a critical control mechanism in the design of adaptive agentic systems, enabling them to dynamically alter their execution path in response to variable inputs and internal states. Its utility spans multiple domains by providing a necessary layer of conditional logic.

<mark>路由模式是自适应智能体系统设计中的关键控制机制，让系统能够根据可变输入和内部状态动态改变执行路径。通过提供必要的条件逻辑层，它在多个领域都发挥着重要作用。以下是一些实际应用场景：</mark>

**1. Human-Computer Interaction:** In human-computer interaction, such as with virtual assistants or AI-driven tutors, routing is employed to interpret user intent. An initial analysis of a natural language query determines the most appropriate subsequent action, whether it is invoking a specific information retrieval tool, escalating to a human operator, or selecting the next module in a curriculum based on user performance. This allows the system to move beyond linear dialogue flows and respond contextually.

<mark><strong>1. 人机交互：</strong>在虚拟助手或 AI 驱动的导师等人机交互场景中，路由用于解析用户意图。系统首先分析自然语言查询，确定最合适的后续行动——是调用特定的信息检索工具、转接人工操作员，还是根据用户表现选择课程的下一个模块。这让系统能够超越线性的对话流程，根据上下文灵活响应。</mark>

**2. Automated Data Processing:** Within automated data and document processing pipelines, routing serves as a classification and distribution function. Incoming data, such as emails, support tickets, or API payloads, is analyzed based on content, metadata, or format. The system then directs each item to a corresponding workflow, such as a sales lead ingestion process, a specific data transformation function for JSON or CSV formats, or an urgent issue escalation path.

<mark><strong>2. 自动化数据处理：</strong>在自动化数据和文档处理管道中，路由承担着分类和分发的职责。系统会根据内容、元数据或格式，对传入的数据（如电子邮件、支持工单或 API 负载）进行分析，然后将每个项目引导到相应的工作流——例如销售线索的录入流程、针对 JSON 或 CSV 格式的数据转换功能，或是紧急问题的上报通道。</mark>

**3. Multi-Agent Systems:** In complex systems involving multiple specialized tools or agents, routing acts as a high-level dispatcher. A research system composed of distinct agents for searching, summarizing, and analyzing information would use a router to assign tasks to the most suitable agent based on the current objective. Similarly, an AI coding assistant uses routing to identify the programming language and user's intent—to debug, explain, or translate—before passing a code snippet to the correct specialized tool.

<mark><strong>3. 多智能体系统：</strong>在涉及多个专门工具或智能体的复杂系统中，路由作为高级调度器。由用于搜索、总结和分析信息的不同智能体组成的研究系统，会使用路由器根据当前目标将任务分配给最合适的智能体。同样，AI 编程助手也会利用路由来识别编程语言和用户意图——是调试、解释还是翻译——然后再将代码片段传递给正确的专业工具。</mark>

Ultimately, routing provides the capacity for logical arbitration that is essential for creating functionally diverse and context-aware systems. It transforms an agent from a static executor of pre-defined sequences into a dynamic system that can make decisions about the most effective method for accomplishing a task under changing conditions.

<mark>归根结底，路由提供了智能决策的能力，这对于创建功能多样、能感知上下文的系统至关重要。它将智能体从执行预定序列的静态系统，转变为能够在变化条件下自主决策、以最高效方式完成任务的动态系统。</mark>

---

## Hands-On Code Example (LangChain) | <mark>实践代码示例（LangChain）</mark>

Implementing routing in code involves defining the possible paths and the logic that decides which path to take. Frameworks like LangChain and LangGraph provide specific components and structures for this. LangGraph's state-based graph structure is particularly intuitive for visualizing and implementing routing logic.

<mark>在代码中实现路由，需要定义可能的路径以及决定路径选择的逻辑。LangChain 和 LangGraph 等框架为此提供了专门的组件和结构。LangGraph 基于状态的图结构在可视化和实现路由逻辑方面尤为直观。</mark>

This code demonstrates a simple agent-like system using LangChain and Google's Generative AI. It sets up a "coordinator" that routes user requests to different simulated "sub-agent" handlers based on the request's intent (booking, information, or unclear). The system uses a language model to classify the request and then delegates it to the appropriate handler function, simulating a basic delegation pattern often seen in multi-agent architectures.

<mark>此代码演示了使用 LangChain 与 Google 生成式 AI 构建的简单类智能体系统。它设置了一个「协调器」，根据请求意图（预订、信息查询或意图不明）将用户请求路由到不同的模拟「子智能体」处理函数。系统利用语言模型对请求进行分类，然后将其委派给相应的处理函数，这模拟了多智能体架构中常见的基础委派模式。</mark>

First, ensure you have the necessary libraries installed:

<mark>首先，确保你安装了必要的库：</mark>

```bash path=null start=null
pip install langchain langgraph google-cloud-aiplatform langchain-google-genai google-adk deprecated pydantic
```

You will also need to set up your environment with your API key for the language model you choose (e.g., OpenAI, Google Gemini, Anthropic).

<mark>你还需要在环境中设置所选语言模型（如 OpenAI、Google Gemini、Anthropic）的 API 密钥。</mark>

```python path=null start=null
# Copyright (c) 2025 Marco Fago
# https://www.linkedin.com/in/marco-fago/
#
# This code is licensed under the MIT License.
# See the LICENSE file in the repository for the full license text.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch

# --- Configuration ---
# Ensure your API key environment variable is set (e.g., GOOGLE_API_KEY)
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    print(f"Language model initialized: {llm.model}")
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None

# --- Define Simulated Sub-Agent Handlers ---

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

# --- Define Coordinator Router Chain ---
coordinator_router_prompt = ChatPromptTemplate.from_messages([
    ("system", """Analyze the user's request and determine which specialist handler should process it.
    - If the request is related to booking flights or hotels, 
      output 'booker'.
    - For all other general information questions, output 'info'.
    - If the request is unclear or doesn't fit either category, 
      output 'unclear'.
    ONLY output one word: 'booker', 'info', or 'unclear'."""),
    ("user", "{request}")
])

if llm:
    coordinator_router_chain = coordinator_router_prompt | llm | StrOutputParser()

# --- Define the Delegation Logic ---
branches = {
    "booker": RunnablePassthrough.assign(output=lambda x: booking_handler(x['request']['request'])),
    "info": RunnablePassthrough.assign(output=lambda x: info_handler(x['request']['request'])),
    "unclear": RunnablePassthrough.assign(output=lambda x: unclear_handler(x['request']['request'])),
}

# Create the RunnableBranch
delegation_branch = RunnableBranch(
    (lambda x: x['decision'].strip() == 'booker', branches["booker"]),
    (lambda x: x['decision'].strip() == 'info', branches["info"]),
    branches["unclear"] # Default branch
)

# Combine the router chain and delegation branch
coordinator_agent = {
    "decision": coordinator_router_chain,
    "request": RunnablePassthrough()
} | delegation_branch | (lambda x: x['output'])

# --- Example Usage ---
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

As mentioned, this Python code constructs a simple agent-like system using the LangChain library and Google's Generative AI model, specifically gemini-2.5-flash. In detail, It defines three simulated sub-agent handlers: booking_handler, info_handler, and unclear_handler, each designed to process specific types of requests.

<mark>如前所述，这段 Python 代码使用 LangChain 库和 Google 的 gemini-2.5-flash 生成式 AI 模型构建了一个简单的类智能体系统。详细来说，它定义了三个模拟的子智能体处理器：booking_handler、info_handler 和 unclear_handler，分别用于处理特定类型的请求。</mark>

A core component is the coordinator_router_chain, which utilizes a ChatPromptTemplate to instruct the language model to categorize incoming user requests into one of three categories: 'booker', 'info', or 'unclear'. The output of this router chain is then used by a RunnableBranch to delegate the original request to the corresponding handler function. The RunnableBranch checks the decision from the language model and directs the request data to either the booking_handler, info_handler, or unclear_handler. The coordinator_agent combines these components, first routing the request for a decision and then passing the request to the chosen handler. The final output is extracted from the handler's response.

<mark>核心组件 coordinator_router_chain 利用 ChatPromptTemplate 指示语言模型将传入用户请求分类为三个类别之一：'booker'、'info' 或 'unclear'。随后 RunnableBranch 使用路由链的输出将原始请求委派给相应的处理函数。RunnableBranch 检查语言模型的决策，并将请求数据引导至 booking_handler、info_handler 或 unclear_handler。coordinator_agent 组合了这些组件，首先路由请求以获得决策，然后将请求传递给选中的处理器。最终输出从处理器的响应中提取。</mark>

The main function demonstrates the system's usage with three example requests, showcasing how different inputs are routed and processed by the simulated agents. Error handling for language model initialization is included to ensure robustness. The code structure mimics a basic multi-agent framework where a central coordinator delegates tasks to specialized agents based on intent.

<mark>main 函数用三个示例请求演示了系统的使用，展示了不同输入如何被路由并由模拟智能体处理。包含了语言模型初始化的错误处理以确保健壮性。代码结构模拟了一个基础的多智能体框架，其中中央协调器根据意图将任务委派给专门的智能体。</mark>

---

## Hands-On Code Example (Google ADK) | <mark>实践代码示例（Google ADK）</mark>

The Agent Development Kit (ADK) is a framework for engineering agentic systems, providing a structured environment for defining an agent's capabilities and behaviours. In contrast to architectures based on explicit computational graphs, routing within the ADK paradigm is typically implemented by defining a discrete set of "tools" that represent the agent's functions. The selection of the appropriate tool in response to a user query is managed by the framework's internal logic, which leverages an underlying model to match user intent to the correct functional handler.

<mark>Google Agent Developer Kit（Google ADK）是用于工程化智能体系统的框架，为定义智能体的能力与行为提供结构化环境。与基于显式计算图的架构相比，ADK 范式中的路由通常通过定义代表智能体功能的离散「工具」集合来实现。框架的内部逻辑会负责选择合适的工具来响应用户查询，它利用底层模型将用户意图与正确的功能处理器进行匹配。</mark>

This Python code demonstrates an example of an Agent Development Kit (ADK) application using Google's ADK library. It sets up a "Coordinator" agent that routes user requests to specialized sub-agents ("Booker" for bookings and "Info" for general information) based on defined instructions. The sub-agents then use specific tools to simulate handling the requests, showcasing a basic delegation pattern within an agent system.

<mark>这段 Python 代码演示了一个使用 Google ADK 库的应用示例。它设置了一个「协调器」智能体，根据预设指令，将用户请求路由到专门的子智能体（「Booker」负责预订，「Info」负责一般信息）。这些子智能体随后会使用特定工具来模拟处理请求，展示了智能体系统内一种基础的委派模式。</mark>

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

# --- Define Tool Functions ---
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

# --- Create Tools from Functions ---
booking_tool = FunctionTool(booking_handler)
info_tool = FunctionTool(info_handler)

# Define specialized sub-agents
booking_agent = Agent(
    name="Booker",
    model="gemini-2.0-flash",
    description="A specialized agent that handles all flight and hotel booking requests.",
    tools=[booking_tool]
)

info_agent = Agent(
    name="Info",
    model="gemini-2.0-flash",
    description="A specialized agent that provides general information and answers user questions.",
    tools=[info_tool]
)

# Define the parent agent with explicit delegation instructions
coordinator = Agent(
    name="Coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "You are the main coordinator. Your only task is to analyze"
        " incoming user requests "
        "and delegate them to the appropriate specialist agent. "
        "Do not try to answer the user directly.\n"
        "- For any requests related to booking flights or hotels,"
        " delegate to the 'Booker' agent.\n"
        "- For all other general information questions, delegate to the 'Info' agent."
    ),
    description="A coordinator that routes user requests to the correct specialist agent.",
    # The presence of sub_agents enables LLM-driven delegation (Auto-Flow) by default.
    sub_agents=[booking_agent, info_agent]
)

# --- Execution Logic ---
async def run_coordinator(runner: InMemoryRunner, request: str):
    """Runs the coordinator agent with a given request and delegates."""
    print(f"\n--- Running Coordinator with request: '{request}' ---")
    final_result = ""
    try:
        user_id = "user_123"
        session_id = str(uuid.uuid4())
        await runner.session_service.create_session(
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
                if hasattr(event.content, 'text') and event.content.text:
                    final_result = event.content.text
                elif event.content.parts:
                    text_parts = [part.text for part in event.content.parts if part.text]
                    final_result = "".join(text_parts)
                break

        print(f"Coordinator Final Response: {final_result}")
        return final_result
    except Exception as e:
        print(f"An error occurred while processing your request: {e}")
        return f"An error occurred while processing your request: {e}"

async def main():
    """Main function to run the ADK example."""
    print("--- Google ADK Routing Example (ADK Auto-Flow Style) ---")
    print("Note: This requires Google ADK installed and authenticated.")

    runner = InMemoryRunner(coordinator)
    
    # Example Usage
    result_a = await run_coordinator(runner, "Book me a hotel in Paris.")
    print(f"Final Output A: {result_a}")
    
    result_b = await run_coordinator(runner, "What is the highest mountain in the world?")
    print(f"Final Output B: {result_b}")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    await main()
```

This script consists of a main Coordinator agent and two specialized sub_agents: Booker and Info. Each specialized agent is equipped with a FunctionTool that wraps a Python function simulating an action. The booking_handler function simulates handling flight and hotel bookings, while the info_handler function simulates retrieving general information. The unclear_handler is included as a fallback for requests the coordinator cannot delegate, although the current coordinator logic doesn't explicitly use it for delegation failure in the main run_coordinator function.

<mark>该脚本包含一个主要的 Coordinator 智能体和两个专业的子智能体：Booker 和 Info。每个专业智能体都配备了一个 FunctionTool，该工具封装了一个模拟具体操作的 Python 函数。booking_handler 函数模拟处理机票和酒店预订，而 info_handler 函数模拟检索一般信息。unclear_handler 作为协调器无法委派请求时的后备方案，尽管当前协调器逻辑在主 run_coordinator 函数中并未显式地将其用于委派失败。</mark>

The Coordinator agent's primary role, as defined in its instruction, is to analyze incoming user messages and delegate them to either the Booker or Info agent. This delegation is handled automatically by the ADK's Auto-Flow mechanism because the Coordinator has sub_agents defined. The run_coordinator function sets up an InMemoryRunner, creates a user and session ID, and then uses the runner to process the user's request through the coordinator agent. The runner.run method processes the request and yields events, and the code extracts the final response text from the event.content.

<mark>Coordinator 智能体的主要职责（如其 instruction 中所定义）是分析传入用户消息并将其委派给 Booker 或 Info。由于 Coordinator 定义了 sub_agents，ADK 的自动流（Auto-Flow）机制会自动处理委派逻辑。run_coordinator 函数设置了一个 InMemoryRunner，创建用户和会话 ID，然后通过运行器处理用户请求。runner.run 方法处理请求并产生事件，代码从 event.content 中提取最终的响应文本。</mark>

The main function demonstrates the system's usage by running the coordinator with different requests, showcasing how it delegates booking requests to the Booker and information requests to the Info agent.

<mark>main 函数通过不同的请求展示了系统的使用，演示了协调器如何将预订请求委派给 Booker，将信息请求委派给 Info 智能体。</mark>

![Routing Pattern Diagram](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdwM05fNyWY-P9mUV8W3wxnGZux5Y1GghdTm9kiWCTy_gGxycR4zA12f2YmwWSUxpvrwNh7O5l3nwwYxyRXSXhXP8-KbSE_zRV-qsH-fk9ilk5vqLSU2_Pq39N7y0XNmg?key=7vJcEhu1QiId0k62gPNSMw)

**Fig.1:** Router pattern, using an LLM as a Router

<mark><strong>图 1：</strong>路由器模式：使用 LLM 作为路由器。</mark>

---

## At a Glance | <mark>要点速览</mark>

**What:** Agentic systems must often respond to a wide variety of inputs and situations that cannot be handled by a single, linear process. A simple sequential workflow lacks the ability to make decisions based on context. Without a mechanism to choose the correct tool or sub-process for a specific task, the system remains rigid and non-adaptive. This limitation makes it difficult to build sophisticated applications that can manage the complexity and variability of real-world user requests.

<mark><strong>问题所在：</strong>智能体系统往往需要应对各种各样的输入和情境，单一的线性流程无法满足这一需求。简单的顺序工作流缺乏基于上下文做出决策的能力。如果没有为特定任务选择正确工具或子流程的机制，系统就会显得僵化且缺乏适应性。这种限制使得我们很难构建出能够应对真实世界用户请求的复杂性和多变性的成熟应用程序。</mark>

**Why:** The Routing pattern provides a standardized solution by introducing conditional logic into an agent's operational framework. It enables the system to first analyze an incoming query to determine its intent or nature. Based on this analysis, the agent dynamically directs the flow of control to the most appropriate specialized tool, function, or sub-agent. This decision can be driven by various methods, including prompting LLMs, applying predefined rules, or using embedding-based semantic similarity. Ultimately, routing transforms a static, predetermined execution path into a flexible and context-aware workflow capable of selecting the best possible action.

<mark><strong>解决之道：</strong>路由模式通过在智能体的操作框架中引入条件逻辑，提供了一套标准化的解法。系统首先分析传入的查询以确定其意图或性质；基于此分析，智能体动态地将控制流引导至最合适的专门工具、功能或子智能体。这个决策可以由多种方法驱动，包括提示 LLM、应用预定义规则或使用基于嵌入的语义相似度。最终，路由将一个静态、预定的执行路径，转变为一个灵活且能感知上下文的工作流，能够选择最佳的行动方案。</mark>

**Rule of Thumb:** Use the Routing pattern when an agent must decide between multiple distinct workflows, tools, or sub-agents based on the user's input or the current state. It is essential for applications that need to triage or classify incoming requests to handle different types of tasks, such as a customer support bot distinguishing between sales inquiries, technical support, and account management questions.

<mark><strong>经验法则：</strong>当智能体必须基于用户输入或当前状态在多个不同的工作流、工具或子智能体之间做决定时，使用路由模式。对于需要对传入请求进行分类或分流以处理不同类型任务的应用程序来说，这是必不可少的，例如一个需要区分销售咨询、技术支持和账户管理问题的客户支持机器人。</mark>

**Visual summary** | <mark>可视化总结</mark>

---

## Key Takeaways | <mark>核心要点</mark>

Here are some key takeaways:

<mark>以下是本章的核心要点：</mark>

- Routing enables agents to make dynamic decisions about the next step in a workflow based on conditions.

   <mark>路由使智能体能够基于条件对工作流中的下一步做出动态决策。</mark>

- It allows agents to handle diverse inputs and adapt their behavior, moving beyond linear execution.

- <mark>它使智能体能够处理多样化输入并自适应地调整行为，突破线性执行的限制。</mark>

- Routing logic can be implemented using LLMs, rule-based systems, or embedding similarity.

- <mark>路由逻辑可以使用 LLM、基于规则的系统或嵌入相似性来实现。</mark>

- Frameworks like LangGraph and Google ADK provide structured ways to define and manage routing within agent workflows, albeit with different architectural approaches.

- <mark>像 LangGraph 和 Google ADK 这类框架，为在智能体工作流中定义和管理路由提供了结构化的方法，尽管它们的架构取径有所不同。</mark>

---

## Conclusion | <mark>结语</mark>

The Routing pattern is a critical step in building truly dynamic and responsive agentic systems. By implementing routing, we move beyond simple, linear execution flows and empower our agents to make intelligent decisions about how to process information, respond to user input, and utilize available tools or sub-agents.

<mark>路由模式是构建真正动态且响应迅速的智能体系统的关键一步。通过实现路由，我们超越了简单的线性执行流程，赋予智能体智能决策能力——让它们知道如何处理信息、响应用户输入，以及利用可用的工具或子智能体。</mark>

We've seen how routing can be applied in various domains, from customer service chatbots to complex data processing pipelines. The ability to analyze input and conditionally direct the workflow is fundamental to creating agents that can handle the inherent variability of real-world tasks.

<mark>我们已经看到，路由可以应用于从客服聊天机器人到复杂数据处理管道等各个领域。分析输入并有条件地引导工作流的能力，是创建能够应对真实世界任务固有多变性的智能体的根本所在。</mark>

The code examples using LangChain and Google ADK demonstrate two different, yet effective, approaches to implementing routing. LangGraph's graph-based structure provides a visual and explicit way to define states and transitions, making it ideal for complex, multi-step workflows with intricate routing logic. Google ADK, on the other hand, often focuses on defining distinct capabilities (Tools) and relies on the framework's ability to route user requests to the appropriate tool handler, which can be simpler for agents with a well-defined set of discrete actions.

<mark>使用 LangChain 和 Google ADK 的代码示例展示了两种不同但同样有效的路由实现方法。LangGraph 基于图的结构提供了可视化、显式定义状态和转换的方式，非常适合具有复杂路由逻辑的多步工作流。而 Google ADK 则侧重于定义离散的功能（工具），依赖框架将用户请求路由到合适的工具处理程序，对于具有明确离散动作集的智能体来说更为简便。</mark>

Mastering the Routing pattern is essential for building agents that can intelligently navigate different scenarios and provide tailored responses or actions based on context. It's a key component in creating versatile and robust agentic applications.

<mark>掌握路由模式对于构建能够智能应对不同场景、并根据上下文提供定制化响应或行动的智能体至关重要。它是创建多功能、稳健智能体应用的核心组件。</mark>

---

## References | <mark>参考文献</mark>

1. LangGraph Documentation: https://www.langchain.com/
2. Google Agent Developer Kit Documentation: https://google.github.io/adk-docs/
