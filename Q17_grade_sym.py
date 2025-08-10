# Assign grade with /+ -(A+, B,- etc.) based on marks.

marks = int(input("Enter Your Marks: "))

if(marks >= 97):
    grade = "A+"
elif(marks >= 93):
    grade = "A"
elif(marks >= 90):
    grade = "A-"
elif(marks >= 87):
    grade = "B+"
elif(marks >= 83):
    grade = "B"
elif(marks >= 80):
    grade = "B-"
elif(marks >= 77):
    grade = "C+"
elif(marks >= 73):
    grade = "C"
elif(marks >= 70):
    grade = "C-"
elif(marks >= 67):
    grade = "D+"
elif(marks >= 63):
    grade = "D"
elif(marks >= 60):
    grade = "D-"
else:
    grade = "F"
print("Your Grade is :",grade)

