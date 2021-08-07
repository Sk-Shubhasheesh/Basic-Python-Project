# Hello, In the 3rd challenge we create a Temperature Conversion App
print("Welcome to the Temperature Conversion App")
# Gather user input
temp_f=float(input("\nWhat is given Temperature in Degrees Fahrenheit: "))
# Convert temp:
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15
# Round temp:
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)
# Display the temp:
print("\nDegrees  Fahrenheit : " + str(temp_f))
print("Degrees  Celsius : " + str(temp_c))
print("Degrees  Kelvin : " + str(temp_k))

