import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from connecting import HumanMessage,SystemMessage

def AssistantMessage(content):
    return { "role":"assistant", "content":content}
# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please check your .env file")

client = OpenAI(api_key=api_key)

messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("What is the capital of France?"),
    AssistantMessage("The capital of France is Paris"),
    HumanMessage("What is an interesting fact of Paris") 
]
model = "gpt-4-1106-preview"
def ask_chatgpt(messages):
   response = client.chat.completions.create(
       messages=messages,
       model=model,
       temperature=0.7
   ) 
   response_model = response.model_dump()
   print(json.dumps(response_model, indent=4))
   return response.choices[0].message.content

response = ask_chatgpt(messages)
print(response)