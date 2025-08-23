# Find all elements greater than average.

myy = [1,2,3,4,5,6,7]
avg = sum(myy)/len(myy)
for i in myy:
    if i > avg:
        print(i)    