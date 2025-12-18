import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # <-- THIS IS CRITICAL

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set")

client = Groq(api_key=api_key)

def ask_groq(messages):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.3,
        max_tokens=512,
    )
    return completion.choices[0].message.content



# import os
# from groq import Groq
#
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))
#
# def ask_groq(messages):
#     completion = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=messages,
#         temperature=0.3,
#         max_tokens=512,
#     )
#     return completion.choices[0].message.content
#
