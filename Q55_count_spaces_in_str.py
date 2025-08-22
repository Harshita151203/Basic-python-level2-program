# Count spaces in string.

my = input("Enter: ")
count = 0

for ch in my:
    if ch == " ":
        count += 1
print("Number of spaces :", count)

