from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Node:
    value: Any
    children: List["Node"] = field(default_factory=list)

    def add_child(self, child: "Node") -> None:
        self.children.append(child)


# Exercise 1 - Build a Small Tree
a = Node("A")
b = Node("B")
c = Node("C")
a.children = [b, c]


# Exercise 2 - Build a File System Tree
documents = Node("Documents")

photos = Node("Photos")
school = Node("School")

beach = Node("beach.jpg")
dog = Node("dog.png")

cs101 = Node("CS101")
notes = Node("Notes")

photos.children = [beach, dog]
school.children = [cs101, notes]
documents.children = [photos, school]


# Exercise 3 - Tree Vocabulary
# 1. Root:
# Your answer: Documents
#
# 2. Leaves:
# Your answer: beach.jpg, dog.png, CS101, Notes
#
# 3. Parent of Notes:
# Your answer: School
#
# 4. Subtree rooted at Photos:
# Your answer: Photos and its children, beach.jpg and dog.png


# Exercise 4 - Recursive Factorial
def factorial(n: int) -> int:
    if n == 1:
        return 1

    return n * factorial(n - 1)


# Exercise 5 - Trace Recursion
def countdown(n: int) -> None:
    if n == 0:
        return

    print(n)
    countdown(n - 1)


def mystery(n: int) -> None:
    if n == 0:
        return

    mystery(n - 1)
    print(n)


# Why does countdown(3) print 3 2 1, but mystery(3) prints 1 2 3?
# Your answer: countdown prints before the recursive call, so each number is
# printed while the calls are going deeper. mystery prints after the recursive
# call, so it waits until the base case is reached and then prints as the calls
# return.


# Exercise 6 - Count All Nodes
def count_nodes(node: Node) -> int:
    total = 1

    for child in node.children:
        total += count_nodes(child)

    return total


# Exercise 7 - Count Leaves
def count_leaves(node: Node) -> int:
    if len(node.children) == 0:
        return 1

    total = 0

    for child in node.children:
        total += count_leaves(child)

    return total


# Exercise 8 - Compute Tree Height
def height(node: Node) -> int:
    if len(node.children) == 0:
        return 0

    child_heights = []

    for child in node.children:
        child_heights.append(height(child))

    return 1 + max(child_heights)


# Exercise 9 - Preorder Traversal
def preorder(node: Node) -> list:
    result = [node.value]

    for child in node.children:
        result.extend(preorder(child))

    return result


# Exercise 10 - Pretty Print a Tree
def print_tree(node: Node, depth: int = 0) -> None:
    indent = "  " * depth
    print(indent + str(node.value))

    for child in node.children:
        print_tree(child, depth + 1)


@dataclass
class ExprNode:
    value: Any
    left: Optional["ExprNode"] = None
    right: Optional["ExprNode"] = None

    @property
    def is_number(self) -> bool:
        return isinstance(self.value, (int, float))

    @property
    def is_operator(self) -> bool:
        return self.value in ["+", "-", "*", "/", "**"]


# Exercise 11 - Build an Expression Tree
expr = ExprNode(
    "+",
    left=ExprNode(1),
    right=ExprNode(
        "*",
        left=ExprNode(2),
        right=ExprNode(3),
    ),
)


# Exercise 12 - Evaluate an Expression Tree
def evaluate(node: ExprNode) -> float:
    if node.is_number:
        return node.value

    left = evaluate(node.left)
    right = evaluate(node.right)

    if node.value == "+":
        return left + right
    elif node.value == "-":
        return left - right
    elif node.value == "*":
        return left * right
    elif node.value == "/":
        return left / right
    elif node.value == "**":
        return left**right
    else:
        raise ValueError(f"Unknown operator: {node.value}")


# Exercise 13 - Build and Evaluate Another Expression
expr2 = ExprNode(
    "*",
    left=ExprNode(
        "+",
        left=ExprNode(2),
        right=ExprNode(3),
    ),
    right=ExprNode(5),
)


# Exercise 14 - Pretty Print Expression Trees
def pretty(node: ExprNode) -> str:
    if node.is_number:
        return str(node.value)

    left = pretty(node.left)
    right = pretty(node.right)

    return "(" + left + " " + node.value + " " + right + ")"


# Part 6 - Reflection
# 1. Why are trees useful for representing programs?
# Your answer: Programs have nested structure, and trees show how smaller
# pieces like numbers, operators, and expressions fit inside larger pieces.
#
# 2. Why does recursion work well on trees?
# Your answer: Each child of a tree is also a smaller tree, so the same function
# can solve the problem for the current node and then for each child.
#
# 3. Why does the evaluator evaluate children before the parent?
# Your answer: An operator needs the values of its left and right children
# before it can combine them.
#
# 4. What part of this homework was most confusing?
# Your answer: The trickiest part was tracking whether work happens before or
# after the recursive call, because that changes the order of the output.


# Stretch 1 - Add Power Operator
expr_power = ExprNode(
    "**",
    left=ExprNode(2),
    right=ExprNode(3),
)


# Stretch 2 - Collect Operators
def operators(node: ExprNode) -> list:
    if node.is_number:
        return []

    result = [node.value]

    result.extend(operators(node.left))
    result.extend(operators(node.right))

    return result


# Stretch 3 - Validate Expression Trees
def is_valid_expr_tree(node: ExprNode) -> bool:
    if node.is_number:
        return node.left is None and node.right is None

    if not node.is_operator:
        return False

    if node.left is None or node.right is None:
        return False

    return is_valid_expr_tree(node.left) and is_valid_expr_tree(node.right)


if __name__ == "__main__":
    assert a.children == [b, c]
    assert photos.children == [beach, dog]
    assert school.children == [cs101, notes]
    assert documents.children == [photos, school]

    assert factorial(5) == 120
    assert count_nodes(documents) == 7
    assert count_leaves(documents) == 4
    assert height(documents) == 2
    assert preorder(documents) == [
        "Documents",
        "Photos",
        "beach.jpg",
        "dog.png",
        "School",
        "CS101",
        "Notes",
    ]

    assert evaluate(expr) == 7
    assert evaluate(expr2) == 25
    assert pretty(expr) == "(1 + (2 * 3))"
    assert evaluate(expr_power) == 8
    assert operators(expr) == ["+", "*"]
    assert is_valid_expr_tree(expr) is True

    print("Workshop 2 checks passed")
