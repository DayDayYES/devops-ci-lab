def add(left: int, right: int) -> int:
    return left + right


def subtract(left: int, right: int) -> int:
    return left - right


def multiply(left: int, right: int) -> int:
    return left * right


def divide(left: int, right: int) -> float:
    if right == 0:
        raise ValueError("right must not be zero")
    return left / right


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
