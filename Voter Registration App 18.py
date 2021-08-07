# Hello, In the 18th challenge we create a Voter Registration App
print("Welcome to The Voter Registration App")
# User input
name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

# Define our political party
parties = ['BJP', 'CONGRESS', 'SAMAJWADI PARTY', 'TMC', 'REPUBLIC']

# If the user is 18 or older
if age > 17:
    print("\nCongratulation " + name + " ! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")
    # display our political parties
    for party in parties:
        print("\t- " + party)
    # User input for the party they wish to join
    chosen_party = input("\nWhat party would you like to join: ").title().strip()
    # Print a message specific to the party chosen
    if chosen_party in parties:
        print("\nCongratulation " + name + " ! You have joined the " + chosen_party + " party!")
        if chosen_party == "BJP":
            print("That is a major party!")
        elif chosen_party == "SAMAJWADI PARTY" or chosen_party == "CONGRESS":
            print("That is not a major party!")
        else:
            print("This party is not a major and good party.")
    else:
        print("That is not a given party.")
# if user is not greater then 18
else:
    print("\nYou are not enough to register to vote.")
