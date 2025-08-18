# Capitalize first letter of each word manually

user_input = input("Enter: ")
a = user_input.split()
new = ""

for ch in a:
      new += ch[0].upper() + ch[1:].lower() + " "
print(new.strip())
