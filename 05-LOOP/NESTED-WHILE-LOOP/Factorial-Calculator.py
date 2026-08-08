num = int(input("Enter your num for find factorial : "))

fact, i = 1, 1

# while i <= num :
#     fact = fact * i
#     i += 1

#     print(num,"*",i,"=",fact,"\n")


for i in range (1, num+1):
    fact = fact * i

    print(num, "*", i, "=", fact, "\n")

