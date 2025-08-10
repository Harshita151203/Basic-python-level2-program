#  Print squares of even numbers only up to N.

n = int(input("Enter: "))

for i in range(1,n+1):
    if i % 2 == 0:
        sq = i**2
        print(sq)  

