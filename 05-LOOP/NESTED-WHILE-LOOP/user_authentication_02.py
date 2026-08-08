attempt = 3

pin = 1234

while attempt > 0 :

    guess = int (input ("\nENTER YOUR PIN:- "))

    if guess == pin :

        print("LOGING SUCESSFUL\n")

        break

    else :
        attempt -= 1

        if attempt > 0 :
            print(f"WRONG PASSWORD, ATTEMPT LEFT- {attempt}\n")

        else :
            print("ACCOUNT LOCKED\n")