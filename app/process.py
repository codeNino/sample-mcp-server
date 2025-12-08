# from fastapi import FastAPI

# server = FastAPI()

# @server.get("/add")
# def add(a: int, b: int):
#     return {"result": a + b}

# @server.get("/greet")
# def greet(name: str):
#     return {"message": f"Hello, {name}!"}

from fastmcp import FastMCP

mcp = FastMCP("example")

@mcp.tool()
def add(a: int, b: int):
    return a + b

@mcp.tool()
def greet(name: str):
    return f"Hello {name}"

