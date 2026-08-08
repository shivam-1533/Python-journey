# Print numbers from 1 up to the given number using a while loop.

# Take the ending number as input.
number = int(input("Enter your number: "))

# Start counting from 1.
i = 1

# Print numbers until the given number is reached.
while i <= number:
    print(i)
    i += 1


# Print numbers from 1 to 10 using range().
i = 1

while i in range(1, 11):
    print(i)
    i += 1
