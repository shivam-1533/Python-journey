day = int(input("Enter day : "))

match day:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12 :
        print("Day in",day,"month is 31 ")

    case 2:
        print("Day in",day,"month is 28 / 29 ")

    case 4 | 6 | 9 | 11 :
        print("Day in",day,"moth is 30 ")