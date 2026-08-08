# Create an e-commerce billing system.

# Take customer details as input.
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter product price: ₹"))
quantity = int(input("Enter quantity: "))

# Calculate the total product price.
total = price * quantity

# Calculate discount based on the total amount.
if total < 500:
    discount_percentage = 0

elif total < 2000:
    discount_percentage = 5

elif total < 5000:
    discount_percentage = 10

else:
    discount_percentage = 20

# Calculate the first discount.
discount = total * discount_percentage / 100
amount_after_discount = total - discount

# Take coupon code as input.
coupon = input("Enter coupon code (SAVE10/SAVE20/NONE): ").upper()

# Apply the coupon discount.
if coupon == "SAVE10":
    coupon_percentage = 10

elif coupon == "SAVE20":
    coupon_percentage = 20

else:
    coupon_percentage = 0

coupon_discount = amount_after_discount * coupon_percentage / 100

# Calculate the amount after the coupon discount.
amount_after_coupon = amount_after_discount - coupon_discount

# Calculate GST.
gst = amount_after_coupon * 18 / 100

# Calculate delivery charges.
if amount_after_coupon >= 1000:
    delivery_charge = 0

else:
    delivery_charge = 50

# Calculate the final bill.
final_amount = amount_after_coupon + gst + delivery_charge

# Display payment options.
print("\n========== PAYMENT METHODS ==========")
print("1. UPI")
print("2. Card")
print("3. Cash on Delivery")

payment_choice = int(input("Enter payment method: "))

# Determine the payment method.
if payment_choice == 1:
    payment_method = "UPI"

elif payment_choice == 2:
    payment_method = "Card"

elif payment_choice == 3:
    payment_method = "Cash on Delivery"

else:
    payment_method = "Invalid"

# Display the final invoice.
print("\n========================================")
print("           SHOPPING INVOICE")
print("========================================")
print(f"Customer        : {customer_name}")
print(f"Product         : {product_name}")
print(f"Quantity        : {quantity}")
print(f"Product Price   : ₹{price:.2f}")
print(f"Total Amount    : ₹{total:.2f}")
print(f"Discount        : ₹{discount:.2f}")
print(f"Coupon Discount : ₹{coupon_discount:.2f}")
print(f"GST (18%)       : ₹{gst:.2f}")
print(f"Delivery Charge : ₹{delivery_charge:.2f}")
print("----------------------------------------")
print(f"Final Bill      : ₹{final_amount:.2f}")
print(f"Payment Method  : {payment_method}")
print("========================================")
print("        Thank You for Shopping! 🙏")
print("========================================\n")
