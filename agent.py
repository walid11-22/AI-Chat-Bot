from ollama import chat
from tools import tools, run_tool


MODEL = "qwen3:4b-instruct"


print("AI Agent started!")
print("Type 'quit' to exit.\n")


system_prompt = """
You are a helpful local AI assistant.

Answer the user's questions clearly and concisely.
For simple factual questions, give a short direct answer.
Use the calculator tool when you need to perform arithmetic.
Do not provide unnecessary explanations unless the user asks for them.
"""



def ask_ai(messages, tools=None):
    return chat(
        model=MODEL,
        messages=messages,
        tools=tools,
        think=False,
    )




messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]



while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = ask_ai(messages, tools=tools)

    if response.message.tool_calls:
        tool_call = response.message.tool_calls[0]

        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        result = run_tool(tool_name, arguments)

        messages.append(response.message)

        messages.append(
            {
                "role": "tool",
                "tool_name": tool_call.function.name,
                "content": str(result),
            }
        )

        response = ask_ai(messages, tools=tools)

    print("Agent:", response.message.content)