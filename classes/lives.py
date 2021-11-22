from classes.sprite import Sprite
from config import COLORS
import pygame


class Lives:
    def __init__(self, lives: int = 5, x_position: int = 5, y_position: int = 0, size: int = 25):
        self.lives = lives
        self.max_lives = lives
        self.size = size
        self.x_position = x_position
        self.y_position = y_position
        self.position = (self.x_position, self.y_position)
        self.color = COLORS.get('RED')
        self.background_color = COLORS.get('BLUE')
        self.font = pygame.font.Font('fonts/seguisym.ttf', self.size)
        self.text = '♥ ' * self.lives + '♡ ' * \
            (0 + (self.max_lives - self.lives))
        self.sprite = self.font.render(
            self.text, True, self.color, self.background_color)

    def remove(self):
        self.lives -= 1
        self.text = '♥ ' * self.lives + '♡ ' * \
            (0 + (self.max_lives - self.lives))
        self.sprite = self.font.render(
            self.text, True, self.color, self.background_color)

    def add(self):
        self.lives += 1
        self.text = '♥ ' * self.lives + '♡ ' * \
            (0 + (self.max_lives - self.lives))
        self.sprite = self.font.render(
            self.text, True, self.color, self.background_color)
