# Print a descending star pattern using nested while loops.

# Set the number of rows.
row = 5

# Print stars in descending order.
while row >= 1:
    col = 1

    while col <= row:
        print("*", end=" ")
        col += 1

    print()
    row -= 1
