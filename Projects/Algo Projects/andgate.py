''' An AND Gate is a logic gate in boolean algebra which results to false(0) if any of the input is
   0, and True(1) if  both the inputs are 1.
   Following is the truth table of an AND Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      0      |
   |      0      |     1      |      0      |
   |      1      |     0      |      0      |
   |      1      |     1      |      1      |
'''
'''Following is the code implementation of the AND Gate'''

def AND_Gate(input_1,input_2):
    return input_1*input_2
if __name__== '__main__':
    print('Truth Table of AND Gate:')
    print('| Input 1 |',' Input 2 |',' Output |')
    print('|      0      |','     0      |     ',AND_Gate(0,0),'     |')
    print('|      0      |','     1      |     ',AND_Gate(0,1),'     |')
    print('|      1      |','     0      |     ',AND_Gate(1,0),'     |')
    print('|      1      |','     1      |     ',AND_Gate(1,1),'     |')
    
'''Code provided by Akshaj Vishwanathan'''          
          
