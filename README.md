# MCP Server Project

This project contains multiple MCP servers for handling various tasks such as customer interviews, E2E testing, and go-live processes. Each MCP server is implemented using the FastMCP framework.

## Prerequisites

- Python 3.11 or higher
- `uv` package manager (used instead of `pip`)

## Setup

1. Clone the repository:
   ```zsh
   git clone <repository-url>
   cd CopilotMCP
   ```

2. Install dependencies using `uv`:
   ```zsh
   uv install
   ```

## Running the Project

To run a specific MCP server, use the following command:

```zsh
uv run main.py --mcp <mcp_server_name>
```

Replace `<mcp_server_name>` with the name of the MCP server you want to run. Available options are:

- `hello`
- `customer_mcp`
- `interview_mcp`
- `go_live_mcp`
- `testing_e2e_mcp`

### Example

To run the `customer_mcp` server:

```zsh
uv run main.py --mcp customer_mcp
```

This will start the `customer_mcp` server and make it accessible at:

```
http://127.0.0.1:8000/customer-mcp-server/mcp
```

## Configuring MCP Servers in VSCode

To configure MCP servers in VSCode, you can add entries to your `settings.json` file under the `mcp.servers` section. This allows you to define and manage MCP server endpoints for easy access.

### Example Configuration

To configure the `hello-mcp-server`, add the following entry to your `settings.json` file:

```jsonc
"hello-mcp-server": {
    "url": "http://127.0.0.1:8000/hello-server/mcp/http",
    "type": "http"
}
```

Then you can access hello server `hello` tool by executing: `#hello <something>` in Copilot.

### Steps to Add Configuration

1. Open your VSCode `settings.json` file.
2. Locate or create the `mcp.servers` section.
3. Add the configuration for the desired MCP server, as shown in the example above.

### Accessing the Server

Once configured, you can use the defined URL to interact with the MCP server. For example, the `hello-mcp-server` will be accessible at:

```
http://127.0.0.1:8000/hello-server/mcp/http
```

This setup ensures that you can easily manage and test MCP servers directly from VSCode.

## Project Structure

- `main.py`: Entry point for running MCP servers.
- `customer_mcp.py`: Handles customer interview-related tasks.
- `interview_mcp.py`: Manages customer interview steps.
- `go_live_mcp.py`: Handles go-live processes.
- `testing_e2e_mcp.py`: Manages E2E testing tasks.
- `hello.py`: Example MCP server for testing.

## Notes

- Ensure that the `uv` package manager is installed and configured correctly.
- Use the `--mcp` argument to specify which MCP server to run.