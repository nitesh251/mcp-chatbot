# Customer Support Chatbot Demo

This is a prototype customer support chatbot for a computer products company, using an MCP server and a lightweight LLM.

## Features

- Answers customer queries for printers, monitors, and more using MCP API.
- Grok-powered LLM for open-domain fallback answers.
- Demo UI built with Streamlit.
- Easy to run on HuggingFace Spaces or locally.

## How to Run

#### 1. Install dependencies

```
pip install -r requirements.txt
```

#### 2. Start the backend API

```
python backend.py
```

#### 3. Start the Streamlit UI (in a new terminal)

```
streamlit run app.py
```

#### 4. Usage

- Open `http://localhost:8501` (Streamlit).
- Type a question (e.g., "My printer is not working").
- The bot answers using the MCP backend if possible, else uses Grok LLM.

## Deployment

- Deploy `backend.py` on HuggingFace Spaces as a FastAPI Space.
- Deploy `app.py` on HuggingFace Spaces as a Streamlit Space.
- Adjust `API_URL` in `app.py` to point to the backend.

## Customizing the Bot

- Change the LLM or add intents in `backend.py` for other products/features.
- Add more MCP endpoints as needed.

## Further Development Ideas

- Add login/auth.
- Support images/screenshots for support tickets.
- Train/fine-tune a smaller custom LLM if cost is a concern.