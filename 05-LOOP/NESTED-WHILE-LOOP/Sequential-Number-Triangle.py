# Logic:-
# i → rows control karta hai
# j → har row me kitne numbers print honge, wo control karta hai
# num → continuously number badhata hai (1, 2, 3, 4...)

n = int(input("Enter number of rows: "))

num = 1
i = 1

while i <= n:
    j = 1

    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1

    print()
    i += 1
