import random as rd 
logo ='''
 ____                      _               _____                       
|  __ \                   (_)             |  __ \                      
| |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___  
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \ 
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/ 
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___| 
                                    __/ |                              
                                   |___/                               
'''




EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS =5
#function to check user's guess against actual answer
def check_answer(guess,answer ,turns):
    ''' checks answer against guess.Returs the number of turns remaining'''
    if guess > answer :
        print('Too high')
        return turns-1
    elif guess < answer:
        print('Too low')
        return turns-1
    else:
        print(f'You got it! the answer was {answer}.')

def set_difficulty():
    level = input('Choose a difficulty. type "easy" or "hard :"').lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():  
    print(logo)
    print('Welcome To The Guessing Game !')
    print('I am thinking the number between 1 and 100')
    answer = rd.randint(1,100)
    turns = set_difficulty()
    guess=0
    while guess!= answer:
        print(f'You have {turns} attempts remaining to guess the number')
        guess = int(input('Make A Guess :'))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
