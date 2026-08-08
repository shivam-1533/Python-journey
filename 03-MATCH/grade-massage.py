grade = input("Enter Grade (A/B/C/D/F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")
