#  Write a program to calculate the percentage of marks of 5 subs.

Hindi = float(input("Enter Merks in Hindi: "))
Math = float(input("Enter Merks in Math: "))
English = float(input("Enter Merks in English: "))
Schience = float(input("Enter Merks in Science: "))
cs = float(input("Enter Merks in CS: "))

percentage = ((Hindi + Math + English + Schience + cs) / 500) * 100

print(f"Your percentage is: {percentage}")