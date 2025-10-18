# Chapter 14: Knowledge Retrieval (RAG) | <mark>第十四章：知识检索（RAG）</mark>

LLMs exhibit substantial capabilities in generating human-like text. However, their knowledge base is typically confined to the data on which they were trained, limiting their access to real-time information, specific company data, or highly specialized details. Knowledge Retrieval (RAG, or Retrieval Augmented Generation), addresses this limitation. RAG enables LLMs to access and integrate external, current, and context-specific information, thereby enhancing the accuracy, relevance, and factual basis of their outputs.

<mark>大语言模型（LLM）在生成类人文本方面表现出强大能力。然而，它们的知识库通常仅限于训练数据，难以覆盖实时信息、特定公司数据或高度专业化的细节。知识检索（RAG，Retrieval Augmented Generation）针对这一局限，帮助 LLM 访问并整合外部的、最新的、具备上下文的知识，从而提升输出的准确性、相关性与事实基础。</mark>

For AI agents, this is crucial as it allows them to ground their actions and responses in real-time, verifiable data beyond their static training. This capability enables them to perform complex tasks accurately, such as accessing the latest company policies to answer a specific question or checking current inventory before placing an order. By integrating external knowledge, RAG transforms agents from simple conversationalists into effective, data-driven tools capable of executing meaningful work.

<mark>对于 AI 智能体而言，RAG 至关重要，因为它让智能体可以依托静态训练数据之外的实时、可验证信息来行动。凭借这一能力，智能体能够准确完成复杂任务，例如调用最新公司政策回答问题，或在下单前查询实时库存。通过整合外部知识，RAG 能够把智能体从简单的对话者转化为高效的数据驱动型工具。</mark>

---

## Knowledge Retrieval (RAG) Pattern Overview | <mark>知识检索（RAG）模式概述</mark>

The Knowledge Retrieval (RAG) pattern significantly enhances the capabilities of LLMs by granting them access to external knowledge bases before generating a response. Instead of relying solely on their internal, pre-trained knowledge, RAG allows LLMs to "look up" information, much like a human might consult a book or search the internet. This process empowers LLMs to provide more accurate, up-to-date, and verifiable answers.

<mark>知识检索（RAG）模式在生成回答前向 LLM 提供外部知识库，显著提升其能力。不再局限于预训练知识，RAG 让模型像人类一样「查阅」资料，因此能够给出更准确、更新、可验证的答案。</mark>

When a user poses a question or gives a prompt to an AI system using RAG, the query isn't sent directly to the LLM. Instead, the system first scours a vast external knowledge base—a highly organized library of documents, databases, or web pages—for relevant information. This search is not a simple keyword match; it's a "semantic search" that understands the user's intent and the meaning behind their words. This initial search pulls out the most pertinent snippets or "chunks" of information. These extracted pieces are then "augmented," or added, to the original prompt, creating a richer, more informed query. Finally, this enhanced prompt is sent to the LLM. With this additional context, the LLM can generate a response that is not only fluent and natural but also factually grounded in the retrieved data.

<mark>当用户向采用 RAG 的系统提问时，查询不会直接发送给 LLM。系统会先在庞大的外部知识库（结构化的文档、数据库或网页）中进行语义搜索，理解用户意图并定位最相关的文本块。这些片段随后会增强原始提示，形成信息更充足的请求，最终再交给 LLM。借助新增的上下文，模型可以生成既流畅自然又具有事实依据的回答。</mark>

The RAG framework provides several significant benefits. It allows LLMs to access up-to-date information, thereby overcoming the constraints of their static training data. This approach also reduces the risk of "hallucination"—the generation of false information—by grounding responses in verifiable data. Moreover, LLMs can utilize specialized knowledge found in internal company documents or wikis. A vital advantage of this process is the capability to offer "citations," which pinpoint the exact source of information, thereby enhancing the trustworthiness and verifiability of the AI's responses.

<mark>RAG 带来多重优势：它让模型获取最新信息，克服静态训练数据的限制；通过可验证数据支撑，显著降低「幻觉」风险；同时可以利用公司内部文档或 Wiki 的专业知识。最重要的是，它能够提供精确的引用来源，增强回答的可信度与可验证性。</mark>

To fully appreciate how RAG functions, it's essential to understand a few core concepts (see Fig. 1):

<mark>要深入理解 RAG，需要先掌握几项核心概念（见图 1）：</mark>

