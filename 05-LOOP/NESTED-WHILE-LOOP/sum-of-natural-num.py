# Calculate the sum of natural numbers from 1 to n.

# Take the upper limit as input.
n = int(input("Enter a number: "))

# Initialize the sum and counter.
total = 0
i = 1

# Add each natural number to the total.
while i <= n:
    total += i
    i += 1

# Display the calculated sum.
print(f"Sum = {total}")
