# Print factorial of only odd numbers from 1 to N.

def myfact(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n*myfact(n-1)
        
n = int(input("Enter: "))

for i in range(1, n + 1):
   if(i % 2 != 0):
    print(f"{i}! = {myfact(i)}")




