"""A simple calculator that evaluates math expressions."""

import math


def calculate(expression: str) -> str:
    """Evaluate a math expression and return the result as a string.

    Supports basic arithmetic and functions from the math module.
    Examples: "847 * 293", "10000 * (1.07 ** 5)", "math.sqrt(144)"
    """
    allowed = {"__builtins__": {}, "abs": abs, "round": round, "min": min, "max": max}
    allowed.update({k: v for k, v in vars(math).items() if not k.startswith("_")})

    try:
        result = eval(expression, allowed)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # Quick test
    print(calculate("847 * 293"))          # 248171
    print(calculate("10000 * (1.07 ** 5)"))  # 14025.517...
    print(calculate("sqrt(144)"))          # 12.0
