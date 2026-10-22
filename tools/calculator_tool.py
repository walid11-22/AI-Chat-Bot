calculator_tool = {
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


from calculator import calculate


def run_calculator(expression):
    return calculate(expression)