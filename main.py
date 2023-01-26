# create tictactoe game
# use pygame
# player vs bot with random moves

import pygame
import random
import sys

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((600, 600))

# title and icon
pygame.display.set_caption("Tic Tac Toe")

# create board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# create board
def create_board():
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, (255, 255, 255), (i * 200, j * 200, 200, 200), 5)


# create x
def create_x(x, y):
    pygame.draw.line(screen, (255, 255, 255), (x * 200 + 20, y * 200 + 20), (x * 200 + 180, y * 200 + 180), 5)
    pygame.draw.line(screen, (255, 255, 255), (x * 200 + 180, y * 200 + 20), (x * 200 + 20, y * 200 + 180), 5)


# create o
def create_o(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x * 200 + 100, y * 200 + 100), 80, 5)


# check if someone won
def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0


# check if board is full
def check_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


# bot move
def bot_move():
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == 0:
            board[x][y] = 2
            break


# main loop
def main():
    # game loop
    running = True
    while running:
        # background
        screen.fill((0, 0, 0))

        # create board
        create_board()

        # events
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0] // 200
                y = event.pos[1] // 200
                if board[x][y] == 0:
                    board[x][y] = 1
                    bot_move()

        # draw x and o
        for i in range(3):
            for j in range(3):
                if board[i][j] == 1:
                    create_x(i, j)
                elif board[i][j] == 2:
                    create_o(i, j)

        # check if someone won
        if check_win() == 1:
            print("Player 1 won!")
            running = False
        elif check_win() == 2:
            print("Player 2 won!")
            running = False
        elif check_full():
            print("Draw!")
            running = False

        # update screen
        pygame.display.update()


if __name__ == "__main__":
    main()
