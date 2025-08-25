# Convert String to list of ASCII codes.

mystr = input("Enter: ")

new_list = [ord(ch) for ch in mystr]
print(new_list)



