# Hello, In the 23th challenge we create a Yes Or No Polling App
print("Welcome to the Yes or No Polling App")

# Get user input
issue = input("What is the yes or no issue you will be voting on today: ")
vote_number = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for the polling results: ")

# Initilize our variable
yes = 0
no = 0
result = {}
# Simulate voting
for i in range(vote_number):
    name = input("\nEnter your full name: ").title().strip()
    if name in result.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here is our issue: " + issue)
        choice = input("What do you think...yes or no: ").lower().strip()
        if choice == 'yes' or choice == 'y':
            choice = 'yes'
            yes += 1
        elif choice == 'no' or choice == 'n':
            choice = 'no'
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
        # Add vote to the dictionary result
        result[name] = choice
        print("\nThank you " + name + "! Your vote of " + result[name] + " has been recorded.")


# Show who actually vote
total_votes = len(result.keys())
for key in result.keys():
    print(key)

# Summary the voting results
print("\nOn the following issue: " + issue)
if yes > no:
    print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
    print("No wins! " + str(no) + " votes to " + str(yes) + ".")
else:
    print("It was a Tie! " + str(no) + " votes to " + str(yes) + ".")



# Allow the admin to see actual vote
guess = input("\nTo see the voting results enter the admin password: ")
if guess == password:
    for key, value in result.items():
        print("Voter: " + key + "\t\t\tVote: " + value)
else:
    print("Sorry, that is not  the correct password.  Goodbye...")
print("\nThank you for using Yes Or No Issue Polling App.")