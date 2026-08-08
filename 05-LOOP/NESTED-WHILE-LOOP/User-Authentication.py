#  to take user input for his password 

password = 'shivam1234'

while True:
    passw = input("Enter your password e.g(a-z+0-9) : ")

    if passw == password:
        print("\n<------ Loging Success-full ------->\n")

        break
    else:
        print("\n<------ Try Again ------->\n")