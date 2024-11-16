import math

first_name = input('Please enter your first name: ')

def calculate_quadratic():
    equ_type = input('Is the equation in the form a*x^2 + b*x + c = 0? (Y/N) ')
    if equ_type.upper() == 'Y':
        a = float(input('Please enter the value of a: '))
        b = float(input('Please enter the value of b: '))
        c = float(input('Please enter the value of c: '))

        print(f'a = {a} | b = {b} | c = {c}')

        discriminant = (b ** 2) - (4 * a * c)

        if discriminant >= 0:
            X1 = (-b + math.sqrt(discriminant)) / (2 * a)
            X2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f'X1 = {X1} | X2 = {X2}')
        else:
            print("The equation has no real roots.")
    else:
        print("Invalid input or unsupported equation format.")

def calculate_kinetic_energy():
    mass = float(input('Please enter the MASS: '))
    velocity = float(input('Please enter the VELOCITY: '))
    result = 0.5 * mass * velocity ** 2
    print(f'Kinetic Energy = {result}')

def gravitational_force():
    mass1 = float(input('Please enter the first mass: '))
    mass2 = float(input('Please enter the second mass: '))
    radius = float(input('Please enter radius: '))

    
    G = 6.674 * (10 ** -11)
    force = G * (mass1 * mass2) / (radius ** 2)
    print(f'Gravitational force = {force}')

def calculate_AP():
    a = float(input('Please enter the first term: '))
    n = float(input('Please enter the number of terms: '))
    d = float(input('Please enter the common difference: '))
    result = a + (n - 1) * d
    print(f'The nth term of the arithmetic progression is {result}')


def calculate_power():
    workdone = float(input('Please enter the work done: '))
    time = float(input('Please enter the time: '))

    power = workdone / time
    print(f'Power = {power}')


def main_menu():
    print("\nChoose an option from the following:")
    print("a) Solve a Quadratic Equation")
    print("b) Calculate Kinetic Energy")
    print("c) Calculate Gravitational Force")
    print("d) Find the nth Term of an Arithmetic Progression (AP)")
    print("e) Calculate Power")

    choice = input("Enter your choice (a, b, c, d, e): ").lower()

    if choice == 'a':
        calculate_quadratic()
    elif choice == 'b':
        calculate_kinetic_energy()
    elif choice == 'c':
        gravitational_force()
    elif choice == 'd':
        calculate_AP()
    elif choice == 'e':
        calculate_power()
    else:
        print("Invalid choice. Please select a valid option.")


main_menu()

print(f'Thank you {first_name} for using my App')
