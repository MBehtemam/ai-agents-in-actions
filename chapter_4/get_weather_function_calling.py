from openai import OpenAI
from dotenv import load_dotenv
from pprint import pprint
import requests
import json

load_dotenv()
client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number",
                },
                "longitude": {"type": "number"},
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]
input_messages =[{"role": "user", "content": "What is the weather like in Shiraz today? "}]

response = client.responses.create(model="gpt-4.1", input=input_messages, tools=tools)
# pprint(response)

def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


tool_call = response.output[0]
args = json.loads(tool_call.arguments)
result = get_weather(args["latitude"], args["longitude"])

input_messages.append(tool_call)
input_messages.append({
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4.1",
    input = input_messages,
    tools=tools
)

print(response_2.output_text)