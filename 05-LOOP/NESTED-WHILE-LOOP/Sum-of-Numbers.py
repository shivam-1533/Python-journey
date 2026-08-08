total = 0

while True:
    num = int(input("\n<-- To Exit 'Press -1' -->\n\nEnter Your Number To Add : "))

    if num >= 0:

        total += num

        print("\n<------------- Result ------------->\n")
        print("\tResult Is = ",total)
        print("\n<----------------------------------->\n\n")

    if num == -1:
        print("\n<---------------------------------------->")
        print("\t<--- PROGRAMM IS END --->")
        print("<---------------------------------------->\n\n")

        break

