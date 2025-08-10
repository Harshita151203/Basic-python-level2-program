# Print sum of numbers divisible by 7 up to N.  

n = int(input("Enter: "))
my_sum = 0
for i in range(1,n+1):
    if (i % 7 == 0):
      my_sum += i

print(my_sum)      