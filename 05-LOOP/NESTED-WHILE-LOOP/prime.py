# Find all prime numbers from 1 up to the given number.

# Take the upper limit as input.
limit = int(input("Enter your number: "))

# Start checking numbers from 1.
num = 1

# Check each number up to the given limit.
while num <= limit:
    count = 0
    i = 1

    # Count the number of factors of the current number.
    while i <= num:
        if num % i == 0:
            count += 1

        i += 1

    # A prime number has exactly two factors.
    if count == 2:
        print(f"{num} is prime.")

    num += 1
