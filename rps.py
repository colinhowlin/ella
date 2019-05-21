# Imports
import random, time

# Variable Definitions
hands = {1:'Rock', 2:'Paper', 3:'Scissors'}
draws = 0
wins = 0
losses = 0

def rock():
    print ('          _______')
    print ("      ---'   ____)")
    print ('            (_____)')
    print ('            (_____)')
    print ('            (____)')
    print ('      ---.__(___)')
def paper():
    print ('          _______')
    print ("      ---'   ____)____")
    print ('                ______)')
    print ('                _______)')
    print ('               _______)')
    print ('      ---.__________)')
def scissors():
    print ('          _______')
    print ("      ---'   ____)____")
    print ('                ______)')
    print ('             __________)')
    print ('            (____)')
    print ('      ---.__(___)')

# Welcome screen (& menu)
print("********************************")
print("Welcome to Rock, Paper Scissors!")
print("********************************\n")

while True:
    # Get player choice
    print("\nMake your choice!")
    print("1 for Rock")
    print("2 for Paper")
    print("3 for Scissors")

    while True:
        playerChoice = int(input(">"))
        if playerChoice < 1 or playerChoice > 3:
            print("Please choose either 1, 2 or 3!")
        else:
            break

    # Get computer choice
    computerChoice = random.randint(1, 3)

    # Print game to screen
    print("\nRock,")
    rock()
    time.sleep(1)
    print("Paper,")
    paper()
    time.sleep(1)
    print("Scissors,")
    scissors()
    time.sleep(1)
    print("Shoot!\n")
    time.sleep(1)

    print(f"Player chooses {hands[playerChoice]} <---> Computer chooses {hands[computerChoice]}")

    # Compare player and computer hands
    handDifference = playerChoice - computerChoice

    if (handDifference == 0):
        print("It's a draw!")
        draws += 1
    elif (handDifference % 3 == 1):
        print("Player Wins!")
        wins += 1
    else:
        print("Computer Wins :(")
        losses += 1
        
    print("\nWould you like to play again?")
    if (int(input("1 for yes, any other key for no: ")) == 1):
        continue
    else:
        print("\nGame results")
        print(f"Player wins: {wins}")
        print(f"Computer Wins: {losses}")
        print(f"Draws: {draws}")
        break
    