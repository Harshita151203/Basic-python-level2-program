#  Swap case of all characters.

# Method 1:
my = input("Enter: ")
new = ""
for ch in my:
    if(ch == ch.upper()):
       new += ch.lower()

    else:
       new += ch.upper()
print(new)

# OR

# Method 2:
myvar = input("Enter: ")
print(myvar.swapcase())