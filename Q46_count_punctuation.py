# Count all punctuation characters.

import string

n = input("Enter: ")
count = 0

for ch in n:
    if ch in string.punctuation:
         count += 1
print(f"Total Number of punctuation character: {count}")

