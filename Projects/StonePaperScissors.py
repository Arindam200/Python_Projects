def game():
    import random
    print("""
-----------------Stone Paper Scissors GAME!-----------------
1 - Stone
2 - Paper
3 - Scissors
""")

    a = ["Stone", "Paper", "Scissors"]
    i = 1
    rounds = 5
    comp = 0
    you = 0

    while i <= rounds:
        b = random.choice(a)
        c = input("Enter your Choice: ")

        if c == "1":
            c = "Stone"
        elif c == "2":
            c = "Paper"
        elif c == "3":
            c = "Scissors"
        else:
            print("Please enter a valid input!")
            continue

        if b == c:
            print(f"\nComputer: {b}\nYou: {c}\nDraw!")
            print("Rounds left: ", rounds - i)
            i += 1
        elif b == "Stone" and c == "Paper":
            print(f"\nComputer: {b}\nYou: {c}\nYou won!")
            print("Rounds left: ", rounds - i)
            you += 1
            i += 1
        elif b == "Paper" and c == "Stone":
            print(f"\nComputer: {b}\nYou: {c}\nComp won!")
            print("Rounds left: ", rounds - i)
            comp += 1
            i += 1
        elif b == "Scissors" and c == "Stone":
            print(f"\nComputer: {b}\nYou: {c}\nYou won!")
            print("Rounds left: ", rounds - i)
            you += 1
            i += 1
        elif b == "Stone" and c == "Scissors":
            print(f"\nComputer: {b}\nYou: {c}\nComp won!")
            print("Rounds left: ", rounds - i)
            comp += 1
            i += 1
        elif b == "Scissors" and c == "Paper":
            print(f"Computer: {b}\nYou: {c}\nComp won!")
            print("Rounds left: ", rounds - i)
            comp += 1
            i += 1
        elif b == "Paper" and c == "Scissors":
            print(f"\nComputer: {b}\nYou: {c}\nYou won!")
            print("Rounds left: ", rounds - i)
            you += 1
            i += 1
        else:
            print("Rounds left: ", rounds - i + 1)

        print(f"\nScore ->  Computer - {comp}   |   You - {you}\n")

    if comp > you:
        print("Better luck next time!")
    elif you > comp:
        print("Winner winner chicken dinner!")
    else:
        print("Its a TIE!")

    print("GAME OVER!\n")


game()

while True:
    replay = input("Do you want to play again[y/n]: ")
    if replay == "y":
        game()
    elif replay == "n":
        break
    else:
        continue

print("\nThanks for playing!")
input("\nPress any key to exit")
