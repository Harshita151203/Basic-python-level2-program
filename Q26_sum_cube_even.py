# Find sum of cubes of even numbers up to N.

n = int(input("Enter: "))
my_sum = 0
for i in range(2,n+1): # method2: step = 2 (skip odd numbers)
    if i % 2 == 0:
        my_cube = i**3
        my_sum += my_cube
print(my_sum)