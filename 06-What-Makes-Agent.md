# What makes an AI system an Agent? | <mark>是什么让 AI 系统成为「智能体」？</mark>

---

In simple terms, an **AI agent** is a system designed to perceive its environment and take actions to achieve a specific goal. It's an evolution from a standard Large Language Model (LLM), enhanced with the abilities to plan, use tools, and interact with its surroundings. Think of an Agentic AI as a smart assistant that learns on the job. It follows a simple, five-step loop to get things done (see Fig.1):

<mark>简单来说，<strong>AI 智能体</strong>是一个能够感知环境并采取行动以实现特定目标的系统。它是标准大语言模型（LLM）的演进版本，增强了规划、工具使用和环境交互能力。可以将智能体 AI 想象成一个在工作中学习的智能助手，它遵循一个简单的五步循环来完成任务（见图 1）：</mark>

1. **Get the Mission:** You give it a goal, like "organize my schedule."

1. <mark><strong>获取任务：</strong>你给它一个目标，比如「整理我的日程安排」。</mark>

2. **Scan the Scene:** It gathers all the necessary information—reading emails, checking calendars, and accessing contacts—to understand what's happening.

2. <mark><strong>扫描环境：</strong>收集所有必要信息——阅读邮件、查看日历、访问联系人——以了解当前状况。</mark>

3. **Think It Through:** It devises a plan of action by considering the optimal approach to achieve the goal.

3. <mark><strong>深度思考：</strong>通过权衡实现目标的最优方法来制定行动计划。</mark>

4. **Take Action:** It executes the plan by sending invitations, scheduling meetings, and updating your calendar.

4. <mark><strong>采取行动：</strong>通过发送邀请、安排会议、更新日历来执行计划。</mark>

5. **Learn and Get Better:** It observes successful outcomes and adapts accordingly. For example, if a meeting is rescheduled, the system learns from this event to enhance its future performance.

5. <mark><strong>学习并改进：</strong>观察成功结果并相应调整。例如，如果会议被重新安排，系统会从中学习以提升未来表现。</mark>

