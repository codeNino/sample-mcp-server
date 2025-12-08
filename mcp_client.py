import httpx
from fastmcp import FastMCP

mcp = FastMCP("cloud-mcp-wrapper")

API_URL = "https://sample-mcp-server-xny6.onrender.com"

@mcp.tool()
def add(a: int, b: int):
    resp = httpx.get(f"{API_URL}/add", params={"a": a, "b": b})
    return resp.json()["result"]

@mcp.tool()
def greet(name: str):
    resp = httpx.get(f"{API_URL}/greet", params={"name": name})
    return resp.json()["message"]

if __name__ == "__main__":
    mcp.run()
