import pygame
import sys
from Pole import Pole
from Play import Menu
pygame.init()


class Main:
    def __init__(self):
        self.pole = Pole()
        self.menu = Menu()

    def start(self):
        self.pole()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
main = Main()
main.start()