# Calculate the factorial of a number using a for loop.

# Take the number as input from the user.
num = int(input("Enter a number to find its factorial: "))

# Initialize the factorial value.
fact = 1

# Multiply each number from 1 to the given number.
for i in range(1, num + 1):
    fact *= i

# Display the factorial result.
print(f"{num}! = {fact}")
