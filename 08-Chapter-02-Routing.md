# Chapter 2: Routing | <mark>第二章：路由</mark>

---

## Routing Pattern Overview | <mark>路由模式概述</mark>

While sequential processing via prompt chaining is a foundational technique for executing deterministic, linear workflows with language models, its applicability is limited in scenarios requiring adaptive responses. Real-world agentic systems must often arbitrate between multiple potential actions based on contingent factors, such as the state of the environment, user input, or the outcome of a preceding operation. This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing.

<mark>虽然通过提示链的顺序处理是使用语言模型执行确定性、线性工作流的基础技术，但其在需要自适应响应的场景中适用性有限。现实世界的智能体系统常需基于情境因素（如环境状态、用户输入或前一操作结果）在多个潜在行动之间做出取舍。这种动态决策能力会将控制流导向不同的专门功能、工具或子流程，并通过称为「路由」的机制来实现。</mark>

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.

<mark>路由在智能体的操作框架中引入条件逻辑，使系统从固定执行路径转向一种模型：智能体根据特定标准进行动态评估，并在一组可能的后续行动中进行选择。由此，系统行为更灵活，也更具上下文感知能力。</mark>

For instance, an agent designed for customer inquiries, when equipped with a routing function, can first classify an incoming query to determine the user's intent. Based on this classification, it can then direct the query to a specialized agent for direct question-answering, a database retrieval tool for account information, or an escalation procedure for complex issues, rather than defaulting to a single, predetermined response pathway. Therefore, a more sophisticated agent using routing could:

<mark>例如，为客户咨询设计的智能体，当配备路由功能时，可以首先对传入查询进行分类以确定用户意图。基于此分类，它可将查询导向专门智能体进行直接问答、用于账户信息的数据库检索工具，或面向复杂问题的升级流程，而非默认采用单一、预设的响应路径。因此，采用路由的更复杂智能体可以：</mark>

1. Analyze the user's query.

1. <mark>分析用户的查询。</mark>

2. **Route** the query based on its *intent*:

2. <mark><strong>路由</strong>基于其<em>意图</em>的查询：</mark>

   - If the intent is "check order status", route to a sub-agent or tool chain that interacts with the order database.

   <mark>- 若意图为「检查订单状态」，则路由至与订单数据库交互的子智能体或工具链。</mark>

   - If the intent is "product information", route to a sub-agent or chain that searches the product catalog.

   <mark>- 若意图为「产品信息」，则路由至搜索产品目录的子智能体或链。</mark>

   - If the intent is "technical support", route to a different chain that accesses troubleshooting guides or escalates to a human.

   <mark>- 若意图为「技术支持」，则路由至访问故障排除指南或升级到人工的不同链。</mark>

   - If the intent is unclear, route to a clarification sub-agent or prompt chain.

   <mark>- 如果意图不清楚，路由到澄清子智能体或提示链。</mark>

The core component of the Routing pattern is a mechanism that performs the evaluation and directs the flow. This mechanism can be implemented in several ways:

<mark>路由模式的核心组件是执行评估和引导流的机制。这种机制可以通过几种方式实现：</mark>

### Routing Implementation Methods | <mark>路由实现方法</mark>

**LLM-based Routing:** The language model itself can be prompted to analyze the input and output a specific identifier or instruction that indicates the next step or destination. For example, a prompt might ask the LLM to "Analyze the following user query and output only the category: 'Order Status', 'Product Info', 'Technical Support', or 'Other'." The agentic system then reads this output and directs the workflow accordingly.

<mark><strong>基于 LLM 的路由：</strong>可通过提示让语言模型分析输入，并输出指示下一步或目标的标识或指令。例如，可提示 LLM：「分析以下用户查询，并仅输出类别：『订单状态』、『产品信息』、『技术支持』或『其他』。」随后，智能体系统读取该输出并相应引导工作流。</mark>

**Embedding-based Routing:** The input query can be converted into a vector embedding (see RAG, Chapter 14). This embedding is then compared to embeddings representing different routes or capabilities. The query is routed to the route whose embedding is most similar. This is useful for semantic routing, where the decision is based on the meaning of the input rather than just keywords.

<mark><strong>基于嵌入的路由：</strong>输入查询可以转换为向量嵌入（参见 RAG，第 14 章）。然后将此嵌入与代表不同路线或能力的嵌入进行比较。查询被路由到嵌入最相似的路线。这对语义路由很有用，其中决策基于输入的含义而不仅仅是关键字。</mark>

**Rule-based Routing:** This involves using predefined rules or logic (e.g., if-else statements, switch cases) based on keywords, patterns, or structured data extracted from the input. This can be faster and more deterministic than LLM-based routing, but is less flexible for handling nuanced or novel inputs.

<mark><strong>基于规则的路由：</strong>这涉及使用基于关键字、模式或从输入提取的结构化数据的预定义规则或逻辑（如 if-else 语句、switch 情况）。这可以比基于 LLM 的路由更快、更确定，但在处理细致入微或新颖输入方面灵活性较差。</mark>

