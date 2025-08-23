# Replace all zeros with -1.

mylist = [1,2,9,0,4,9,0,3,4,0]
newlist = []

for i in mylist:
    if i != 0:
       newlist.append(i)
    else:
         newlist.append(-1)

print("Updated List: ",newlist)