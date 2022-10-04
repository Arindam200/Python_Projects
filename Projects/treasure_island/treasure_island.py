'''
code author: Athar Mujtaba Wani
github: @waniathar
'''

import time


def asciiArt():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/____[github:@waniathar]
*******************************************************************************                                                        
    ''')


def HighScore(startTime, endTime, playerName):
    score = round(endTime - startTime)
    print("Player: {name} Score: {score} secs".format(
        name=playerName, score=round(endTime-startTime, 2)))
    with open('score.txt', 'a+') as f:
        # if the file is empty, write the first line
        f.write("Player: {name} ; Score: {score} secs".format(
            name=playerName, score=round(endTime-startTime, 2)))
        # else if this is the high score then write it on the top of the file


def findTreausre():
    asciiArt()
    win = False
    print('''
    Welcome to Treasure Island.
    Your mission is to find the treasure.
    ''')
    print("********RULES********")
    print("--> You have to find treasure in 3 steps.")
    print("--> You have to enter the correct answer to move to the next step.")
    print("--> You have to find the treasue in least amount of time.\n\n")
    playerName = input("Enter your name: ").capitalize()

    print("The player: ", playerName)
    input("Press \"enter\" to start the game: ")
    startTime = time.time()
    firstChoice = input(
        'You\'re at a cross road. Where do you want to go? Type "left" or "right" ').lower()
    if firstChoice == 'left':
        secondChoice = input(
            'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
        if secondChoice == 'wait':
            thirdChoice = input(
                'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
            if thirdChoice == 'red':
                print('It\'s a room full of fire🔥🔥🔥. Game Over.')
            elif thirdChoice == 'yellow':
                print('You found the treasure!🏆🏆🏆 You Win!')
                win = True
            elif thirdChoice == 'blue':
                print('You enter a room of beasts👹👹👹. Game Over.')
            else:
                print('You chose a door that doesn\'t exist🙅🙅🙅. Game Over.')
        else:
            print('You get attacked by an angry trout🐊🐊🐊. Game Over.')
    else:
        print('You fell into a hole🕳️🕳️🕳️. Game Over.')
        win = False
    endTime = time.time()
    if win:
        HighScore(startTime, endTime, playerName)


if __name__ == '__main__':
    findTreausre()