**Embeddings:** In the context of LLMs, embeddings are numerical representations of text, such as words, phrases, or entire documents. These representations are in the form of a vector, which is a list of numbers. The key idea is to capture the semantic meaning and the relationships between different pieces of text in a mathematical space. Words or phrases with similar meanings will have embeddings that are closer to each other in this vector space. For instance, imagine a simple 2D graph. The word "cat" might be represented by the coordinates (2, 3), while "kitten" would be very close at (2.1, 3.1). In contrast, the word "car" would have a distant coordinate like (8, 1), reflecting its different meaning. In reality, these embeddings are in a much higher-dimensional space with hundreds or even thousands of dimensions, allowing for a very nuanced understanding of language.

<mark><strong>嵌入（Embeddings）：</strong>在 LLM 场景下，嵌入是对文本（单词、短语或整篇文档）的数值表示，以向量形式存储，旨在捕捉语义和文本之间的关系。语义相似的词在向量空间中更接近。例如，「cat」可能位于坐标 (2, 3)，与之含义接近的「kitten」则位于 (2.1, 3.1)。现实中，嵌入通常处于数百甚至上千维的空间，从而更细腻地刻画语言特征。</mark>

**Text Similarity:** Text similarity refers to the measure of how alike two pieces of text are. This can be at a surface level, looking at the overlap of words (lexical similarity), or at a deeper, meaning-based level. In the context of RAG, text similarity is crucial for finding the most relevant information in the knowledge base that corresponds to a user's query. For instance, consider the sentences: "What is the capital of France?" and "Which city is the capital of France?" While the wording is different, they are asking the same question. A good text similarity model would recognize this and assign a high similarity score to these two sentences, even though they only share a few words. This is often calculated using the embeddings of the texts.

<mark><strong>文本相似度（Text Similarity）：</strong>文本相似度衡量两段文本的相似程度，既可关注关键词的重合，也可基于语义理解。在 RAG 场景中，相似度决定了系统能否从知识库中定位与查询最契合的内容。例如，「What is the capital of France?」与「Which city is the capital of France?」虽然表达不同，但意图一致，优秀的模型会给出较高的相似度评分。</mark>

**Semantic Similarity and Distance:** Semantic similarity is a more advanced form of text similarity that focuses purely on the meaning and context of the text, rather than just the words used. It aims to understand if two pieces of text convey the same concept or idea. Semantic distance is the inverse of this; a high semantic similarity implies a low semantic distance, and vice versa. In RAG, semantic search relies on finding documents with the smallest semantic distance to the user's query. For instance, the phrases "a furry feline companion" and "a domestic cat" have no words in common besides "a". However, a model that understands semantic similarity would recognize that they refer to the same thing and would consider them to be highly similar. This is because their embeddings would be very close in the vector space, indicating a small semantic distance. This is the "smart search" that allows RAG to find relevant information even when the user's wording doesn't exactly match the text in the knowledge base.

<mark><strong>语义相似度与语义距离：</strong>语义相似度关注文本表达的含义，而非具体词汇；语义距离与之相反，相似度越高，距离越小。RAG 中的语义搜索会寻找与查询语义距离最小的文档。例如，「a furry feline companion」与「a domestic cat」几乎没有共同词汇，但语义相同，因此被视作高度相似。</mark>

**Fig. 1:** RAG Core Concepts: Chunking, Embeddings, and Vector Database.

<mark><strong>图 1：</strong>RAG 核心概念：分块、嵌入与向量数据库。</mark>

**Chunking of Documents:** Chunking is the process of breaking down large documents into smaller, more manageable pieces, or "chunks." For a RAG system to work efficiently, it cannot feed entire large documents into the LLM. Instead, it processes these smaller chunks. The way documents are chunked is important for preserving the context and meaning of the information. For instance, instead of treating a 50-page user manual as a single block of text, a chunking strategy might break it down into sections, paragraphs, or even sentences. For instance, a section on "Troubleshooting" would be a separate chunk from the "Installation Guide." When a user asks a question about a specific problem, the RAG system can then retrieve the most relevant troubleshooting chunk, rather than the entire manual. This makes the retrieval process faster and the information provided to the LLM more focused and relevant to the user's immediate need. Once documents are chunked, the RAG system must employ a retrieval technique to find the most relevant pieces for a given query. The primary method is vector search, which uses embeddings and semantic distance to find chunks that are conceptually similar to the user's question. An older, but still valuable, technique is BM25, a keyword-based algorithm that ranks chunks based on term frequency without understanding semantic meaning. To get the best of both worlds, hybrid search approaches are often used, combining the keyword precision of BM25 with the contextual understanding of semantic search. This fusion allows for more robust and accurate retrieval, capturing both literal matches and conceptual relevance.

