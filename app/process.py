from fastmcp import FastMCP

mcp = FastMCP("example")


@mcp.tool()
def onboard_lead(firstname: str, lastname: str, email: str):
    print(f"Lead acquired with name {firstname} {lastname} and email {email}")
    return f"{firstname} onboarded successfully"