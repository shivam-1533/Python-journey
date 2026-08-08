# Reverse the digits of a number.

# Take a number as input from the user.
num = int(input("Enter the number you want to reverse: "))

# Initialize the reversed number.
reverse = 0

# Extract and reverse each digit.
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

# Display the reversed number.
print(f"Reversed number: {reverse}")
