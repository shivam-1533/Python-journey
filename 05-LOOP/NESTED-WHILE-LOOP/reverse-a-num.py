# Digit Reverser

num = int(input("Enter The Number You Want To Reverse : ")) # to take user input for reverse a number 

reverse = 0 

while num > 0:
    digit = num % 10 
    reverse = reverse * 10 + digit
    num //= 10

print(reverse)