# Chapter 6: Planning | <mark>第六章：规划</mark>

---

Intelligent behavior often involves more than just reacting to the immediate input. It requires foresight, breaking down complex tasks into smaller, manageable steps, and strategizing how to achieve a desired outcome. This is where the Planning pattern comes into play. At its core, planning is the ability for an agent or a system of agents to formulate a sequence of actions to move from an initial state towards a goal state.

<mark>智能行为远不止对眼前输入作出反应。它需要前瞻性，需要把复杂任务拆解为更小且可管理的步骤，并制定实现预期结果的策略。这正是规划模式发挥作用之处。其核心在于：智能体（或智能体系统）能够制定一系列行动，使系统从初始状态迈向目标状态。</mark>

---

## Planning Pattern Overview | <mark>规划模式概览</mark>

In the context of AI, it's helpful to think of a planning agent as a specialist to whom you delegate a complex goal. When you ask it to "organize a team offsite," you are defining the what—the objective and its constraints—but not the how. The agent's core task is to autonomously chart a course to that goal. It must first understand the initial state (e.g., budget, number of participants, desired dates) and the goal state (a successfully booked offsite), and then discover the optimal sequence of actions to connect them. The plan is not known in advance; it is created in response to the request.

<mark>在 AI 的语境下，把规划智能体看作可以委派复杂目标的专家会更容易理解。当你请它「组织团队外出活动」时，你定义了「什么」——目标及其约束条件——但没有定义「如何」。智能体的核心任务是自主规划通往该目标的路径。它必须先理解初始状态（如预算、参与人数、期望日期）和目标状态（成功预订的外出活动），再找出连接二者的最优行动序列。计划不是预先给定的；而是在响应请求时生成的。</mark>

A hallmark of this process is adaptability. An initial plan is merely a starting point, not a rigid script. The agent's real power is its ability to incorporate new information and steer the project around obstacles. For instance, if the preferred venue becomes unavailable or a chosen caterer is fully booked, a capable agent doesn't simply fail. It adapts. It registers the new constraint, re-evaluates its options, and formulates a new plan, perhaps by suggesting alternative venues or dates.

<mark>这个过程的标志是适应性。初始计划只是起点，而非僵化脚本。智能体的真正能力在于吸收新信息、带领项目绕开障碍。例如，若首选场地不可用或餐饮商已被订满，有能力的智能体不会就此失败；而是会适应：记录新的约束，重新评估选项，并制定新计划，例如改换场地或日期。</mark>

However, it is crucial to recognize the trade-off between flexibility and predictability. Dynamic planning is a specific tool, not a universal solution. When a problem's solution is already well-understood and repeatable, constraining the agent to a predetermined, fixed workflow is more effective. This approach limits the agent's autonomy to reduce uncertainty and the risk of unpredictable behavior, guaranteeing a reliable and consistent outcome. Therefore, the decision to use a planning agent versus a simple task-execution agent hinges on a single question: does the "how" need to be discovered, or is it already known?

<mark>不过，必须认识到灵活性与可预测性之间的权衡。动态规划是一种特定工具，而非通用解。对于已被充分理解且可重复的问题，将智能体约束在预设的固定流程中更有效。这样可以限制自主性，从而降低不确定性与不可预测行为的风险，保证结果可靠且一致。因此，是否采用规划智能体而非简单的任务执行智能体，关键在于一问：「如何做」是否需要探索，抑或已经明确？</mark>

---

## Practical Applications & Use Cases | <mark>实际应用和用例</mark>

The Planning pattern is a core computational process in autonomous systems, enabling an agent to synthesize a sequence of actions to achieve a specified goal, particularly within dynamic or complex environments. This process transforms a high-level objective into a structured plan composed of discrete, executable steps.

<mark>规划模式是自主系统中的核心计算过程，使智能体能够综合一系列行动来实现指定目标，特别是在动态或复杂环境中。这个过程将高级目标转换为由离散、可执行步骤组成的结构化计划。</mark>

In domains such as procedural task automation, planning is used to orchestrate complex workflows. For example, a business process like onboarding a new employee can be decomposed into a directed sequence of sub-tasks, such as creating system accounts, assigning training modules, and coordinating with different departments. The agent generates a plan to execute these steps in a logical order, invoking necessary tools or interacting with various systems to manage dependencies.