**Machine Learning Model-Based Routing:** It employs a discriminative model, such as a classifier, that has been specifically trained on a small corpus of labeled data to perform a routing task. While it shares conceptual similarities with embedding-based methods, its key characteristic is the supervised fine-tuning process, which adjusts the model's parameters to create a specialized routing function.

<mark><strong>基于机器学习模型的路由：</strong>它采用判别模型（如分类器），专门在标记数据的小型语料库上训练以执行路由任务。虽然它与基于嵌入的方法在概念上相似，但其关键特征是监督微调过程，该过程调整模型参数以创建专门的路由功能。</mark>

---

## Practical Applications & Use Cases | <mark>实际应用和用例</mark>

The routing pattern is a critical control mechanism in the design of adaptive agentic systems, enabling them to dynamically alter their execution path in response to variable inputs and internal states. Its utility spans multiple domains by providing a necessary layer of conditional logic.

<mark>路由模式是自适应智能体系统设计中的关键控制机制，使它们能够根据可变输入和内部状态动态改变执行路径。通过提供必要的条件逻辑层，其效用跨越多个领域。</mark>

### Human-Computer Interaction | <mark>人机交互</mark>

In human-computer interaction, such as with virtual assistants or AI-driven tutors, routing is employed to interpret user intent. An initial analysis of a natural language query determines the most appropriate subsequent action, whether it is invoking a specific information retrieval tool, escalating to a human operator, or selecting the next module in a curriculum based on user performance.

<mark>在人机交互中，如虚拟助手或 AI 驱动的导师，路由用于解释用户意图。对自然语言查询的初始分析确定最合适的后续行动，无论是调用特定的信息检索工具、升级到人工操作员，还是基于用户表现选择课程中的下一个模块。</mark>

### Automated Data Processing | <mark>自动化数据处理</mark>

Within automated data and document processing pipelines, routing serves as a classification and distribution function. Incoming data, such as emails, support tickets, or API payloads, is analyzed based on content, metadata, or format. The system then directs each item to a corresponding workflow.

<mark>在自动化数据和文档处理管道中，路由作为分类和分发功能。传入数据（如电子邮件、支持工单或 API 负载）根据内容、元数据或格式进行分析。系统然后将每个项目引导到相应的工作流。</mark>

### Multi-Agent Systems | <mark>多智能体系统</mark>

In complex systems involving multiple specialized tools or agents, routing acts as a high-level dispatcher. A research system composed of distinct agents for searching, summarizing, and analyzing information would use a router to assign tasks to the most suitable agent based on the current objective.

<mark>在涉及多个专门工具或智能体的复杂系统中，路由作为高级调度器。由用于搜索、总结和分析信息的不同智能体组成的研究系统将使用路由器根据当前目标将任务分配给最合适的智能体。</mark>

---

## Hands-On Code Example (LangChain) | <mark>实践代码示例 (LangChain)</mark>

Implementing routing in code involves defining the possible paths and the logic that decides which path to take. Frameworks like LangChain and LangGraph provide specific components and structures for this.

<mark>在代码中实现路由涉及定义可能的路径和决定选择哪条路径的逻辑。LangChain 和 LangGraph 等框架为此提供特定的组件和结构。</mark>

This code demonstrates a simple agent-like system using LangChain and Google's Generative AI. It sets up a "coordinator" that routes user requests to different simulated "sub-agent" handlers based on the request's intent.

<mark>此代码演示了使用 LangChain 与 Google 生成式 AI 的简单类智能体系统。它设置了一个「协调器」，并依据请求意图将用户请求路由到不同的模拟「子智能体」处理函数。</mark>

First, ensure you have the necessary libraries installed:

<mark>首先，确保您安装了必要的库：</mark>

```bash path=null start=null
pip install langchain langgraph google-cloud-aiplatform langchain-google-genai google-adk deprecated pydantic
```

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

This Python code constructs a simple agent-like system that demonstrates the routing pattern. The coordinator_router_chain utilizes a ChatPromptTemplate to instruct the language model to categorize incoming user requests. The RunnableBranch then uses this decision to delegate the original request to the corresponding handler function.

<mark>这段 Python 代码构建了一个演示路由模式的简单类智能体系统。coordinator_router_chain 利用 ChatPromptTemplate 指示语言模型对传入用户请求进行分类；随后 RunnableBranch 使用该决策将原始请求委托给相应处理函数。</mark>

---

## Hands-On Code Example (Google ADK) | <mark>实践代码示例（Google ADK）</mark>

The Agent Development Kit (ADK) is a framework for engineering agentic systems, providing a structured environment for defining an agent's capabilities and behaviours. In contrast to architectures based on explicit computational graphs, routing within the ADK paradigm is typically implemented by defining a discrete set of "tools" that represent the agent's functions.

<mark>Google Agent Developer Kit（Google ADK）是用于工程化智能体系统的框架，为定义智能体的能力与行为提供结构化环境。与基于显式计算图的架构相比，ADK 范式中的路由通常通过定义代表智能体功能的离散「工具」集合来实现。</mark>

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

