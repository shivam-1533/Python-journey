num = int(input("Enter your num : "))

n = 1

while n <= num:
    print('\n table of',n,end='\n\n')
    i = 1

    while i <= 10:
        print(n,"*",i, "=",n * i)

        i +=1

    n += 1
