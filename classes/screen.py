import pygame
from config import COLORS

class Display:
    def __init__(self, width: int = 600, height: int = 600, caption: str = 'Space Invaders'):
        self.width = width
        self.height = height
        self.caption = caption
        self.size = (self.width, self.height)
        # array of tuples where 
        self.sprites = []
        self.create()

    def create(self):
        pygame.init()
        self.display = pygame.display
        self.screen = pygame.display.set_mode(size = self.size)
        self.display.set_caption(self.caption)

    def fill(self, color: tuple = None):
        if not color:
            color = COLORS.get('BLUE')
        self.screen.fill(color)

    def update(self):
        self.fill()
        self.draw()
        self.display.update()

    def draw(self):
        for sprite in self.sprites:
            print("{} at position {}".format(sprite, sprite.position))
            self.screen.blit(sprite.sprite, sprite.position)