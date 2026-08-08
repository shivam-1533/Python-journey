# Skip numbers that are divisible by 2 or 3.

# Take the upper limit as input.
num = int(input("Enter your number: "))

# Start counting from 0.
i = 0

# Continue until the given number is reached.
while i <= num:
    i += 1

    # Skip numbers divisible by 2 or 3.
    if i % 2 == 0 or i % 3 == 0:
        continue

    # Display the number if it is not divisible by 2 or 3.
    print(i)
