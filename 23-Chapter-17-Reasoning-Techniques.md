------

# Chapter 17: Reasoning Techniques | <mark>第 17 章：推理技术</mark>

This chapter delves into advanced reasoning methodologies for intelligent agents, focusing on multi-step logical inferences and problem-solving. These techniques go beyond simple sequential operations, making the agent's internal reasoning explicit. This allows agents to break down problems, consider intermediate steps, and reach more robust and accurate conclusions.  A core principle among these advanced methods is the allocation of increased computational resources during inference. This means granting the agent, or the underlying LLM, more processing time or steps to process a query and generate a response. Rather than a quick, single pass, the agent can engage in iterative refinement, explore multiple solution paths, or utilize external tools. This extended processing time during inference often significantly enhances accuracy, coherence, and robustness, especially for complex problems requiring deeper analysis and deliberation.

<mark>本章深入探讨了智能体的先进推理方法，重点介绍多步逻辑推理和问题解决技术。这些技术超越了简单的顺序操作，使智能体的内部推理过程更加明确。这使得智能体能够分解问题、考虑中间步骤，并得出更加稳健和准确的结论。在这些先进方法中，一个核心原则是在推理过程中分配更多的计算资源。这意味着给予智能体或底层 LLM 更多的处理时间或步骤来处理查询并生成响应。智能体可以进行迭代优化、探索多种解决方案路径或利用外部工具，而不是进行快速的单次处理。这种在推理过程中延长的处理时间通常能显著提高准确性、连贯性和稳健性，尤其对于需要深入分析和思考的复杂问题。</mark>

## Practical Applications & Use Cases | <mark>实际应用与使用案例</mark>

Practical applications include:

<mark>实际应用包括：</mark>

●**Complex Question Answering**: Facilitating the resolution of multi-hop queries, which necessitate the integration of data from diverse sources and the execution of logical deductions, potentially involving the examination of multiple reasoning paths, and benefiting from extended inference time to synthesize information.

<mark>●**复杂问答**：促进多跳查询的解决，这类查询需要整合来自不同来源的数据并执行逻辑推理，可能涉及检查多条推理路径，并得益于更长的推理时间来综合信息。</mark>

●**Mathematical Problem Solving**: Enabling the division of mathematical problems into smaller, solvable components, illustrating the step-by-step process, and employing code execution for precise computations, where prolonged inference enables more intricate code generation and validation.

<mark>●**数学问题解决**：将数学问题分解为更小、可解决的组成部分，展示逐步解决过程，并使用代码执行进行精确计算，其中长时间的推理能够支持更复杂的代码生成和验证。</mark>

●**Code Debugging and Generation**: Supporting an agent's explanation of its rationale for generating or correcting code, pinpointing potential issues sequentially, and iteratively refining the code based on test results (Self-Correction), leveraging extended inference time for thorough debugging cycles.

<mark>●**代码调试与生成**：支持代理对其生成或修正代码的推理依据进行解释，顺序识别潜在问题，并根据测试结果迭代优化代码（自我修正），利用扩展的推理时间进行彻底的调试周期。</mark>

●**Strategic Planning**: Assisting in the development of comprehensive plans through reasoning across various options, consequences, and preconditions, and adjusting plans based on real-time feedback (ReAct), where extended deliberation can lead to more effective and reliable plans.

<mark>●**战略规划**：通过推理各种选项、结果和先决条件来协助制定全面计划，并根据实时反馈（ReAct）调整计划，其中深入的思考可以导致更有效和可靠的计划。</mark>

●**Medical Diagnosis**: Aiding an agent in systematically assessing symptoms, test outcomes, and patient histories to reach a diagnosis, articulating its reasoning at each phase, and potentially utilizing external instruments for data retrieval (ReAct). Increased inference time allows for a more comprehensive differential diagnosis.

