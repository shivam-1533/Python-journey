# ============================================================
#               SMALLEST & LARGEST NUMBER
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


smallest = numbers[0]
largest = numbers[0]


for num in numbers:
    if num < smallest:
        smallest = num

    if num > largest:
        largest = num


print("\n" + "=" * 60)
print("                 FINAL RESULT")
print("=" * 60)

print(f"\nSMALLEST IS : {smallest}")
print(f"LARGEST IS  : {largest}")


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
