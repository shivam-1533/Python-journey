# WAP FOR DISCOUNT PRISE IN ANY PRODUCT 

'''

finel_prize = float(input("ENTER FINEL PRIZE OF THE PRODUCT: "))

orignel_prize = float(input("ENTER ORIGNEL PRIZE OF THE PRODUCT: "))

dis_per = float(input("ENTER HOW MUCH DISC YOU WANT GIVE THE COSTUMER: "))

discount = orignel_prize - (finel_prize * dis_per / 100)

print(discount)

'''


original_prize = float(input("ENTER ORIGINAL PRIZE OF PRODUCT: "))
disc_per = float(input("ENTER PERCENT DISCOUNT YOU WANT TO GIVE THE CUSTUMER: "))

finel_prize = original_prize - (original_prize * disc_per / 100)
dis_prize = (original_prize * disc_per / 100)

print(f"FINEL PRIZE IS: {finel_prize} AND DISCOUNT IS: {dis_prize}")