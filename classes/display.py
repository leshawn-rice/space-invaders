import pygame
import random
import datetime
from config import COLORS
from classes.bullet import Bullet
from classes.player import Player
from classes.star import Star


class Display:
    def __init__(self, width: int = 600, height: int = 600, caption: str = 'Space Invaders'):
        self.width = width
        self.height = height
        self.caption = caption
        self.size = (self.width, self.height)
        self.stars = set()
        self.sprites = set()
        self.is_fullscreen = False
        self.created_stars = datetime.datetime.now()
        self.create()


    def create_stars(self):
        current_time = datetime.datetime.now()
        time_diff_ms = (current_time -  self.created_stars).total_seconds() * 1000
        if time_diff_ms >= 250 or len(self.stars) == 0:
            self.created_stars = current_time
            for i in range(50):
                x = random.randint(1, self.width)
                y = random.randint(1, self.height)
                star = Star(x_position=x, y_position=y)
                self.stars.add(star)

            

    def create(self):
        pygame.init()
        self.display = pygame.display
        self.screen = pygame.display.set_mode(size = self.size, flags=pygame.RESIZABLE)
        self.display.set_caption(self.caption)
        self.create_stars()


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
        sprites_copy = self.sprites.copy()
        player = None
        self.create_stars()
        stars_copy = self.stars.copy()
        for star in stars_copy:
            star.update(self)
            self.screen.blit(star.sprite, star.position)
        for sprite in sprites_copy:
            sprite.update(self)
            if not isinstance(sprite, Player):
                self.screen.blit(sprite.sprite, sprite.position)
            else: 
                player = sprite
        self.screen.blit(player.sprite, player.position)