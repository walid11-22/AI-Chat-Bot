from ollama import chat
from calculator import calculate


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate."
                    }
                },
                "required": ["expression"],
            },
        },
    }
]


messages = [
    {
        "role": "system",
        "content": """
You are a helpful local AI assistant.

Use the calculator tool for arithmetic.
After receiving the calculator result, give only the final answer.
Do not explain your reasoning.
"""
    },
    {
        "role": "user",
        "content": "What is 2 + 2?"
    }
]


print("=== FIRST RESPONSE ===")

response = chat(
    model="qwen3:4b",
    messages=messages,
    tools=tools,
    think=False,
)

print(response.message)

print("\n=== TOOL CALLS ===")
print(response.message.tool_calls)

if response.message.tool_calls:
    tool_call = response.message.tool_calls[0]

    expression = tool_call.function.arguments["expression"]

    print("\n=== EXPRESSION ===")
    print(expression)

    result = calculate(expression)

    print("\n=== CALCULATOR RESULT ===")
    print(result)

    messages.append(response.message)

    messages.append(
        {
            "role": "tool",
            "tool_name": tool_call.function.name,
            "content": str(result),
        }
    )

    print("\n=== SECOND RESPONSE ===")

    response = chat(
        model="qwen3:4b",
        messages=messages,
        tools=tools,
        think=False,
    )

    print(response.message)