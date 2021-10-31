import pygame
import datetime
from config import COLORS
from classes.player import Player
from classes.enemy import Enemy
from classes.star import Star


class Display:
    def __init__(self, width: int = 1200, height: int = 600, caption: str = 'Space Invaders'):
        self.width = width
        self.height = height
        self.caption = caption
        self.size = (self.width, self.height)
        self.stars = set()
        self.sprites = set()
        self.is_fullscreen = False
        self.created_stars = datetime.datetime.now()
        self.create()

    def create(self):
        pygame.init()
        self.display = pygame.display
        self.screen = pygame.display.set_mode(
            size=self.size, flags=pygame.RESIZABLE)
        self.display.set_caption(self.caption)
        self.created_stars = Star.create(
            display=self, last_recorded_time=self.created_stars, is_initial=True)

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
        enemies = set()
        self.created_stars = Star.create(
            display=self, last_recorded_time=self.created_stars)
        for sprite in sprites_copy:
            sprite.update(self)
            if isinstance(sprite, Player):
                player = sprite
            elif isinstance(sprite, Enemy):
                enemies.add(sprite)
            else:
                self.screen.blit(sprite.sprite, sprite.position)
        for enemy in enemies:
            self.screen.blit(enemy.sprite, enemy.position)
        self.screen.blit(player.sprite, player.position)
