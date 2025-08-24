# Find Second max and Second min. 

mylist = [1,2,83,2,5,77,11,5,21]

newlist = list(set(mylist))
newlist.sort()

if(len(mylist)<2):
    print("Not Enough Unique Elements")
else:
    sec_min = newlist[1]
    sec_max = newlist[-2]
print(f"Second Minimum Element: {sec_min}")
print(f"Second Maximum Element: {sec_max}")

