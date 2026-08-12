n = int(input("Enter number of rows: "))

num = 1
i = 1

while i <= n :
    j = 1
    while j <= i :
        print(num, end=" ")
        num += 1
        j += 1

    print()
    i += 1


# For reverse 


n = int(input("Enter number of rows: "))

i = 1

while i <= n:
    j = 1

    while j <= n - i + 1:
        print(i, end=" ")
        j += 1

    print()
    i += 1
