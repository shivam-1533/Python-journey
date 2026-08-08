# WAP TO FIND THE LARGEST NUMBER AMONG THREE NUMBERS. 

num_01 = float(input("ENTER FIRST NUMBER:"))
num_02 = float(input("ENTER SECOND NUMBER:"))
num_03 = float(input("ENTER THIRD NUMBER:"))

# Logic to find the largest number

if num_01 >= num_02 and num_01 >= num_03:
    largest = num_01

elif num_02 >= num_01 and num_02 >= num_03:
    largest = num_02

else:
    largest = num_03

print(f"THE LARGEST NUMBER IS: {largest}")


# WE CAN ALSO USE THE MAX TO FIND LARGEST NUMBER
#  num_01 = float(input("ENTER FIRST NUMBER:"))
# num_02 = float(input("ENTER SECOND NUMBER:"))
# num_03 = float(input("ENTER THIRD NUMBER:"))
# largest = max(num_01, num_02, num_03)