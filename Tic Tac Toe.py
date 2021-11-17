import pygame
import sys
import numpy as np
from pygame import color
from pygame import display
from pygame import event
from pygame import draw
from pygame.constants import MOUSEBUTTONDOWN, QUIT
import time


pygame.init()

board = np.zeros((3, 3))

game_over = False


# constante
BOARD_ROWS = 3
BOARD_COLS = 3
WIDTH = 900
HEIGHT = 900
BG_COLOR = (224, 224, 224)
LINES_COLOR = (87, 85, 84)
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
WIN_LINE = (192, 192, 192)
myfont = pygame.font.SysFont('Comic Sans MS', 130)

# setari ecran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption("Tic Tac Toe aka X si O")


def check_availible(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def player_move(row, col, player):
     board[row][col] = player


def draw_lines():
    pygame.draw.line(screen, LINES_COLOR, (300, 30), (300, 870), 5)
    pygame.draw.line(screen, LINES_COLOR, (600, 30), (600, 870), 5)
    pygame.draw.line(screen, LINES_COLOR, (30, 300), (870, 300), 5)
    pygame.draw.line(screen, LINES_COLOR, (30, 600), (870, 600), 5)


def draw_x_y():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, WHITE, (col * 300 + 50, row * 300 + 250), (col * 300 + 250, row * 300 + 50), 15)
                pygame.draw.line(screen, WHITE, (col * 300 + 50, row * 300 + 50), (col * 300 + 250, row * 300 + 250), 15)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLACK, (col * 300 + 150, row * 300 + 150), 100, 15)


def check_winner(player):
    counter = 0
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        pygame.draw.line(screen, WIN_LINE, (50, 150), (850, 150), 10)
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        pygame.draw.line(screen, WIN_LINE, (50, 450), (850, 450), 10)
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        pygame.draw.line(screen, WIN_LINE, (50, 750), (850, 750), 10) 
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(screen, WIN_LINE, (30, 30), (870, 870), 10)
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        pygame.draw.line(screen, WIN_LINE, (50, 850), (850, 50), 10)
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        pygame.draw.line(screen, WIN_LINE, (150, 20), (150, 880), 10)
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        pygame.draw.line(screen, WIN_LINE, (450, 20), (450, 880), 10)
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        pygame.draw.line(screen, WIN_LINE, (750, 20), (750, 880), 10)
        return True
    else:
        return False



# main loop
player = 1

draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            clicked_row = int(mouse_y // 300)
            clicked_col = int(mouse_x // 300)

            print(clicked_row, clicked_col)

            if check_availible(clicked_row, clicked_col) and not game_over:
                if player == 1:
                    player_move(clicked_row, clicked_col, 1)
                    check_winner(1)
                    print(check_winner(1))
                    draw_x_y()
                    player = 2

                elif player == 2:
                    player_move(clicked_row, clicked_col, 2)
                    check_winner(2)
                    print(check_winner(2))
                    draw_x_y()
                    player = 1

            if check_winner(1):
                game_over = True
                textsurface = myfont.render('Player 1 wins!', True, (255, 15, 0))
                screen.blit(textsurface,(50, 350))
            
            if check_winner(2):
                game_over = True
                textsurface = myfont.render('Player 2 wins!', True, (255, 15, 0))
                screen.blit(textsurface,(50, 350))
                
    
    pygame.display.update()

