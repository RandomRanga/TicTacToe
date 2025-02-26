import pygame
import sys

from constants import *

#Pygame setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
WIN.fill(BG_COLOR)


class Game:

    def __init__(self):
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
      




def main():

    #Creates the board
    game = Game()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()