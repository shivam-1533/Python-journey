opt_1 = "play"
opt_2 = "settings"

print("\n To Exit The Game Enter Num- 3\n")

while True:
    opt = int(input("\nYour Option Is -->\n\n1- Play\n2-Settings\n3-Exit\nEnter Your Option : "))

    if opt == 1:
        print("\nYou Have Entered option for- ", opt_1, "\n")

    elif opt == 2:
        print("\nYou Have Entered option for- ",opt_2,"\n")

    elif opt == 3:
        print("\n<-----THIS GAME IS OVER ----->\n")
        exit()
