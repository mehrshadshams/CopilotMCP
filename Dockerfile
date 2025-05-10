# Use the official Python image as the base image
FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Copy the project into the image
COPY . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked

# Set an environment variable for the MCP server
ENV MCP=hello

# Expose the port that the MCP server will run on
EXPOSE 8000

# Set the default command to run the main.py script with the MCP parameter
CMD ["uv", "run", "main.py"]
