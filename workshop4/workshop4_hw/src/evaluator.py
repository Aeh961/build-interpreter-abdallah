from src.ast_nodes import Number, Variable, Assignment, BinaryOp
from src.environment import Environment


def evaluate(node, env: Environment):
    if isinstance(node, Number):
        return node.value

    if isinstance(node, BinaryOp):
        left = evaluate(node.left, env)
        right = evaluate(node.right, env)

        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "*":
            return left * right
        if node.op == "/":
            return left / right

        raise ValueError(f"Unknown operator: {node.op}")

    if isinstance(node, Variable):
        # TODO: look up node.name in env.
        raise NotImplementedError("TODO: evaluate Variable")

    if isinstance(node, Assignment):
        # TODO:
        # 1. evaluate node.value
        # 2. store it in env
        # 3. return the stored value
        raise NotImplementedError("TODO: evaluate Assignment")

    raise TypeError(f"Unknown AST node: {node}")
