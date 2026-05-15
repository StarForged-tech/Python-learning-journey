''' 
Types of Comparison Operators:
  >   greater than
  <   less than
  >=  greater than or equal to
  <=  less than or equal to
  ==  equal to
  !=  not equal to       '''

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")


''' Program to check whether the student is Pass or Fail. If marks are greater than or equal to 40 then print Pass otherwise Fail.
Take input from user   ''' 
marks = float(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")
