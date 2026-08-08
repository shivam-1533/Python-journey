color = input("Enter signal color: ").lower()

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid Color")