<mark>在流程自动化等领域，规划用于编排复杂工作流。例如，新员工入职这样的业务流程可以分解成一系列有序的子任务，如创建系统账户、分配培训模块、与各部门协调。智能体会生成计划，并按逻辑顺序执行这些步骤，调用必要的工具或与各类系统交互以管理依赖关系。</mark>

Within robotics and autonomous navigation, planning is fundamental for state-space traversal. A system, whether a physical robot or a virtual entity, must generate a path or sequence of actions to transition from an initial state to a goal state. This involves optimizing for metrics such as time or energy consumption while adhering to environmental constraints, like avoiding obstacles or following traffic regulations.

<mark>在机器人和自主导航中，规划是状态空间遍历的基础。系统，无论是物理机器人还是虚拟实体，必须生成路径或行动序列以从初始状态转换到目标状态。这涉及优化时间或能源消耗等指标，同时遵守环境约束，如避开障碍物或遵循交通规则。</mark>

This pattern is also critical for structured information synthesis. When tasked with generating a complex output like a research report, an agent can formulate a plan that includes distinct phases for information gathering, data summarization, content structuring, and iterative refinement. Similarly, in customer support scenarios involving multi-step problem resolution, an agent can create and follow a systematic plan for diagnosis, solution implementation, and escalation.

<mark>这种模式对结构化的信息整合也至关重要。当任务需要生成研究报告等复杂输出时，智能体可以制定包含信息收集、数据归纳、内容结构化与迭代打磨等阶段的计划。同样，在多步骤问题排查与客户支持场景中，智能体可以创建并遵循诊断、实施解决方案与升级处理的系统化流程。</mark>

In essence, the Planning pattern allows an agent to move beyond simple, reactive actions to goal-oriented behavior. It provides the logical framework necessary to solve problems that require a coherent sequence of interdependent operations.

<mark>本质上，规划模式允许智能体超越简单的反应式行动，转向目标导向的行为。它提供了解决需要一系列相互依赖操作的问题所必需的逻辑框架。</mark>

---

## Hands-on code (Crew AI) | <mark>使用 CrewAI 的实战代码</mark>

The following section will demonstrate an implementation of the Planner pattern using the Crew AI framework. This pattern involves an agent that first formulates a multi-step plan to address a complex query and then executes that plan sequentially.

<mark>以下部分演示如何使用 CrewAI 框架实现规划模式。该模式要求智能体先制定多步计划以应对复杂问题，再按顺序执行。</mark>

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Load environment variables from .env file for security
load_dotenv()

# 1. Explicitly define the language model for clarity
llm = ChatOpenAI(model="gpt-4-turbo")

# 2. Define a clear and focused agent
planner_writer_agent = Agent(
   role='Article Planner and Writer',
   goal='Plan and then write a concise, engaging summary on a specified topic.',
   backstory=(
       'You are an expert technical writer and content strategist. '
       'Your strength lies in creating a clear, actionable plan before writing, '
       'ensuring the final summary is both informative and easy to digest.'
   ),
   verbose=True,
   allow_delegation=False,
   llm=llm # Assign the specific LLM to the agent
)

# 3. Define a task with a more structured and specific expected output
topic = "The importance of Reinforcement Learning in AI"
high_level_task = Task(
   description=(
       f"1. Create a bullet-point plan for a summary on the topic: '{topic}'.\n"
       f"2. Write the summary based on your plan, keeping it around 200 words."
   ),
   expected_output=(
       "A final report containing two distinct sections:\n\n"
       "### Plan\n"
       "- A bulleted list outlining the main points of the summary.\n\n"
       "### Summary\n"
       "- A concise and well-structured summary of the topic."
   ),
   agent=planner_writer_agent,
)

# Create the crew with a clear process
crew = Crew(
   agents=[planner_writer_agent],
   tasks=[high_level_task],
   process=Process.sequential,
)

# Execute the task
print("## Running the planning and writing task ##")
result = crew.kickoff()

