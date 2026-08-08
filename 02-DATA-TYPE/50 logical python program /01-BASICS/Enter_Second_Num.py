#  Write a program to calculate simple interest.

P = float(input("Enter Principal Ammount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time: "))

Interest = (P * R * T) / 100

print(f"Your simple interest is {Interest}")