<mark><strong>文档分块（Chunking of Documents）：</strong>分块是将大型文档拆成更小的文本块，便于处理和检索。合理的分块策略可以保留上下文，例如把 50 页手册划分为「安装指南」和「故障排查」等部分。当用户咨询特定问题时，系统只需检索相关的故障排查片段即可。主流检索方法是向量搜索，通过嵌入和语义距离匹配概念相近的文本块；BM25 等基于关键词的传统算法仍具价值，混合检索常常能够兼顾字面匹配与语义相关性。</mark>

**Vector databases:** A vector database is a specialized type of database designed to store and query embeddings efficiently. After documents are chunked and converted into embeddings, these high-dimensional vectors are stored in a vector database. Traditional retrieval techniques, like keyword-based search, are excellent at finding documents containing exact words from a query but lack a deep understanding of language. They wouldn't recognize that "furry feline companion" means "cat." This is where vector databases excel. They are built specifically for semantic search. By storing text as numerical vectors, they can find results based on conceptual meaning, not just keyword overlap. When a user's query is also converted into a vector, the database uses highly optimized algorithms (like HNSW - Hierarchical Navigable Small World) to rapidly search through millions of vectors and find the ones that are "closest" in meaning. This approach is far superior for RAG because it uncovers relevant context even if the user's phrasing is completely different from the source documents. In essence, while other techniques search for words, vector databases search for meaning. This technology is implemented in various forms, from managed databases like Pinecone and Weaviate to open-source solutions such as Chroma DB, Milvus, and Qdrant. Even existing databases can be augmented with vector search capabilities, as seen with Redis, Elasticsearch, and Postgres (using the pgvector extension). The core retrieval mechanisms are often powered by libraries like Meta AI's FAISS or Google Research's ScaNN, which are fundamental to the efficiency of these systems.

<mark><strong>向量数据库（Vector databases）：</strong>向量数据库专门存储与检索嵌入。当文本被分块并转换为高维嵌入后，会被写入向量数据库。相比关键词检索，向量数据库能够基于语义找到相关内容，即便用户描述与原文完全不同。它通过优化算法（如 HNSW）在海量向量中找到语义最近的结果。Pinecone、Weaviate 等托管服务，以及 Chroma DB、Milvus、Qdrant 等开源方案都提供此类能力；Redis、Elasticsearch、Postgres（配合 pgvector 扩展）等传统数据库也可增量支持向量搜索。底层常由 FAISS、ScaNN 等库提供高效检索。</mark>

**RAG's Challenges:** Despite its power, the RAG pattern is not without its challenges. A primary issue arises when the information needed to answer a query is not confined to a single chunk but is spread across multiple parts of a document or even several documents. In such cases, the retriever might fail to gather all the necessary context, leading to an incomplete or inaccurate answer. The system's effectiveness is also highly dependent on the quality of the chunking and retrieval process; if irrelevant chunks are retrieved, it can introduce noise and confuse the LLM. Furthermore, effectively synthesizing information from potentially contradictory sources remains a significant hurdle for these systems. Besides that, another challenge is that RAG requires the entire knowledge base to be pre-processed and stored in specialized databases, such as vector or graph databases, which is a considerable undertaking. Consequently, this knowledge requires periodic reconciliation to remain up-to-date, a crucial task when dealing with evolving sources like company wikis. This entire process can have a noticeable impact on performance, increasing latency, operational costs, and the number of tokens used in the final prompt.

<mark><strong>RAG 的挑战：</strong>尽管强大，RAG 仍面临诸多挑战。例如，同一答案需要跨越多段文本时，检索器可能无法一次性收集所有关键信息，导致回答不完整。分块与检索质量也至关重要，召回无关文本会引入噪声、干扰模型。此外，当信息来源存在矛盾时，如何有效整合仍是一大难题。RAG 还需要对整个知识库执行预处理并存储于专用数据库，工作量巨大；同时必须定期同步，确保数据紧跟最新动态。这些步骤会显著增加延迟、成本与提示 token 的消耗。</mark>

