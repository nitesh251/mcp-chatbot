import streamlit as st
from groq_llm import ask_groq
from mcp_client import call_mcp

st.set_page_config(page_title="Customer Support Bot", page_icon="🖥️")

st.title("🖥️ Computer Products Support Chatbot")
st.caption("Support for Monitors, Printers, and Accessories")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a professional customer support agent for a company "
                "that sells computer products such as monitors and printers. "
                "Be concise, helpful, and friendly."
            ),
        }
    ]

# Render chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about setup, troubleshooting, or warranty...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Simple MCP routing
    mcp_context = ""
    try:
        if "warranty" in user_input.lower():
            result = call_mcp("check_warranty", {"query": user_input})
            mcp_context = f"Warranty Info: {result}"

        elif "printer" in user_input.lower():
            result = call_mcp("troubleshoot_printer", {"issue": user_input})
            mcp_context = f"Printer Troubleshooting: {result}"

        elif "monitor" in user_input.lower():
            result = call_mcp("monitor_setup_help", {"issue": user_input})
            mcp_context = f"Monitor Setup: {result}"
    except Exception as e:
        mcp_context = f"MCP server unavailable: {e}"

    messages = st.session_state.messages.copy()
    if mcp_context:
        messages.append({"role": "system", "content": mcp_context})

    response = ask_groq(messages)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)












# import streamlit as st
# import requests
#
# API_URL = "http://localhost:8000/chat/"  # Set this to the correct backend endpoint upon deployment
#
# st.title("Customer Support Chatbot Demo")
#
# if "history" not in st.session_state:
#     st.session_state["history"] = []
#
# def submit_message():
#     user_message = st.session_state["user_input"]
#     if user_message:
#         resp = requests.post(API_URL, json={"user_message": user_message})
#         bot_msg = resp.json()["bot_response"]
#         st.session_state["history"].append(("You", user_message))
#         st.session_state["history"].append(("Bot", bot_msg))
#         st.session_state["user_input"] = ""
#
# for speaker, msg in st.session_state["history"]:
#     st.chat_message(speaker).write(msg)
#
# st.text_input("Type your message:", key="user_input", on_change=submit_message)