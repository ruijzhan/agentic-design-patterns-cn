from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import nest_asyncio
import asyncio

# Define variables required for Session setup and Agent execution
# 定义会话和智能体执行所需变量
APP_NAME="Google Search_agent"
USER_ID="user1234"
SESSION_ID="1234"


# Define Agent with access to search tool
# 定义智能体并授予其使用搜索工具的能力
root_agent = ADKAgent(
   name="basic_search_agent",
   model="gemini-2.0-flash-exp",
   description="Agent to answer questions using Google Search.",
   instruction="I can answer your questions by searching the internet. Just ask me anything!",
   tools=[google_search] # Google Search is a pre-built tool to perform Google searches.
)

# Agent Interaction
# 智能体交互
async def call_agent(query):
   """
   Helper function to call the agent with a query.
   辅助函数，用于调用智能体并发送查询。
   """

   # Session and Runner
   # 会话和执行器
   session_service = InMemorySessionService()
   session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
   runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

   content = types.Content(role='user', parts=[types.Part(text=query)])
   events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)


   for event in events:
       if event.is_final_response():
           final_response = event.content.parts[0].text
           print("Agent Response: ", final_response)

nest_asyncio.apply()
asyncio.run(call_agent("what's the latest ai news?"))