print("\n\n---\n## Task Result ##\n---")
print(result)
```

This code uses the CrewAI library to create an AI agent that plans and writes a summary on a given topic. It starts by importing necessary libraries, including Crew.ai and langchain_openai, and loading environment variables from a .env file. A ChatOpenAI language model is explicitly defined for use with the agent. An Agent named planner_writer_agent is created with a specific role and goal: to plan and then write a concise summary. The agent's backstory emphasizes its expertise in planning and technical writing. A Task is defined with a clear description to first create a plan and then write a summary on the topic "The importance of Reinforcement Learning in AI", with a specific format for the expected output. A Crew is assembled with the agent and task, set to process them sequentially. Finally, the crew.kickoff() method is called to execute the defined task and the result is printed.

<mark>此代码使用 <code>CrewAI</code> 库创建一个在给定主题上进行规划并撰写摘要的 AI 智能体。它先导入必要的库，包括 <code>crewai</code> 与 <code>langchain_openai</code>，并从 <code>.env</code> 文件加载环境变量。随后显式指定用于该智能体的 <code>ChatOpenAI</code> 语言模型。接着创建名为 <code>planner_writer_agent</code> 的智能体，角色与目标明确：先规划，再撰写一篇简洁的摘要。其背景强调在规划与技术写作方面的专长。随后定义任务：先生成计划，再就「强化学习在 AI 中的重要性」撰写摘要，并对期望输出格式作出具体要求。最后组建包含该智能体与任务的 Crew，设置为顺序处理，并调用 <code>crew.kickoff()</code> 执行任务并打印结果。</mark>

---

## Google DeepResearch | <mark>Google DeepResearch</mark>

Google Gemini DeepResearch (see Fig.1) is an agent-based system designed for autonomous information retrieval and synthesis. It functions through a multi-step agentic pipeline that dynamically and iteratively queries Google Search to systematically explore complex topics. The system is engineered to process a large corpus of web-based sources, evaluate the collected data for relevance and knowledge gaps, and perform subsequent searches to address them. The final output consolidates the vetted information into a structured, multi-page summary with citations to the original sources.

<mark>Google Gemini DeepResearch（见图 1）是一个面向自主信息检索与整合的智能体系统。它通过多步智能体管道运行，动态、迭代地查询 Google Search，系统性地探索复杂主题。系统能够处理海量的网络来源，评估所收集数据的相关性与知识缺口，并执行后续搜索加以弥补。最终输出不是简单拼接，而是将经核验的信息整合为带引用的结构化多页摘要。</mark>

Expanding on this, the system's operation is not a single query-response event but a managed, long-running process. It begins by deconstructing a user's prompt into a multi-point research plan (see Fig. 1), which is then presented to the user for review and modification. This allows for a collaborative shaping of the research trajectory before execution. Once the plan is approved, the agentic pipeline initiates its iterative search-and-analysis loop. This involves more than just executing a series of predefined searches; the agent dynamically formulates and refines its queries based on the information it gathers, actively identifying knowledge gaps, corroborating data points, and resolving discrepancies.

<mark>进一步来说，系统并非一次性的问答事件，而是受控的、长时运行的过程。它会先把用户的提示拆解成多点研究计划（见图 1），再呈现给用户审阅与修改，以便在执行前协同确认研究路径。一旦计划获批，智能体管道便启动迭代的搜索—分析循环。这不仅仅是执行一串预设搜索；智能体会依据收集到的信息动态制定与优化查询，主动识别知识缺口、佐证关键数据点并化解矛盾。</mark>

![Google Deep Research Plan](/images/chapter06_fig1.png)

<mark>图 1：Google Deep Research 智能体生成使用 Google Search 作为工具的执行计划。</mark>

A key architectural component is the system's ability to manage this process asynchronously. This design ensures that the investigation, which can involve analyzing hundreds of sources, is resilient to single-point failures and allows the user to disengage and be notified upon completion. The system can also integrate user-provided documents, combining information from private sources with its web-based research. The final output is not merely a concatenated list of findings but a structured, multi-page report. During the synthesis phase, the model performs a critical evaluation of the collected information, identifying major themes and organizing the content into a coherent narrative with logical sections. The report is designed to be interactive, often including features like an audio overview, charts, and links to the original cited sources, allowing for verification and further exploration by the user. In addition to the synthesized results, the model explicitly returns the full list of sources it searched and consulted (see Fig.2). These are presented as citations, providing complete transparency and direct access to the primary information. This entire process transforms a simple query into a comprehensive, synthesized body of knowledge.

<mark>一个关键的架构要素是系统对整个流程的异步管理能力。这样的设计使得可能涉及数百个来源的研究既能抵御单点故障，也允许用户中途离开，完成后再行通知。系统还能整合用户提供的文档，把私有来源的信息与基于网络的研究相结合。最终输出并非发现列表的简单拼接，而是结构化的多页报告。在整合阶段，模型会对收集的信息进行批判性评估，识别主要主题，并将内容组织成逻辑清晰、连贯的叙述。报告通常具备交互性功能，如音频概览、图表及指向原始引用来源的链接，便于用户验证并进一步探索。除整合后的结论外，模型还会明确返回其搜索与参考的完整来源列表（见图 2），以引用形式呈现，确保完全透明并可直接访问一手信息。整个过程把简单的查询转化为一套全面、整合的知识体系。</mark>

![Deep Research Execution](/images/chapter06_fig2.png)

<mark>图 2：Deep Research 计划执行示例：将 Google Search 作为工具，搜索各类网络来源。</mark>

By mitigating the substantial time and resource investment required for manual data acquisition and synthesis, Gemini DeepResearch provides a more structured and exhaustive method for information discovery. The system's value is particularly evident in complex, multi-faceted research tasks across various domains.

<mark>通过减轻手动数据获取和综合所需的大量时间和资源投入，Gemini DeepResearch 为信息发现提供了更结构化和详尽的方法。该系统的价值在各个领域的复杂、多方面研究任务中特别明显。</mark>

For instance, in competitive analysis, the agent can be directed to systematically gather and collate data on market trends, competitor product specifications, public sentiment from diverse online sources, and marketing strategies. This automated process replaces the laborious task of manually tracking multiple competitors, allowing analysts to focus on higher-order strategic interpretation rather than data collection (see Fig. 3).

<mark>例如，在竞争分析中，智能体可以被指示系统性地收集并整理市场趋势、竞争对手产品规格、来自多种在线渠道的公众舆情与营销策略等数据。该自动化流程取代了手动跟踪多家竞品的繁重工作，使分析师能把精力放在更高阶的战略解读，而非繁琐的数据收集（见图 3）。</mark>

![Deep Research Output](/images/chapter06_fig3.png)

<mark>图 3：Google Deep Research 智能体生成的最终输出——代表我们对通过 Google Search 获取的来源进行分析。</mark>

Similarly, in academic exploration, the system serves as a powerful tool for conducting extensive literature reviews. It can identify and summarize foundational papers, trace the development of concepts across numerous publications, and map out emerging research fronts within a specific field, thereby accelerating the initial and most time-consuming phase of academic inquiry.

<mark>同样，在学术探索中，该系统是进行广泛文献综述的强大工具。它可以识别并归纳基础论文，追踪概念在众多出版物中的演进，并勾勒特定领域的新兴研究前沿，从而加速学术研究中最初且最耗时的阶段。</mark>

The efficiency of this approach stems from the automation of the iterative search-and-filter cycle, which is a core bottleneck in manual research. Comprehensiveness is achieved by the system's capacity to process a larger volume and variety of information sources than is typically feasible for a human researcher within a comparable timeframe. This broader scope of analysis helps to reduce the potential for selection bias and increases the likelihood of uncovering less obvious but potentially critical information, leading to a more robust and well-supported understanding of the subject matter.

<mark>这种方法的效率源于对迭代式「搜索—过滤」循环的自动化，这是手动研究中的核心瓶颈。系统能够在相近时间内处理远超人类研究者的海量、异质信息来源，从而确保覆盖面。这种更广的分析范围有助于减少选择偏差，也更可能发掘那些不显眼但可能至关重要的信息，使对主题的理解更稳健、更有依据。</mark>

---

## OpenAI Deep Research API | <mark>OpenAI Deep Research API</mark>

The OpenAI Deep Research API is a specialized tool designed to automate complex research tasks. It utilizes an advanced, agentic model that can independently reason, plan, and synthesize information from real-world sources. Unlike a simple Q&A model, it takes a high-level query and autonomously breaks it down into sub-questions, performs web searches using its built-in tools, and delivers a structured, citation-rich final report. The API provides direct programmatic access to this entire process, using at the time of writing models like o3-deep-research-2025-06-26 for high-quality synthesis and the faster o4-mini-deep-research-2025-06-26 for latency-sensitive application

<mark>OpenAI Deep Research API 是一个专为自动化复杂研究任务设计的专用工具。它利用高级智能体模型，能够独立推理、规划，并从真实世界来源整合信息。不同于简单的问答模型，它接收高层查询并自主拆解为子问题，借助内置工具进行网络搜索，最终给出结构化且富含引用的报告。API 提供对整个流程的直接编程访问；在撰写本文时，常用 <code>o3-deep-research-2025-06-26</code> 等模型以进行高质量整合，亦可使用更快速、适用于时延敏感应用的 <code>o4-mini-deep-research-2025-06-26</code>。</mark>

The Deep Research API is useful because it automates what would otherwise be hours of manual research, delivering professional-grade, data-driven reports suitable for informing business strategy, investment decisions, or policy recommendations. Its key benefits include:

<mark>Deep Research API 很有用，因为它自动化了本来需要数小时手动研究的工作，提供可用于支撑商业策略、投资决策或政策建议的专业级、数据驱动报告。其主要好处包括：</mark>

- **Structured, Cited Output:** It produces well-organized reports with inline citations linked to source metadata, ensuring claims are verifiable and data-backed.

- <mark><strong>结构化、有引用的输出：</strong>它生成组织良好的报告，带有链接到来源元数据的内联引用，确保声明可验证且有数据支撑。</mark>

- **Transparency:** Unlike the abstracted process in ChatGPT, the API exposes all intermediate steps, including the agent's reasoning, the specific web search queries it executed, and any code it ran. This allows for detailed debugging, analysis, and a deeper understanding of how the final answer was constructed.

- <mark><strong>透明度：</strong>与 ChatGPT 中的抽象过程不同，API 暴露所有中间步骤，包括智能体的推理、它执行的具体网络搜索查询以及运行的任何代码。这允许详细的调试、分析和对最终答案如何构建的更深理解。</mark>

- **Extensibility:** It supports the Model Context Protocol (MCP), enabling developers to connect the agent to private knowledge bases and internal data sources, blending public web research with proprietary information.

- <mark><strong>可扩展性：</strong>它支持模型上下文协议（MCP），使开发者能够将智能体连接到私有知识库和内部数据源，将公共网络研究与专有信息结合。</mark>

To use the API, you send a request to the client.responses.create endpoint, specifying a model, an input prompt, and the tools the agent can use. The input typically includes a system_message that defines the agent's persona and desired output format, along with the user_query. You must also include the web_search_preview tool and can optionally add others like code_interpreter or custom MCP tools (see Chapter 10) for internal data.

<mark>要使用 API，你向 <code>client.responses.create</code> 端点发送请求，指定模型、输入提示和智能体可以使用的工具。输入通常包括定义智能体角色和期望输出格式的 <code>system_message</code>，以及 <code>user_query</code>。你还必须包含 <code>web_search_preview</code> 工具，并可以可选地添加其他工具，如 <code>code_interpreter</code> 或自定义 MCP 工具（见第 10 章）用于内部数据。</mark>

```python
from openai import OpenAI

