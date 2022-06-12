import random

#welcome page
print("Welcome to Rock Paper Scissors \n")
#user input
myChoice = input("What is you input?\n Enter R, P, S \n").upper().strip()
#computer choice
computerChoice = ['R', 'P', 'S']
computer = random.choice(computerChoice)
#setting up my code

while True:
    if myChoice == computer:
        print("It's a tie")
    elif myChoice == "R":
        if computer == "S":
            print(f'you picked {myChoice} for Rock and computer picked {computer} for Scissor')
            print("You Win")
        else:
            print("You lose computer wins!!")
    elif myChoice == "P":
        if computer == "R":
            print(f'You picked {myChoice}for Paper and computer picked {computer}for Rock')
            print("You Win")
        else:
            print("You lose computer wins!!")
    elif myChoice == "S":
        if computer == "P":
            print(f'You picked {myChoice} for Scissor and computer picked {computer} for Papper')
            print("You Win")
        else:
            print("You lose computer wins!!")
    else:
        print('Enter a Valid Input')

    #asking to play again??????
    print('Do You Want to Play Again????')
    answer = input('Y or N \n').upper()

    if answer != 'Y':
        break
    else:
        continue