In summary, the Retrieval-Augmented Generation (RAG) pattern represents a significant leap forward in making AI more knowledgeable and reliable. By seamlessly integrating an external knowledge retrieval step into the generation process, RAG addresses some of the core limitations of standalone LLMs. The foundational concepts of embeddings and semantic similarity, combined with retrieval techniques like keyword and hybrid search, allow the system to intelligently find relevant information, which is made manageable through strategic chunking. This entire retrieval process ultimately empowers AI systems to provide answers that are not only contextually appropriate but also backed by factual data, increasing their utility in specialized, knowledge-intensive domains.

<mark>综上所述，RAG 让 AI 在知识性与可靠性方面迈出重要一步。它把外部检索无缝嵌入生成流程，弥补了独立 LLM 的局限。借助嵌入、语义相似度，以及关键词与混合检索等技术，系统能够智能地定位相关信息，并通过合理的分块策略高效交付给模型，从而输出具有上下文且有事实支持的答案，适用于专业、知识密集型场景。</mark>

Applications include:

<mark><strong>典型应用包括：</strong></mark>

- Enterprise Search and Q&A: Organizations can develop internal chatbots that respond to employee inquiries using internal documentation such as HR policies, technical manuals, and product specifications. The RAG system extracts relevant sections from these documents to inform the LLM's response.
- <mark><strong>企业搜索与问答</strong>：组织可以开发内部聊天机器人，利用人力资源政策、技术手册和产品规格等内部文档来回应员工的询问。RAG 系统从这些文档中提取相关部分，为 LLM 的响应提供信息。</mark>

  <mark>企业搜索与问答：构建内部聊天机器人，利用人力资源政策、技术手册、产品规格等资料回答员工问题，RAG 会提取最相关的文档片段提供给模型。</mark>

- Customer Support and Helpdesks: RAG-based systems can offer precise and consistent responses to customer queries by accessing information from product manuals, frequently asked questions (FAQs), and support tickets. This can reduce the need for direct human intervention for routine issues.

  <mark>客户支持与服务台：系统可以调用产品手册、FAQ、支持工单等资料，为客户提供精准一致的答复，减少人工介入。</mark>

- Personalized Content Recommendation: Instead of basic keyword matching, RAG can identify and retrieve content (articles, products) that is semantically related to a user's preferences or previous interactions, leading to more relevant recommendations.

  <mark>个性化内容推荐：RAG 基于语义而非关键词匹配，为用户检索与喜好或历史交互相关的内容，提升推荐效果。</mark>

- News and Current Events Summarization: LLMs can be integrated with real-time news feeds. When prompted about a current event, the RAG system retrieves recent articles, allowing the LLM to produce an up-to-date summary.

  <mark>新闻与时事摘要：LLM 接入实时新闻源，用户询问当前事件时，RAG 会检索最新报道，帮助模型生成及时的总结。</mark>

By incorporating external knowledge, RAG extends the capabilities of LLMs beyond simple communication to function as knowledge processing systems.

<mark>借助外部知识，RAG 让 LLM 超越简单对话，成为真正的知识处理系统。</mark>

---

## Hands-On Code Example (ADK) | <mark>使用 ADK 的实战代码</mark>

To illustrate the Knowledge Retrieval (RAG) pattern, let's see three examples.

<mark>下面通过三个示例演示知识检索（RAG）的具体实现。</mark>

First, is how to use Google Search to do RAG and ground LLMs to search results. Since RAG involves accessing external information, the Google Search tool is a direct example of a built-in retrieval mechanism that can augment an LLM's knowledge.

<mark>首先，演示如何使用 Google 搜索实现 RAG，将模型回答锚定在搜索结果上。由于 RAG 需要访问外部信息，Google 搜索是增强 LLM 知识的直接手段。</mark>

```python
from google.adk.tools import google_search
from google.adk.agents import Agent

search_agent = Agent(
    name="research_assistant",
    model="gemini-2.0-flash-exp",
    instruction="You help users research topics. When asked, use the Google Search tool",
    tools=[google_search]
)
```

