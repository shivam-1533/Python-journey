fruit = input("Enter fruit: ").lower()

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
        print("Fruit not available")
