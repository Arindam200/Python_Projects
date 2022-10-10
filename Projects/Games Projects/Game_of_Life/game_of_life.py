'''
Python Implementation of the famous zero-player game — Conway's Game of Life
Visualized using Python Turtle
Author: D1Dayer99
'''


import turtle
import random
import copy

class Game_of_Life:

    def __init__(self):
        self.screen = turtle.Screen()
        self.t = turtle.Turtle()
        turtle.tracer(0,0)
        self.t.hideturtle()
        self.lives = self.get_lives()

    def get_lives(self) -> list:
        '''
        Randomly generates 'lives' based on the chance inputted, currently set to 40% chance
        '''
        lives = []
        self.n=30
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if random.random()<0.4:
                    row.append(1)
                else:
                    row.append(0)
            lives.append(row)
        return lives
    
    def draw_square(self,x,y,size):
        '''
        Draw a square based on the input (x,y) coordinates and the length of 1 side
        Represents individual life on the board
        '''
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()
        self.t.setheading(0)
        self.t.begin_fill()
        for i in range(4):
            self.t.fd(size)
            self.t.right(90)
        self.t.end_fill()

    def display_lives(self):
        '''
        Visualize all the lives that has been randomly generated in get_lives()
        '''
        for i in range(self.n):
            for j in range(self.n):
                if self.lives[i][j] == 1:
                    self.draw_square((400/self.n)*i-200,(400/self.n)*j-200,400/self.n - 2)
        
    def check_neighbours(self,row,column) -> int:
        '''
        Check the number of 1s (neigbours) in the 'square' around the cell, not counting itself
        '''
        neighbours=0
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i == row and j == column:
                    continue
                if i < 0 or i >= self.n:
                    continue
                if j < 0 or j >= self.n:
                    continue
                if self.lives[i][j]==1:
                    neighbours += 1
        return neighbours

    def update_lives(self):
        '''
        Rule of the game: (copied from Wikipedia article of Conway's Game of Life, available at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):

        1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        '''
        temp_lives = copy.deepcopy(self.lives)
        for i in range(self.n):
            for j in range(self.n):
                num_neighbors = self.check_neighbours(i,j)
                if self.lives[i][j]==1:
                    if num_neighbors<2:
                        temp_lives[i][j] = 0
                    elif num_neighbors ==3 or num_neighbors ==2:
                        temp_lives[i][j] = 1
                    elif num_neighbors >3:
                        temp_lives[i][j] = 0
                else:
                    if num_neighbors == 3:
                        temp_lives[i][j] = 1
        self.lives = copy.deepcopy(temp_lives)
    
    def run(self):
        while True:
            self.t.clear()
            self.display_lives()
            self.update_lives()
            turtle.update()

gol = Game_of_Life()
gol.run()
turtle.done()
