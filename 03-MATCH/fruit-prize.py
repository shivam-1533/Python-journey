# Display the price of a fruit using the match-case statement.

# Take the fruit name as input and convert it to lowercase.
fruit = input("Enter fruit: ").lower()

# Display the price based on the selected fruit.
match fruit:
    case "apple":
        print("Price = ₹120/kg")

    case "banana":
        print("Price = ₹50/dozen")

    case "mango":
        print("Price = ₹150/kg")

    case "orange":
        print("Price = ₹80/kg")

    case _:
        print("Fruit not available.")
