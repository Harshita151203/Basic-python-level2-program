# Input marks in float for 3 subjects, print percentage.

try: 
    hindi = float(input("Enter: "))
    english = float(input("Enter: "))
    maths =float(input("Enter: "))
    sum = hindi+english+maths
    per = sum/3
    print(f"Percentage: {round(per,2)}%")  
except ValueError:
    print("INVALID")


 
