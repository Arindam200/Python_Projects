import requests
import time

tellajoke = True

while tellajoke:
    ans = str(input('\n\nDo you want to read a joke?(y => yes; n => exit): '))
    if ans == 'y':
        x = requests.get('https://v2.jokeapi.dev/joke/Any')
        x = x.json()

        if 'joke' in x:
            print('\n' + x['joke'])
        else:
            print('\n' + x['setup'])
            print('...')
            time.sleep(1)
            print(x['delivery'])
    else:
        tellajoke = False
