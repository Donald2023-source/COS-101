age = int(input('Enter your age '))

if age >= 100:
    print('You are too old to sign up')
elif age >= 18:
    print('Sign up Successfull')
else:
    print('You can not sign up')


operator = input("Enter an operator (+ - * /) ")
num1 = float(input('Enter your 1st number '))
num2 = float(input('Enter your 2nd number '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('You have not selected a valid operator')

unit = input('Please select Kg(k) or Lb(L) ')
weight = float(input('Enter your weight '))

if unit.upper() == 'K':
    print(f"{weight * 2.204} lbs")
elif unit.upper() == 'L':
    print(f"{weight * 0.45} kg ")
else:
    print('Something went wrong ')