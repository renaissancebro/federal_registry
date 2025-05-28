# summarize.py
from ollama import Client
import sys
import json

model = "llama3"  # or whatever you've loaded
client = Client()

text = sys.stdin.read()

response = client.chat(model=model, messages=[{
    "role": "user",
    "content": f"Summarize this:\n\n{text}"
}])

print(response['message']['content'])
