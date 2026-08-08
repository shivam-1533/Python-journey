# Display the weekday based on a number from 1 to 7.

# Take the user's name and day number as input.
name = input("Enter your name: ")
day = int(input("Enter the day number (1-7): "))

# Check whether the entered day number is valid.
if day < 1 or day > 7:
    print("Invalid input! Please enter a number between 1 and 7.")

elif day == 1:
    print(f"{day} is Monday. Today is a working day for you. 👨‍💻")

elif day == 2:
    print(f"{day} is Tuesday. Today is a working day for you. 👨‍💻")

elif day == 3:
    print(f"{day} is Wednesday. Today is a working day for you. 👨‍💻")

elif day == 4:
    print(f"{day} is Thursday. Today is a working day for you. 👨‍💻")

elif day == 5:
    print(f"{day} is Friday. Today is a working day for you. 👨‍💻")

elif day == 6:
    print(f"{day} is Saturday. It's the weekend. Enjoy! 🎉")

elif day == 7:
    print(f"{day} is Sunday. It's your day off. 🧘")

# Display a thank-you message.
print(f"{name}, thank you for visiting! 🙏")
