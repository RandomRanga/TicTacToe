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
        print(self.squares)

    #Marks the correct square with correct player
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

    #Checks if square is empty return bool
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0




class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1
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
                    game.next_turn()
                    print(board.squares)
                



        pygame.display.update()


main()