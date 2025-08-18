# Check if number is neon number.
  
# Check if a number is Neon Number

num = int(input("Enter a number: "))

# Step 1: square of number
sq = num * num  

# Step 2: sum of digits of square
digit_sum = 0
while sq > 0:
    digit_sum += sq % 10
    sq //= 10

# Step 3: compare with original number
if digit_sum == num:
    print(num, "is a Neon Number")
else:
    print(num, "is NOT a Neon Number")
