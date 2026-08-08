#  WAP to skip the num 
num = int(input("ENTER YOUR NUM : "))

i = 0

while i <= num:
    i += 1

    if i % 2 == 0 or i % 3 == 0 :
        continue
        # break

    print(i)