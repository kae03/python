# if statement
x=1
marks=49
grade=2000
day="monday"
if(x>0):
    print("The number is positive")
# if...else statement
if(marks>=50):
    print("You have passed the exam")
else:
    print("You have failed your exam")
# if ...elif.. else statement
if(grade<=29 and grade<0):
    print("You failed")
elif grade>=30 and grade<=49:
    print("You have passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distinction")
else:
    print("wrong grade entered")
#if...elif...else
if day=="monday":
    print ("you were early")
if day=="wednesday":
    print("You were on time")
elif day=="friday" :
    print("you were late")
else :
   print("you were disqualifed")
