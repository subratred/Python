
#code for checking if a given year by the user is leap year or not.

# User enters the year
year = int(input("Enter Year: "))

# Checking for leap year
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
