# ============================================================
#                  PYTHON LIST - PRACTICE
# ============================================================
# Is program mein hum Python List ke kuch important
# operations ko practice karenge.
#
# Topics:
# 1. List ki length nikalna
# 2. First element access karna
# 3. Last element access karna
# 4. List ke item ko replace karna
# 5. Specific position par item add karna
# 6. List ke end mein item add karna
# 7. List se item remove karna
# 8. List ko ascending order mein sort karna
# 9. Sirf even numbers ki list banana
# 10. Har number ka square nikalna
# 11. List ko reverse karna
# ============================================================


numbers = [10, 25, 30, 45, 50, 65, 80]


# ------------------------------------------------------------
# 1. List Ki Length Nikalna - len()
# ------------------------------------------------------------
# len() function list ke andar total items ki counting
# return karta hai.
#
# Is list mein total 7 elements hain.

print("=" * 60)
print("1. LIST KI LENGTH - len()")
print("=" * 60)

print("\nTotal Elements:", len(numbers))


# ------------------------------------------------------------
# 2. First Element Print Karna
# ------------------------------------------------------------
# Python list ki indexing 0 se start hoti hai.
#
# Isliye first element ka index 0 hota hai.
#
# numbers[0] -> list ka first element

print("\n" + "=" * 60)
print("2. FIRST ELEMENT")
print("=" * 60)

print("\nFirst Element:", numbers[0])


# ------------------------------------------------------------
# 3. Last Element Print Karna
# ------------------------------------------------------------
# Negative indexing ka use karke hum list ka last element
# easily access kar sakte hain.
#
# numbers[-1] -> list ka last element

print("\n" + "=" * 60)
print("3. LAST ELEMENT")
print("=" * 60)

print("\nLast Element:", numbers[-1])


# ------------------------------------------------------------
# 4. List Ke Item Ko Replace Karna
# ------------------------------------------------------------
# List mutable hoti hai, iska matlab hai ki hum existing
# item ki value ko change kar sakte hain.
#
# Yahan index 2 par 30 ko 35 se replace kiya gaya hai.

print("\n" + "=" * 60)
print("4. LIST ITEM REPLACE KARNA")
print("=" * 60)

numbers[2] = 35

print("\n30 ko 35 se replace karne ke baad:")
print(numbers)


# ------------------------------------------------------------
# 5. Specific Position Par Item Add Karna - insert()
# ------------------------------------------------------------
# insert() method kisi specific index par new item add karta hai.
#
# Syntax:
# list.insert(index, value)
#
# Yahan index 2 par 40 add kiya gaya hai.

print("\n" + "=" * 60)
print("5. insert() - SPECIFIC POSITION PAR ITEM ADD")
print("=" * 60)

numbers.insert(2, 40)

print("\nIndex 2 par 40 add karne ke baad:")
print(numbers)


# ------------------------------------------------------------
# 6. List Ke End Mein Item Add Karna - append()
# ------------------------------------------------------------
# append() method list ke END mein ek new item add karta hai.
#
# Yahan list ke end mein 100 add kiya gaya hai.

print("\n" + "=" * 60)
print("6. append() - END MEIN ITEM ADD KARNA")
print("=" * 60)

numbers.append(100)

print("\n100 add karne ke baad:")
print(numbers)


# ------------------------------------------------------------
# 7. List Se Item Remove Karna - remove()
# ------------------------------------------------------------
# remove() method kisi particular VALUE ko list se remove
# karta hai.
#
# Yahan 25 ko list se remove kiya gaya hai.
#
# Note:
# remove() index nahi, balki value ko remove karta hai.

print("\n" + "=" * 60)
print("7. remove() - LIST SE ITEM REMOVE KARNA")
print("=" * 60)

numbers = [10, 25, 30, 45, 50, 65, 80]

numbers.remove(25)

print("\n25 remove karne ke baad:")
print(numbers)


# ------------------------------------------------------------
# 8. List Ko Ascending Order Mein Sort Karna - sort()
# ------------------------------------------------------------
# sort() method list ke numbers ko ascending order mein
# arrange karta hai.
#
# Ascending order:
# Smallest -> Largest
#
# Example:
# 10, 25, 30, 45, 50...

print("\n" + "=" * 60)
print("8. SORTING - ASCENDING ORDER")
print("=" * 60)

numbers = [10, 25, 30, 45, 50, 65, 80]

numbers.sort()

print("\nAscending Order:")
print(numbers)


# ------------------------------------------------------------
# 9. Sirf Even Numbers Ki List Banana
# ------------------------------------------------------------
# List comprehension ka use karke hum sirf even numbers
# ki ek new list bana sakte hain.
#
# num % 2 == 0 check karta hai ki number even hai ya nahi.
#
# Agar remainder 0 hai, to number even hai.

print("\n" + "=" * 60)
print("9. EVEN NUMBERS KI LIST")
print("=" * 60)

numbers = [10, 25, 30, 45, 50, 65, 80]

even = [num for num in numbers if num % 2 == 0]

print("\nEven Numbers:")
print(even)


# ------------------------------------------------------------
# 10. Har Number Ka Square Nikalna
# ------------------------------------------------------------
# List comprehension ki help se hum list ke har number
# ka square calculate karke new list bana sakte hain.
#
# num ** 2 ka matlab hai:
# num × num

print("\n" + "=" * 60)
print("10. HAR NUMBER KA SQUARE")
print("=" * 60)

numbers = [10, 25, 30, 45, 50, 65, 80]

square = [num**2 for num in numbers]

print("\nSquares:")
print(square)


# ------------------------------------------------------------
# 11. List Ko Reverse Karna - reverse()
# ------------------------------------------------------------
# reverse() method list ke items ka order ulta kar deta hai.
#
# Example:
# [1, 2, 3]
#
# reverse() ke baad:
# [3, 2, 1]

print("\n" + "=" * 60)
print("11. LIST REVERSE KARNA - reverse()")
print("=" * 60)

numbers = [10, 25, 30, 45, 50, 65, 80]

numbers.reverse()

print("\nReversed List:")
print(numbers)


# ============================================================
#                         END
# ============================================================

print("\n" + "=" * 60)
print("           LIST PRACTICE COMPLETE")
print("=" * 60)
print("         Total Questions: 11")
print("=" * 60)
