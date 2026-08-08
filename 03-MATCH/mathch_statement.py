# Display the day of the week based on the entered number.

# Take the day number as input from the user.
day = int(input("Enter day (1-7): "))

# Display the corresponding day using the match-case statement.
match day:
    case 1:
        print("Today is Monday")

    case 2:
        print("Today is Tuesday")

    case 3:
        print("Today is Wednesday")

    case 4:
        print("Today is Thursday")

    case 5:
        print("Today is Friday")

    case 6:
        print("Today is Saturday")

    case 7:
        print("Today is Sunday")

    case _:
        print("Invalid day number.")
