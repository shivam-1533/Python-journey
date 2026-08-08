# Check whether a number is Prime

num_01 = int(input("ENTER FIRST NUMBER:  "))

if num_01 <=0:
    print(num_01,"Is not a Valid no for 'Prime Number Logic' ")

elif num_01 % 2 == 0 or num_01 % 3 == 0:
    print(num_01,"Ia not Prime Number ")

else:
    print(num_01,"Is Prime Number ")
