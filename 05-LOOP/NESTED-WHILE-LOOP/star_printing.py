# Print an increasing star pattern using nested while loops.

# Take the number of rows as input.
num = int(input("Enter the number of rows to print: "))

# Start from the first row.
row = 1

# Print stars in an increasing pattern.
while row <= num:
    col = 1

    while col <= row:
        print("*", end=" ")
        col += 1

    print()
    row += 1
