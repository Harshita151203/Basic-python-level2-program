# Print numbers 1 to N skipping multiples of 5.

n = int(input("Enter: "))

for i in range(1,n+1):
    if (i % 5 != 0):
     print(i)
    