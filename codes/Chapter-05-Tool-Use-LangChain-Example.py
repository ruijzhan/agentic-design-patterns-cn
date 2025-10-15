import os, getpass
import asyncio
import nest_asyncio
from typing import List
from dotenv import load_dotenv
import logging

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool as langchain_tool
from langchain.agents import create_tool_calling_agent, AgentExecutor

# Colab 代码链接：https://colab.research.google.com/drive/1PNsMB2kcCP-iPgpYamG11bGkBiP3QViz#scrollTo=FW3Eh5_OjUea

# UNCOMMENT
# Prompt the user securely and set API keys as an environment variables
# 安全地提示用户并设置 API 密钥为环境变量
os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

try:
   # A model with function/tool calling capabilities is required.
   # 需要一个具有函数/工具调用能力的模型
   llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
   print(f"✅ Language model initialized: {llm.model}")
except Exception as e:
   print(f"🛑 Error initializing language model: {e}")
   llm = None

# --- Define a Tool ---
# --- 定义一个工具 ---
@langchain_tool
def search_information(query: str) -> str:
   """
   Provides factual information on a given topic. Use this tool to find answers to phrases
   like 'capital of France' or 'weather in London?'.
   # 供关于特定主题的事实信息。使用此工具查找类似「法国的首都是哪里？」或「伦敦的天气如何？」这类问题的答案。
   """
   print(f"\n--- 🛠️ Tool Called: search_information with query: '{query}' ---")
   # Simulate a search tool with a dictionary of predefined results.
   # 模拟一个搜索工具，使用预定义的结果。
   simulated_results = {
       "weather in london": "The weather in London is currently cloudy with a temperature of 15°C.",
       "capital of france": "The capital of France is Paris.",
       "population of earth": "The estimated population of Earth is around 8 billion people.",
       "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
       "default": f"Simulated search result for '{query}': No specific information found, but the topic seems interesting."
   }
   result = simulated_results.get(query.lower(), simulated_results["default"])
   print(f"--- TOOL RESULT: {result} ---")
   return result

tools = [search_information]

# --- Create a Tool-Calling Agent ---
# --- 创建一个工具调用智能体 ---
if llm:
   # This prompt template requires an `agent_scratchpad` placeholder for the agent's internal steps.
   # 这个提示模板需要一个 `agent_scratchpad` 占位符，用于记录智能体的内部步骤。
   agent_prompt = ChatPromptTemplate.from_messages([
       ("system", "You are a helpful assistant."),
       ("human", "{input}"),
       ("placeholder", "{agent_scratchpad}"),
   ])

   # Create the agent, binding the LLM, tools, and prompt together.
   # 创建智能体，将 LLM、工具和提示绑定在一起。
   agent = create_tool_calling_agent(llm, tools, agent_prompt)

   # AgentExecutor is the runtime that invokes the agent and executes the chosen tools.
   # The 'tools' argument is not needed here as they are already bound to the agent.
   # AgentExecutor 是运行时，用于调用智能体并执行选定的工具。这里的 'tools' 参数不需要了，因为它们已经绑定到智能体了。
   agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)

async def run_agent_with_tool(query: str):
   """
   Invokes the agent executor with a query and prints the final response.
   # 调用智能体执行器并打印最终响应。
   """
   print(f"\n--- 🏃 Running Agent with Query: '{query}' ---")
   try:
       response = await agent_executor.ainvoke({"input": query})
       print("\n--- ✅ Final Agent Response ---")
       print(response["output"])
   except Exception as e:
       print(f"\n🛑 An error occurred during agent execution: {e}")

async def main():
   """
   Runs all agent queries concurrently.
   # 并发运行所有智能体查询。
   """
   tasks = [
       run_agent_with_tool("What is the capital of France?"),
       run_agent_with_tool("What's the weather like in London?"),
       run_agent_with_tool("Tell me something about dogs.") # Should trigger the default tool response
   ]
   await asyncio.gather(*tasks)

nest_asyncio.apply()
asyncio.run(main())