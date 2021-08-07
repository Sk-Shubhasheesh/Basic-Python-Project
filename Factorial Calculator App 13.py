# Hello, In the 13th challenge we create a Factorial App Program
import math
print("Welcome to the Factorial App")

# Get user input
number = int(input("What number would you like to compute the factorial of: "))

# Display the mathematical relationship of a factorial
print(str(number) + "! = ", end="")
for i in range(1, number):
    print(str(i), end="*")
print(str(number))
# Using a Math library
fact = math.factorial(number)
print("\nHere is the result from math library: ")
print("The Factorial of " + str(number) + " is " + str(fact) + "!")

# Using My own algorithm
fact = 1
for i in range(1, number+1):
    fact = fact * i
print("\nHere is the result from my own algorithm: ")
print("The Factorial of " + str(number) + " is " + str(fact) + "!")

# Summary
print("\nIt is shown twice that " + str(number) + "! = " + str(fact) + "(with excitement)")


