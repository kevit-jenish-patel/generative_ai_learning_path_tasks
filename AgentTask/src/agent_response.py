# File: calculator.py
"""
A small safe calculator that can evaluate basic mathematical expressions.
It uses the Python AST to safely evaluate expressions without executing
arbitrary code.

Supported operators: +, -, *, /, //, %, **, and unary + and -.
Parentheses are supported via normal expression syntax.

This module also exposes a simple CLI via the main() entry point when run
as a script.
"""
from __future__ import annotations

import ast
import operator
import sys
from typing import Union

# Mapping of AST operator nodes to actual functions
_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

Number = Union[int, float]


def _to_number(node: ast.AST) -> Number:
    """Extract a number from an AST node (Num or Constant).

    Raises ValueError if the node does not represent a number.
    """
    if isinstance(node, ast.Num):  # For Python < 3.8 compatibility
        return node.n  # type: ignore[attr-defined]
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value  # type: ignore[return-value]
        raise ValueError("Unsupported constant type for a numeric expression")
    raise ValueError("Expected a numeric literal")


def _evaluate(node: ast.AST) -> Number:
    """Recursively evaluate a sanitized AST node representing a math expression."""
    # Expression wrapper
    if isinstance(node, ast.Expression):
        return _evaluate(node.body)

    # Numeric literals
    if isinstance(node, (ast.Num, ast.Constant)):
        return _to_number(node)  # type: ignore[arg-type]

    # Parenthesized expressions are represented by their inner nodes, so no special case
    # Parent operator: binary operation
    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        op_type = type(node.op)
        if op_type not in _OPERATORS:
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        return _OPERATORS[op_type](left, right)

    # Unary operations: +x, -x
    if isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        op_type = type(node.op)
        if op_type not in _UNARY_OPERATORS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        return _UNARY_OPERATORS[op_type](operand)

    # For safety: disallow names, calls, attributes, etc.
    raise ValueError("Unsupported expression. Only numbers and basic arithmetic are allowed.")


def evaluate_expression(expr: str) -> Number:
    """Safely evaluate a mathematical expression string and return a number.

    Examples:
      evaluate_expression("2 + 3 * 4") -> 14
      evaluate_expression("2**3") -> 8
      evaluate_expression("-5 + 2") -> -3
    """
    if not isinstance(expr, str):
        raise TypeError("expr must be a string")
    try:
        parsed = ast.parse(expr, mode="eval")
        result = _evaluate(parsed)
        # Normalize floats that are whole numbers to int for nicer output
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except ZeroDivisionError:
        # Re-raise to let callers handle it specifically if desired
        raise
    except Exception as exc:
        raise ValueError(f"Invalid expression: {exc}")


def _format_available_ops() -> str:
    return "+, -, *, /, //, %, **; unary + and -"


def main() -> None:
    """Command-line interface for the calculator.

    - If called with -e/--expression, evaluate the given expression and print the result.
    - Otherwise, run in interactive mode, prompting the user for expressions until exit.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Safe calculator CLI supporting basic arithmetic"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-e",
        "--expression",
        dest="expression",
        help="Expression to evaluate",
    )
    group.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode (default if no expression provided)",
    )

    args = parser.parse_args()

    if args.expression is not None:
        try:
            result = evaluate_expression(args.expression)
            print(result)
        except Exception as exc:  # pragma: no cover - error path
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(2)
        return

    # Default or explicit interactive
    print("Simple Calculator CLI. Type expressions to evaluate. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "q"):
            break
        try:
            res = evaluate_expression(user_input)
            print(res)
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":  # pragma: no cover
    main()