<mark>●**医疗诊断**：帮助智能体系统评估症状、检查结果和患者病史以做出诊断，在每个阶段阐述其推理过程，并可能利用外部工具进行数据检索（ReAct）。增加推理时间可以实现更全面的鉴别诊断。</mark>

●**Legal Analysis**: Supporting the analysis of legal documents and precedents to formulate arguments or provide guidance, detailing the logical steps taken, and ensuring logical consistency through self-correction. Increased inference time allows for more in-depth legal research and argument construction.

<mark>●**法律分析**：支持对法律文件和判例的分析，以制定论点或提供指导，详细说明所采取的逻辑步骤，并通过自纠正（self-correction）确保逻辑一致性。增加推理时间可以进行更深入的法律研究和论点构建。</mark>

## Reasoning techniques
## <mark>推理技巧</mark>

To start, let's delve into the core reasoning techniques used to enhance the problem-solving abilities of AI models.

<mark>首先，我们深入探究旨在提升 AI 模型问题解决能力的核心推理技巧。</mark>

**Chain-of-Thought (CoT)** prompting significantly enhances LLMs' complex reasoning abilities by mimicking a step-by-step thought process (see Fig. 1). Instead of providing a direct answer, CoT prompts guide the model to generate a sequence of intermediate reasoning steps. This explicit breakdown allows LLMs to tackle complex problems by decomposing them into smaller, more manageable sub-problems. This technique markedly improves the model's performance on tasks requiring multi-step reasoning, such as arithmetic, common sense reasoning, and symbolic manipulation. A primary advantage of CoT is its ability to transform a difficult, single-step problem into a series of simpler steps, thereby increasing the transparency of the LLM's reasoning process. This approach not only boosts accuracy but also offers valuable insights into the model's decision-making, aiding in debugging and comprehension. CoT can be implemented using various strategies, including offering few-shot examples that demonstrate step-by-step reasoning or simply instructing the model to "think step by step." Its effectiveness stems from its ability to guide the model's internal processing toward a more deliberate and logical progression. As a result, Chain-of-Thought has become a cornerstone technique for enabling advanced reasoning capabilities in contemporary LLMs. This enhanced transparency and breakdown of complex problems into manageable sub-problems is particularly important for autonomous agents, as it enables them to perform more reliable and auditable actions in complex environments.

<mark>**思维链 (CoT)** 提示通过模仿逐步思考的过程（参见图 1），显著增强了大型语言模型（LLM）的复杂推理能力。CoT 提示并非直接给出答案，而是引导模型生成一系列中间推理步骤。这种清晰的拆解使 LLM 能够将复杂问题分解为更小、更易处理的子问题，从而攻克难题。这项技术显著提升了模型在需要多步推理任务上的表现，例如算术、常识推理和符号操作等。</mark>

<mark>CoT 的一个主要优势在于它能够将困难的单步问题转化为一系列简单步骤，进而提高 LLM 推理过程的透明度。这种方法不仅提高了准确性，还为模型的决策提供了有价值的洞察，有助于调试和理解。CoT 可以通过多种策略实现，包括提供展示逐步推理的少样本示例，或者直接指示模型“逐步思考”。其有效性源于它能够引导模型的内部处理流程朝着更审慎、更逻辑化的方向发展。因此，思维链已成为赋能当代 LLM 高级推理能力的关键基石。</mark>

<mark>这种增强的透明度，以及将复杂问题拆解为可管理子问题的做法，对于自主代理（Autonomous Agents）尤为重要，因为它使代理能够在复杂环境中执行更可靠、更可审计的行动。</mark>

<img width="800" height="564" alt="image" src="https://github.com/user-attachments/assets/3f0623d5-867b-41e0-9880-ff355a76aace" />

Fig. 1: CoT prompt alongside the detailed, step-by-step response generated by the agent.
<mark>图 1：思维链提示以及代理生成的详细、逐步响应。</mark>

Let's see an example. It begins with a set of instructions that tell the AI how to think, defining its persona and a clear five-step process to follow. This is the prompt that initiates structured thinking.

