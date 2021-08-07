# Hello, In the first challenge we create a program counter App
print("Welcome to the Letter Counter App")
# Get input from user
name=input("\nWhat is your name: ").title().strip()
print("Hello, " + name + "!")
print("I will count the number of times that a specific letter occurs in a message.")
# take message from the user
message=input("\nPlease enter a message: ")

letter=input("Which letter would you like to count the occurences of: ")
# Standardize to lower case
message=message.lower()
letter=letter.lower()
# Get and display the result
letter_count=message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + " " + letter + "'s in it.")