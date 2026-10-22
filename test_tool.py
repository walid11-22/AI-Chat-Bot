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
        "role": "user",
        "content": "Calculate 123456 * 789"
    }
]


response = chat(
    model="qwen3:4b",
    messages=messages,
    tools=tools,
    think=False,
)


if response.message.tool_calls:
    tool_call = response.message.tool_calls[0]

    expression = tool_call.function.arguments["expression"]

    result = calculate(expression)

    messages.append(response.message)

    messages.append(
        {
            "role": "tool",
            "tool_name": tool_call.function.name,
            "content": str(result),
        }
    )

    final_response = chat(
        model="qwen3:4b",
        messages=messages,
        tools=tools,
        think=False,
    )

    answer = final_response.message.content

    if "</think>" in answer:
        answer = answer.split("</think>", 1)[1].strip()

    print("Agent:", answer)