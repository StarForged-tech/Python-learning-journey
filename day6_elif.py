'''    Some programs have multiple outputs/paths depending upon the conditions applied and for that reason we use elif in our codes      '''
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

else:
    print("Grade: Fail")




'''   Program to ask user for temperature and 
if temperature is greater than or equal to 40 then it displays "Very Hot" or if temperature greater than or equal to 25 then it displays "Pleasant Weather", otherwise displays "Cold Weather"    '''


temp = float(input("Enter temperature: "))
if temp >= 40:
    print("Very Hot")

elif temp >= 25:
    print("Pleasant Weather")

else:
    print("Cold Weather")