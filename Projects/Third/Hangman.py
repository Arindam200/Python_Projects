import random as rd


stages=['''
    +----+-----+
    |    |     |
    |    O     |
    |          |
    |          |
    |          |
    |          |
    ===========
    ''',
    '''
    +----+-----+
    |    |     |
    |    O     |
    |    |     |
    |          | 
    |          |
    |          |
    ============
    ''',
    '''
    +----+-----+
    |    |     |
    |    O     | 
    |   /|     | 
    |          | 
    |          | 
    |          |
    ============
    ''',
    '''
    +----+----+
    |    |    |
    |    O    |
    |   /|\   | 
    |         |
    |         | 
    |         |
    ===========
    ''',
    '''
    +----+----+           
    |    |    |
    |    O    |
    |   /|\   |
    |   /     | 
    |         | 
    |         |
     ========== 
    ''',
    '''

    +----+-----+  
    |    |     |
    |    O     |  
    |   /|\    |
    |   / \    |                      
    |          |
    |          |
     ===========
     
    ''' ]

            
word_list=['python','java','language']  

stage_no=0

empty_list=[]

word_choose=rd.choice(word_list)

for i in word_choose:
    
    empty_list.append('_')
    
end_game= False
    
while not (end_game):
    
    guess=input('Enter The Guess Letter : ')

    for i in range(len(word_choose)):
        
            
        if word_choose[i] == guess:

            empty_list[i] = guess


    if guess not in word_choose:

        print(stages[stage_no])

        stage_no+=1

        if stage_no == 5:

            print(stages[5])

            end_game = True

            print('Awww! Lose. ):')

            break
        
    print(empty_list)
   
    if '_' not in empty_list:

        end_game= True

        print('Hurry ! You Won Game. (:')

        break
    
