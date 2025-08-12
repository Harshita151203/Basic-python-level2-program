# Check if number is palindrome (without converting to string)

num = int(input("Enter: "))
var = num
rev = 0

while var > 0:
    new = var % 10
    rev = rev * 10 + new
    var //= 10

if(num == rev):
    print("Number is Palindrome") 
else:
    print("Number is not Palindrome")