# Initialize the client with your API key
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Define the agent's role and the user's research question
system_message = """You are a professional researcher preparing a structured, data-driven report.
Focus on data-rich insights, use reliable sources, and include inline citations."""
user_query = "Research the economic impact of semaglutide on global healthcare systems."

# Create the Deep Research API call
response = client.responses.create(
 model="o3-deep-research-2025-06-26",
 input=[
   {
     "role": "developer",
     "content": [{"type": "input_text", "text": system_message}]
   },
   {
     "role": "user",
     "content": [{"type": "input_text", "text": user_query}]
   }
 ],
 reasoning={"summary": "auto"},
 tools=[{"type": "web_search_preview"}]
)

# Access and print the final report from the response
final_report = response.output[-1].content[0].text
print(final_report)

# --- ACCESS INLINE CITATIONS AND METADATA ---
print("--- CITATIONS ---")
annotations = response.output[-1].content[0].annotations

if not annotations:
   print("No annotations found in the report.")
else:
   for i, citation in enumerate(annotations):
       # The text span the citation refers to
       cited_text = final_report[citation.start_index:citation.end_index]

       print(f"Citation {i+1}:")
       print(f"  Cited Text: {cited_text}")
       print(f"  Title: {citation.title}")
       print(f"  URL: {citation.url}")
       print(f"  Location: chars {citation.start_index}–{citation.end_index}")