This script demonstrates the Google ADK approach to routing, where a Coordinator agent automatically delegates tasks to specialized sub-agents based on the defined instructions and the Auto-Flow mechanism.

<mark>此脚本演示了 Google ADK 的路由方法：协调器智能体依据已定义的指令与 Auto-Flow 机制，自动将任务委托给专门的子智能体。</mark>

![Routing Pattern Diagram](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdwM05fNyWY-P9mUV8W3wxnGZux5Y1GghdTm9kiWCTy_gGxycR4zA12f2YmwWSUxpvrwNh7O5l3nwwYxyRXSXhXP8-KbSE_zRV-qsH-fk9ilk5vqLSU2_Pq39N7y0XNmg?key=7vJcEhu1QiId0k62gPNSMw)

**Fig.1:** Router pattern, using an LLM as a Router

<mark><strong>图 1：</strong>路由器模式：使用 LLM 作为路由器。</mark>

---

## At a Glance | <mark>一览</mark>

**What:** Agentic systems must often respond to a wide variety of inputs and situations that cannot be handled by a single, linear process. A simple sequential workflow lacks the ability to make decisions based on context. Without a mechanism to choose the correct tool or sub-process for a specific task, the system remains rigid and non-adaptive.

<mark><strong>什么：</strong>智能体系统往往需要应对多样输入与情境，无法由单一线性流程覆盖。简单的顺序工作流缺乏基于上下文的决策能力；若无选择适当工具或子流程的机制，系统将保持僵化且缺乏适应性。</mark>

**Why:** The Routing pattern provides a standardized solution by introducing conditional logic into an agent's operational framework. It enables the system to first analyze an incoming query to determine its intent or nature. Based on this analysis, the agent dynamically directs the flow of control to the most appropriate specialized tool, function, or sub-agent.

<mark><strong>为什么：</strong>路由模式通过在智能体的操作框架中引入条件逻辑，提供标准化解法。系统先分析传入查询以确定其意图或性质；在此基础上，智能体将控制流动态引导至最合适的专门工具、功能或子智能体。</mark>

**Rule of Thumb:** Use the Routing pattern when an agent must decide between multiple distinct workflows, tools, or sub-agents based on the user's input or the current state. It is essential for applications that need to triage or classify incoming requests to handle different types of tasks.

<mark><strong>经验法则：</strong>当智能体必须基于用户输入或当前状态在多个不同的工作流、工具或子智能体之间做决定时，使用路由模式。对于需要对传入请求进行分类或分流以处理不同类型任务的应用程序来说，这是必不可少的。</mark>

---

## Key Takeaways | <mark>关键要点</mark>

- Routing enables agents to make dynamic decisions about the next step in a workflow based on conditions.

- <mark>路由使智能体能够基于条件对工作流中的下一步做出动态决策。</mark>

- It allows agents to handle diverse inputs and adapt their behavior, moving beyond linear execution.

- <mark>它使智能体能处理多样化输入并自适应地调整行为，突破线性执行。</mark>

- Routing logic can be implemented using LLMs, rule-based systems, or embedding similarity.

- <mark>路由逻辑可用 LLM、规则系统或嵌入相似性实现。</mark>

- Frameworks like LangGraph and Google ADK provide structured ways to define and manage routing within agent workflows, albeit with different architectural approaches.

- <mark>LangGraph 与 Google ADK 等框架提供结构化方式来定义与管理智能体工作流中的路由（架构取径虽异）。</mark>

---

## Conclusion | <mark>结论</mark>

The Routing pattern is a critical step in building truly dynamic and responsive agentic systems. By implementing routing, we move beyond simple, linear execution flows and empower our agents to make intelligent decisions about how to process information, respond to user input, and utilize available tools or sub-agents.

<mark>路由模式是构建真正动态、响应式智能体系统的关键环节。通过实现路由，我们超越简单的线性执行流，赋予智能体关于信息处理、用户响应与工具/子智能体利用的智能决策能力。</mark>

We've seen how routing can be applied in various domains, from customer service chatbots to complex data processing pipelines. The ability to analyze input and conditionally direct the workflow is fundamental to creating agents that can handle the inherent variability of real-world tasks.

<mark>我们已见路由在多领域中的应用，从客服聊天机器人到复杂数据处理管道。分析输入并有条件地引导工作流的能力，是构建能应对真实任务多变性的智能体之基础。</mark>

Mastering the Routing pattern is essential for building agents that can intelligently navigate different scenarios and provide tailored responses or actions based on context. It's a key component in creating versatile and robust agentic applications.

<mark>掌握路由模式，对于构建能在不同场景中智能导航并基于上下文提供定制响应/行动的智能体至关重要。它是打造多功能、稳健智能体应用的关键组件。</mark>

---

## References | <mark>参考文献</mark>

1. LangGraph Documentation: https://www.langchain.com/
2. Google Agent Developer Kit Documentation: https://google.github.io/adk-docs/

---