![AI Agent Five-Step Loop](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfxfjS5IHLrkJORnUGchFso6-knfZFKG4bkytsFl1Yh9jf-1SLc9iHZGpSa0VF8ppx2qc7z5bhVXmdKnuvoCDuEr-3hGmFQciP7mT4YRlqpdnDJ8YCBjPd4ynBRWIPSWQ?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig.1:** Agentic AI functions as an intelligent assistant, continuously learning through experience. It operates via a straightforward five-step loop to accomplish tasks.

<mark><strong>图 1：</strong>智能体 AI 作为一个智能助手运作，通过经验持续学习。它通过一个简单的五步循环来完成任务。</mark>

Agents are becoming increasingly popular at a stunning pace. According to recent studies, a majority of large IT companies are actively using these agents, and a fifth of them just started within the past year. The financial markets are also taking notice. By the end of 2024, AI agent startups had raised more than $2 billion, and the market was valued at $5.2 billion. It's expected to explode to nearly $200 billion in value by 2034. In short, all signs point to AI agents playing a massive role in our future economy.

<mark>智能体正以惊人的速度变得越来越受欢迎。根据最近的研究，大多数大型 IT 公司正在积极使用这些智能体，其中五分之一的公司是在过去一年内才开始使用的。金融市场也注意到了这一点。到 2024 年底，AI 智能体初创公司已经筹集了超过 20 亿美元，市场估值为 52 亿美元。预计到 2034 年，价值将爆炸性增长到近 2000 亿美元。简而言之，所有迹象都表明 AI 智能体将在我们未来的经济中发挥巨大作用。</mark>

In just two years, the AI paradigm has shifted dramatically, moving from simple automation to sophisticated, autonomous systems (see Fig. 2). Initially, workflows relied on basic prompts and triggers to process data with LLMs. This evolved with Retrieval-Augmented Generation (RAG), which enhanced reliability by grounding models on factual information. We then saw the development of individual AI Agents capable of using various tools. Today, we are entering the era of Agentic AI, where a team of specialized agents works in concert to achieve complex goals, marking a significant leap in AI's collaborative power.

<mark>仅仅两年时间，AI 范式就发生了戏剧性转变，从简单自动化转向复杂自主系统（见图 2）。最初，工作流依赖基本提示和触发器来用 LLM 处理数据。随着检索增强生成（RAG）的出现，这种方式得以进化：RAG 通过锚定事实信息来提高模型可靠性。随后我们看到了能够使用各种工具的单体 AI 智能体的发展。今天，我们正进入智能体 AI 时代，专业化智能体团队协同工作以实现复杂目标，标志着 AI 协作能力的重大飞跃。</mark>

![AI Evolution Timeline](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqdjZz18XZjLdDMSbhRoTR3FEVwsYvhcENDaO-6XqhD8ycqNGUPliRRzSn7SS_QdrBi2_BUoUXyHYaB7X94BEUfWwecfGfM2SphmmuAHIhHh2FtP-RofOW1YaU3y_ccw?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig 2.:** Transitioning from LLMs to RAG, then to Agentic RAG, and finally to Agentic AI.

<mark><strong>图 2：</strong>从 LLM 到 RAG，再到智能体 RAG，最后到智能体 AI 的转变。</mark>

The intent of this book is to discuss the design patterns of how specialized agents can work in concert and collaborate to achieve complex goals, and you will see one paradigm of collaboration and interaction in each chapter.

<mark>本书旨在讨论专业化智能体如何协同工作以实现复杂目标的设计模式，每章都将展示一种协作与交互的范式。</mark>

Before doing that, let's examine examples that span the range of agent complexity (see Fig. 3).

<mark>在此之前，让我们先看看跨越智能体复杂性谱的一些示例（见图 3）。</mark>

---

## Level 0: The Core Reasoning Engine | <mark>级别 0：核心推理引擎</mark>

While an LLM is not an agent in itself, it can serve as the reasoning core of a basic agentic system. In a 'Level 0' configuration, the LLM operates without tools, memory, or environment interaction, responding solely based on its pretrained knowledge. Its strength lies in leveraging its extensive training data to explain established concepts. The trade-off for this powerful internal reasoning is a complete lack of current-event awareness. For instance, it would be unable to name the 2025 Oscar winner for "Best Picture" if that information is outside its pre-trained knowledge.

<mark>虽然 LLM 本身不是智能体，但它可以作为基本智能体系统的推理核心。在「级别 0」配置中，LLM 在没有工具、记忆或环境交互的情况下运行，仅基于其预训练知识进行响应。它的优势在于利用其广泛的训练数据来解释既定概念。这种强大内部推理的代价是完全缺乏对时事的感知。例如，如果这些信息在其预训练知识之外，它将无法说出 2025 年奥斯卡「最佳影片」获得者。</mark>

---

## Level 1: The Connected Problem-Solver | <mark>级别 1：联网问题解决者</mark>

At this level, the LLM becomes a functional agent by connecting to and utilizing external tools. Its problem-solving is no longer limited to its pre-trained knowledge. Instead, it can execute a sequence of actions to gather and process information from sources like the internet (via search) or databases (via Retrieval Augmented Generation, or RAG). For detailed information, refer to Chapter 14.

<mark>在这个级别，LLM 通过连接和使用外部工具成为功能性智能体。其问题解决不再局限于预训练知识，而是可以执行一系列行动来收集和处理来自互联网（通过搜索）或数据库（通过检索增强生成，即 RAG）等来源的信息。详细信息请参阅第 14 章。</mark>

For instance, to find new TV shows, the agent recognizes the need for current information, uses a search tool to find it, and then synthesizes the results. Crucially, it can also use specialized tools for higher accuracy, such as calling a financial API to get the live stock price for AAPL. This ability to interact with the outside world across multiple steps is the core capability of a Level 1 agent.

<mark>例如，为了寻找新电视节目，智能体会识别到需要当前信息，使用搜索工具找到后再综合结果。关键是，它还能使用专门工具来提高准确性，比如调用金融 API 来获取 AAPL 的实时股价。这种跨多个步骤与外部世界交互的能力，正是级别 1 智能体的核心能力。</mark>

---

## Level 2: The Strategic Problem-Solver | <mark>级别 2：战略问题解决者</mark>

At this level, an agent's capabilities expand significantly, encompassing strategic planning, proactive assistance, and self-improvement, with prompt engineering and context engineering as core enabling skills.

<mark>在这个级别，智能体的能力显著扩展，涵盖战略规划、主动协助和自我改进，其中提示工程和上下文工程是核心赋能技能。</mark>

First, the agent moves beyond single-tool use to tackle complex, multi-part problems through strategic problem-solving. As it executes a sequence of actions, it actively performs context engineering: the strategic process of selecting, packaging, and managing the most relevant information for each step. For example, to find a coffee shop between two locations, it first uses a mapping tool. It then engineers this output, curating a short, focused context—perhaps just a list of street names—to feed into a local search tool, preventing cognitive overload and ensuring the second step is efficient and accurate. To achieve maximum accuracy from an AI, it must be given a short, focused, and powerful context. Context engineering is the discipline that accomplishes this by strategically selecting, packaging, and managing the most critical information from all available sources. It effectively curates the model's limited attention to prevent overload and ensure high-quality, efficient performance on any given task. For detailed information, refer to the Appendix A.

<mark>首先，智能体超越单一工具使用，通过战略性问题解决来处理复杂的多部分问题。在执行一系列行动时，它会主动执行上下文工程：即为每个步骤选择、打包和管理最相关信息的战略过程。例如，为了在两个位置之间找到咖啡店，它先使用地图工具，然后对输出进行工程化，精选出简短聚焦的上下文——也许只是街道名称列表——输入到本地搜索工具中，这样既防止认知过载，又确保第二步高效准确。要让 AI 达到最高准确性，必须为其提供简短、聚焦且有力的上下文。上下文工程正是通过战略性地从所有可用来源中选择、打包和管理最关键信息来实现这一目标。它有效管理模型有限的注意力，防止过载并确保在任何给定任务上的高质量、高效表现。详细信息请参阅附录 A。</mark>

This level leads to proactive and continuous operation. A travel assistant linked to your email demonstrates this by engineering the context from a verbose flight confirmation email; it selects only the key details (flight numbers, dates, locations) to package for subsequent tool calls to your calendar and a weather API.

<mark>这个级别实现了主动且持续的运行方式。连接到你邮箱的旅行助手演示了这一点：它从冗长的航班确认邮件中进行上下文工程化，仅选择关键细节（航班号、日期、位置）进行打包，以便后续调用日历和天气 API。</mark>

In specialized fields like software engineering, the agent manages an entire workflow by applying this discipline. When assigned a bug report, it reads the report and accesses the codebase, then strategically engineers these large sources of information into a potent, focused context that allows it to efficiently write, test, and submit the correct code patch.

<mark>在软件工程等专业领域，智能体通过应用这一方法来管理整个工作流程。当被分配到错误报告时，它会读取报告并访问代码库，然后战略性地将这些大量信息源工程化为有力聚焦的上下文，使其能够高效编写、测试和提交正确的代码补丁。</mark>

Finally, the agent achieves self-improvement by refining its own context engineering processes. When it asks for feedback on how a prompt could have been improved, it is learning how to better curate its initial inputs. This allows it to automatically improve how it packages information for future tasks, creating a powerful, automated feedback loop that increases its accuracy and efficiency over time. For detailed information, refer to Chapter 17.

<mark>最后，智能体通过精化自身的上下文工程过程来实现自我改进。当它询问如何改进提示的反馈时，它正在学习如何更好地策划初始输入。这使它能够自动改进为未来任务打包信息的方式，创建一个强大的自动化反馈循环，随时间不断提高准确性和效率。详细信息请参阅第 17 章。</mark>

![Agent Complexity Levels](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf-9C5vJyI8RosgwJM_WtIZ0Jm3Mz89lXNAi1wrGdDNaGqnPzIqMVjHjwVxGSqZdFgb3hVftFyqAj5vIpGlow15KWQNkDRZLh5qPWt4WDwghjUr0IonaOQdOAqBz4WGdlY?key=x3M3vSiJlWTAiO_iRgvijg)

**Fig. 3:** Various instances demonstrating the spectrum of agent complexity.

<mark><strong>图 3：</strong>演示智能体复杂性谱的各种实例。</mark>

---

## Level 3: The Rise of Collaborative Multi-Agent Systems | <mark>级别 3：协作多智能体系统的兴起</mark>

At Level 3, we see a significant paradigm shift in AI development, moving away from the pursuit of a single, all-powerful super-agent and towards the rise of sophisticated, collaborative multi-agent systems. In essence, this approach recognizes that complex challenges are often best solved not by a single generalist, but by a team of specialists working in concert. This model directly mirrors the structure of a human organization, where different departments are assigned specific roles and collaborate to tackle multi-faceted objectives. The collective strength of such a system lies in this division of labor and the synergy created through coordinated effort. For detailed information, refer to Chapter 7.

<mark>在级别 3，我们看到了 AI 开发中的重大范式转变：从追求单一的全能超级智能体，转向复杂协作多智能体系统的兴起。从本质上讲，这种方法认识到复杂挑战往往不是由单一通才最好解决，而是由协同工作的专家团队来解决。这种模式直接映射了人类组织的结构，其中不同部门被分配特定角色并协作处理多面向的目标。这样一个系统的集体力量在于分工和通过协调努力创造的协同效应。详细信息请参阅第 7 章。</mark>

To bring this concept to life, consider the intricate workflow of launching a new product. Rather than one agent attempting to handle every aspect, a "Project Manager" agent could serve as the central coordinator. This manager would orchestrate the entire process by delegating tasks to other specialized agents: a "Market Research" agent to gather consumer data, a "Product Design" agent to develop concepts, and a "Marketing" agent to craft promotional materials. The key to their success would be the seamless communication and information sharing between them, ensuring all individual efforts align to achieve the collective goal.

<mark>为了具象化这个概念，不妨以推出新产品的复杂工作流程为例。与其让单个智能体尝试处理每个环节，不如由「项目经理」智能体担任中央协调者。该经理通过把任务委派给其他专业智能体来编排整个过程：「市场研究」智能体收集消费者数据、「产品设计」智能体开发概念、「营销」智能体制作促销材料。成功的关键在于它们之间无缝的沟通和信息共享，确保所有个体努力协调一致以实现集体目标。</mark>

While this vision of autonomous, team-based automation is already being developed, it's important to acknowledge the current hurdles. The effectiveness of such multi-agent systems is presently constrained by the reasoning limitations of LLMs they are using. Furthermore, their ability to genuinely learn from one another and improve as a cohesive unit is still in its early stages. Overcoming these technological bottlenecks is the critical next step, and doing so will unlock the profound promise of this level: the ability to automate entire business workflows from start to finish.

<mark>虽然这种基于团队的自主自动化愿景已经在开发中，但必须承认当前的障碍。这种多智能体系统的有效性目前受到所用 LLM 推理能力限制的约束。此外，它们真正相互学习并作为一个有凝聚力的整体来改进的能力仍处于早期阶段。克服这些技术瓶颈是关键的下一步，而这将释放出这个级别的巨大潜力：从头到尾自动化整个业务工作流程。</mark>

---

## The Future of Agents: Top 5 Hypotheses | <mark>智能体的未来：五大假设</mark>

AI agent development is progressing at an unprecedented pace across domains such as software automation, scientific research, and customer service among others. While current systems are impressive, they are just the beginning. The next wave of innovation will likely focus on making agents more reliable, collaborative, and deeply integrated into our lives. Here are five leading hypotheses for what's next (see Fig. 4).

<mark>AI 智能体开发正在软件自动化、科学研究和客户服务等领域以前所未有的速度推进。虽然当前的系统令人印象深刻，但它们仅仅是开始。下一波创新浪潮可能会专注于使智能体更可靠、更协作，并深度集成到我们的生活中。以下是关于下一步发展的五个主要假设（见图 4）。</mark>

### Hypothesis 1: The Emergence of the Generalist Agent | <mark>假设 1：通才智能体的出现</mark>

The first hypothesis is that AI agents will evolve from narrow specialists into true generalists capable of managing complex, ambiguous, and long-term goals with high reliability. For instance, you could give an agent a simple prompt like, "Plan my company's offsite retreat for 30 people in Lisbon next quarter." The agent would then manage the entire project for weeks, handling everything from budget approvals and flight negotiations to venue selection and creating a detailed itinerary from employee feedback, all while providing regular updates. Achieving this level of autonomy will require fundamental breakthroughs in AI reasoning, memory, and near-perfect reliability. An alternative, yet not mutually exclusive, approach is the rise of Small Language Models (SLMs). This "Lego-like" concept involves composing systems from small, specialized expert agents rather than scaling up a single monolithic model. This method promises systems that are cheaper, faster to debug, and easier to deploy. Ultimately, the development of large generalist models and the composition of smaller specialized ones are both plausible paths forward, and they could even complement each other.

<mark>第一个假设是，AI 智能体将从狭窄的专家，发展为能够高可靠性地管理复杂、模糊与长期目标的真正通才。例如，你可以给智能体一个简单的提示，如「为下个季度在里斯本为 30 人规划我们公司的异地团建活动」。智能体随后将管理整个项目数周，处理从预算审批与航班谈判到场地选择，以及依据员工反馈创建详细行程等全部事项，并持续提供更新。实现这种自主水平将需要在 AI 推理、记忆与近乎完美可靠性方面取得根本性突破。另一条并非互斥的路径，是小语言模型（SLM）的兴起。这种「乐高式」理念，是由小型且专门的专家智能体组合系统，而非一味扩展单一的整体模型。此法有望带来更低成本、更快调试与更易部署的系统。最终，大型通才模型的演进与更小专门模型的组合，都是可行的前进道路，甚至能够相辅相成。</mark>

### Hypothesis 2: Deep Personalization and Proactive Goal Discovery | <mark>假设 2：深度个性化和主动目标发现</mark>

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

### Hypothesis 5: The Goal-Driven, Metamorphic Multi-Agent System | <mark>假设 5：目标驱动的变形多智能体系统</mark>

This hypothesis posits the emergence of intelligent systems that operate not from explicit programming, but from a declared goal. The user simply states the desired outcome, and the system autonomously figures out how to achieve it. This marks a fundamental shift towards metamorphic multi-agent systems capable of true self-improvement at both the individual and collective levels.

<mark>这个假设假定智能系统的出现，它们不是从显式编程运行，而是从声明的目标运行。用户只需说明期望的结果，系统就会自主找出如何实现它。这标志着向能够在个体和集体层面进行真正自我改进的变形多智能体系统的根本转变。</mark>

This system would be a dynamic entity, not a single agent. It would have the ability to analyze its own performance and modify the topology of its multi-agent workforce, creating, duplicating, or removing agents as needed to form the most effective team for the task at hand. This evolution happens at multiple levels:

<mark>这个系统将是一个动态实体，而不是单一智能体。它将有能力分析自己的性能并修改其多智能体工作团队的拓扑结构，根据需要创建、复制或移除智能体，以形成最有效的团队来处理手头的任务。这种进化发生在多个层面：</mark>

- **Architectural Modification:** At the deepest level, individual agents can rewrite their own source code and re-architect their internal structures for higher efficiency, as in the original hypothesis.

- <mark><strong>架构修改：</strong>在最深层次，个体智能体可以重写它们自己的源代码并重新架构它们的内部结构以获得更高效率，如原始假设中所述。</mark>

- **Instructional Modification:** At a higher level, the system continuously performs automatic prompt engineering and context engineering. It refines the instructions and information given to each agent, ensuring they are operating with optimal guidance without any human intervention.

- <mark><strong>指令修改：</strong>在更高层次，系统持续执行自动提示工程和上下文工程。它改进给予每个智能体的指令和信息，确保它们在没有任何人工干预的情况下以最优指导运行。</mark>

For instance, an entrepreneur would simply declare the intent: "Launch a successful e-commerce business selling artisanal coffee." The system, without further programming, would spring into action. It might initially spawn a "Market Research" agent and a "Branding" agent. Based on the initial findings, it could decide to remove the branding agent and spawn three new specialized agents: a "Logo Design" agent, a "Webstore Platform" agent, and a "Supply Chain" agent. It would constantly tune their internal prompts for better performance. If the webstore agent becomes a bottleneck, the system might duplicate it into three parallel agents to work on different parts of the site, effectively re-architecting its own structure on the fly to best achieve the declared goal.

<mark>例如，企业家将简单地声明意图：「启动一个成功的手工咖啡电子商务业务」。系统在没有进一步编程的情况下将立即采取行动。它可能最初生成一个「市场研究」智能体和一个「品牌」智能体。基于初始发现，它可能决定移除品牌智能体，并生成三个新的专门智能体：一个「标志设计」智能体、一个「网店平台」智能体和一个「供应链」智能体。它会不断调整它们的内部提示以获得更好性能。如果网店智能体成为瓶颈，系统可能将其复制为三个并行智能体来处理网站的不同部分，动态地重构其自身结构，以更好地实现声明的目标。</mark>

---

## Conclusion | <mark>结论</mark>

In essence, an AI agent represents a significant leap from traditional models, functioning as an autonomous system that perceives, plans, and acts to achieve specific goals. The evolution of this technology is advancing from single, tool-using agents to complex, collaborative multi-agent systems that tackle multifaceted objectives. Future hypotheses predict the emergence of generalist, personalized, and even physically embodied agents that will become active participants in the economy. This ongoing development signals a major paradigm shift towards self-improving, goal-driven systems poised to automate entire workflows and fundamentally redefine our relationship with technology.

<mark>从本质上讲，AI 智能体代表着相较于传统模型的重大飞跃：它作为能够感知、规划与行动以实现特定目标的自主系统运行。这项技术正从单一、依赖工具的智能体，演进为能够处理多元目标的复杂协作式多智能体系统。前瞻性设想预示通才、个性化，甚至物理具身的智能体将出现，并成为经济中的积极参与者。这一持续演进标志着向自我改进、目标驱动系统的重大范式转变：这些系统正准备自动化完整工作流程，并从根本上重塑我们与技术的关系。</mark>

---

## References | <mark>参考文献</mark>

1. Cloudera, Inc. (April 2025), 96% of enterprises are increasing their use of AI agents. [https://www.cloudera.com/about/news-and-blogs/press-releases/2025-04-16-96-percent-of-enterprises-are-expanding-use-of-ai-agents-according-to-latest-data-from-cloudera.html](https://www.cloudera.com/about/news-and-blogs/press-releases/2025-04-16-96-percent-of-enterprises-are-expanding-use-of-ai-agents-according-to-latest-data-from-cloudera.html)

1. <mark>Cloudera, Inc.（2025 年 4 月），96% 的企业正在增加对 AI 智能体的使用。</mark>

2. Autonomous generative AI agents: [https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/autonomous-generative-ai-agents-still-under-development.html](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/autonomous-generative-ai-agents-still-under-development.html)

2. <mark>自主生成式 AI 智能体：</mark>

3. Market.us. Global Agentic AI Market Size, Trends and Forecast 2025–2034. [https://market.us/report/agentic-ai-market/](https://market.us/report/agentic-ai-market/)

3. <mark>Market.us. 全球智能体 AI 市场规模、趋势和 2025-2034 年预测。</mark>

---
