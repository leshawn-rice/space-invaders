from classes.sprite import Sprite
from classes.bullet import Bullet
import pygame


class Player(Sprite):
    def __init__(self, image: str = 'images/player.png', width: int = 100, height: int = 100):
        super().__init__(image=image, width=width, height=height, x_position=200, y_position=600 - height)
        self.bullets = set()

    def shoot_bullet(self):
        bullet = Bullet(image='images/bullet.png', x_position=(self.x_position+(self.width / 2) - 24 / 2), y_position=(self.y_position + 25))
        bullet.was_shot = True
        self.bullets.add(bullet)



    