print("\n" + "="*50 + "\n")

# --- INSPECT INTERMEDIATE STEPS ---
print("--- INTERMEDIATE STEPS ---")

# 1. Reasoning Steps: Internal plans and summaries generated by the model.
try:
   reasoning_step = next(item for item in response.output if item.type == "reasoning")
   print("\n[Found a Reasoning Step]")
   for summary_part in reasoning_step.summary:
       print(f"  - {summary_part.text}")
except StopIteration:
   print("\nNo reasoning steps found.")

# 2. Web Search Calls: The exact search queries the agent executed.
try:
   search_step = next(item for item in response.output if item.type == "web_search_call")
   print("\n[Found a Web Search Call]")
   print(f"  Query Executed: '{search_step.action['query']}'")
   print(f"  Status: {search_step.status}")
except StopIteration:
   print("\nNo web search steps found.")

# 3. Code Execution: Any code run by the agent using the code interpreter.
try:
   code_step = next(item for item in response.output if item.type == "code_interpreter_call")
   print("\n[Found a Code Execution Step]")
   print("  Code Input:")
   print(f"  ```python\n{code_step.input}\n  ```")
   print("  Code Output:")
   print(f"  {code_step.output}")
except StopIteration:
   print("\nNo code execution steps found.")
```

This code snippet utilizes the OpenAI API to perform a "Deep Research" task. It starts by initializing the OpenAI client with your API key, which is crucial for authentication. Then, it defines the role of the AI agent as a professional researcher and sets the user's research question about the economic impact of semaglutide. The code constructs an API call to the o3-deep-research-2025-06-26 model, providing the defined system message and user query as input. It also requests an automatic summary of the reasoning and enables web search capabilities. After making the API call, it extracts and prints the final generated report.

<mark>此代码片段利用 OpenAI API 执行「深度研究」任务。它首先使用你的 API 密钥初始化 OpenAI 客户端，用于身份验证。随后定义 AI 智能体的角色（专业研究员），并设置关于司美格鲁肽对全球医疗体系经济影响的研究问题。接着构造对 <code>o3-deep-research-2025-06-26</code> 模型的 API 调用，传入系统消息与用户查询，同时请求自动生成推理摘要并启用网络搜索功能。完成调用后，代码会提取并打印最终生成的报告。</mark>

Subsequently, it attempts to access and display inline citations and metadata from the report's annotations, including the cited text, title, URL, and location within the report. Finally, it inspects and prints details about the intermediate steps the model took, such as reasoning steps, web search calls (including the query executed), and any code execution steps if a code interpreter was used.

<mark>随后，代码会从报告的注释中读取并展示内联引用与元数据，包括被引用的文本、标题、URL 以及在报告中的位置。最后，它还会检查并打印模型执行过的中间步骤的细节，如推理步骤、网络搜索调用（含具体查询）以及在启用代码解释器时的代码执行步骤。</mark>

---

## At a Glance | <mark>要点速览</mark>

**What:** Complex problems often cannot be solved with a single action and require foresight to achieve a desired outcome. Without a structured approach, an agentic system struggles to handle multifaceted requests that involve multiple steps and dependencies. This makes it difficult to break down high-level objectives into a manageable series of smaller, executable tasks. Consequently, the system fails to strategize effectively, leading to incomplete or incorrect results when faced with intricate goals.

<mark><strong>问题所在：</strong>复杂问题往往无法靠单一动作解决，需要具备前瞻性才能达成预期结果。若缺乏结构化方法，智能体系统就难以处理包含多步骤与依赖关系的复杂请求，也难以把高层目标拆解成可管理的、可执行的小任务。结果就是：面对复杂目标时难以有效制定策略，产出不完整或错误。</mark>

**Why:** The Planning pattern offers a standardized solution by having an agentic system first create a coherent plan to address a goal. It involves decomposing a high-level objective into a sequence of smaller, actionable steps or sub-goals. This allows the system to manage complex workflows, orchestrate various tools, and handle dependencies in a logical order. LLMs are particularly well-suited for this, as they can generate plausible and effective plans based on their vast training data. This structured approach transforms a simple reactive agent into a strategic executor that can proactively work towards a complex objective and even adapt its plan if necessary.

<mark><strong>解决之道：</strong>规划模式的做法是先由智能体生成一套连贯的计划，再据此推进目标。它将高层目标拆解为一系列更小、可执行的步骤或子目标，使系统能够管理复杂工作流、编排各类工具，并按逻辑顺序处理依赖。LLM 尤其擅长此类任务，能够基于其广泛的训练语料生成合理、有效的计划。借助这种结构化方法，简单的反应式智能体被转化为能主动朝复杂目标推进、并在必要时调整计划的战略执行者。</mark>

**Rule of thumb:** Use this pattern when a user's request is too complex to be handled by a single action or tool. It is ideal for automating multi-step processes, such as generating a detailed research report, onboarding a new employee, or executing a competitive analysis. Apply the Planning pattern whenever a task requires a sequence of interdependent operations to reach a final, synthesized outcome.

<mark><strong>经验法则：</strong>当用户请求复杂到无法由单一动作或工具完成时，采用此模式。它适用于多步骤流程的自动化，例如生成详尽的研究报告、办理新员工入职或开展竞品分析。凡是任务需要一系列相互依赖的操作才能得到最终的整合性结果，都应考虑使用规划模式。</mark>

**Visual summary:**

<mark><strong>可视化总结：</strong></mark>

![Planning Design Pattern](/images/chapter06_fig4.png)

<mark>图 4：规划设计模式</mark>

---

## Key Takeaways | <mark>核心要点</mark>

- Planning enables agents to break down complex goals into actionable, sequential steps.

- <mark>规划使智能体能够将复杂目标分解为可操作的有序步骤。</mark>

- It is essential for handling multi-step tasks, workflow automation, and navigating complex environments.

- <mark>它对于处理多步骤任务、工作流程自动化以及在复杂环境中行动至关重要。</mark>

- LLMs can perform planning by generating step-by-step approaches based on task descriptions.

- <mark>LLM 可依据任务描述生成分步方案，从而完成规划。</mark>

- Explicitly prompting or designing tasks to require planning steps encourages this behavior in agent frameworks.

- <mark>通过明确提示或将任务设计为需要规划的形式，可在智能体框架中鼓励这种行为。</mark>

- Google Deep Research is an agent analyzing on our behalf sources obtained using Google Search as a tool. It reflects, plans, and executes.

- <mark>Google Deep Research 会将 Google Search 作为工具代表我们检索与分析来源，具备反思、规划与执行能力。</mark>

---

## Conclusion | <mark>结语</mark>

In conclusion, the Planning pattern is a foundational component that elevates agentic systems from simple reactive responders to strategic, goal-oriented executors. Modern large language models provide the core capability for this, autonomously decomposing high-level objectives into coherent, actionable steps. This pattern scales from straightforward, sequential task execution, as demonstrated by the CrewAI agent creating and following a writing plan, to more complex and dynamic systems. The Google DeepResearch agent exemplifies this advanced application, creating iterative research plans that adapt and evolve based on continuous information gathering. Ultimately, planning provides the essential bridge between human intent and automated execution for complex problems. By structuring a problem-solving approach, this pattern enables agents to manage intricate workflows and deliver comprehensive, synthesized results.

<mark>总之，规划模式是把智能体系统从简单的被动响应者，提升为战略性、目标导向执行者的基础能力。现代大语言模型提供了核心支撑，能够自主将高层目标拆解为连贯且可执行的步骤。该模式既可用于简单的顺序式任务执行（如 CrewAI 智能体创建并遵循写作计划），也可扩展到更复杂、更加动态的系统。Google Deep Research 智能体便是进阶范例：它会基于持续的信息收集不断适应与演进，迭代生成研究计划。归根结底，规划为复杂问题搭起了人类意图与自动化执行之间的桥梁。通过结构化的问题求解路径，该模式使智能体能够掌控复杂工作流并产出全面而整合的结果。</mark>

---

## References | <mark>参考文献</mark>

1. Google DeepResearch (Gemini Feature): [gemini.google.com](https://gemini.google.com)

   <mark>Google DeepResearch（Gemini 功能）：[gemini.google.com](https://gemini.google.com)</mark>

2. OpenAI, Introducing deep research: [https://openai.com/index/introducing-deep-research/](https://openai.com/index/introducing-deep-research/)

   <mark>OpenAI，介绍深度研究：[https://openai.com/index/introducing-deep-research/](https://openai.com/index/introducing-deep-research/)</mark>

3. Perplexity, Introducing Perplexity Deep Research: [https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)

   <mark>Perplexity，介绍 Perplexity 深度研究：[https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)</mark>
