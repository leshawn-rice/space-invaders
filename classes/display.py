import pygame
from config import COLORS
from classes.bullet import Bullet


class Display:
    def __init__(self, width: int = 600, height: int = 600, caption: str = 'Space Invaders'):
        self.width = width
        self.height = height
        self.caption = caption
        self.size = (self.width, self.height)
        self.sprites = set()
        self.is_fullscreen = False
        self.create()


    def create(self):
        pygame.init()
        self.display = pygame.display
        self.screen = pygame.display.set_mode(size = self.size, flags=pygame.RESIZABLE)
        self.display.set_caption(self.caption)


    def fill(self, color: tuple = None):
        if not color:
            color = COLORS.get('BLUE')
        self.screen.fill(color)


    def update(self):
        self.fill()
        self.draw()
        self.width, self.height = self.display.get_surface().get_size()
        self.display.update()

    def draw(self):
        for sprite in self.sprites:
            if isinstance(sprite, Bullet):
                sprite.travel('up')
            self.screen.blit(sprite.sprite, sprite.position)