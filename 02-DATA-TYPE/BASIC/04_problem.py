# WAP a Porogram to compair between two number

a=input("Enter a number : ")

b=input("Enter a number : ")

print(a,"Is grater then",b , a>b)

print("\n\n <================ THIS PROGRAM IS FINISHED================>\n\n")


# We can make this program with if else statement

num_1 = float(input("Enter Your First Number : "))

num_2 = float(input("\nEnter Your Second Number : "))

print("\n<================== RESULT ==================>\n")

if num_1 > num_2:
    print(f"\n\n{num_1} Is Max Number\n")

elif num_1 == num_2:
    print(f"\n{num_1} And {num_2} Is Equal\n")

else:
    print(f"{num_2} Is Max Number ")
