a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print("Answer =", a + b)
elif op == "-":
    print("Answer =", a - b)
elif op == "*":
    print("Answer =", a * b)
elif op == "/":
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")

