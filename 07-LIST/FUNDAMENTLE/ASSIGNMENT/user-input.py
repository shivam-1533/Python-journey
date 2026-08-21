# ============================================================
#                    NAME COLLECTION
# ============================================================


n = int(input("\nENTER THE NUMBER OF ELEMENTS: "))

names = []


print("\n" + "-" * 60)
print("              ENTER ELEMENT NAMES")
print("-" * 60)

for index in range(n):
    element = input(f"ENTER NAME AT INDEX {index}: ")
    names.append(element)


print("\n" + "=" * 60)
print("                 YOUR COLLECTION")
print("=" * 60)

print(f"\nCOLLECTION : {names}")


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
