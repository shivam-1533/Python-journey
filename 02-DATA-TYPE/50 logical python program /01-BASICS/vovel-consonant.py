# Check whether an alphabet is a Vowel or a Consonant.

a = input("Enter word: ")

vovel = "a" or "e" or "i" or "o" or "u"
if vovel in a:
    print(a,"is vovel")
else:
    print(a,"is consonant")