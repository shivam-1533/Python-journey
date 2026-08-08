#  WRITE A PROGRAM TO FIND LEAP YEAR OR NOT 

#  to take year input from user  
year = int(input("Enter Your Year:  "))

#  take logic for find leap- year or not 

if (year % 400 == 0) or (year % 4 ==0) and (year % 100 != 0):
    print(year,"This is a Leap Year ")

# if not leap- year then print not a leap year 

else:
    print(year,"This is not a Leap Year")