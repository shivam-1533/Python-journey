# Create a simple calculator using the match-case statement.

# Take two numbers as input from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Take the arithmetic operator as input.
op = input("Enter an operator (+, -, *, /): ")

# Perform the calculation based on the selected operator.
match op:
    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        print("Result =", num1 / num2)

    case _:
        print("Invalid operator.")
