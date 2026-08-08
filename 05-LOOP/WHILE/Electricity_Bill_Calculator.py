#  WAP TO FIND ELECTICITY BILL

cs_name = input("Enter Your Name:- ").strip()

account = input("\nEnter Your ID:- ")

#  logic for find bill according to unit charges
#  (first 100 units = ₹5/unit, next 100 = ₹7/unit, above 200 = ₹10/unit).

if not (cs_name.isalpha):
    print("Your Name Is Not Matched")
    exit()

else:
    print("\n<===== Loging-Successfull =====>\n")

#  after the successfull loging take user's unit that he used.

unit = float(input("\nEnter Your Units consumed:- "))

if unit <= 100 :
    net_bill = unit * 5

elif unit <= 200 and unit >100 :
        net_bill = unit * 7

elif unit > 200 :
        net_bill = unit * 10


print("\nYour Net Bill is:- ",net_bill,'\n')
