from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount


mcp = FastMCP(name="MyServer")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

mcp_app = mcp.streamable_http_app(path="/hello")

app = Starlette(
    routes=[
        Mount("/hello-server", app=mcp_app)
    ],
    lifespan=mcp_app.router.lifespan_context,
    debug=True,
)

if __name__ == "__main__":
    mcp.run(transport="streamable-http",host="127.0.0.1",
        port=4200,
        path="/mcp",
        log_level="debug")