Second, this section explains how to utilize Vertex AI RAG capabilities within the Google ADK. The code provided demonstrates the initialization of VertexAiRagMemoryService from the ADK. This allows for establishing a connection to a Google Cloud Vertex AI RAG Corpus. The service is configured by specifying the corpus resource name and optional parameters such as SIMILARITY_TOP_K and VECTOR_DISTANCE_THRESHOLD. These parameters influence the retrieval process. SIMILARITY_TOP_K defines the number of top similar results to be retrieved. VECTOR_DISTANCE_THRESHOLD sets a limit on the semantic distance for the retrieved results. This setup enables agents to perform scalable and persistent semantic knowledge retrieval from the designated RAG Corpus. The process effectively integrates Google Cloud's RAG functionalities into an ADK agent, thereby supporting the development of responses grounded in factual data.

<mark>其次，展示如何在 Google ADK 中调用 Vertex AI 的 RAG 功能。代码演示了如何初始化 VertexAiRagMemoryService，连接到 Google Cloud Vertex AI 的 RAG 语料库，并通过 SIMILARITY_TOP_K 和 VECTOR_DISTANCE_THRESHOLD 等参数控制检索策略，从而实现可扩展、持久的语义检索，帮助智能体生成有事实依据的回复。</mark>

```python
from google.adk.memory import VertexAiRagMemoryService

RAG_CORPUS_RESOURCE_NAME = "projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id"

# Number of top similar results to retrieve.
SIMILARITY_TOP_K = 5

# Maximum semantic distance allowed for retrieved results.
VECTOR_DISTANCE_THRESHOLD = 0.7

memory_service = VertexAiRagMemoryService(
    rag_corpus=RAG_CORPUS_RESOURCE_NAME,
    similarity_top_k=SIMILARITY_TOP_K,
    vector_distance_threshold=VECTOR_DISTANCE_THRESHOLD
)
```

---

## Hands-On Code Example (LangChain) | <mark>使用 LangChain 的实战代码</mark>

Third, let's walk through a complete example using LangChain.

<mark>最后，我们用 LangChain 搭建一个端到端的示例。</mark>

```python
import os
import requests
from typing import List, Dict, Any, TypedDict
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Weaviate
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import StateGraph, END
import weaviate
from weaviate.embedded import EmbeddedOptions
import dotenv

dotenv.load_dotenv()
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# --- 1. Data Preparation (Preprocessing) ---
url = "https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/state_of_the_union.txt"
res = requests.get(url)
with open("state_of_the_union.txt", "w") as f:
    f.write(res.text)

loader = TextLoader("./state_of_the_union.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

client = weaviate.Client(
    embedded_options=EmbeddedOptions()
)

vectorstore = Weaviate.from_documents(
    client=client,
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    by_text=False
)

retriever = vectorstore.as_retriever()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# --- 2. Define the State for LangGraph ---
class RAGGraphState(TypedDict):
    question: str
    documents: List[Document]
    generation: str

# --- 3. Define the Nodes (Functions) ---
def retrieve_documents_node(state: RAGGraphState) -> RAGGraphState:
    """Retrieves documents based on the user's question."""
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question, "generation": ""}

def generate_response_node(state: RAGGraphState) -> RAGGraphState:
    """Generates a response using the LLM based on retrieved documents."""
    question = state["question"]
    documents = state["documents"]

    template = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""
    prompt = ChatPromptTemplate.from_template(template)

    context = "\n\n".join([doc.page_content for doc in documents])

    rag_chain = prompt | llm | StrOutputParser()

    generation = rag_chain.invoke({"context": context, "question": question})
    return {"question": question, "documents": documents, "generation": generation}

# --- 4. Build the LangGraph Graph ---
workflow = StateGraph(RAGGraphState)
workflow.add_node("retrieve", retrieve_documents_node)
workflow.add_node("generate", generate_response_node)
workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()

# --- 5. Run the RAG Application ---
if __name__ == "__main__":
    print("\n--- Running RAG Query ---")
    query = "What did the president say about Justice Breyer"
    inputs = {"question": query}
    for s in app.stream(inputs):
        print(s)

    print("\n--- Running another RAG Query ---")
    query_2 = "What did the president say about the economy?"
    inputs_2 = {"question": query_2}
    for s in app.stream(inputs_2):
        print(s)
```

