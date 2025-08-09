#  Check if character is alphabet and lowercase.

my_char = input("Enter: ")

if(my_char.isalpha()):
 is_alpha = True
else:
 is_alpha = False

if(my_char.islower()):
 is_lower = True
else:
 is_lower = False

if(is_alpha and is_lower ):
 print("Character is an alphabet and in lowercase")
elif(is_alpha):
 print("Character is an alphabet but not in lowercase")
elif(is_lower):
 print("Character is in lowercase but not an alphabet")
else:
 print("Character is neither an alphabet nor in lowercase")