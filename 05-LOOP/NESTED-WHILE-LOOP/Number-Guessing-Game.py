#  take a gusing number from user 

secret = 9

while True:

    guess = int(input("Enter a num : "))

    if guess == secret:
        print("\n==== You Won ====\n")
        exit()
    else:
        print("\n==== Try Again ====\n")