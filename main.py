import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent



async def main():
    # Create MCP client
    client = MultiServerMCPClient(
        {
        "weather": {
                "transport": "streamable_http",
                "url": "http://localhost:8000/mcp",
            }
        }
    )

    # Fetch tools from the MCP server
    tools = await client.get_tools()
    print("Loaded tools:", tools)
    # for t in tools:
    #     print(" -", t.name)

#     agent = create_agent(
#     "claude-sonnet-4-5-20250929",
#     tools  
# )
#     response = await agent.ainvoke(
#     {"messages": [{"role": "user", "content": "Add 14 and 17"}]}
# )




if __name__ == "__main__":
    asyncio.run(main())
