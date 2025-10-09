# Chapter 1: Prompt Chaining | <mark>第一章：提示链</mark>

---

## Prompt Chaining Pattern Overview | <mark>提示链模式概述</mark>

Prompt chaining, sometimes referred to as Pipeline pattern, represents a powerful paradigm for handling intricate tasks when leveraging large language models (LLMs). Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy. The core idea is to break down the original, daunting problem into a sequence of smaller, more manageable sub-problems. Each sub-problem is addressed individually through a specifically designed prompt, and the output generated from one prompt is strategically fed as input into the subsequent prompt in the chain.

<mark>提示链（有时也称为「管道模式」）是在利用大语言模型（LLM）处理复杂任务时的强大范式。与期望 LLM 在单一、整体步骤中解决复杂问题不同，提示链倡导「分而治之」的策略。核心思想是将原始、令人望而生畏的问题分解为一系列更小、更易管理的子问题。每个子问题通过专门设计的提示单独解决，一个提示生成的输出被策略性地作为链中后续提示的输入。</mark>

This sequential processing technique inherently introduces modularity and clarity into the interaction with LLMs. By decomposing a complex task, it becomes easier to understand and debug each individual step, making the overall process more robust and interpretable. Each step in the chain can be meticulously crafted and optimized to focus on a specific aspect of the larger problem, leading to more accurate and focused outputs.

<mark>这种顺序处理技术本质上为与 LLM 的交互引入了模块化与清晰性。通过分解复杂任务，更容易理解和调试每个单独步骤，使整个过程更为稳健、可解释。链中的每一步都可以精心打磨与优化，专注于更大问题的特定方面，从而产出更准确、聚焦的结果。</mark>

The output of one step acting as the input for the next is crucial. This passing of information establishes a dependency chain, hence the name, where the context and results of previous operations guide the subsequent processing. This allows the LLM to build on its previous work, refine its understanding, and progressively move closer to the desired solution.

<mark>一个步骤的输出作为下一个步骤的输入至关重要。这种信息传递建立了依赖链（因此得名），先前操作的上下文与结果会引导后续处理。这使得 LLM 能在既有成果之上构建、完善理解，并逐步逼近目标解。</mark>

Furthermore, prompt chaining is not just about breaking down problems; it also enables the integration of external knowledge and tools. At each step, the LLM can be instructed to interact with external systems, APIs, or databases, enriching its knowledge and abilities beyond its internal training data. This capability dramatically expands the potential of LLMs, allowing them to function not just as isolated models but as integral components of broader, more intelligent systems.

<mark>此外，提示链不仅用于分解问题；它还便于整合外部知识与工具。在每一步，LLM 可以被指示与外部系统、API 或数据库交互，使其能力超越内部训练数据。这一能力大幅扩展了 LLM 的潜力，使其不再是孤立的模型，而成为更广泛、更智能系统的有机组成。</mark>

**Limitations of single prompts:** For multifaceted tasks, using a single, complex prompt for an LLM can be inefficient, causing the model to struggle with constraints and instructions, potentially leading to instruction neglect where parts of the prompt are overlooked, contextual drift where the model loses track of the initial context, error propagation where early errors amplify, prompts which require a longer context window where the model gets insufficient information to respond back and hallucination where the cognitive load increases the chance of incorrect information.

<mark>**单一提示的局限性：**对于多面任务，对 LLM 使用单一、复杂提示可能效率低下，导致模型在约束和指令方面遇到困难，可能导致指令忽视（提示的部分被忽略）、上下文漂移（模型失去初始上下文的轨迹）、错误传播（早期错误被放大）、需要更长上下文窗口的提示（模型获得不足的信息来响应）以及幻觉（认知负载增加了错误信息的机会）。</mark>

**Enhanced Reliability Through Sequential Decomposition:** Prompt chaining addresses these challenges by breaking the complex task into a focused, sequential workflow, which significantly improves reliability and control. Given the example above, a pipeline or chained approach can be described as follows:

<mark>**通过顺序分解增强可靠性：**提示链通过将复杂任务分解为聚焦且顺序的工作流来应对这些挑战，从而显著提升可靠性与可控性。基于上述示例，管道或链式方法可描述如下：</mark>

1. Initial Prompt (Summarization): "Summarize the key findings of the following market research report: [text]." The model's sole focus is summarization, increasing the accuracy of this initial step.

<mark>1. 初始提示（总结）：「总结以下市场研究报告的关键发现：[文本]」。模型的唯一焦点是总结，从而提升该初始步骤的准确性。</mark>

2. Second Prompt (Trend Identification): "Using the summary, identify the top three emerging trends and extract the specific data points that support each trend: [output from step 1]." This prompt is now more constrained and builds directly upon a validated output.

<mark>2. 第二个提示（趋势识别）：「基于上述总结，识别三大新兴趋势，并提取支持每一趋势的具体数据点：[步骤 1 的输出]」。该提示更为收敛，并直接建立在已验证的输出之上。</mark>

3. Third Prompt (Email Composition): "Draft a concise email to the marketing team that outlines the following trends and their supporting data: [output from step 2]."

