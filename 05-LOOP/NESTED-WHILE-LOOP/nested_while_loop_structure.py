# Convert minutes into seconds using nested while loops.

# Take the number of minutes as input.
num = int(input("\nEnter the number of minutes: "))

# Start counting minutes from 1.
minute = 1

# Process each minute until the given limit.
while minute <= num:
    second = 1

    # Display each second within the current minute.
    while second <= 60:
        print(f"Minute {minute} | Second {second}")
        second += 1

    # Display the appropriate message after each minute.
    if minute < num:
        print("\nStarting the next minute...\n")
    else:
        print("\nProgram ended.\n")

    minute += 1
