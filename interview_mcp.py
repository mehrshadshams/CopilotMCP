from fastmcp import FastMCP

mcp = FastMCP("InterviewMCP")

@mcp.tool()
async def present_intake_form() -> dict:
    """Present the intake form to the customer."""
    return {"message": "Intake form presented."}

@mcp.tool()
async def guide_and_validate_responses() -> dict:
    """Guide the customer and validate their responses."""
    return {"message": "Responses validated."}

@mcp.tool()
async def suggest_billing_model() -> dict:
    """Suggest a billing model to the customer."""
    return {"message": "Billing model suggested."}

@mcp.tool()
async def provide_progress_and_suggestions() -> dict:
    """Provide progress updates and suggestions to the customer."""
    return {"message": "Progress and suggestions provided."}

if __name__ == "__main__":
    mcp.run()
