#the program takes a number from the user and checks for the sign of that number also for zero.
#Using Nested if


num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
