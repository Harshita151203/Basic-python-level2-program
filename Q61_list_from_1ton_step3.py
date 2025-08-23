# Create list from 1 to N with step of 3.

# Method 1:
n = int(input("Enter: "))
my = []
for i in range (1,n+1,3):
   my.append(i)
print(my)

# Method 2:
n= int(input("Enter: "))
new = list(range(1, n+1, 3))
print(new)