<mark>让我们看一个例子。它首先包含一组指令，告诉 AI 如何思考，定义其角色以及一个明确的五步流程。这是启动结构化思考的提示。</mark>

Following that, the example shows the CoT process in action. The section labeled "Agent's Thought Process" is the internal monologue where the model executes the instructed steps. This is the literal "chain of thought." Finally, the "Agent's Final Answer" is the polished, comprehensive output generated as a result of that careful, step-by-step reasoning process

<mark>随后，该示例展示了 CoT 过程的实际应用。标记为"Agent's Thought Process"的部分是模型执行指定步骤时的内心独白，这就是字面意义上的"思维链"。最后，"Agent's Final Answer"是经过仔细、逐步推理过程后生成的精炼且全面的输出。</mark>

```python
You are an Information Retrieval Agent. Your goal is to answer the user's question comprehensively and accurately by thinking step-by-step.
Here's the process you must follow:

1. **Analyze the Query:** Understand the core subject and specific requirements of the user's question. Identify key entities, keywords, and the type of information being sought.
2. **Formulate Search Queries (for Knowledge Base):** Based on your analysis, generate a list of precise search queries that you would use to retrieve relevant information from a knowledge base or external tools.
3. **Simulate Information Retrieval (Self-Correction/Reasoning):**For each search query, mentally consider what kind of information you expect to find. If you were to retrieve the content, what would be the most relevant snippets? Think about potential ambiguities or
missing pieces.
4. **Synthesize Information:** Based on the simulated retrieval and your understanding of the user's original query, synthesize the gathered information into a coherent and complete answer. Ensure all aspects of the query are addressed.
5. **Review and Refine:** Before finalizing, critically evaluate your answer. Is it accurate? Is it comprehensive? Is it easy to understand? Is it concise? If not, identify what needs to be improved and how.

**User Query:** "Explain the main differences between classical computers and quantum computers, and briefly describe a potential application of quantum computing."

**Agent's Thought Process (Internal CoT Output - encouraged by the prompt):**

**Thought 1 (Analyze Query):**
The user wants two things:
1. Main differences between classical and quantum computers.
2. One potential application of quantum computing.
Keywords: classical computers, quantum computers, differences, potential application.

**Thought 2 (Formulate Search Queries):**
- "differences classical vs quantum computers"
- "how quantum computers work"
- "how classical computers work"
- "applications of quantum computing"

**Thought 3 (Simulate Information Retrieval & Identify Key Concepts):**
- From "differences": Expect concepts like bits vs. qubits, superposition, entanglement, probabilistic nature, computational power for specific problems.
- From "how they work": Classical uses transistors/binary. Quantum uses quantum mechanics.
- From "applications": Expect drug discovery, material science, cryptography, optimization.

**Thought 4 (Synthesize Information):**
Classical computers use bits (0 or 1), processing information sequentially. Quantum computers use qubits, which can be 0, 1, or both simultaneously (superposition), and can be entangled, allowing for vastly different computational approaches. This enables them to
solve certain problems (like factoring large numbers or simulating complex molecules) far more efficiently than classical computers. A potential application is in drug discovery, where quantum computers could simulate molecular interactions with unprecedented accuracy,
accelerating the development of new medicines.

**Thought 5 (Review and Refine):**
- Differences are covered (bits vs qubits, superposition, entanglement, processing).
- Application is given (drug discovery).
- Is it brief? Yes.
- Is it clear? Yes.
- Looks good.

**Agent's Final Answer (Output to User):**
Classical computers process information using bits, which can be either a 0 or a 1 at any given time, performing operations sequentially. In contrast, quantum computers utilize qubits, which can exist in multiple states simultaneously through superposition and can be linked through entanglement, allowing for exponentially more complex computations. This fundamental difference enables quantum machines to tackle certain problems, such as simulating molecular structures or breaking complex encryption, that are intractable for even the most powerful classical supercomputers. A significant potential application of quantum computing lies in drug discovery, where its ability to precisely model molecular behavior could revolutionize the development of new pharmaceuticals.

```

