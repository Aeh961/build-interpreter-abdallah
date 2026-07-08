from src.ast_nodes import Number, BinaryOp


def pretty_ast(node, indent: str = "") -> str:
    # Return a readable multi-line representation of an AST.

    if isinstance(node, Number):
        # Return something like: Number(1)
        return f"{indent}Number({node.value})"

    if isinstance(node, BinaryOp):
        # Return a multi-line representation of a BinaryOp.
        #
        # Hint:
        # left = pretty_ast(node.left, indent + "  ")
        # right = pretty_ast(node.right, indent + "  ")
        left = pretty_ast(node.left, indent + "  ")
        right = pretty_ast(node.right, indent + "  ")

        return (
            f"{indent}BinaryOp(\n"
            f"{indent}  op={node.op!r},\n"
            f"{indent}  left=\n{left},\n"
            f"{indent}  right=\n{right}\n"
            f"{indent})"
        )

    raise TypeError(f"Unknown AST node: {node}")
