import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


def calculate(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        return evaluate(tree.body)

    except Exception as e:
        return f"Error: {e}"


def evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = evaluate(node.left)
        right = evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        value = evaluate(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        return value

    raise ValueError("Only mathematical expressions are allowed")
