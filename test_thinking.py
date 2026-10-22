from ollama import chat

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "What is 2 + 2? Answer with only the number."
        }
    ],
    think=False,
)

print(response.message.content)