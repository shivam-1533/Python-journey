# Find the sum of all even numbers between 1 to n

n = int(input("Enter a number: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum =", sum)
