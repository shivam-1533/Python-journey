# Calculate the final shopping bill after applying a discount.

# Take customer and product details as input.
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter product price: ₹"))
quantity = int(input("Enter quantity: "))

# Calculate the total price.
total = price * quantity

# Calculate the discount based on the total amount.
if total < 1000:
    discount_percentage = 0

elif total < 5000:
    discount_percentage = 5

elif total < 10000:
    discount_percentage = 10

else:
    discount_percentage = 20

# Calculate the discount amount.
discount = total * discount_percentage / 100

# Calculate the final amount.
final_amount = total - discount

# Display the bill.
print("\n========== SHOPPING BILL ==========")
print(f"Customer        : {customer_name}")
print(f"Product         : {product_name}")
print(f"Price           : ₹{price:.2f}")
print(f"Quantity        : {quantity}")
print(f"Total Amount    : ₹{total:.2f}")
print(f"Discount        : {discount_percentage}%")
print(f"Discount Amount : ₹{discount:.2f}")
print(f"Final Amount    : ₹{final_amount:.2f}")
print("===================================")