<mark>3. 第三个提示（电子邮件撰写）：「起草一封简洁邮件给营销团队，概述以下趋势及其支撑数据：[步骤 2 的输出]」。</mark>

**The Role of Structured Output:** The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial.

<mark>**结构化输出的作用：**提示链的可靠性高度依赖步骤间传递数据的完整性。若某一步的输出含糊或格式欠佳，后续提示可能因输入不当而失败。为减轻此风险，应指定结构化输出格式（如 JSON 或 XML）。</mark>

For example, the output from the trend identification step could be formatted as a JSON object:

<mark>例如，趋势识别步骤的输出可以格式化为 JSON 对象：</mark>

```json path=null start=null
{
  "trends": [
    {
      "trend_name": "AI-Powered Personalization",
      "supporting_data": "73% of consumers prefer to do business with brands that use personal information to make their shopping experiences more relevant."
    },
    {
      "trend_name": "Sustainable and Ethical Brands",
      "supporting_data": "Sales of products with ESG-related claims grew 28% over the last five years, compared to 20% for products without."
    }
  ]
}
```

This structured format ensures that the data is machine-readable and can be precisely parsed and inserted into the next prompt without ambiguity.

<mark>这种结构化格式确保数据是机器可读的，可以精确解析并插入下一个提示中，没有歧义。</mark>

![Context Engineering Diagram](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcHupYjMq7oEFgnAnvg5ClNDChSu33SrUgBbvKNhXcA20jyOdU-YJGMBlcV7VxdIv5JkDmp8d9hPUAy8-JMZMGvlmjsVEDUYpRGoUsYVTslIEpKUJIAFYPoqg-pZIAfK0r0L4fuf2KQkqqsTl1GCA?key=MUzX2jQEWvTbVkykMGz9x_tt)

**Fig.1:** Context Engineering is the discipline of building a rich, comprehensive informational environment for an AI, as the quality of this context is a primary factor in enabling advanced Agentic performance.

<mark>**图 1：**上下文工程，是为 AI 构建丰富且全面的信息环境的方法论；该环境的质量，是实现高级智能体性能的关键因素。</mark>

---

## Practical Applications & Use Cases | <mark>实际应用和用例</mark>

Prompt chaining is a versatile pattern applicable in a wide range of scenarios when building agentic systems. Its core utility lies in breaking down complex problems into sequential, manageable steps. Here are several practical applications:

<mark>提示链是一种多功能模式，在构建智能体系统时适用于广泛场景。其核心效用在于将复杂问题分解为顺序、可管理的步骤。如下为若干实际应用：</mark>

### 1. Information Processing Workflows | <mark>1. 信息处理工作流</mark>

Many tasks involve processing raw information through multiple transformations. For instance, summarizing a document, extracting key entities, and then using those entities to query a database or generate a report.

<mark>许多任务涉及通过多次转换处理原始信息。例如，总结文档、提取关键实体，然后使用这些实体查询数据库或生成报告。</mark>

### 2. Complex Query Answering | <mark>2. 复杂查询回答</mark>

Answering complex questions that require multiple steps of reasoning or information retrieval is a prime use case. For example, "What were the main causes of the stock market crash in 1929, and how did government policy respond?"

<mark>回答需要多步推理或信息检索的复杂问题，是重要用例之一。例如：「1929 年股市崩盘的主要原因是什么？政府政策如何回应？」</mark>

### 3. Data Extraction and Transformation | <mark>3. 数据提取和转换</mark>

The conversion of unstructured text into a structured format is typically achieved through an iterative process, requiring sequential modifications to improve the accuracy and completeness of the output.

<mark>将非结构化文本转换为结构化格式通常通过迭代过程实现，需要顺序修改以提高输出的准确性和完整性。</mark>

### 4. Content Generation Workflows | <mark>4. 内容生成工作流</mark>

The composition of complex content is a procedural task that is typically decomposed into distinct phases, including initial ideation, structural outlining, drafting, and subsequent revision.

<mark>复杂内容的创作是一个程序性任务，通常分解为不同阶段，包括初始构思、结构大纲、起草和后续修订。</mark>

---

## Hands-On Code Example | <mark>实践代码示例</mark>

The following code implements a two-step prompt chain that functions as a data processing pipeline. The initial stage is designed to parse unstructured text and extract specific information. The subsequent stage then receives this extracted output and transforms it into a structured data format.

<mark>以下代码实现两步提示链，作为数据处理管道运行。第一步解析非结构化文本，提取特定信息；第二步接收该输出并将其转换为结构化数据格式。</mark>

First, install the required libraries:

<mark>首先，安装所需的库：</mark>

```bash path=null start=null
pip install langchain langchain-community langchain-openai langgraph
```

