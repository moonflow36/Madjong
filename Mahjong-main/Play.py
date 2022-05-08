import pygame
import random
import sys


class Play:
    def __init__(self):
        pygame.init()
        self.pole = pygame.image.load(r"img/pole.png")
        self.pos = (0, 0)
        self.HEIGHT = 800
        self.WEIGHT = 1200
        self.screen = pygame.display.set_mode((self.WEIGHT, self.HEIGHT))
        self.image1 = pygame.image.load(r"img/kartinka1.png")
        self.image2 = pygame.image.load(r"img/kartinka2.png")
        self.image3 = pygame.image.load(r"img/kartinka3.png")
        self.image4 = pygame.image.load(r"img/kartinka4.png")
        self.o = [self.image1, self.image1, self.image2, self.image2, self.image3, self.image3, self.image4,
                  self.image4]

    def close(self):
        self.screen.blit(self.pole, self.pos)
        self.position_and_draw_picture()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.flip()

    def position_and_draw_picture(self):
        pos = pygame.mouse.get_pos()
        mouse_x, mouse_y = pos[0], pos[1]
        pos_x = []
        pos_y = []
        for i in range(len(self.o)):
            x = random.randint(0, 1100)
            pos_x.append(x)
            y = random.randint(0, 700)
            pos_y.append(y)
        for j in range(8):
            self.screen.blit(self.o[j], (pos_x[j], pos_y[j]))
        if pos[0]+50 <= pos_x[0] and pos[1]+100 <= pos_y[0]:
            pass

    def delete(self):

