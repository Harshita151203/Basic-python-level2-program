# Input n names and sort alphabetically.

n = int(input("Enter number of names: ")) 
mylist = []

for i in range(n):
   names = input(f"Enter name {i+1}: ")
   mylist.append (names)

mylist.sort()

print(" Names in alphabetical onder:")

for item in mylist:
   print(item)