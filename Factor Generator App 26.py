# Hello, In the 26th challenge we create a Factor Generate App
print("Welcome to The Factor Generator App")

running = True
# Run the program until user quits
while running:
    # Get user Input
    number = int(input("\nEnter a number to determine all factors of that number: "))

    # Find the factor of the user given number
    factors = []

    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)

    # Print for the all factor
    print("\nFactors of " + str(number) + " are: ")
    for factor in factors:
        print(factor)
    # Print a summer of the factors mathematically
    print("\nIn Summary:")
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(number))

    # Ask the use if they would like to quite
    choice = input("\nRun Again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program. Have Aa great day...")



