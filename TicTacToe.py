import copy
import random
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


    def final_state(self, show = False):
        '''
            @return 0 if there is no win yet 
            @return 1 if player 1 wins 
            @return 2 if player 2 wins 
        '''

        #Vertical wins 
        for col in range (COLS):
            #Checks everything in a col is the same and not empty. reutrns winning player
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show: 
                    if self.squares[0][col] == 2:
                        color = O_COLOR
                    else:
                        color = X_COLOR

                    start_pos = (col * SQSIZE + SQSIZE // 2, 20)
                    finish_pos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)


                    pygame.draw.line(WIN, color, start_pos, finish_pos, LINE_WIDTH)

                return self.squares[0][col]
        
        #Horizontal wins 
        for row in range (ROWS):
            #Checks everything in a row is the same and not empty. reutrns winning player
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show: 
                    if self.squares[row][0] == 2:
                        color = O_COLOR
                    else:
                        color = X_COLOR

                    start_pos = (2, row * SQSIZE + SQSIZE // 2)
                    finish_pos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)

                    pygame.draw.line(WIN, color, start_pos, finish_pos, LINE_WIDTH)
                return self.squares[row][0]

        #Diagonal wins then returns winning player
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show: 
                if self.squares[1][1] == 2:
                    color = O_COLOR
                else:
                    color = X_COLOR

                start_pos = (20, 20)
                finish_pos = (WIDTH - 20, HEIGHT - 20)

                pygame.draw.line(WIN, color, start_pos, finish_pos, LINE_WIDTH)
            return self.squares[1][1]


        if self.squares[2][0] == self.squares [1][1] == self.squares[0][2] != 0:
            if show: 
                if self.squares[1][1] == 2:
                    color = O_COLOR
                else:
                    color = X_COLOR

                start_pos = (20, HEIGHT - 20)
                finish_pos = (WIDTH - 20, 20)

                pygame.draw.line(WIN, color, start_pos, finish_pos, LINE_WIDTH)
            return self.squares[1][1]
           

        #If there is no win yet 
        return 0 

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
        return self.marked_sqrs == 9

    #Checks if all the squares are empty
    def isempty(self):
        return self.marked_sqrs == 0 

  
class AI:
    
    def __init__(self, level = 1, player = 2):
        self.level = level 
        self.player = player 

    #Returns a random empty row and col 
    def rand(self, board):
        empty_sqrs = board.get_empty_sqrs()
        index = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[index]
    
    def minimax(self, board, maximizing):
        #Check terminal case 
        case = board.final_state()

        #Player 1 wins 
        if case == 1:
            return 1, None
        #Player 2 wins
        elif case == 2:
            return -1, None
        #Draw 
        elif board.isfull():
            return 0, None

        if maximizing: 
            max_eval = -100
            best_move = None 
            empty_sqrs = board.get_empty_sqrs()

            #For each empty sqr 
            for (row, col) in empty_sqrs:
                #Create a copy of current board to not damage main board 
                temp_board = copy.deepcopy(board)
                #Marks the move on copy 
                temp_board.mark_sqr(row, col, 1)
                #Recursivly calls the function with other person turn and gets first item in list 
                eval = self.minimax(temp_board, False) [0]

                #Saves the best move 
                if eval > max_eval: 
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move


        elif not maximizing:
            min_eval = 100
            best_move = None 
            empty_sqrs = board.get_empty_sqrs()

            #For each empty sqr 
            for (row, col) in empty_sqrs:
                #Create a copy of current board to not damage main board 
                temp_board = copy.deepcopy(board)
                #Marks the move on copy 
                temp_board.mark_sqr(row, col, self.player)
                #Recursivly calls the function with other person turn and gets the first
                eval = self.minimax(temp_board, True) [0]

                #Saves the best move 
                if eval < min_eval: 
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move




    def eval(self, main_board):
        if self.level == 0:
            #Random choice bot 
            move = self.rand(main_board)
            eval = 'random'

        else: 
            #Minimax choices
            eval, move = self.minimax(main_board, False)
        
        print(f'AI has chosen the square in pos {move} with an eval of {eval}.' )

        return move



class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1  # 1 = X   2 = O
        self.gamemode = 'ai'
        self.isrunning = True
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


        elif self.player == 2: 
            #Draws a circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2 )
            pygame.draw.circle(WIN, O_COLOR, center, RADIUS, XO_WIDTH)

    #Changes whos turn it is
    def next_turn(self):
        self.player = self.player % 2 + 1

    #Checks to see if the game is over 
    def isover(self):
        return self.board.final_state(show=True) != 0 or self.board.isfull()





def main():

    #Creates the board
    game = Game()
    board = game.board
    ai = game.ai


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Checks for when mouse button is press
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #Use floor division to find which square somone has clicked on
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE


                #Ensures square is empty then marks it with correct player
                if board.empty_sqr(row, col) and game.isrunning:
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)


                    #Checks for a win and stops game if someone has won
                    if game.isover():
                        game.isrunning = False

                    #Goes to next players turn
                    game.next_turn()      


        if game.gamemode == 'ai' and game.player == ai.player:
            #Updates the screen 
            pygame.display.update()
             
            #AI methods 
            row, col = ai.eval(board)



           
            board.mark_sqr(row, col, game.player)
            game.draw_fig(row, col)
            game.next_turn()  



        #Updates the window to show everything new
        pygame.display.update()


main()