# Shift list left by 2 positions.

# Method 1: Slicing
mylist = [1,2,3,4,5]
shift_var = 2

mylist = mylist[shift_var:] + mylist[:shift_var]
print(mylist)

# Method 2: (deque.rotate)
from collections import deque
mylist = [1,2,3,4,5]
dq = deque(mylist)
dq.rotate(-2)

print(list(dq))