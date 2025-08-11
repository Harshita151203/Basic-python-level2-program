#  Find how many numbers between 1 to 100 are divisible by 3 but not 6

count = 0
for i in range(1,101):
    if(i % 3 == 0) and (i % 6 != 0):
        count += 1
        print(i)
print(f"Total: {count}")