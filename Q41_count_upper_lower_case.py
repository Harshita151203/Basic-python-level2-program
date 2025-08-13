# Count uppercase and lowercase separately.

num = input("Enter: ")
count1 = 0
count2 = 0 

for ch in num:
 if ch.islower():
   count1 += 1
 elif ch.isupper():
   count2 += 1

print("Number of lowercase: ",count1)
print("Number of uppercase: ",count2) 