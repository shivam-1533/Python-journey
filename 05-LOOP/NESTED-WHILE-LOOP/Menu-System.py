# Create a simple game menu using a while loop.

# Define the available menu options.
option_1 = "Play"
option_2 = "Settings"

print("\nTo exit the game, enter option 3.")

# Keep displaying the menu until the user chooses to exit.
while True:
    option = int(
        input(
            "\nYour Options Are:\n\n"
            "1 - Play\n"
            "2 - Settings\n"
            "3 - Exit\n"
            "Enter Your Option: "
        )
    )

    # Handle the selected menu option.
    if option == 1:
        print(f"\nYou selected: {option_1}\n")

    elif option == 2:
        print(f"\nYou selected: {option_2}\n")

    elif option == 3:
        print("\n<----- GAME OVER ----->\n")
        break

    else:
        print("\nInvalid option. Please choose 1, 2, or 3.\n")
