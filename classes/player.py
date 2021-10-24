from classes.sprite import Sprite
from classes.bullet import Bullet
import pygame
import datetime


class Player(Sprite):
    def __init__(self, image: str = 'images/player.png', width: int = 50, height: int = 50):
        super().__init__(image=image, width=width, height=height, x_position=200, y_position=600 - height)
        self.bullets = set()
        self.last_shot = datetime.datetime.now()

    def shoot_bullet(self):
        current_time = datetime.datetime.now()
        time_diff_ms = (current_time -  self.last_shot).total_seconds() * 1000
        if time_diff_ms >= 50:
            self.last_shot = current_time
            bullet = Bullet(image='images/bullet.png', x_position=(self.x_position+(self.width / 2) - 24 / 2), y_position=self.y_position - 25, shooter=self)
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



    