#  WAP TO FIND TABLE OF NUMBER AND TAKE INPUT FROM USER. 

num = int(input("Enter Number To Find Table: "))

#  LOGIC TO FIND TABLE

for i in range (1, 11):
    print(num,"x",i,"=",num * i)