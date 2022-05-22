import pygame
import random
import sys
from pygame.color import THECOLORS

from Image import Image


class Play:
    def __init__(self):
        pygame.init()
        self.pole = pygame.image.load(r"img/pole.png")
        self.pos = (0, 0)
        self.HEIGHT = 800
        self.WEIGHT = 1200
        self.screen = pygame.display.set_mode((self.WEIGHT, self.HEIGHT))
        self.images = []
        self.fill_images()
        self.select = False
        self.select_image = None

    def fill_images(self):

        for i in range(1, 5):
            self.images.append(Image(f"img//kartinka{i}.png", random.randint(1, 1100), random.randint(1, 750)))
            self.images.append(Image(f"img//kartinka{i}.png", random.randint(1, 1100), random.randint(1, 750)))

    def close(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for image in self.images:
                        if image.pos_x <= pos[0] <= image.pos_x + 50 and image.pos_y <= pos[1] <= image.pos_y + 100:
                            if self.select:
                                # print(image.image_name, self.select_image.image_name)
                                if image.image_name == self.select_image.image_name:
                                    # print(image.image_name, self.select_image.image_name)
                                    self.select_image = None
                                    self.select = False
                                    image.select = False
                                    image.hidden = True
                                    for img in self.images:
                                        if img.select:
                                            img.select = False
                                            img.hidden = True
                                else:
                                    self.select_image = None
                                    self.select = False

                            else:
                                self.select_image = image
                                self.select = True
                                image.select = True
                        if image.pos_x >= pos[0] >= image.pos_x+50 and image.pos_y >= pos[1] >= image.pos_y+100:
                            if self.select:
                                if image.image_name != self.select_image.image_name:
                                    self.select_image = None
                                    self.select = True
                                    image.select = False
                                    image.hidden = False
                                    for img in self.images:
                                        if img.select:
                                            img.select = True
                                            img.hidden = False
                            else:
                                self.select_image = image
                                self.select = False
                                image.select = False


    def draw(self):
        self.screen.blit(self.pole, self.pos)
        for image in self.images:
            image.draw(self.screen)
        pygame.display.flip()

