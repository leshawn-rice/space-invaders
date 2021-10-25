from classes.sprite import Sprite
from classes.bullet import Bullet
import pygame
import datetime


class Enemy(Sprite):
    def __init__(self, image: str = 'images/enemy.png', width: int = 50, height: int = 50, x_position=200, y_position=0):
        super().__init__(image=image, width=width, height=height,
                         x_position=x_position, y_position=y_position)
        self.bullets = set()
        self.will_be_destroyed = False
        self.destroyed = False
        self.speed = 0.25

    def shoot_bullet(self):
        time_diff_ms = self.get_time_diff()
        if time_diff_ms >= 50:
            self.last_recorded_time = self.current_time
            bullet = Bullet(image='images/bullet.png', x_position=self.x_position +
                            (self.width / 2) - 10 / 2, y_position=self.y_position, shooter=self)
            bullet.direction = 'down'
            self.bullets.add(bullet)

    def check_collision_bullet(self, player):
        for bullet in player.bullets:
            if self.x_position <= bullet.x_position <= self.x_position + self.width and self.y_position <= bullet.y_position <= self.y_position + self.height:
                self.image = pygame.image.load('images/explosion.png')
                self.sprite = pygame.transform.scale(self.image, self.size)
                self.destroyed = True

    def check_bound(self, display):
        if self.y_position > display.height:
            display.sprites.remove(self)

    def display_bullets(self, display):
        for bullet in self.bullets:
            if bullet not in display.sprites:
                display.sprites.add(bullet)

    def check_destroyed(self, display):
        if self.destroyed:
            display.sprites.remove(self)

    def update(self, display):
        self.check_bound(display)
        self.display_bullets(display)
        self.check_destroyed(display)
        self.move_down()
