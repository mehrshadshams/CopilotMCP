from fastmcp import FastMCP

mcp = FastMCP("GoLiveMCP")

@mcp.tool()
async def onboarding_complete() -> dict:
    """Mark the onboarding process as complete."""
    return {"message": "Onboarding complete. Go live enabled."}

if __name__ == "__main__":
    mcp.run()
