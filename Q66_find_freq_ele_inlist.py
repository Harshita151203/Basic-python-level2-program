# Find Frequency of each element in list.

# Method 1: Manual dictionary counting.
my_list = [1,2,7,5,0,2,4,6]
new = {}

for i in my_list:
    if i in new:
        new[i] += 1
    else:
        new[i] = 1
print("Frequency of each elements in the list")

for key, value in new.items():
    print(key,":",value)


# Method 2:Using collections.Counter
from collections import Counter

mylist = [1,56,2,4,1,9]
freq = Counter(mylist)
for key ,values in freq.items():
 print(key,":",values)