from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import os

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "https://vipfapwm3x.us-east-1.awsapprunner.com/mcp")

app = FastAPI()

class ChatInput(BaseModel):
    user_message: str

@app.post("/chat/")
async def chat(input: ChatInput):
    user_message = input.user_message

    if "printer" in user_message.lower():
        mcp_payload = {"query": user_message}
        try:
            res = requests.post(f"{MCP_SERVER_URL}/printer", json=mcp_payload)
            mcp_data = res.json()
        except Exception as e:
            return {"bot_response": f"Error contacting MCP server: {e}"}
        answer = mcp_data.get("result", "Could not fetch printer information.")
        return {"bot_response": answer}

    # Fallback answer for general cases
    return {"bot_response": "I'm using Grok, and I couldn’t fully understand your query. Please be more specific."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)