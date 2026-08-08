
# Program: List Directory Contents

# This program displays all files and folders
# present in the current working directory.

import os

# Specify the directory path.
path = "."

# Get the list of files and folders in the directory.
contents = os.listdir(path)

# Print each item in the directory.
for item in contents:
    print(item)
