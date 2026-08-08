# Compare two numbers using the comparison operator.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(a, "is greater than", b, ":", a > b)

print("\n<================ PROGRAM FINISHED ================>\n")


# Compare two numbers using if-elif-else statements.

num_1 = float(input("Enter your first number: "))
num_2 = float(input("\nEnter your second number: "))

print("\n<================== RESULT ==================>\n")

if num_1 > num_2:
    print(f"{num_1} is the greater number.")

elif num_1 == num_2:
    print(f"{num_1} and {num_2} are equal.")

else:
    print(f"{num_2} is the greater number.")
