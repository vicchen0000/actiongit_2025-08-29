def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print("Add: ", add(2, 3))
    print("Subtract: ", subtract(5, 2))
    print("Multiply: ", multiply(4, 6))
    print("Divide: ", divide(10, 2))
