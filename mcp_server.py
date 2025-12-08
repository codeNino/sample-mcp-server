# from fastmcp import FastMCP
# from app.process import add as add_route, greet as greet_route

# mcp = FastMCP("fastapi-mcp-server")


# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Expose FastAPI /add endpoint logic as MCP tool."""
#     return add_route(a=a, b=b)["result"]


# @mcp.tool()
# def greet(name: str) -> str:
#     """Expose FastAPI /greet endpoint logic as MCP tool."""
#     return greet_route(name=name)["message"]


# if __name__ == "__main__":
#     mcp.run()

from app.process import mcp



if __name__ == "__main__":
    mcp.run(transport="streamable-http",
        host="0.0.0.0",
        port=8000)