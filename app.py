import streamlit as st
import requests

API_URL = "http://localhost:8000/chat/"  # Set this to the correct backend endpoint upon deployment

st.title("Customer Support Chatbot Demo")

if "history" not in st.session_state:
    st.session_state["history"] = []

def submit_message():
    user_message = st.session_state["user_input"]
    if user_message:
        resp = requests.post(API_URL, json={"user_message": user_message})
        bot_msg = resp.json()["bot_response"]
        st.session_state["history"].append(("You", user_message))
        st.session_state["history"].append(("Bot", bot_msg))
        st.session_state["user_input"] = ""

for speaker, msg in st.session_state["history"]:
    st.chat_message(speaker).write(msg)

st.text_input("Type your message:", key="user_input", on_change=submit_message)