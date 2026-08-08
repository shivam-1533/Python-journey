# Create a shopping cart and billing system using nested while loops.

# Take customer details.
customer_name = input("Enter customer name: ")

total = 0
product_count = 0

# Keep the shopping system active until checkout.
while True:
    print("\n================================")
    print("        SHOPPING MENU")
    print("================================")
    print("1. Add Product")
    print("2. View Current Bill")
    print("3. Checkout")
    print("4. Exit")
    print("================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Add multiple products until the customer stops.
        while True:
            print("\n---------- PRODUCTS ----------")
            print("1. Laptop       - ₹55000")
            print("2. Smartphone   - ₹25000")
            print("3. Headphones   - ₹3000")
            print("4. Keyboard     - ₹1500")
            print("5. Mouse        - ₹800")
            print("6. Back")

            product = int(input("Select product: "))

            if product == 6:
                break

            if product == 1:
                product_name = "Laptop"
                price = 55000

            elif product == 2:
                product_name = "Smartphone"
                price = 25000

            elif product == 3:
                product_name = "Headphones"
                price = 3000

            elif product == 4:
                product_name = "Keyboard"
                price = 1500

            elif product == 5:
                product_name = "Mouse"
                price = 800

            else:
                print("Invalid product.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity.")
                continue

            item_total = price * quantity
            total += item_total
            product_count += quantity

            print("\nProduct added successfully.")
            print(f"Product : {product_name}")
            print(f"Quantity: {quantity}")
            print(f"Amount  : ₹{item_total:.2f}")

    elif choice == 2:
        print("\n========== CURRENT BILL ==========")
        print(f"Customer      : {customer_name}")
        print(f"Total Items   : {product_count}")
        print(f"Subtotal      : ₹{total:.2f}")
        print("==================================")

    elif choice == 3:
        if total == 0:
            print("Your cart is empty.")
            continue

        # Calculate discount.
        if total >= 50000:
            discount_rate = 20

        elif total >= 20000:
            discount_rate = 15

        elif total >= 10000:
            discount_rate = 10

        elif total >= 5000:
            discount_rate = 5

        else:
            discount_rate = 0

        discount = total * discount_rate / 100
        after_discount = total - discount

        # Calculate GST.
        gst = after_discount * 18 / 100

        # Apply free delivery above ₹1000.
        if after_discount >= 1000:
            delivery = 0
        else:
            delivery = 100

        final_amount = after_discount + gst + delivery

        print("\n======================================")
        print("          FINAL SHOPPING BILL")
        print("======================================")
        print(f"Customer        : {customer_name}")
        print(f"Total Items     : {product_count}")
        print(f"Subtotal        : ₹{total:.2f}")
        print(f"Discount ({discount_rate}%) : ₹{discount:.2f}")
        print(f"GST             : ₹{gst:.2f}")
        print(f"Delivery        : ₹{delivery:.2f}")
        print("--------------------------------------")
        print(f"FINAL AMOUNT    : ₹{final_amount:.2f}")
        print("======================================")

        print("\nThank you for shopping!")
        break

    elif choice == 4:
        print("Shopping session ended.")
        break

    else:
        print("Invalid choice.")