This Python code illustrates a Retrieval-Augmented Generation (RAG) pipeline implemented with LangChain and LangGraph. The process begins with the creation of a knowledge base derived from a text document, which is segmented into chunks and transformed into embeddings. These embeddings are then stored in a Weaviate vector store, facilitating efficient information retrieval. A StateGraph in LangGraph is utilized to manage the workflow between two key functions: `retrieve_documents_node` and `generate_response_node`. The `retrieve_documents_node` function queries the vector store to identify relevant document chunks based on the user's input. Subsequently, the `generate_response_node` function utilizes the retrieved information and a predefined prompt template to produce a response using an OpenAI Large Language Model (LLM). The `app.stream` method allows the execution of queries through the RAG pipeline, demonstrating the system's capacity to generate contextually relevant outputs.

<mark>这段 Python 代码展示了基于 LangChain 与 LangGraph 的 RAG 流水线：先从文本构建知识库并切分成文本块，再生成嵌入并写入 Weaviate 向量存储；随后定义 `retrieve_documents_node` 与 `generate_response_node` 两个节点，通过 LangGraph 的 StateGraph 串联流程。前者负责检索相关文本块，后者结合检索结果与提示模板调用 OpenAI 的 LLM 生成回答。`app.stream` 函数则用于执行查询，展示系统生成上下文相关输出的能力。</mark>

---

## At a Glance | <mark>要点速览</mark>

**What:** LLMs possess impressive text generation abilities but are fundamentally limited by their training data. This knowledge is static, meaning it doesn't include real-time information or private, domain-specific data. Consequently, their responses can be outdated, inaccurate, or lack the specific context required for specialized tasks. This gap restricts their reliability for applications demanding current and factual answers.

<mark><strong>问题所在：</strong>LLM 虽然擅长文本生成，但其知识完全基于训练数据，缺乏实时与专有信息，可能导致回答过时、不准确或缺乏必要上下文，从而削弱在事实敏感场景中的可靠性。</mark>

**Why:** The Retrieval-Augmented Generation (RAG) pattern provides a standardized solution by connecting LLMs to external knowledge sources. When a query is received, the system first retrieves relevant information snippets from a specified knowledge base. These snippets are then appended to the original prompt, enriching it with timely and specific context. This augmented prompt is then sent to the LLM, enabling it to generate a response that is accurate, verifiable, and grounded in external data. This process effectively transforms the LLM from a closed-book reasoner into an open-book one, significantly enhancing its utility and trustworthiness.

<mark><strong>解决之道：</strong>检索增强生成通过接入外部知识源来扩展模型输入。系统先检索相关片段再增强提示，确保模型基于实时、可验证数据作答，将 LLM 从「闭卷」推理者转化为「开卷」专家，显著提高可用性与可信度。</mark>

**Rule of thumb:** Use this pattern when you need an LLM to answer questions or generate content based on specific, up-to-date, or proprietary information that was not part of its original training data. It is ideal for building Q&A systems over internal documents, customer support bots, and applications requiring verifiable, fact-based responses with citations.

<mark><strong>经验法则：</strong>当需要模型引用最新、专有或特定信息且必须提供可追溯答案时，应采用 RAG。它尤其适用于内部文档问答、客户支持以及需附带引用的事实类应用。</mark>

---

## Visual Summary | <mark>可视化总结</mark>

Knowledge Retrieval pattern: an AI agent to query and retrieve information from structured databases.

<mark><strong>图示：</strong>知识检索模式中，智能体查询并检索结构化数据库的信息。</mark>

Fig. 3: Knowledge Retrieval pattern—an AI agent to find and synthesize information from the public internet in response to user queries.

<mark><strong>图 3：</strong>知识检索模式中，智能体根据用户问题在公共互联网上查找并综合信息。</mark>

---

## Key Takeaways | <mark>核心要点</mark>

- Knowledge Retrieval (RAG) enhances LLMs by allowing them to access external, up-to-date, and specific information.

  <mark>知识检索（RAG）让 LLM 能够获取外部、最新且特定的信息，从而增强能力。</mark>

