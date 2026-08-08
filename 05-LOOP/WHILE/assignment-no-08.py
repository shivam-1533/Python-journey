# Find the sum of all odd numbers between 1 and n

n = int(input("Enter a number: "))

i = 1
total = 0

# Add all odd numbers from 1 to n.
while i <= n:
    total += i
    i += 2

print("Sum =", total)
