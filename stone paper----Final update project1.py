import random
guess=1
game_over=False
computer_choice=["Stone","Paper","Scissor"]

print("This Is a Stone Paper Scissor Game...")
while True:
    round = 1
    cs=0
    us=0

    print("Do You Want to play Game--->")
    u1=(input("Press Number...\n1--Play\n2--No\n---> "))
    if u1=="1" :

        for i in range(1,4):
            print(f"ROUND----> {round}")
            print("Select an option-->")
            ui=input("s-Stone\np-Paper\nsc-Scissor\n---->")
            if ui=="s":
                ui="Stone"
            elif ui=="p":
                ui="Paper"
            elif ui=="sc":
                ui="Scissor"
            round+=1
            cc = random.choice(computer_choice)

            print("Computer Choice is " + cc)
            print("Your Choice " + ui)

            if ui == cc:
                print("There is a tie\n")
            elif (ui == "Stone" and cc == "Scissor") or (ui == "Paper" and cc == "Stone") or (ui == "Scissor" and cc == "Paper"):
                print("You Won\n")
                us+=1

            else:
                print("You Lost\n")
                cs+=1

        print(f"Your Score {us}")
        print(f"Computer Score {cs}")

        if us>cs:
                print("YOU ARE THE WINNER")
        elif cs==us:
            print("There is a TIE")
        else:
                print("COMPUTER IS THE WINNER")


    elif u1=="2":

        print("Thanku For spending time\nGame Over")
        break
    else:
        print("Invalid Character")