```python path=null start=null
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the Language Model
llm = ChatOpenAI(temperature=0)

# --- Prompt 1: Extract Information ---
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the following text:\n\n{text_input}"
)

# --- Prompt 2: Transform to JSON ---
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)

# --- Build the Chain using LCEL ---
extraction_chain = prompt_extract | llm | StrOutputParser()

full_chain = (
    {"specifications": extraction_chain}
    | prompt_transform
    | llm
    | StrOutputParser()
)

# --- Run the Chain ---
input_text = "The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."

final_result = full_chain.invoke({"text_input": input_text})

print("\n--- Final JSON Output ---")
print(final_result)
```

This code demonstrates how to use LangChain to process text through a two-stage pipeline: first extracting technical specifications, then formatting them into JSON.

<mark>这段代码演示了如何使用 LangChain 通过两阶段管道处理文本：首先提取技术规格，然后将其格式化为 JSON。</mark>

![Prompt Chaining Pattern Diagram](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfD_gS5rkzKc1qimyyzrCxRtUlQ3OYpK67J7fC3a7cH2B1KcwErzqZkk9pvWn4SXmE2ImnwkLfdd1IFMa1GyTqu02vF11_IrHCMG7dU6Hy7Unaoziyt7UQ5N2YSa1XGUssvVAsjpgKa765-YCtLCg?key=MUzX2jQEWvTbVkykMGz9x_tt)

**Fig. 2:** Prompt Chaining Pattern: Agents receive a series of prompts from the user, with the output of each agent serving as the input for the next in the chain.

<mark>**图 2：**提示链模式：智能体从用户接收一系列提示，每个智能体的输出作为链中下一个的输入。</mark>

---

## At a Glance | <mark>一览</mark>

**What:** Complex tasks often overwhelm LLMs when handled within a single prompt, leading to significant performance issues. The cognitive load on the model increases the likelihood of errors such as overlooking instructions, losing context, and generating incorrect information.

<mark>**什么：**复杂任务在单个提示中处理时经常使 LLM 不堪重负，导致显著的性能问题。模型的认知负载增加了错误的可能性，如忽略指令、失去上下文和生成错误信息。</mark>

**Why:** Prompt chaining provides a standardized solution by breaking down a complex problem into a sequence of smaller, interconnected sub-tasks. Each step uses a focused prompt to perform a specific operation, significantly improving reliability and control.

<mark>**为什么：**提示链通过将复杂问题分解为一系列更小、相互关联的子任务来提供标准化解决方案。每个步骤使用聚焦的提示执行特定操作，显著提高可靠性和控制。</mark>

**Rule of thumb:** Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires interaction with external tools between steps, or when building agentic systems that need to perform multi-step reasoning and maintain state.

<mark>**经验法则：**当任务对单个提示过于复杂、涉及多个不同的处理阶段、需要在步骤间与外部工具交互，或构建需要执行多步推理和维持状态的智能体系统时，使用此模式。</mark>

---

## Key Takeaways | <mark>关键要点</mark>

- Prompt Chaining breaks down complex tasks into a sequence of smaller, focused steps. This is occasionally known as the Pipeline pattern.

<mark>- 提示链将复杂任务分解为更小且聚焦的步骤；有时也称为「管道模式」。</mark>

- Each step in a chain involves an LLM call or processing logic, using the output of the previous step as input.

<mark>- 链中每一步涉及 LLM 调用或处理逻辑，并把前一步的输出作为输入。</mark>

- This pattern improves the reliability and manageability of complex interactions with language models.

<mark>- 该模式提高了与语言模型复杂交互的可靠性与可管理性。</mark>

- Frameworks like LangChain/LangGraph, and Google ADK provide robust tools to define, manage, and execute these multi-step sequences.

<mark>- LangChain/LangGraph 与 Google ADK 等框架，提供强大工具以定义、管理并执行这些多步序列。</mark>

---

## Conclusion | <mark>结论</mark>

By deconstructing complex problems into a sequence of simpler, more manageable sub-tasks, prompt chaining provides a robust framework for guiding large language models. This "divide-and-conquer" strategy significantly enhances the reliability and control of the output by focusing the model on one specific operation at a time. As a foundational pattern, it enables the development of sophisticated AI agents capable of multi-step reasoning, tool integration, and state management.

<mark>通过把复杂问题解构为一系列更简单、可管理的子任务，提示链为引导大语言模型提供稳健框架。此「分而治之」策略让模型一次专注于一个特定操作，从而显著增强输出的可靠性与可控性。作为基础模式，它支撑多步推理、工具集成与状态管理等能力，助力构建更复杂的 AI 智能体。</mark>

---

## References | <mark>参考文献</mark>

1. LangChain Documentation on LCEL: https://python.langchain.com/v0.2/docs/core_modules/expression_language/
2. LangGraph Documentation: https://langchain-ai.github.io/langgraph/
3. Prompt Engineering Guide - Chaining Prompts: https://www.promptingguide.ai/techniques/chaining
4. OpenAI API Documentation: https://platform.openai.com/docs/guides/gpt/prompting
5. Crew AI Documentation: https://docs.crewai.com/
6. Google AI for Developers: https://cloud.google.com/discover/what-is-prompt-engineering?hl=en
7. Vertex Prompt Optimizer: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer

---
