#  WAP TO CALCULATE CURRENCY NUMBER IN YOU AMMOUNT .

first_name = input("Enter your First Name: ").strip()
last_name = input("Enter your Last Name: ").strip()

#  cheak if the input is not charector the whole program breaked and ended up if input is a str then good to go.

if not (first_name.isalpha() and last_name.isalpha()):
    print("\n[ERROR] Invalid input! Names must contain letters only (no numbers or symbols). Program stopping.")
    exit()

amount = int(input("Enter the total amount: "))

# note2000 = amount // 2000 # commented becouse 2000 currency is retired 
# amount = amount % 2000

note500 = amount // 500
amount = amount % 500

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

print("\n--- Currency Notes Breakdown ---")
# print("2000 Notes :", note2000)
print("500 Notes  :", note500)
print("100 Notes  :", note100)
print("50 Notes   :", note50)
print("20 Notes   :", note20)
print("10 Notes   :", note10)

# Agar 10 se kam (1, 2, 5 rs) bach jaye toh
if amount > 0:
    print("Remaining Balance :", amount)

print("Thank You🙏", first_name,last_name)