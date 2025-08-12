# Count total prime digits in number.

num = input("Enter Numbers as string: ")
set_prime_no = {2,3,5,7}
count = 0

for i in num:
    if int(i) in set_prime_no:
        count += 1

print(f"Total Prime Digits: {count}")