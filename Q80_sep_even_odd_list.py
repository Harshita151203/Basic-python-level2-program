# Separate even and odd numbers into two lists.

mylist = [2,67,12,9,11,3,5,89,1]

list1 = [i for i in mylist if i % 2 == 0]
list2 = [i for i in mylist if i % 2 != 0]
print("List of Even Numbers: ",list1)
print("List of odd Numbers: ",list2) 