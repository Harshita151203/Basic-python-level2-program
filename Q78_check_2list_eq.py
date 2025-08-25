# check if two list are equal.

list1 = [1,6,2,9,1,4]
list2 = [6,1,2,1,4,9]

if sorted(list1) == sorted(list2):
    print("Both Lists Have Same Elements")
else:
    print("List Are Not Equal")   