
num = int(input("\nEnter Your Minut To Convert Into Second :- "))

big = 1

while big <= num :
    small = 1

    while small <= 60:
        print(f"Minut {big} | Second {small}")

        small += 1


    if big < num :
        print("\nNext Minut Start\n")

    else :
        print("\nProgram Is End\n")
        
    big += 1