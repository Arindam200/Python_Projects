import requests
import time

tellajoke = True

category = "Any"
while tellajoke:
    ans = str(input('\n\nDo you want to read a joke?(y => yes; n => exit; s=> settings): '))

    if ans == 'y':
        x = requests.get('https://v2.jokeapi.dev/joke/' + category)
        x = x.json()

        if 'joke' in x:
            print('\n' + x['joke'])
        else:
            print('\n' + x['setup'])
            print('...')
            time.sleep(1)
            print(x['delivery'])
    elif ans == 's':
        s_ans = str(input('Which settings would you like to edit? (c => category): '))
        if s_ans == "c":
            c_ans = str(input('Selectable categories:\n a => Any\n p => Programming\n m => Misc\n d => dark\n s => '
                              'Spooky\n c => Christmas\n'))
            if c_ans == 'p':
                category = 'Programming'
            elif c_ans == "m":
                category = "Misc"
            elif c_ans == "d":
                category = "Dark"
            elif c_ans == "s":
                category = "Spooky"
            elif c_ans == "c":
                category = "Christmas"
            elif c_ans == "a":
                category = "Any"
            print("Category " + category + " set!")
    else:
        tellajoke = False
