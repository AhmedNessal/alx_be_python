def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2


def modulus(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 % num2


def perform_operation(num1, num2, operation):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return divide(num1, num2)
    elif operation == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return modulus(num1, num2)
    else:
        raise ValueError("Invalid operation.")


# ----- User Interaction -----

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /, %): ")

    result = perform_operation(num1, num2, operation)
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError as e:
    print(e)
