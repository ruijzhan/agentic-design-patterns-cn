# What makes an AI system an Agent? | <mark>是什么让 AI 系统成为「智能体」？</mark>

In simple terms, an **AI agent** is a system designed to perceive its environment and take actions to achieve a specific goal. It's an evolution from a standard Large Language Model (LLM), enhanced with the abilities to plan, use tools, and interact with its surroundings. Think of an Agentic AI as a smart assistant that learns on the job. It follows a simple, five-step loop to get things done (see Fig.1):

<mark>简单来说，<strong>AI 智能体</strong>是一个能够感知环境并采取行动以实现特定目标的系统。它从标准大语言模型演进而来，增强了规划、工具使用与环境交互能力。可以把智能体 AI 想象成一位边做边学的智能助理：它按一个简单的五步循环来完成任务（见图 1）。</mark>

1. **Get the Mission:** You give it a goal, like "organize my schedule."

 <mark><strong>获取任务：</strong>你给它一个目标，比如「整理我的日程安排」。</mark>

2. **Scan the Scene:** It gathers all the necessary information—reading emails, checking calendars, and accessing contacts—to understand what's happening.

 <mark><strong>扫描环境：</strong>收集所有必要信息——阅读邮件、查看日历、访问联系人——以了解当前状况。</mark>

3. **Think It Through:** It devises a plan of action by considering the optimal approach to achieve the goal.

   <mark><strong>深度思考：</strong>通过权衡实现目标的最优方法来制定行动计划。</mark>

4. **Take Action:** It executes the plan by sending invitations, scheduling meetings, and updating your calendar.

   <mark><strong>采取行动：</strong>通过发送邀请、安排会议、更新日历来执行计划。</mark>

5. **Learn and Get Better:** It observes successful outcomes and adapts accordingly. For example, if a meeting is rescheduled, the system learns from this event to enhance its future performance.

   <mark><strong>学习并改进：</strong>观察成功结果并相应调整。例如，如果会议被重新安排，系统会从中学习以提升未来表现。</mark>

