# Hello, In the 26th challenge we create a Even Odd Number Sorter App
print("Welcome to the Even Odd Number Sorter App")
running = True
# Run this program aas longer as the user wants
while running:
    # Get user input
    num_string = input("Enter a string of numbers separated by a comma (,) : ")
    num_string = num_string.replace(' ', '')
    # Convert string into list
    num_list = num_string.split(",")
    # Initialize lists to hold even/odd values
    evens = []
    odds = []

    # Calculate whether the number is even or odd
    print("\n---- Result Summary ----")
    for number in num_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print("\t" + str(number) + " is even!")
        else:
            odds.append(number)
            print("\t" + str(number) + " is odd!")

    #  Sort the list evens and odds
    evens.sort()
    odds.sort()

    # Show the even numbers
    print("\nThe following " + str(len(evens)) + " numbers are even: ")
    for even in evens:
        print("\t" + str(even))

    # Show the odds numbers
    print("\nThe following " + str(len(odds)) + " numbers are even: ")
    for odd in odds :
        print("\t" + str(odd))

    # Quit the program if the user  does not enter in 'y'
    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program. Goodbye..")