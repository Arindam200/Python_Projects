import os
import random as rd

paper = """

                ________
      --------'  _______)___
                 ___________)__
                  ______________)
                  _____________)
      ---------\______________) """
rock = """
            ______ 
    -------'   ___)__
              (______)
              (______)
              (_____)
    ------\___(____)  """


scissors = """

          _________
    -----'    _____)____
               _________)__
              _____________)                      
              (_______) 
    ----\_____(______) """


available_choice = [paper, rock, scissors]
score = 0

while True:
    os.system("clear")
    print("**************** Happy Gaming ********************")

    print(r"Enter '0' For Paper")

    print(r"Enter '1' For Rock")

    print(r"Enter '2' For scissors")

    try:

        user_choice = int(input(("Please Enter Your Choice: ")))

    except ValueError:

        print("Invalid Input Entered! Please Try Again")

    else:

        if user_choice >= 0 and user_choice <= 2:

            is_draw = False
            won = False

            print(f"Your Choice: {available_choice[user_choice]}\n")

            print("Computer Choice: ")

            computer_choice = rd.randint(0, 2)

            print(available_choice[computer_choice])

            if user_choice == computer_choice:

                is_draw = True

            elif user_choice == 0 and computer_choice == 1:

                won = True

            elif user_choice == 1 and computer_choice == 2:

                won = True

            elif user_choice == 2 and computer_choice == 0:

                won = True

            if is_draw:

                print("It's A Draw")

            elif won:

                score += 1
                print(r"You Won! (:")

            else:
                if score > 0:
                    score -= 1

                print("You Lost! ):")

            print(f"Score: {score}")

        else:

            print("Invalid Input Entered! Please Try Again")

    restart = input("Try Again? (y/n): ").lower()

    if restart != "y":
        break
