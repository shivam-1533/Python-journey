# Find the sum of all even numbers between 1 and n

n = int(input("Enter a number: "))

i = 2
total = 0

# Add all even numbers from 2 to n.
while i <= n:
    total += i
    i += 2

print("Sum =", total)
