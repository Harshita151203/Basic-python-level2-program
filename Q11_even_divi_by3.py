#  Check if number is even and divisible by 3.

num = int(input("Enter: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"Yes, {num} is an Even Number and Divisible by 3")  
else:
    print(f"No, {num} is either not even or not divisible by 3")

