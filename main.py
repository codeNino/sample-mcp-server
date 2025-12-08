import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent



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


if __name__ == "__main__":
    asyncio.run(main())
