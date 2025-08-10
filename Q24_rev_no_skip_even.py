# Print numbers in reverse skipping even numbers.

'''Note: range(n, 0) generates nothing because in Python,
the default step for range(start, stop) is +1,
and if the start (n) is greater than the stop (0),
the loop will never run.'''

n = int(input("Enter: "))

for i in range(n,0,-1):
    if i % 2 != 0:
        print(i)
