from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
#function to query the ChatGPT
def prompt_llm(messages, model="gpt-4-1106-preview", base_url=None, api_key=""):
    if(base_url):
        client = OpenAI(base_url=base_url, api_key=api_key)
    else:
        client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages = messages,
        temperature= 0.7
    )
    return response.choices[0].message