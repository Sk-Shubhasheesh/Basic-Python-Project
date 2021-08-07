# Hello, In the 19th challenge we create a Guess My Number App
import random
print("Welcome to The Guess My Number App")

# Get user input
name = input("\nHello! What is your name: ").title().strip()

# Pick a Random integer 1 to 20
print("Wellcome " + name + ", I am thinking of a number between 1 to 20.")
number = random.randint(1, 20)

# Guss The number five time
for guess_num in range(5):
    guess = int(input("\nTake a guess: "))
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
       break
# The game is done, recap winning and recap
if guess == number:
    print("\nGood job, " "! You guessed my number in " + str(guess_num+1) + " guesses!")

else:
    print("\nGame Over. The number I was thinking of was " + str(number) + ".")

