# Check if number is divisible by both 2 and 5.

num = int(input("Enter: "))

if num % 2 == 0 and num % 5 == 0:
    print(f"{num} is Divisible by 2 and 5")
else:
    print(f"{num} is not Divisible by both 2 and 5")