import pygame
import sys
import numpy as np

from constants import *

#Pygame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
WIN.fill(BG_COLOR)


class Board:

    #Creates a matrix of zeros with dimentions rows, cols 
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        #List of empty squares, at start is all the squares
        self.empty_sqrs = self.squares
        #Num of squares with something in them
        self.marked_sqrs = 0


    #Marks the correct square with correct player
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    #Checks if square is empty return bool
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    #Finds which squares are emtpy and returns them
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs

    #Checks if all the squares have been marked 
    def isfull(self):
        return self.mark_sqr == 9

    #Checks if all the squares are empty
    def isempty(self):
        return self.empty_sqr == 0 

    




class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1  # 1 = X   2 = O
        self.showlines()

    def showlines(self):
        # Vertical lines 
        pygame.draw.line(WIN, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(WIN, LINE_COLOR, (2 * SQSIZE, 0), (2 * SQSIZE, HEIGHT), LINE_WIDTH)
        

        # Horizontal lines 
        pygame.draw.line(WIN, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(WIN, LINE_COLOR, (0, 2 * SQSIZE), (WIDTH, 2 * SQSIZE), LINE_WIDTH)


        #Draws the boarder if we want it
        # pygame.draw.line(WIN, LINE_COLOR, (0, 0), (0, HEIGHT), LINE_WIDTH)
        # pygame.draw.line(WIN, LINE_COLOR, (3 * SQSIZE, 0), (3 * SQSIZE, HEIGHT), LINE_WIDTH)
        # pygame.draw.line(WIN, LINE_COLOR, (0, (3 * SQSIZE)), (WIDTH, (3 * SQSIZE)), LINE_WIDTH)
        # pygame.draw.line(WIN, LINE_COLOR, (0, 0), (WIDTH, 0), LINE_WIDTH)

    #Draws a circle or cross in the correct location 
    def draw_fig(self, row, col):
        
        if self.player == 1: 
            #Draws a cross
            #Descending line 
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET )
            pygame.draw.line(WIN, X_COLOR, start_desc, end_desc, XO_WIDTH )
            #Accending line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET )
            pygame.draw.line(WIN, X_COLOR, start_asc, end_asc, XO_WIDTH )


            

        
        if self.player == 2: 
            #Draws a circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2 )
            pygame.draw.circle(WIN, O_COLOR, center, RADIUS, XO_WIDTH)


    #Changes whos turn it is
    def next_turn(self):
        self.player = self.player % 2 + 1




def main():

    #Creates the board
    game = Game()
    board = game.board


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Checks for when mouse button is press
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #use floor division to find which square somone has clicked on
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                
                #Ensures square is empty then marks it with correct player
                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)

                    game.next_turn()
                    
                    
             
                    
                



        pygame.display.update()


main()