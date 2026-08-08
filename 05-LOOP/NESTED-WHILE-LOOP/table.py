# Print the multiplication table of a given number.

# Take the number as input from the user.
number = int(input("Enter the number: "))

# Generate the multiplication table from 1 to 10.
i = 1

while i <= 10:
    result = number * i
    print(f"{number} × {i} = {result}")
    i += 1
