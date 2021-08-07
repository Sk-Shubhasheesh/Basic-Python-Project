# Hello, In the 4th challenge we create a Right Triangle Solver App
import math
print("Welcome to the Right Triangle Solver App")
# Get user input:
side_a = float(input("\nWhat is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))
# Calculator:
side_c = math.sqrt(side_a**2 + side_b**2)
side_c = round(side_c, 4)

area = 0.5*side_a*side_b
area = round(area, 3)
# Display the Msg:
print("\nFor a triangle with leg of " + str(side_a) + " and " + str(side_b) + " the hypotenuse is : " + str(side_c))
print("\nFor a triangle with leg of " + str(side_a) + " and " + str(side_b) + " the area is : " + str(area))

