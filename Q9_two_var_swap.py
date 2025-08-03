# Input two float numbers and swap them.

num1 = float(input("Enter: "))
num2 = float(input("Enter: "))

num1, num2 = num2, num1
print(f"Value of num1: {num1}")
print(f"Value of num2: {num2}")

# OR

a = float(input("Enter: "))
b = float(input("Enter: "))

temp = a
a = b
b = temp
print(f"After Swapping:\n a = {a}\n b = {b}")
