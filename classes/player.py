from classes.sprite import Sprite
import pygame


class Player(Sprite):
    def __init__(self, image: str = 'images/player.png', width: int = 100, height: int = 100):
        super().__init__(image, width, height, x_position=200, y_position=600 - height)



    