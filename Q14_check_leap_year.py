# Check if the given year is a leap year, and also check if the year is a century year.
# (Century year = 100, 200, 300, ..., 1900, 2000, etc.)

year = int(input("Enter Year: "))

# For Leap Year: 
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False

# For Century:
if(year % 100 == 0):
    century = True
else:
    century = False

# For Output:

if leap and century :
    print(f"{year} is leap year and also century")
elif leap:
    print(f"{year} is leap year but not century")
elif century:
    print(f"{year} is a century but not a leap year")
else:
    print(f"{year} is neither a leap year nor a century")