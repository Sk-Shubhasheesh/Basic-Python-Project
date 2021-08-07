# Hello, In the 20th challenge we create a Rock , paper and scissor game
import random
print("Welcome to a Game of Rock, Paper, Scissors")

# Get user input
rounds = int(input("\nHow Many Rounds would you like to Play: "))
# Initialize variable
moves = ['rock', 'paper', 'scissors']
p_score = 0
c_score = 0
# The main game loop
for game_round in range(rounds):
    # print the main game screen  and get user input
    print("\nRound " + str(game_round + 1))
    print("\nPlayer: " + str(p_score) + "\tComputer: " + str(c_score))

    # Get the computer score
    c_index = random.randint(0,2)
    c_choice = moves[c_index]

    # Get the players move
    p_choice = input("Time to pick.....rock, paper, scissors: ").lower().strip()

    # If players makes a valid choice
    if p_choice in moves:
        print("\tComputer: " + c_choice)
        print("\tPlayer: " + p_choice)
        # if computer choose rock
        if p_choice == 'rock' and c_choice == 'rock':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif p_choice == 'paper' and c_choice == 'rock':
            winner = 'player'
            phrase = 'Paper Covers Rock!'
        elif p_choice == 'scissors' and c_choice == 'rock':
            winner = 'computer'
            phrase = 'Rock Smashes Scissors!'
        # Computer choose paper
        elif p_choice == 'rock' and c_choice == 'paper':
            winner = 'computer'
            phrase = 'Paper Covers Rock'
        elif p_choice == 'paper' and c_choice == 'paper':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif p_choice == 'scissors' and c_choice == 'paper':
            winner = 'player'
            phrase = 'Scissors Cut Paper!'
        # Computer choose Scissors
        elif p_choice == 'rock' and c_choice == 'scissors':
            winner = 'player'
            phrase = 'Rock Smashes Scissors!'
        elif p_choice == 'paper' and c_choice == 'scissors':
            winner = 'computer'
            phrase = 'Scissors Cut Paper!'
        elif p_choice == 'scissors' and c_choice == 'scissors':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        # Catch for any other condition
        else:
            print("Round Winner not Calculated.")
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        # Display round result
        print("\t" + phrase)
        if winner == 'player':
            print("\tYou Win Round " + str(game_round+1) + ".")
            p_score += 1
        elif winner == 'computer':
            print("\tComputer Wins Round " + str(game_round+1) + ".")
            c_score +=1
        else:
            print("\tThis Round was a Tie.")
    # Else the player did not make a valid move
    else:
        print("That is not a valid game option!")
        print("Computer gets the pont!")
        c_score += 1


# Game has ended print final result

print("\nFinal Game Results")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(p_score))
print("\tComputer Score: " + str(c_score))

if p_score > c_score:
    print("\tWINNER:   PLAYER!!!")
elif c_score > p_score:
    print("\tWINNER:  COMPUTER :-(")
else:
    print("\tThe Game was Tie.")





