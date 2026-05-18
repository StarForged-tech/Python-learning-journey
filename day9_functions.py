# Learning how to organize reusable code using functions

# Function definition
# always use def keyword to define a fucntion
def greet():
    print("Hello, Ekansh!")
    print("Welcome to Python learning.")

# Calling the function
greet() # Always used outside the function definition 


# Function with parameter
# Remember parameters are container(s) without any data type. So, you can pass any data type.
def greet_user(name): #variables used in function definition are known as Parameters 
    print("Hello,", name)

# Passing argument to function
greet_user("Ekansh") #variable/values used in function calling is known as Arguments 
greet_user("Developer")


# Using function, do addition of 2 numbers and display the sum.
def sum(a,b): #function definition 
  print("Sum is",a+b)

sum(10,20) #function calling
sum(37.47,4.48)
