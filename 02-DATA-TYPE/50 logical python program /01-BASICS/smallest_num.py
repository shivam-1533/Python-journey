# WAP TO FIND THE SMALLEST NUMBER AMONG THREE NUMBERS. 

num_01 = float(input("ENTER FIRST NUMBER:"))
num_02 = float(input("ENTER SECOND NUMBER:"))
num_03 = float(input("ENTER THIRD NUMBER:"))

# Logic to find the smallest number

if num_01 <= num_02 and num_01 <= num_03:
    smallest = num_01

elif num_02 <= num_01 and num_02 <= num_03:
    smallest = num_02

else:
    smallest = num_03

print(f"THE SMALLEST NUMBER IS: {smallest}")


# YOU CAN ALSO USE MIN TO FIND THE SMALLEST NUMBER IN THE GIVEN NUM

num_01 = float(input("ENTER FIRST NUMBER:"))
num_02 = float(input("ENTER SECOND NUMBER:"))
num_03 = float(input("ENTER THIRD NUMBER:"))

smallest = min(num_01, num_02, num_03)

print(smallest)