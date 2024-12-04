import math
#variables: Are reusable containers of value. E.g String, boolean, float, integer

#Strings: We can use an f-string when you want to use a variable as it is used below
first_name = "Donald"
print(f"Hello {first_name}")

#integers
quantity = 12


#Float
price = 10.99

#Boolean True | False

#Typecasting is the process of converting a variable from one type to another.
name = "Donald"
age = 25
gpa = 3.2
is_Student = True

gpa = int(gpa) #converting a float to an integer
age = str(age) #converting an integer into a string
name = bool(name) #When typecasting a string to a boolean it returns true on-less the string is empty. A use case is checking if a user has entered a name in a form.

print(gpa)

#Area of a rectangle
width = float(input('Width? '))
length = float(input('Length? '))
Area = width * length
print(f"Area is { Area }cm")

#Shopping cart
item = input('What item do you want? ')
my_price = float(input('What is the price? '))
my_quantity = int(input('How many would you want? '))

print(f"You ordered { my_quantity } { item } and your total is ${ my_price * my_quantity}")


#Area of a cirlce
radius = float(input('Please enter your radius? '))
result = math.pi * pow(radius,  2)
print(result)

