import random as rd

paper='''

                ________
      --------'  _______)___
                 ___________)__
                  ______________)
                  _____________)
      ---------\______________) '''
rock='''
            ______ 
    -------'   ___)__
              (______)
              (______)
              (_____)
    ------\___(____)  '''
     
     
scissors='''

          _________
    -----'    _____)____
               _________)__
              _____________)                      
              (_______) 
    ----\_____(______) '''
    

available_choice=[paper,rock,scissors]    

print('**************** Happy Gaming ********************')

print(r"Enter '0' For Paper")

print(r"Enter '1' For Rock")

print(r"Enter '2' For scissors")


user_choice=int(input(('Please Enter You Choice : ')))

if user_choice >=0 and  user_choice <=2:

    print(f'Your Choice  : {available_choice[user_choice]}\n')

    print('Computer Choice : ')

    computer_choice=rd.randint(0,2)

    print(available_choice[computer_choice])

    if user_choice > computer_choice :

        if computer_choice == 0:

            print(r'You Win ! (:')

        else:

            print(r'You Lose ! ):')

    elif user_choice < computer_choice :

        if computer_choice == 1:

            print(r'You Lose !):')

        else:

            print(r'You Win ! (:')

    elif user_choice == 1:

        if computer_choice == 0:

            print(r'You Lose ! (:')

        elif computer_choice == 2:

            print(r'You Win ! ):')

    elif user_choice == computer_choice :

        print("It's A Draw")

else:

    print('Invalid Input Entered ! Please Try Again' )
