import argparse
import uvicorn

from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

mcps = [
    "hello",
    "customer_mcp",
    "interview_mcp",
    "go_live_mcp",
    "testing_e2e_mcp",
]

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Run a specific MCP server.")
parser.add_argument("--mcp", type=str, required=True, help="The MCP server to run (e.g., 'hello', 'customer_mcp').")
args = parser.parse_args()

# Validate the provided MCP server
if args.mcp not in mcps:
    raise ValueError(f"Invalid MCP server: {args.mcp}. Available options are: {', '.join(mcps)}")

# Import the specified MCP module dynamically
module = __import__(args.mcp, fromlist=[''])
mcp_instance = getattr(module, 'mcp', None)
if not mcp_instance:
    raise ValueError(f"MCP instance not found in module: {args.mcp}")

# Create the ASGI app for the specified MCP instance
mcp_app = mcp_instance.streamable_http_app(path='/mcp')

# Create a Starlette app and mount the specified MCP server
app = Starlette(
    routes=[Mount(f"/{args.mcp.replace('_', '-')}-server", app=mcp_app)],
    lifespan=mcp_app.router.lifespan_context,
    debug=True,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)