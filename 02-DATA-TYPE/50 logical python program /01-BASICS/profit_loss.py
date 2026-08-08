#  WAP TO FIND PROFIT OR LOSS IN MY BUSINESS. 

name = input("ENTER YOUR NAME:  ")

p_value = float(input("ENTER YOUR PURCHES PRIZE: "))
s_value = float(input("ENTER YOUR SELLING PRIZE: "))

if p_value > s_value:
    print(f"{name} YOU ARE IN LOSS 😥")

else:
    print(f"{name} YOU ARE IN PROFIT 😍\n")

print(name,"DO YOU WANT TO CHEACK HOW MANY PROFIT/LOSS 'type 'yes'\n")

respose = input("Enter your resposce 'yes'/'no : '").strip().lower()

if respose == 'yes':
    print(" \n----THANK YOU FOR YOUR RESPOSCE-----\n")

elif respose == 'no':
    print("\n----THANK FOR VISIT ON OUR WEBSITE----")
    exit()

elif p_value > s_value:
    print(name,"YOUR LOSS IS",s_value - p_value,"rs")

elif p_value < s_value:
    print(name,"YOUR FROFIT IS",s_value - p_value,"rs")

else:
    print("YOU ARE NITHER PROFIT NITHER LOSS")