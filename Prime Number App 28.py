# Hello, In the 28th challenge we create a Prime Number App
import time
print("Welcome to the Prime Number App")

running = True
# Run the program as long as the user wants
while running:
    # user Input
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    option = input("Enter your choice 1 or 2: ")

    # Determine if a single number is prime
    if option == '1':
        number = int(input("\nEnter a number to determine if it is prime or not: "))
        # Prime status check
        prime_status = True
        for i in range(2, number):

            if number % i == 0:
                prime_status = False
                break
        # Print Summary
        if prime_status:
            print(str(number) + " is prime!")
        else:
            print(str(number) + " is not a prime!")


    # Determine primes within a range of values and time the calculations
    elif option == '2':
        l_bound = int(input("\nEnter the lower bond of your range: "))
        u_bound = int(input("Enter the upper bond of your range: "))

        primes = []
        # Get the current time



        start_time = time.time()

        # Check the prime status of all numbers whithin l bound and u bound
        for prime_candidate in range(l_bound, u_bound + 1):
            # 1 is note prime
            if prime_candidate > 1:
                prime_status = True
                for i in range(2, prime_candidate):
                    if prime_candidate % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            # Prime candidate is in fact prime!
            if prime_status:
                primes.append(prime_candidate)

    # Get the current time
    end_time = time.time()
    # Determine the time the calculation took
    delta_time = round(end_time - start_time, 6)

    print("\nCalculation took a total of " + str(delta_time) + " seconds.")
    print("The following number between " + str(l_bound) + " and " + str(u_bound) + " are prime: ")
    input("Press Enter to Continue..")

    for prime in primes:
        print(prime)

    else:
        print("\nThat is not valid option.")

    choice = input("\nWould you like to run the program again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for using the program. Goodbye..")