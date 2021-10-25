from classes.sprite import Sprite
from classes.bullet import Bullet
import pygame
import datetime


class Player(Sprite):
    def __init__(self, image: str = 'images/player.png', width: int = 75, height: int = 75, x_position=200):
        super().__init__(image=image, width=width, height=height, x_position=x_position, y_position=600 - height)
        self.bullets = set()

    def shoot_bullet(self):
        time_diff_ms = self.get_time_diff()
        if time_diff_ms >= 50:
            self.last_recorded_time = self.current_time
            bullet = Bullet(image='images/bullet.png', x_position=self.x_position+(self.width / 2) - 10 / 2, y_position=self.y_position, shooter=self)
            self.bullets.add(bullet)

    def check_bound(self, display):
        if self.x_position <= 0:
            self.x_position = 0
        if self.x_position + self.width >= display.width:
            self.x_position = display.width - self.width
        if self.y_position <= 0:
            self.y_position = 0
        if self.y_position + self.height >= display.height:
            self.y_position = display.height - self.height

        self.position = (self.x_position, self.y_position)

    def display_bullets(self, display):
        for bullet in self.bullets:
            if bullet not in display.sprites:
                display.sprites.add(bullet)

    def update(self, display):
        self.check_bound(display)
        self.display_bullets(display)



    