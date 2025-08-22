# Count digits in string.

my_input = input("Enter: ")
count = 0
for ch in my_input:
    if ch.isdigit():
       count += 1

print("Number of digits: ", count)