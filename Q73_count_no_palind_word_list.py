# count number of palindromic  words in list.

count = 0
n = int(input("Enter number of words: "))
mylist = []

for i in range(n):
   word = input(f"Enter word {i+1}: ") 
   mylist.append(word)
   
for item in mylist:
   rev = item[::-1]
   if item == rev:
     count += 1
print ("Number of palindromic words: ",count)