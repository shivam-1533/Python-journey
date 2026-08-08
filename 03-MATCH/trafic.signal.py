# Display the appropriate action based on the traffic signal color.

# Take the signal color as input and convert it to lowercase.
color = input("Enter signal color: ").lower()

# Display the action based on the entered color.
match color:
    case "red":
        print("Stop")

    case "yellow":
        print("Ready")

    case "green":
        print("Go")

    case _:
        print("Invalid color.")
