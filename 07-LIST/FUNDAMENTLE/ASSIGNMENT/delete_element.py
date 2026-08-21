# ============================================================
#                  DELETE ELEMENT USING pop()
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


position = int(input("\nENTER POSITION NUMBER: "))

deleted_element = numbers.pop(position)


print("\n" + "=" * 60)
print("                 FINAL RESULT")
print("=" * 60)

print(f"\nDELETED ELEMENT : {deleted_element}")
print(f"NEW COLLECTION  : {numbers}")


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
    