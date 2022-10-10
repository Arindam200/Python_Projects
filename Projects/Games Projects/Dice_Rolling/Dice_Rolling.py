import random
print("-: Welcome to Dice Rolling Game :-")
while True:
    choice= input("Do you want to play?[Y/N]: ")
    if choice.lower()=="y":
        print("Rolling the dice...")
        number=random.randint(1,6)
        print("The number on the dice is: ",number)
    elif choice.lower()=="n":
        print("Ending the game...")
        break
    else:
        print("Invalid choice")