![AI Agent Five-Step Loop](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfxfjS5IHLrkJORnUGchFso6-knfZFKG4bkytsFl1Yh9jf-1SLc9iHZGpSa0VF8ppx2qc7z5bhVXmdKnuvoCDuEr-3hGmFQciP7mT4YRlqpdnDJ8YCBjPd4ynBRWIPSWQ?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig.1:** Agentic AI functions as an intelligent assistant, continuously learning through experience. It operates via a straightforward five-step loop to accomplish tasks.

<mark><strong>图 1：</strong>具智能体特性的人工智能如同智能助理，会通过经验不断学习与改进；它以一个简单的五步循环来完成任务。</mark>

Agents are becoming increasingly popular at a stunning pace. According to recent studies, a majority of large IT companies are actively using these agents, and a fifth of them just started within the past year. The financial markets are also taking notice. By the end of 2024, AI agent startups had raised more than $2 billion, and the market was valued at $5.2 billion. It's expected to explode to nearly $200 billion in value by 2034. In short, all signs point to AI agents playing a massive role in our future economy.

<mark>智能体正以惊人的速度变得越来越受欢迎。根据最近的研究，大多数大型 IT 公司正在积极使用这些智能体，其中五分之一的公司是在过去一年内才开始使用的。金融市场也注意到了这一点。到 2024 年底，AI 智能体初创公司累计融资已经超过 20 亿美元，市场规模为 52 亿美元。预计到 2034 年，价值将爆炸性增长到近 2000 亿美元。简而言之，所有迹象都表明 AI 智能体将在我们未来的经济中发挥巨大作用。</mark>

In just two years, the AI paradigm has shifted dramatically, moving from simple automation to sophisticated, autonomous systems (see Fig. 2). Initially, workflows relied on basic prompts and triggers to process data with LLMs. This evolved with Retrieval-Augmented Generation (RAG), which enhanced reliability by grounding models on factual information. We then saw the development of individual AI Agents capable of using various tools. Today, we are entering the era of Agentic AI, where a team of specialized agents works in concert to achieve complex goals, marking a significant leap in AI's collaborative power.

<mark>短短两年间，AI 的范式便急剧转变：从简单自动化迈向复杂的自主系统（见图 2）。最初，工作流依赖基础提示与触发器，借由 LLM 处理数据；随着检索增强生成（RAG）的出现，范式进化——RAG 将模型输出与事实信息对齐，显著增强了可靠性。随后，个体智能体学会调用多样工具。今天，我们步入智能体 AI 时代：一支由专业化智能体组成的“团队”协作达成复杂目标，AI 的协同能力因此实现跨越式提升。</mark>

![AI Evolution Timeline](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqdjZz18XZjLdDMSbhRoTR3FEVwsYvhcENDaO-6XqhD8ycqNGUPliRRzSn7SS_QdrBi2_BUoUXyHYaB7X94BEUfWwecfGfM2SphmmuAHIhHh2FtP-RofOW1YaU3y_ccw?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig 2.:** Transitioning from LLMs to RAG, then to Agentic RAG, and finally to Agentic AI.

<mark><strong>图 2：</strong>从 LLM 到 RAG，再到智能体 RAG，最终走向智能体 AI 的演进。</mark>

The intent of this book is to discuss the design patterns of how specialized agents can work in concert and collaborate to achieve complex goals, and you will see one paradigm of collaboration and interaction in each chapter.

<mark>本书旨在讨论专业化智能体如何协同工作以实现复杂目标的设计模式，每章都将展示一种协作与交互的范式。</mark>

Before doing that, let's examine examples that span the range of agent complexity (see Fig. 3).

<mark>在此之前，我们先看一些示例：它们覆盖了智能体复杂度的不同层次（见图 3）。</mark>

---

## Level 0: The Core Reasoning Engine | <mark>级别 0：核心推理引擎</mark>

While an LLM is not an agent in itself, it can serve as the reasoning core of a basic agentic system. In a 'Level 0' configuration, the LLM operates without tools, memory, or environment interaction, responding solely based on its pretrained knowledge. Its strength lies in leveraging its extensive training data to explain established concepts. The trade-off for this powerful internal reasoning is a complete lack of current-event awareness. For instance, it would be unable to name the 2025 Oscar winner for "Best Picture" if that information is outside its pre-trained knowledge.

<mark>虽然 LLM 本身不是智能体，但它可以作为基础智能体系统的推理引擎。在「级别 0」配置中，LLM 在无工具、无记忆、无环境交互的前提下运行，仅基于其预训练知识做出回应。它的优势在于借助广泛训练数据解释既定概念；代价则是完全缺乏对时事的感知。例如，若相关信息不在其预训练知识内，它将无法说出 2025 年奥斯卡「最佳影片」得主。</mark>

---

## Level 1: The Connected Problem-Solver | <mark>级别 1：联网问题解决者</mark>

At this level, the LLM becomes a functional agent by connecting to and utilizing external tools. Its problem-solving is no longer limited to its pre-trained knowledge. Instead, it can execute a sequence of actions to gather and process information from sources like the internet (via search) or databases (via Retrieval Augmented Generation, or RAG). For detailed information, refer to Chapter 14.

<mark>在这个级别，LLM 通过连接并使用外部工具，摇身成为功能性智能体。它的解题能力不再局限于预训练知识，而是能执行一系列行动，从互联网（通过搜索）或数据库（通过检索增强生成，即 RAG）等渠道收集与处理信息。更多细节见第 14 章。</mark>

For instance, to find new TV shows, the agent recognizes the need for current information, uses a search tool to find it, and then synthesizes the results. Crucially, it can also use specialized tools for higher accuracy, such as calling a financial API to get the live stock price for AAPL. This ability to interact with the outside world across multiple steps is the core capability of a Level 1 agent.

<mark>例如，为了寻找新电视节目，智能体会识别到需要当前信息，使用搜索工具找到后再综合结果。关键是，它还能使用专门工具来提高准确性，比如调用金融 API 来获取 AAPL 的实时股价。这种跨多个步骤与外部世界交互的能力，正是级别 1 智能体的核心能力。</mark>

---

## Level 2: The Strategic Problem-Solver | <mark>级别 2：战略问题解决者</mark>

At this level, an agent's capabilities expand significantly, encompassing strategic planning, proactive assistance, and self-improvement, with prompt engineering and context engineering as core enabling skills.

<mark>在这个级别，智能体的能力显著扩展，涵盖战略规划、主动协助和自我改进，其中提示工程和上下文工程是核心赋能技能。</mark>

First, the agent moves beyond single-tool use to tackle complex, multi-part problems through strategic problem-solving. As it executes a sequence of actions, it actively performs context engineering: the strategic process of selecting, packaging, and managing the most relevant information for each step. For example, to find a coffee shop between two locations, it first uses a mapping tool. It then engineers this output, curating a short, focused context—perhaps just a list of street names—to feed into a local search tool, preventing cognitive overload and ensuring the second step is efficient and accurate. To achieve maximum accuracy from an AI, it must be given a short, focused, and powerful context. Context engineering is the discipline that accomplishes this by strategically selecting, packaging, and managing the most critical information from all available sources. It effectively curates the model's limited attention to prevent overload and ensure high-quality, efficient performance on any given task. For detailed information, refer to the Appendix A.

<mark>首先，智能体从“只会用单个工具”进阶为“能以策略解题”，以此处理复杂的多部分问题。在执行一系列行动时，它会主动进行“上下文工程”——也就是为每一步选择、打包并管理最相关的信息。例如，要在两个地点之间找到咖啡店，智能体先使用地图工具，然后对输出做工程化处理，精选出简短而聚焦的上下文——也许只是几条街道名——再馈送给本地搜索工具，既避免认知过载，又保证第二步高效准确。要让 AI 达到更高准确性，必须为其提供简短、聚焦且有效的上下文。上下文工程，正是通过策略性地从所有可用来源中挑选、打包与管理最关键信息来达成这一点。它能有效管理模型有限的注意力，避免过载，并确保在任何给定任务上输出高质量且高效率的结果。详见附录 A。</mark>

This level leads to proactive and continuous operation. A travel assistant linked to your email demonstrates this by engineering the context from a verbose flight confirmation email; it selects only the key details (flight numbers, dates, locations) to package for subsequent tool calls to your calendar and a weather API.

<mark>这个级别带来主动且持续的运行方式。连接你邮箱的旅行助手就是一例：它会对冗长的航班确认邮件做上下文工程，仅选取关键细节（航班号、日期、地点）进行打包，以便随后调用日历与天气 API。</mark>

In specialized fields like software engineering, the agent manages an entire workflow by applying this discipline. When assigned a bug report, it reads the report and accesses the codebase, then strategically engineers these large sources of information into a potent, focused context that allows it to efficiently write, test, and submit the correct code patch.

<mark>在软件工程等专业领域，智能体会以此方法管理整条工作流。接到缺陷报告，它会阅读报告并检索代码库，再把海量信息策略性地浓缩为清晰、聚焦的上下文，从而高效地编写、测试并提交正确的代码补丁。</mark>

Finally, the agent achieves self-improvement by refining its own context engineering processes. When it asks for feedback on how a prompt could have been improved, it is learning how to better curate its initial inputs. This allows it to automatically improve how it packages information for future tasks, creating a powerful, automated feedback loop that increases its accuracy and efficiency over time. For detailed information, refer to Chapter 17.

<mark>最后，智能体会通过打磨自身的上下文工程流程实现自我提升。例如，当它征求“如何改进某个提示”的反馈时，实则在学习如何更好地筹备初始输入。由此，它能持续改进未来任务中的信息打包方式，形成强有力的自动反馈回路，随时间推移不断提升准确性与效率。详见第 17 章。</mark>

![Agent Complexity Levels](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf-9C5vJyI8RosgwJM_WtIZ0Jm3Mz89lXNAi1wrGdDNaGqnPzIqMVjHjwVxGSqZdFgb3hVftFyqAj5vIpGlow15KWQNkDRZLh5qPWt4WDwghjUr0IonaOQdOAqBz4WGdlY?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig. 3:** Various instances demonstrating the spectrum of agent complexity.

<mark><strong>图 3：</strong>展示不同复杂度智能体的多种实例。</mark>

---

## Level 3: The Rise of Collaborative Multi-Agent Systems | <mark>级别 3：协作型多智能体系统的兴起</mark>

At Level 3, we see a significant paradigm shift in AI development, moving away from the pursuit of a single, all-powerful super-agent and towards the rise of sophisticated, collaborative multi-agent systems. In essence, this approach recognizes that complex challenges are often best solved not by a single generalist, but by a team of specialists working in concert. This model directly mirrors the structure of a human organization, where different departments are assigned specific roles and collaborate to tackle multi-faceted objectives. The collective strength of such a system lies in this division of labor and the synergy created through coordinated effort. For detailed information, refer to Chapter 7.

<mark>在级别 3，我们见证 AI 开发范式的重大迁移：不再追求单一“全能体”，而是转向更复杂、可协同的多智能体系统。换言之，面对复杂问题，与其依赖一个通才，不如让一支各有所长的队伍并肩作战。这种模式近似于人类组织结构：不同部门分担各自职责，协作应对多维目标。其集体力量源于清晰分工，以及通过协调所产生的协同效应。详见第 7 章。</mark>

To bring this concept to life, consider the intricate workflow of launching a new product. Rather than one agent attempting to handle every aspect, a "Project Manager" agent could serve as the central coordinator. This manager would orchestrate the entire process by delegating tasks to other specialized agents: a "Market Research" agent to gather consumer data, a "Product Design" agent to develop concepts, and a "Marketing" agent to craft promotional materials. The key to their success would be the seamless communication and information sharing between them, ensuring all individual efforts align to achieve the collective goal.

<mark>为了具象化这个概念，不妨以推出新产品的复杂工作流程为例。与其让单个智能体尝试处理每个环节，不如由「项目经理」智能体担任中央协调者。该经理通过把任务委派给其他专业智能体来编排整个过程：「市场研究」智能体收集消费者数据、「产品设计」智能体开发概念、「营销」智能体制作促销材料。成功的关键在于它们之间无缝的沟通和信息共享，确保所有个体努力协调一致以实现集体目标。</mark>

While this vision of autonomous, team-based automation is already being developed, it's important to acknowledge the current hurdles. The effectiveness of such multi-agent systems is presently constrained by the reasoning limitations of LLMs they are using. Furthermore, their ability to genuinely learn from one another and improve as a cohesive unit is still in its early stages. Overcoming these technological bottlenecks is the critical next step, and doing so will unlock the profound promise of this level: the ability to automate entire business workflows from start to finish.

<mark>虽然这种基于团队的自主自动化愿景已经在开发中，但必须承认当前的障碍。这种多智能体系统的有效性目前受到所用模型推理能力限制的约束。此外，它们真正相互学习并作为一个有凝聚力的整体来改进的能力仍处于早期阶段。克服这些技术瓶颈是关键的下一步，而这将释放出这个级别的巨大潜力：从头到尾自动化整个业务工作流程。</mark>

---

## The Future of Agents: Top 5 Hypotheses | <mark>智能体的未来：五大假设</mark>

AI agent development is progressing at an unprecedented pace across domains such as software automation, scientific research, and customer service among others. While current systems are impressive, they are just the beginning. The next wave of innovation will likely focus on making agents more reliable, collaborative, and deeply integrated into our lives. Here are five leading hypotheses for what's next (see Fig. 4).

<mark>AI 智能体开发正在软件自动化、科学研究和客户服务等领域以前所未有的速度推进。虽然当前的系统令人印象深刻，但它们仅仅是开始。下一波创新浪潮可能会专注于使智能体更可靠、更协作，并深度集成到我们的生活中。以下是关于下一步发展的五个主要假设（见图 4）。</mark>

### Hypothesis 1: The Emergence of the Generalist Agent | <mark>假设 1：通用智能体的崛起</mark>

The first hypothesis is that AI agents will evolve from narrow specialists into true generalists capable of managing complex, ambiguous, and long-term goals with high reliability. For instance, you could give an agent a simple prompt like, "Plan my company's offsite retreat for 30 people in Lisbon next quarter." The agent would then manage the entire project for weeks, handling everything from budget approvals and flight negotiations to venue selection and creating a detailed itinerary from employee feedback, all while providing regular updates. Achieving this level of autonomy will require fundamental breakthroughs in AI reasoning, memory, and near-perfect reliability. An alternative, yet not mutually exclusive, approach is the rise of Small Language Models (SLMs). This "Lego-like" concept involves composing systems from small, specialized expert agents rather than scaling up a single monolithic model. This method promises systems that are cheaper, faster to debug, and easier to deploy. Ultimately, the development of large generalist models and the composition of smaller specialized ones are both plausible paths forward, and they could even complement each other.

<mark>假设之一是，AI 代理会从专门化的狭域系统演进为真正的通用体，能够以高可靠性处理复杂、模糊且长期的目标。例如，你可以给智能体一个简单的提示，如「为下个季度在里斯本为 30 人规划我们公司的异地团建活动」。智能体随后将管理整个项目数周，处理从预算审批与航班谈判到场地选择，以及依据员工反馈创建详细行程等全部事项，并持续提供更新。实现这种自主水平将需要在 AI 推理、记忆与近乎完美可靠性方面取得根本性突破。另一条并非互斥的路径，是小语言模型的兴起。这种「乐高式」理念，是由小型且专门的专家智能体组合系统，而非一味扩展单一的整体模型。此法有望带来更低成本、更快调试与更易部署的系统。总之，发展大型通用模型与组合小型专用模型都是合理的路线，两者也可能互为补充。</mark>

### Hypothesis 2: Deep Personalization and Proactive Goal Discovery | <mark>假设 2：深度个性化和主动发现用户目标</mark>

The second hypothesis posits that agents will become deeply personalised and proactive partners. We are witnessing the emergence of a new class of agent: the proactive partner. By learning from your unique patterns and goals, these systems are beginning to shift from just following orders to anticipating your needs. AI systems operate as agents when they move beyond simply responding to chats or instructions. They initiate and execute tasks on behalf of the user, actively collaborating in the process. This moves beyond simple task execution into the realm of proactive goal discovery.

<mark>第二个假设认为智能体将成为深度个性化且主动的合作伙伴。我们正在见证一个新类别智能体的出现：主动合作伙伴。通过学习你独特的模式与目标，这些系统开始从仅仅遵循命令，转向预测你的需求。当 AI 系统超越简单地响应聊天或指令时，它们就以智能体的方式运行。它们代表用户发起并执行任务，在过程中积极协作。这超越了简单的任务执行，进入主动目标发现的领域。</mark>

For instance, if you're exploring sustainable energy, the agent might identify your latent goal and proactively support it by suggesting courses or summarizing research. While these systems are still developing, their trajectory is clear. They will become increasingly proactive, learning to take initiative on your behalf when highly confident that the action will be helpful. Ultimately, the agent becomes an indispensable ally, helping you discover and achieve ambitions you have yet to fully articulate.

<mark>例如，如果你正在探索可持续能源，智能体可能会识别你的潜在目标，并通过建议课程或总结研究来主动支持它。虽然这些系统仍在发展中，但它们的轨迹很清楚。它们将变得越来越主动，并在高度确信该行动将有帮助时，学会代表你采取行动。最终，智能体将成为不可或缺的盟友，帮助你发现并实现你尚未完全阐明的抱负。</mark>

![Future Agent Hypotheses](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeEML8n7ITjKYHbdYpIlud4Z5tyVxO1CNwaSzTPuTZhkbddy6fMO8rARp_RnFg99v9d4GmKXw-7iZcFHsPUiP8uUPjxXUUAOWFa-2AHz96YHhvSVbk_HuoC44Zx9Iu1plk?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig. 4:** Five hypotheses about the future of agents

<mark><strong>图 4：</strong>关于智能体未来的五个假设</mark>

### Hypothesis 3: Embodiment and Physical World Interaction | <mark>假设 3：具身化和物理世界交互</mark>

This hypothesis foresees agents breaking free from their purely digital confines to operate in the physical world. By integrating agentic AI with robotics, we will see the rise of "embodied agents." Instead of just booking a handyman, you might ask your home agent to fix a leaky tap. The agent would use its vision sensors to perceive the problem, access a library of plumbing knowledge to formulate a plan, and then control its robotic manipulators with precision to perform the repair. This would represent a monumental step, bridging the gap between digital intelligence and physical action, and transforming everything from manufacturing and logistics to elder care and home maintenance.

<mark>这个假设预见智能体突破其纯数字边界，在物理世界中运作。通过将智能体 AI 与机器人技术集成，我们将看到「具身智能体」的兴起。与其只是预约修理工，你可能会要求你的家庭智能体修复漏水的水龙头。智能体将使用其视觉传感器来感知问题，访问管道知识库来制定计划，然后精确控制其机器人执行器来完成修复。这将代表一个里程碑式步骤，弥合数字智能与物理行动之间的差距，并转变从制造与物流到老年护理与家庭维护的一切。</mark>

### Hypothesis 4: The Agent-Driven Economy | <mark>假设 4：智能体驱动的经济</mark>

The fourth hypothesis is that highly autonomous agents will become active participants in the economy, creating new markets and business models. We could see agents acting as independent economic entities, tasked with maximising a specific outcome, such as profit. An entrepreneur could launch an agent to run an entire e-commerce business. The agent would identify trending products by analysing social media, generate marketing copy and visuals, manage supply chain logistics by interacting with other automated systems, and dynamically adjust pricing based on real-time demand. This shift would create a new, hyper-efficient "agent economy" operating at a speed and scale impossible for humans to manage directly.

<mark>第四个假设是，高度自主的智能体将成为经济中的积极参与者，创造新的市场与商业模式。我们可能会看到智能体作为独立的经济实体，负责最大化特定结果（如利润）。企业家可以启动一个智能体来运营整个电子商务业务。智能体将通过分析社交媒体识别热门产品，生成营销文案与视觉内容，通过与其他自动化系统交互管理供应链物流，并基于实时需求动态调整定价。这种转变将催生全新的、超高效的「智能体经济」，以超越人类直接管理的速度与规模运行。</mark>

### Hypothesis 5: The Goal-Driven, Metamorphic Multi-Agent System | <mark>假设 5：目标驱动、可变形的多智能体系统</mark>

This hypothesis posits the emergence of intelligent systems that operate not from explicit programming, but from a declared goal. The user simply states the desired outcome, and the system autonomously figures out how to achieve it. This marks a fundamental shift towards metamorphic multi-agent systems capable of true self-improvement at both the individual and collective levels.

<mark>这个假设假定智能系统的出现，它们不是从显式编程运行，而是从声明的目标运行。用户只需说明期望的结果，系统就会自主找出如何实现它。这标志着向能够在个体和集体层面进行真正自我改进的变形多智能体系统的根本转变。</mark>

This system would be a dynamic entity, not a single agent. It would have the ability to analyze its own performance and modify the topology of its multi-agent workforce, creating, duplicating, or removing agents as needed to form the most effective team for the task at hand. This evolution happens at multiple levels:

<mark>这个系统将是一个动态实体，而不是单一智能体。它将有能力分析自己的性能并修改其多智能体工作团队的拓扑结构，根据需要创建、复制或移除智能体，以形成最有效的团队来处理手头的任务。这种进化发生在多个层面：</mark>

- **Architectural Modification:** At the deepest level, individual agents can rewrite their own source code and re-architect their internal structures for higher efficiency, as in the original hypothesis.

- <mark><strong>架构修改：</strong>在最深层次，个体智能体可以重写它们自己的源代码并重新架构它们的内部结构以获得更高效率，如原始假设中所述。</mark>

- **Instructional Modification:** At a higher level, the system continuously performs automatic prompt engineering and context engineering. It refines the instructions and information given to each agent, ensuring they are operating with optimal guidance without any human intervention.

- <mark><strong>指令修改：</strong>在更高层次，系统持续执行自动提示工程和上下文工程。它改进给予每个智能体的指令和信息，确保它们在没有任何人工干预的情况下以最优指导运行。</mark>

For instance, an entrepreneur would simply declare the intent: "Launch a successful e-commerce business selling artisanal coffee." The system, without further programming, would spring into action. It might initially spawn a "Market Research" agent and a "Branding" agent. Based on the initial findings, it could decide to remove the branding agent and spawn three new specialized agents: a "Logo Design" agent, a "Webstore Platform" agent, and a "Supply Chain" agent. It would constantly tune their internal prompts for better performance. If the webstore agent becomes a bottleneck, the system might duplicate it into three parallel agents to work on different parts of the site, effectively re-architecting its own structure on the fly to best achieve the declared goal.

<mark>例如，企业家只需声明一个意图：「启动一个成功的手工咖啡电商业务」。系统无需进一步编程即刻行动：它可能先生成「市场研究」与「品牌」两个智能体；随后基于初步结论，移除品牌智能体，并衍生出三个更细分的角色：「标志设计」「网店平台」「供应链」。系统会持续调校它们的内部提示以优化表现。若网店平台成为瓶颈，系统还会将其拆分为三个并行智能体，分别负责站点不同部分，实时重构自身结构，以更好地实现既定目标。</mark>

---

## Conclusion | <mark>总结</mark>

In essence, an AI agent represents a significant leap from traditional models, functioning as an autonomous system that perceives, plans, and acts to achieve specific goals. The evolution of this technology is advancing from single, tool-using agents to complex, collaborative multi-agent systems that tackle multifaceted objectives. Future hypotheses predict the emergence of generalist, personalized, and even physically embodied agents that will become active participants in the economy. This ongoing development signals a major paradigm shift towards self-improving, goal-driven systems poised to automate entire workflows and fundamentally redefine our relationship with technology.

<mark>归根就底，AI 智能体相较传统模型实现了重要跃迁：它以能感知、能规划、能行动以达成特定目标的自主系统形态运行。技术正从单一、依赖工具的智能体，演进为可协作、能处理多元目标的复杂多智能体系统。未来，具通用能力、深度个性化，乃至具身实体的智能体都有望成为经济中的积极参与者。这一进程预示着以目标驱动、可自我改进的系统时代到来：它们将自动化端到端工作流，并从根本上重塑我们与技术的关系。</mark>

---

## References | <mark>参考文献</mark>

1. Cloudera, Inc. (April 2025), 96% of enterprises are increasing their use of AI agents. [https://www.cloudera.com/about/news-and-blogs/press-releases/2025-04-16-96-percent-of-enterprises-are-expanding-use-of-ai-agents-according-to-latest-data-from-cloudera.html](https://www.cloudera.com/about/news-and-blogs/press-releases/2025-04-16-96-percent-of-enterprises-are-expanding-use-of-ai-agents-according-to-latest-data-from-cloudera.html)

   <mark>Cloudera, Inc.（2025 年 4 月），96% 的企业正在增加对 AI 智能体的使用。</mark>

2. Autonomous generative AI agents: [https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/autonomous-generative-ai-agents-still-under-development.html](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/autonomous-generative-ai-agents-still-under-development.html)

   <mark>自主生成式 AI 智能体：</mark>

3. Market.us. Global Agentic AI Market Size, Trends and Forecast 2025–2034. [https://market.us/report/agentic-ai-market/](https://market.us/report/agentic-ai-market/)

   <mark>Market.us. 全球智能体 AI 市场规模、趋势和 2025-2034 年预测。</mark>

---
