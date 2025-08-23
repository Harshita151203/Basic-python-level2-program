# Take n numbers as input, remove all odd numbers.

num = int(input("Enter Number of elements: "))
var1 = []

for i in range(num):
    n = int(input(f"Enter Element {i+1}: "))
    var1.append(n)
  
var2 = []
for item in var1:
    if item % 2 == 0:
        var2.append(item)  
print(var2)

