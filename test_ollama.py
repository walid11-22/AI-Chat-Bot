from ollama import chat

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Hello! Give me a one-sentence introduction."
        }
    ],
)

print(response.message.content)