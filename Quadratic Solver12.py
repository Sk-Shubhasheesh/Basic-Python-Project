# Hello, In the 12th challenge we create a Quadratic Equation  Solver App
import cmath
# Print Welcome information
print("Welcome to the Quadratic Equation Solver App")
print("\nA Quadratic Equation is of the from ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is imaginary portion.")

# Get user input
eq_number = int(input("\nHow many equtions would like to solve today: "))
# Loop throug and solve each eqution
for i in range(eq_number):
    print("\nSolving equation #" + str(i+1))
    print("---------------------------------------")
    a = float(input("\nPlease enter your value of a (coefficient of x^2):"))
    b = float(input("\nPlease enter your value of b (coefficient of x):"))
    c = float(input("\nPlease enter your value of c (coefficient):"))
    # solving the Quadratic  formula
    x1 = (-b + cmath.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2-4*a*c))/(2*a)

    print("\nThe solutions to " + str(a) + "x^2" + str(b) + "x " + str(c) + " =0 are: ")
    print("\n\tx1 = " + str(x1))
    print("\n\tx2 = " + str(x2))

print("\nThank you for using the Quadratic Equation  Solver App. Goodbye. ")




