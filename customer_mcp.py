from fastmcp import FastMCP

mcp = FastMCP("CustomerMCP")

@mcp.tool()
async def start_interview() -> dict:
    """Trigger the start of the customer interview process."""
    return {"message": "Interview started. Redirecting to Customer Interview MCP."}

if __name__ == "__main__":
    mcp.run()
