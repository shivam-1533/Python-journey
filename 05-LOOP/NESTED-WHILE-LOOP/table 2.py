table = int(input("\nENTER RANGE FOR TABLE :- "))

row = 1

while row <= 10 :

    col = 1

    while col <= table :
        print(f"{row * col}",end="\t")

        col += 1

    print()

    row += 1

# for i in range (1, 11) :
#     print(f"{table} * {i} = ",i * table)

    


print("\n\n\n\n")



num = 1

while num <= table :

    nnum = 1

    while nnum <= 10 :

        print(f"{num} * {nnum} = ", num * nnum)

        nnum += 1

    # if num == 10:
    #     print("Next Table is Bellow")

    # else :
    #     print("Your Table is Complete")

    num += 1
