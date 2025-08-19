# Remove duplicate characters.

my_char = input("Enter: ")
new = ""
for ch in my_char:
    if ch not in new:
        new += ch

print("After Removing Duplicates: ",new)      
