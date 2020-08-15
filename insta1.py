import random
from time import sleep
import os

clear = lambda : os.system('cls')

playerOne = 0
playerTwo = 0
win_score = 500
dice_values = [1, 2, 3, 4, 5, 6]
round_ply = 0

def roll_dice():
    dice_val = random.choice(dice_values)
    return dice_val

def curr_score():
    print(""""
        ^^^^^^^^^^^^^^^^^^^^^^
        Round Played : {}
        Player One : {}
        Player Two : {}
    """.format(round_ply, playerOne, playerTwo))

while True:
    clear()
    curr_score()
    round_ply += 1 
    print("""
    =================================
    Player 1 it's your turn.
    press Enter to roll the dice
    or
    type 'q' and enter to quit.
    =================================
    """)
    userOneInput = input(">>>")
    if userOneInput == "":
        curr_roll_value = roll_dice()
        playerOne = playerOne + curr_roll_value

        print("Player 1 rolled ", curr_roll_value)
        sleep(1)

        clear()
        curr_score()

        print("""
        =================================
        Player 2 it's your turn.
        press Enter to roll the dice
        or
        type 'q' and enter to quit.
        =================================
        """)
        userTwoInput = input(">>>")
        if userTwoInput == "":
            curr_roll_value = roll_dice()
            playerTwo = playerTwo + curr_roll_value

            print("Player 2 rolled ", curr_roll_value)
            sleep(1)
            if playerOne > win_score and playerTwo < win_score:
                print("""
                + + + + + + + + + + + + + + +
                +      Player One win       +
                + + + + + + + + + + + + + + +
                """)
                break
            elif playerOne >= win_score and playerTwo >= win_score:
                print("""
                + + + + + + + + + + + + + + +
                +           Draw            +
                + + + + + + + + + + + + + + +
                """)
                break
            elif playerOne < win_score and playerTwo > win_score:
                print("""
                + + + + + + + + + + + + + + +
                +      Player Two win       +
                + + + + + + + + + + + + + + +
                """)
                break
            
        elif userTwoInput == "q":
            print("Player 1 wins this round! ")
            playerOneWins += 1
        else:
            print("Program ended ")
            break
    elif userOneInput == "q":
        print ("Player 2 wins this round! ")
        playerTwoWins += 1
    else:
        print("Program ended . ")
        break
    
    sleep(2)
    
