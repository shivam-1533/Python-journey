range = int(input('enter your num: '))

num = 1

while num <= range:
    count = 0

    i = 1

    while i <= num :

        if (num % i == 0):
            count += 1

        i += 1


    if count == 2 :
        print(num,"is prime\n")

    num += 1