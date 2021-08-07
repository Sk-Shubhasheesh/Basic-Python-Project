# Hello,In the second challenge we create a Miles Per Hour Conversion App
print("Welcome to the MPH to MPS Conversion App")
# Gather user input
mph = float(input("\nWhat is your Speed in Miles Per Hour: "))
# Convert to MPS
mps = mph*0.44704
mps = round(mps, 4)
print("\nYour Speed Meters Per Second is " + str(mps) + ".")

