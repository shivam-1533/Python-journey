# Find the sum of all natural numbers between 1 and n

n = int(input("Enter a number: "))

i = 1
total = 0

# Add each natural number from 1 to n.
while i <= n:
    total += i
    i += 1

print("Sum =", total)
