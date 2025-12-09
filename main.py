import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage

from typing import List
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

async def main():
    # Create MCP client
    client = MultiServerMCPClient(
        {
        "srv": {
                "transport": "streamable_http",
                # "url": "https://sample-mcp-server-xny6.onrender.com/mcp",
            "url": "http://localhost:8000/mcp",
            }
        }
    )

    # Fetch tools from the MCP server
    tools = await client.get_tools()
    print("Loaded tools:", tools)

    advanced_model = ChatOpenAI(model="gpt-4o", api_key=OPENAI_KEY)


    agent = create_agent(
    model=advanced_model,
    tools=tools,
    system_prompt= """
You are an onboarding assistant. Your job is to collect 3 key things to onboard a new lead:
1. First name
2. Last name
3. Email address

You MUST collect each of these clearly before calling any tool.

When you have all three fields, call the tool with the right inputs:

If email format is invalid, ask the user to re-enter it.
Be warm, friendly, and conversational.
"""

)   
    messages: List = []
    print("🧠 Lead Onboarding Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        messages.extend([user_input])
        response = agent.invoke({"input": messages})["messages"][-1].content
        print(f"Agent: {response}\n")
        messages.extend([response])
        print("messages: ", messages)

if __name__ == "__main__":
    asyncio.run(main())
