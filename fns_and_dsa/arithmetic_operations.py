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


# ----- User Interaction -----

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /, %): ")

    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    elif operation == "%":
        print("Result:", modulus(num1, num2))
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError as e:
    print(e)
