import sys
from os import path

import pygame

pygame.init()
from Play import Play


class Pole:
    def __init__(self):
        self.HEIGHT = 800
        self.WEIGHT = 1200
        self.screen = pygame.display.set_mode((self.WEIGHT, self.HEIGHT))
        self.pole = pygame.image.load(r"img/pole.png")
        self.pos = (0, 0)
        self.pos_button = (600, 800)
        self.menu = pygame.image.load(r"img/button_play.png")
        self.play = Play()
        self.r = pygame.Rect(0, 0, 100, 200)

    def close(self):
        self.screen.blit(self.pole, self.pos)
        self._draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.play.close()
                    sys.exit()
            pygame.display.flip()

    def _draw(self):
        self.screen.blit(self.menu, self.pos_button)


pole = Pole()
pole.close()
