from ollama import chat

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "What is 2 + 2?"
        }
    ],
    think=False,
)

print("TYPE:", type(response))
print("\nMESSAGE:")
print(response.message)

print("\nMESSAGE DATA:")
print(response.message.model_dump())