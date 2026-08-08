# Print multiplication tables from 1 up to the given number.

# Take the upper limit as input.
num = int(input("Enter your number: "))

# Start the table from 1.
n = 1

# Generate tables until the given number.
while n <= num:
    print(f"\nTable of {n}\n")

    # Start multiplying from 1.
    i = 1

    # Print the multiplication table up to 10.
    while i <= 10:
        print(f"{n} × {i} = {n * i}")
        i += 1

    n += 1
