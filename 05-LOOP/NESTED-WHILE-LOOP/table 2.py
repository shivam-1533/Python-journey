# Print multiplication tables up to the given number.

# Take the table range as input.
table = int(input("\nEnter the range for tables: "))

# Print multiplication results in a grid format.
row = 1

while row <= 10:
    col = 1

    while col <= table:
        print(f"{row * col}", end="\t")
        col += 1

    print()
    row += 1


# Print the multiplication tables individually.
print("\n")

num = 1

while num <= table:
    print(f"\n========== Table of {num} ==========\n")

    nnum = 1

    while nnum <= 10:
        print(f"{num} × {nnum} = {num * nnum}")
        nnum += 1

    num += 1
