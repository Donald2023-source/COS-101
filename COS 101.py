import math

first_name = input('Please enter your first name: ')

def calculate_area_of_triangle():
    base = float(input('Please enter base '))
    height = float(input('Please enter height '))
    result = 0.5 * base * height
    print(result)

def calculate_kinetic_energy():
    mass = float(input('Please enter the MASS: '))
    velocity = float(input('Please enter the VELOCITY: '))
    result = 0.5 * mass * velocity ** 2
    print(f'Kinetic Energy = {result}')

def calculate_speed():
    distance = float(input('Please enter distance '))
    time = float(input('Please enter time '))
    result = distance * time
    print(result)


def calculate_AP():
    a = float(input('Please enter the first term: '))
    n = float(input('Please enter the number of terms: '))
    d = float(input('Please enter the common difference: '))
    result = a + (n - 1) * d
    print(f'The nth term of the arithmetic progression is {result}')


def calculate_area_of_trapezoid():
    a = float(input('Please enter a '))
    b = float(input('Please enter b '))
    h = float(input('Please enter h '))
    result = ((a + b) * h) / 2
    print(result)


def main_menu():
    print("\nChoose an option from the following:")
    print("a) Calculate Area of a triangle")
    print("b) Calculate Kinetic Energy")
    print("c) Calculate Speed")
    print("d) Find the nth Term of an Arithmetic Progression (AP)")
    print("e) Calculate area of a trapezoid")

    choice = input("Enter your choice (a, b, c, d, e): ").lower()

    if choice == 'a':
        calculate_area_of_triangle()
    elif choice == 'b':
        calculate_kinetic_energy()
    elif choice == 'c':
        calculate_speed()
    elif choice == 'd':
        calculate_AP()
    elif choice == 'e':
        calculate_area_of_trapezoid()
    else:
        print("Invalid choice. Please select a valid option.")


main_menu()

print(f'Thank you {first_name} for using my App')
