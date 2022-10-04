print("WELCOME IN THE GAME OF HANGMAN")
print("THE PINK CITY ???")
word="JAIPUR"
accept="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
accept=list(accept)
word=list(word)
gword="_"*len(word)
gword=list(gword)
c=0
ip=input("ENTER YOUR GUESS LETTER  ")
if(ip not in accept):
        print("!! IT IS NOT A LETTER YOU ARE MISSING YOUR CHANCES OF WINNING GUESS WITH A LETTER !!")
while True:
    if ip.upper() in word:
        index=word.index(ip.upper())
        gword[index]=ip.upper()
        print(''.join(gword))
        word[index] = "_"
    if '_' not in gword:
        print("YOU WON THE GAME THE ANSWER WAS ",word)
        break
    else:
        ip = input("ENTER YOUR GUESS LETTER ")
    c=c+1
    print(str(int(2.5*len(word))-c)+" attempt left")
    if c>2.5*len(word):
        print("The number of available attemps finished")
        print("you cound not win the game sorry")
        break
