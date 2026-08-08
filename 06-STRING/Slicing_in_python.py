# Get the characters from position 2 to position 5 (not included):
# The first character has index 0.

b = "Hello, World!"
print(b[2:5])

# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])


# Slice To the End

b = "Hello, World!"
print(b[2:])


# Negative Indexing

b = "Hello, World!"
print(b[-5:-2])