from openai import OpenAI
# Point to the local server
client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
    model="llama-3.2-3b-instruct",
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role":"user", "content": "Introduce yourself."}
    ],
    temperature=0.7
)

print(completion.choices[0].message)