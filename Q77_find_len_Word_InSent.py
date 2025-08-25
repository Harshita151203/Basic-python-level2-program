# Find length of each word in sentence.

mysent = input("Enter: ")
a = mysent.split()

for ch in a :
    print(ch,"=",len(ch))