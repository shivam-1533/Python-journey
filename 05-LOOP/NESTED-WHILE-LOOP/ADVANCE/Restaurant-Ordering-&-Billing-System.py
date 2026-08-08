# Create a restaurant ordering and billing system using nested while loops.

print("======================================")
print("       RESTAURANT ORDERING SYSTEM")
print("======================================")

customer = input("Enter customer name: ")
total = 0
items = 0

# Main restaurant menu.
while True:
    print("\n========== FOOD CATEGORIES ==========")
    print("1. Pizza")
    print("2. Burger")
    print("3. Drinks")
    print("4. Desserts")
    print("5. View Bill")
    print("6. Checkout")
    print("=====================================")

    category = int(input("Select category: "))

    if category == 1:
        # Pizza menu.
        while True:
            print("\n---------- PIZZA MENU ----------")
            print("1. Margherita - ₹250")
            print("2. Farmhouse   - ₹350")
            print("3. Paneer Pizza - ₹400")
            print("4. Back")

            choice = int(input("Select pizza: "))

            if choice == 4:
                break

            if choice == 1:
                item = "Margherita Pizza"
                price = 250

            elif choice == 2:
                item = "Farmhouse Pizza"
                price = 350

            elif choice == 3:
                item = "Paneer Pizza"
                price = 400

            else:
                print("Invalid choice.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity.")
                continue

            total += price * quantity
            items += quantity

            print(f"{item} added to order.")

    elif category == 2:
        # Burger menu.
        while True:
            print("\n---------- BURGER MENU ----------")
            print("1. Veg Burger     - ₹120")
            print("2. Cheese Burger  - ₹180")
            print("3. Chicken Burger - ₹220")
            print("4. Back")

            choice = int(input("Select burger: "))

            if choice == 4:
                break

            if choice == 1:
                item = "Veg Burger"
                price = 120

            elif choice == 2:
                item = "Cheese Burger"
                price = 180

            elif choice == 3:
                item = "Chicken Burger"
                price = 220

            else:
                print("Invalid choice.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity.")
                continue

            total += price * quantity
            items += quantity

            print(f"{item} added to order.")

    elif category == 3:
        # Drinks menu.
        while True:
            print("\n---------- DRINKS MENU ----------")
            print("1. Coke    - ₹60")
            print("2. Coffee  - ₹100")
            print("3. Juice   - ₹120")
            print("4. Back")

            choice = int(input("Select drink: "))

            if choice == 4:
                break

            if choice == 1:
                item = "Coke"
                price = 60

            elif choice == 2:
                item = "Coffee"
                price = 100

            elif choice == 3:
                item = "Juice"
                price = 120

            else:
                print("Invalid choice.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity.")
                continue

            total += price * quantity
            items += quantity

            print(f"{item} added to order.")

    elif category == 4:
        # Dessert menu.
        while True:
            print("\n---------- DESSERT MENU ----------")
            print("1. Ice Cream - ₹100")
            print("2. Cake      - ₹180")
            print("3. Brownie   - ₹150")
            print("4. Back")

            choice = int(input("Select dessert: "))

            if choice == 4:
                break

            if choice == 1:
                item = "Ice Cream"
                price = 100

            elif choice == 2:
                item = "Cake"
                price = 180

            elif choice == 3:
                item = "Brownie"
                price = 150

            else:
                print("Invalid choice.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity.")
                continue

            total += price * quantity
            items += quantity

            print(f"{item} added to order.")

    elif category == 5:
        print("\n========== CURRENT BILL ==========")
        print(f"Customer : {customer}")
        print(f"Items    : {items}")
        print(f"Subtotal : ₹{total:.2f}")
        print("==================================")

    elif category == 6:
        if total == 0:
            print("No items ordered.")
            continue

        # Calculate discount.
        if total >= 5000:
            discount_rate = 20

        elif total >= 2500:
            discount_rate = 10

        elif total >= 1000:
            discount_rate = 5

        else:
            discount_rate = 0

        discount = total * discount_rate / 100
        after_discount = total - discount
        gst = after_discount * 5 / 100
        final_amount = after_discount + gst

        print("\n======================================")
        print("           FINAL RESTAURANT BILL")
        print("======================================")
        print(f"Customer       : {customer}")
        print(f"Total Items    : {items}")
        print(f"Subtotal       : ₹{total:.2f}")
        print(f"Discount       : ₹{discount:.2f}")
        print(f"GST            : ₹{gst:.2f}")
        print("--------------------------------------")
        print(f"FINAL AMOUNT   : ₹{final_amount:.2f}")
        print("======================================")
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid category.")
