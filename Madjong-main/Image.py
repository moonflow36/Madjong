import pygame


class Image:
    def __init__(self, image, pos_x, pos_y):
        self.image_name = image
        self.image = pygame.image.load(image)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.weight = 50
        self.height = 100
        self.select = False
        self.hidden = False

    def draw(self, screen):
        if not self.hidden:
            screen.blit(self.image, (self.pos_x, self.pos_y))
