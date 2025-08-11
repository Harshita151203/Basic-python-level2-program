#  Print multiplication table from 2 to 10.
   
for ch in range(2,11):
    for i in range(1,11):
        print(f"{ch} X {i} = {i*ch}")
    print()