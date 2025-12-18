# Customer Support Chatbot Demo

This is a prototype customer support chatbot for a computer products company, using an MCP server and a lightweight LLM.

## Features

- Answers customer queries for printers, monitors, and more using MCP API.
- GroQ-powered LLM for open-domain fallback answers.
- Demo UI built with Streamlit.
- Easy to run on HuggingFace Spaces or locally.

# Customer Support Chatbot (Groq + Streamlit)

A demo customer support chatbot for computer products.

## Tech Stack
- Streamlit UI
- Groq LLM (Llama 3 8B instant)
- MCP Server (Streamable HTTP)

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

#### 4. Usage

- Open `http://localhost:8501` (Streamlit).
- Type a question (e.g., "My printer is not working").
- The bot answers using the MCP backend if possible, else uses Grok LLM.

## Further Development Ideas

- Add login/auth.
- Support images/screenshots for support tickets.
- Train/fine-tune a smaller custom LLM if cost is a concern.