- The process involves Retrieval (searching a knowledge base for relevant snippets) and Augmentation (adding these snippets to the LLM's prompt).

  <mark>该流程包括检索（在知识库中查找相关片段）和增强（将片段附到模型提示）两个阶段。</mark>

- RAG helps LLMs overcome limitations like outdated training data, reduces "hallucinations," and enables domain-specific knowledge integration.

  <mark>RAG 能够弥补训练数据过时等问题，降低「幻觉」风险，并整合领域知识。</mark>

- RAG allows for attributable answers, as the LLM's response is grounded in retrieved sources.

  <mark>模型回答基于检索来源，因此可以提供可追溯、可验证的答案。</mark>

- GraphRAG leverages a knowledge graph to understand the relationships between different pieces of information, allowing it to answer complex questions that require synthesizing data from multiple sources.

  <mark>GraphRAG 借助知识图谱理解信息关系，能够回答需综合多源数据的复杂问题。</mark>

- Agentic RAG moves beyond simple information retrieval by using an intelligent agent to actively reason about, validate, and refine external knowledge, ensuring a more accurate and reliable answer.

  <mark>智能体式 RAG 不仅检索，还会主动推理、验证、精炼外部知识，使答案更加精准可靠。</mark>

- Practical applications span enterprise search, customer support, legal research, and personalized recommendations.

  <mark>实践场景覆盖企业搜索、客户支持、法律研究以及个性化推荐等领域。</mark>

---

## Conclusion | <mark>结语</mark>

In conclusion, Retrieval-Augmented Generation (RAG) addresses the core limitation of a Large Language Model's static knowledge by connecting it to external, up-to-date data sources. The process works by first retrieving relevant information snippets and then augmenting the user's prompt, enabling the LLM to generate more accurate and contextually aware responses. This is made possible by foundational technologies like embeddings, semantic search, and vector databases, which find information based on meaning rather than just keywords. By grounding outputs in verifiable data, RAG significantly reduces factual errors and allows for the use of proprietary information, enhancing trust through citations.

<mark>总的来看，检索增强生成通过连接外部最新数据源，弥补了 LLM 静态知识的不足：先检索相关信息，再增强用户提示，使模型能够生成更精准且具上下文意识的回答。嵌入、语义搜索和向量数据库等核心技术让模型能根据语义而非关键词查找信息，并通过可验证的数据减少事实错误，支持引入专有资料并提供引用。</mark>

An advanced evolution, Agentic RAG, introduces a reasoning layer that actively validates, reconciles, and synthesizes retrieved knowledge for even greater reliability. Similarly, specialized approaches like GraphRAG leverage knowledge graphs to navigate explicit data relationships, allowing the system to synthesize answers to highly complex, interconnected queries. This agent can resolve conflicting information, perform multi-step queries, and use external tools to find missing data. While these advanced methods add complexity and latency, they drastically improve the depth and trustworthiness of the final response. Practical applications for these patterns are already transforming industries, from enterprise search and customer support to personalized content delivery. Despite the challenges, RAG is a crucial pattern for making AI more knowledgeable, reliable, and useful. Ultimately, it transforms LLMs from closed-book conversationalists into powerful, open-book reasoning tools.

<mark>进阶形态的智能体式 RAG 为流程引入推理层，主动验证、协调并综合外部知识；GraphRAG 等专门方案依托知识图谱处理复杂关联信息，能够整合多源数据解决问题。这类智能体能够化解冲突信息、执行多步骤查询并调用外部工具补足数据。尽管会增加复杂度与延迟，却显著提升答案的深度与可信度，已在企业搜索、客户支持、个性化内容等行业发挥作用。无论面临何种挑战，RAG 仍是让 AI 更博学、可靠、有用的关键模式，把模型从「闭卷对话者」升级为强大的「开卷推理者」。</mark>

---

## References | <mark>参考资料</mark>

1. Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. https://arxiv.org/abs/2005.11401

   <mark>Lewis, P. 等（2020）。Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks。https://arxiv.org/abs/2005.11401</mark>

2. Google AI for Developers Documentation. Retrieval Augmented Generation. https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview

   <mark>Google AI for Developers Documentation。Retrieval Augmented Generation。https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview</mark>

3. Retrieval-Augmented Generation with Graphs (GraphRAG). https://arxiv.org/abs/2501.00309

   <mark>Retrieval-Augmented Generation with Graphs（GraphRAG）。https://arxiv.org/abs/2501.00309</mark>

4. Monigatti, L. Retrieval-Augmented Generation (RAG): From Theory to LangChain Implementation. https://medium.com/data-science/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2

   <mark>Monigatti, L. Retrieval-Augmented Generation (RAG): From Theory to LangChain Implementation。https://medium.com/data-science/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2</mark>

5. Google Cloud Vertex AI RAG Corpus. https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus#corpus-management

   <mark>Google Cloud Vertex AI RAG Corpus。https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus#corpus-management</mark>
