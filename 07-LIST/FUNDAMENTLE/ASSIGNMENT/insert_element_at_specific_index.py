# ============================================================
#              INSERT ELEMENT AT POSITION
# ============================================================


n = int(input("\nENTER THE NUMBER OF ELEMENTS: "))

numbers = []


print("\n" + "-" * 60)
print("              ENTER LIST ELEMENTS")
print("-" * 60)

for index in range(n):
    element = input(f"ENTER ELEMENT AT INDEX {index}: ")
    numbers.append(element)


print("\n" + "=" * 60)
print("                 YOUR LIST")
print("=" * 60)

print(f"\nCOLLECTION : {numbers}")


position = int(input("\nENTER THE POSITION: "))

new_element = input("ENTER THE NEW ELEMENT: ")


if position < len(numbers):
    numbers.insert(position, new_element)


print("\n" + "=" * 60)
print("                 UPDATED LIST")
print("=" * 60)

print(f"\nCOLLECTION : {numbers}")


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
