import math
import random
import numpy as np
import pygame
from pygame.locals import *
from Board import Board
from Constants import Constants
from Colors import Color


class Conway:
    writing = False
    deleting = False
    delete_all = False
    quantum_fluctuation = False
    running = True

    def __init__(self, board, SCREEN):
        self.paused = None
        self.board = board
        self.SCREEN = SCREEN
        self.board = Board(self.SCREEN)

    def display_text(self, text, x_axis, y_axis, SCREEN):
        font = pygame.font.Font('freesansbold.ttf', 13)
        text = font.render(text, True, Color().get_black(), Color().get_white())
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (x_axis, y_axis)
        SCREEN.blit(text, textRect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                    print("Paused" if self.paused else "Resumed")
                elif event.key == pygame.K_q:
                    self.quantum_fluctuation = not self.quantum_fluctuation

    def run_game(self, SCREEN):
        initial_grid = self.board.create_random_grid(Constants().block_count, Constants().block_count)
        temp = initial_grid.copy()

        while True:
            self.handle_events()

            if self.running:
                pygame.display.update()

                # temp = drawGrid(temp, progress=True)
                temp = self.board.updateBoard(temp, progress=True)

                temp = temp.copy()

                if self.quantum_fluctuation:
                    self.display_text("QUANTUM FLUCTUATION ON", x_axis=92, y_axis=5, SCREEN=SCREEN)
                    r_ = random.randint(1, Constants().QUANTUM_FLUCTUATIONS_INTENSITY)
                    for i in range(r_):
                        a, b = self.board.create_out_of_nothing(Constants().block_count, Constants().block_count)
                        temp[a][b] = 1
                else:
                    self.display_text("QUANTUM FLUCTUATION OFF", x_axis=95, y_axis=5, SCREEN=SCREEN)

                pygame.display.flip()
                pygame.time.Clock().tick(Constants().FPS)
            else:
                pygame.display.update()  # Update the display to show the paused state
            initial_grid = self.board.create_random_grid(Constants().block_count, Constants().block_count)
            temp = initial_grid.copy()

            while True:
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running = False
                        quit()
                    # KEYBOARD OPERATIONS...
                    if event.type == pygame.KEYDOWN:
                        # If pressed key is ESC quit program
                        if event.key == pygame.K_ESCAPE:
                            print("ESC was pressed. quitting...")
                            quit()
                        if event.key == pygame.K_q:
                            self.quantum_fluctuation = not self.quantum_fluctuation

                        if event.key == pygame.K_SPACE:
                            x = temp.copy()
                            a = self.board.updateBoard(x, True)
                            temp = a.copy()
                            #pygame.display.update()
                            self.running = not self.running
                            print("Paused")

                    mouse_presses = pygame.mouse.get_pressed()
                    if not self.running:
                        if mouse_presses[0]:
                           # pygame.display.update()
                            temp = self.board.updateBoard(temp, False)
                            posY, posX = pygame.mouse.get_pos()

                            X = math.floor(posX / (Constants.HEIGHT / Constants.block_count))
                            Y = math.floor(posY / (Constants.HEIGHT / Constants.block_count))
                            self.writing = True

                        if mouse_presses[1]:
                            posY, posX = pygame.mouse.get_pos()
                            temp = temp.copy()
                            self.delete_all = True

                        if mouse_presses[2]:
                            posY, posX = pygame.mouse.get_pos()
                            X = math.floor(posX / (Constants().HEIGHT / Constants().block_count))
                            Y = math.floor(posY / (Constants().HEIGHT / Constants().block_count))
                            self.deleting = True
                if self.writing and not self.running:

                    temp[X][Y] = 1
                    temp = temp.copy()

                    temp = self.board.updateBoard(temp, progress=False)

                    self.display_text("", x_axis=25, y_axis=10, SCREEN=SCREEN)

                    self.writing = False




                elif self.deleting and not self.running:
                    # print("Deleting..")
                    pygame.display.update()

                    temp[X][Y] = 0
                    # temp = drawGrid(temp, progress=False)
                    temp = self.board.updateBoard(temp, progress=False)
                    # temp = temp
                    pygame.display.update()
                    self.deleting = False
                elif self.delete_all and not self.running:
                    print("DELETE ALL")
                    for xx in range(4):
                        for a in range(len(temp)):
                            for b in range(len(temp)):
                                temp[a][b] = 0
                        # temp = drawGrid(temp, progress=False)
                        temp = self.board.updateBoard(temp, progress=False)
                    pygame.display.update()

                    # temp.fill(0)

                    # temp=temp.copy()
                    self.delete_all = False

                if self.running:
                    pygame.display.update()

                    # temp = drawGrid(temp, progress=True)
                    temp = self.board.updateBoard(temp, progress=True)

                    temp = temp.copy()

                    if self.quantum_fluctuation:
                        self.display_text("QUANTUM FLUCTUATION ON", x_axis=92, y_axis=5, SCREEN=SCREEN)
                        r_ = random.randint(1, Constants().QUANTUM_FLUCTUATIONS_INTENSITY)
                        for i in range(r_):
                            a, b = self.board.create_out_of_nothing(Constants().block_count, Constants().block_count)
                            temp[a][b] = 1
                    else:
                        self.display_text("QUANTUM FLUCTUATION OFF", x_axis=95, y_axis=5, SCREEN=SCREEN)

                    pygame.display.flip()
                    pygame.time.Clock().tick(Constants().FPS)
                    #pygame.display.update()
            pygame.display.update()
