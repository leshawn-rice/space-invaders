from classes.sprite import Sprite
from config import COLORS
import pygame


class Lives:
    def __init__(self, lives: int = 5, x_position: int = 13, y_position: int = 13, size: int = 25):
        self.lives = lives
        self.max_lives = lives
        self.size = size
        self.x_position = x_position
        self.y_position = y_position
        self.position = (self.x_position, self.y_position)
        self.color = COLORS.get('WHITE')
        self.background_color = COLORS.get('BLUE')
        self.font = pygame.font.Font("freesansbold.ttf", self.size)
        self.text = '<3 ' * self.lives + '</3' * \
            (0 + (self.max_lives - self.lives))
        self.sprite = self.font.render(
            self.text, True, self.color, self.background_color)

    def remove(self):
        self.lives -= 1
        self.text = '<3 ' * self.lives + '</3' * \
            (0 + (self.max_lives - self.lives))
        self.sprite = self.font.render(
            self.text, True, self.color, self.background_color)

    def add(self):
        self.lives += 1
        self.text = '<3 ' * self.lives + '</3' * \
            (0 + (self.max_lives - self.lives))
        self.sprite = self.font.render(
            self.text, True, self.color, self.background_color)
