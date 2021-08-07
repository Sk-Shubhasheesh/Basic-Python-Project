# Hello, In the 7th challenge we create a Different type of list program
num_strings = ['15','100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_list = [[1,2,3], [4,5,6], [7,8,9]]
# Summary of each table
print("\t\tSummary Table")

print("\nThe Variable num_strings is a " +str(type(num_strings)) +".")
print("It Contains the Element:" +str(num_strings))
print("The Element " + num_strings[0] + " is a " + str(type(num_strings[0])) + ".")

print("\nThe Variable num_ints is a " +str(type(num_ints)) +".")
print("It Contains the Element:" +str(num_ints))
print("The Element " + str(num_ints[0]) + " is a " + str(type(num_ints[0])) + ".")

print("\nThe Variable num_floats is a " +str(type(num_floats)) +".")
print("It Contains the Element:" +str(num_floats))
print("The Element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])) + ".")

print("\nThe Variable num_list is a " +str(type(num_list)) +".")
print("It Contains the Element:" +str(num_list))
print("The Element " + str(num_list[0]) + " is a " + str(type(num_list[0])) + ".")

# sorting the list
num_strings.sort()
num_ints.sort()

print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(num_strings))
print("Sorted num_ints: " + str(num_ints))
print("\nStrings are sorted alphabetically while integers are sorted numerically!!!")