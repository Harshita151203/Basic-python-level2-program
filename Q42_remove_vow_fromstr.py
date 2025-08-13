# Remove all vowels from string.

my_str = input("Enter Your String: ")
new = ""

for ch in my_str:
    if ch not in "aeiouAEIOU":
       new += ch
print("Updated string: ",new)