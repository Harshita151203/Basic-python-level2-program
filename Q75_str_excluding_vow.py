# Create list from string excluding vowels.

mystr = input("Enter a String: ")
vow = "aeiou"
mylist = []
for ch in mystr:
    if ch not in vow:
        mylist += ch

print("List Excluding Vowels",mylist)