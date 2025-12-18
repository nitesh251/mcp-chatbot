import requests
import os

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")

def call_mcp(tool_name: str, payload: dict):
    """
    Calls the MCP server using Streamable HTTP.
    """
    url = f"{MCP_SERVER_URL}/{tool_name}"
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()
