import random


def toString(choice, rock, paper, scissor):
    if choice == rock:
        return 'rock'
    elif choice == paper:
        return 'paper'
    else:
        return 'scissor'


def gameResult(computerChoice, playerChoice, rock, scissor, paper):
    # returns the win condition
    if (computerChoice == rock and playerChoice == scissor) or \
            (computerChoice == paper and playerChoice == rock) or \
            (computerChoice == scissor and playerChoice == paper):
        return 'computer wins'

    elif (playerChoice == rock and computerChoice == scissor) or \
            (playerChoice == paper and computerChoice == rock) or \
            (playerChoice == scissor and computerChoice == paper):
        return 'player wins'

    else:
        return 'draw'


def playGame():
    # starts the game by assigning colors to the players and get users inputs
    playerColor = ''
    computerColor = ''
    rock = 1
    scissor = 2
    paper = 3
    choiceList = [rock, paper, scissor]

    while playerColor != 'blue' and playerColor != 'red':
        playerColor = input('Pick blue or red:')

    print('player:', playerColor)
    if playerColor == 'red':
        computerColor = 'blue'
    else:
        computerColor = 'red'
    print('computer:', computerColor)

    while True:
        print('What do you want to choose[1=rock,2=scissor,3=paper]')
        try:
            playerChoice = int(input())
        except ValueError:
            continue
        if playerChoice == rock or playerChoice == scissor or playerChoice == paper:
            break

    computerChoice = random.choice(choiceList)

    print(computerColor + ': ', toString(computerChoice, rock, paper, scissor))
    print(playerColor + ': ', toString(playerChoice, rock, paper, scissor))

    if gameResult(computerChoice, playerChoice, rock, scissor, paper) == 'computer wins':
        print(computerColor, 'wins')

    elif gameResult(computerChoice, playerChoice, rock, scissor, paper) == 'player wins':
        print(playerColor, 'wins')

    else:
        print('It is a draw')

def displayRules():
    # displays the rules of the game
    print('Each player chooses a color: red or blue')
    print('The player whose color has the most points win')
    print('If the players choose the same, no one wins')
    print('If player A chooses rock and player B chooses scissor, player A wins and get a point')
    print('If player A chooses rock and player B chooses paper, player B wins and get a point')
    print('\n')


def welcome():
    # welcome message and menu
    print('Welcome to Rock Paper Scissors')
    while True:
        print('1. play\t2. rules')
        try:
            menuChoice = int(input())
        except ValueError:
            menuChoice = -1

        if menuChoice == 1:
            playGame()
            break

        elif menuChoice == 2:
            displayRules()

        elif menuChoice == 3:
            print("Game over!")
            break

        else:
            print('invalid choice! Please "1" or "2"')

if __name__ == '__main__':
    welcome()
