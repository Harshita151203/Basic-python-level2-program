# Check if two strings are anagrams. 

str1 = input("Enter: ").replace(" ","").lower() # Take two input from user.
str2 = input("Enter: ").replace(" ","").lower() # replace space and convert into lowercase.

if sorted(str1) == sorted(str2): # Sort values.
    print("String are anagrams") # print 
else:
    print("String are not anagrams")