from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


def ask_chatgpt(user_message):
    tools = [
        {
            "type": "function",
            "function": {
                "name": "recommend",
                "description": "Provide a ... topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "description": "topic, ... for"},
                        "rating": {
                            "type": "string",
                            "description": "the rating ... given",
                            "enum": ["good", "bad", "terrible"],
                        },
                    },
                    "required": ["topic"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role":"system", "content":"You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        tools=tools,
        temperature=0.7
    ) 
    return response.choices[0].message.tool_calls[0].function

#Example usage
user = "Can you please recommend me a time travel movie?"
response = ask_chatgpt(user)
print(response)
user = "Can you please recommend me a good time travel movie?"
response = ask_chatgpt(user)
print(response)
