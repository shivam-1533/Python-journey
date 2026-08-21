# ============================================================
#              LARGEST & SECOND LARGEST NUMBER
# ============================================================


n = int(input("\nENTER THE NUMBER OF ELEMENTS: "))

numbers = []


print("\n" + "-" * 60)
print("              ENTER LIST ELEMENTS")
print("-" * 60)

for index in range(n):
    element = int(input(f"ENTER ELEMENT AT INDEX {index}: "))
    numbers.append(element)


print("\n" + "=" * 60)
print("                 YOUR LIST")
print("=" * 60)

print(f"\nCOLLECTION : {numbers}")


largest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num


second_largest = None


for num in numbers:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num


print("\n" + "=" * 60)
print("                 FINAL RESULT")
print("=" * 60)

print(f"\nLARGEST NUMBER        : {largest}")
print(f"SECOND LARGEST NUMBER : {second_largest}")

print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