```python

你是一名信息检索代理（Information Retrieval Agent）。你的目标是通过循序渐进的思考，全面且准确地回答用户的问题。
你必须遵循以下流程：

1. **分析查询（Analyze the Query）：** 理解用户问题的核心主题和具体要求。识别关键实体、关键词以及所需信息的类型。
2. **制定搜索查询（Formulate Search Queries - 针对知识库）：** 基于你的分析，生成一份精确的搜索查询列表，用于从知识库或外部工具中检索相关信息。
3. **模拟信息检索（Simulate Information Retrieval - 自我修正/推理）：** 对于每项搜索查询，在脑海中思考预期会找到哪种信息。如果检索到内容，哪些片段会是最相关的？思考潜在的歧义或缺失的部分。
4. **综合信息（Synthesize Information）：** 基于模拟检索和你对用户原始查询的理解，将收集到的信息综合成一个连贯且完整的答案。确保回答了查询的所有方面。
5. **审查与优化（Review and Refine）：** 在最终确定答案前，批判性地评估你的回答。它是否准确？是否全面？是否易于理解？是否简洁？如果不是，确定需要改进的内容和方式。

**用户查询：**“解释经典计算机和量子计算机的主要区别，并简要描述一个量子计算的潜在应用。”
**代理的思维过程（内部思维链输出 - 由提示鼓励生成）**

**思考 1（分析查询）：**
用户希望得到两点信息：
1. 经典计算机与量子计算机的主要区别。
2. 一个潜在的量子计算应用。
关键词：经典计算机、量子计算机、区别、潜在应用。

思考 2（制定搜索查询）：
- “经典计算机 vs 量子计算机 区别”
- “量子计算机如何工作”
- “经典计算机如何工作”
- “量子计算应用”

**思考 3（模拟信息检索与识别关键概念）：**
- 从“区别”中：预期会找到比特（bits） vs 量子比特（qubits）、叠加态（superposition）、纠缠（entanglement）、概率性质、解决特定问题的计算能力等概念。
- 从“如何工作”中：经典计算机使用晶体管/二进制。量子计算机使用量子力学。
- 从“应用”中：预期会找到药物发现、材料科学、密码学、优化等。

**思考 4（综合信息）：**
经典计算机使用比特（0 或 1），并按顺序处理信息。量子计算机使用量子比特，量子比特可以同时处于 0、1 或两者兼具的状态（叠加态），并且可以相互纠缠，从而实现截然不同的计算方法。这使它们能够比经典计算机更高效地解决某些特定问题（如分解大数或模拟复杂分子）。一个潜在的应用是药物发现，量子计算机可以前所未有地准确模拟分子相互作用，从而加速新药的研发。

**思考 5（审查与优化）：**
- 区别已涵盖（比特 vs 量子比特、叠加态、纠缠、处理方式）。
- 应用已给出（药物发现）。
- 是否简洁？是。
- 是否清晰？是。
- 看起来不错。

**代理的最终答案（输出给用户）：**
经典计算机使用比特来处理信息，比特在任一时刻只能是 0 或 1，并按顺序执行操作。相比之下，量子计算机利用量子比特，量子比特可以通过叠加态同时存在于多种状态，并通过纠缠相互关联，从而实现指数级复杂的计算。这种根本性的差异使得量子机器能够解决某些问题（例如模拟分子结构或破解复杂加密），这些问题对于最强大的经典超级计算机来说都是无法攻克的。量子计算的一个重要的潜在应用在于药物发现，它精确建模分子行为的能力可以彻底改变新药的研发。

```

Tree-of-Thought (ToT) is a reasoning technique that builds upon Chain-of-Thought
(CoT). It allows large language models to explore multiple reasoning paths
