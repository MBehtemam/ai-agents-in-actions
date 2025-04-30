import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please check you .env file")

client = OpenAI(api_key=api_key)
model = "gpt-4-1106-preview"

def SystemMessage(content):
    return {"role":"system", "content":content}

def HumanMessage(content):
    return { "role": "user", "content": content}

def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model=model,
        messages=[SystemMessage("You are a helpful assistant."),HumanMessage(user_message)],
        temperature=0.7
    )
    return response.choices[0].message.content

user = "What is the capital of France?"
response = ask_chatgpt(user)
print(response)