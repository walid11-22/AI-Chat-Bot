from .calculator_tool import calculator_tool, run_calculator


tools = [
    calculator_tool
]



tool_functions = {
    "calculate": run_calculator,
}


tool_registry = {
    "calculate": {
        "definition": calculator_tool,
        "function": run_calculator,
    }
}



def run_tool(name, arguments):
    if name not in tool_registry:
        raise ValueError(f"Unknown tool: {name}")

    function = tool_registry[name]["function"]

    return function(**arguments)