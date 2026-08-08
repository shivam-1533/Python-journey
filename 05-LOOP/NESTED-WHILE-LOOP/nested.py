total = 1

while True:
    num = int(input("TO EXIT PRESS '-1'\nENTER NUMBER TO MULTIPLY: "))
    if num >= 0:
        total *= num
        print("\n<------------- Result ------------->\n")
        print("\tResult Is = ",total)
        print("\n<----------------------------------->\n\n")

    if num < 0:
        print("\n<---------------------------------------->")
        print("\t<--- PROGRAMM IS END --->")
        print("<---------------------------------------->\n\n")

        break