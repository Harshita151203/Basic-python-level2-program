# Check if character is a symbol (not digit/alphabet).

user_input = input("Enter: ")

if len(user_input) != 1:
    print("Please enter only one character")
elif(user_input.isalnum()):
    print("No,It is not a Symbol")
else:
    print("Yes,It is a Symbol")
