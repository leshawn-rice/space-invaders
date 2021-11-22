import pygame
from classes.sprite import Sprite
from classes.bullet import Bullet
from classes.sound import Sound


class Player(Sprite):
    def __init__(self, image: str = 'images/player.png', width: int = 50, height: int = 75, x_position=200):
        super().__init__(image=image, width=width, height=height,
                         x_position=x_position, y_position=600 - height)
        self.bullets = set()
        self.lives = 5
        self.sounds = {
            'shoot': Sound('sounds/shoot.mp3'),
            'lose-health': Sound('sounds/lose-health.mp3')
        }
        pygame.mixer.Sound.set_volume(self.sounds['lose-health'].sound, 1)

    def shoot_bullet(self):
        time_diff_ms = self.get_time_diff()
        if time_diff_ms >= 50:
            self.last_recorded_time = self.current_time
            bullet = Bullet(image='images/bullet.png', x_position=self.x_position +
                            (self.width / 2) - 10 / 2, y_position=self.y_position, shooter=self)
            self.bullets.add(bullet)
            self.sounds['shoot'].play()

    def check_collision_bullet(self, enemy, display):
        for bullet in enemy.bullets:
            if self.x_position <= bullet.x_position <= self.x_position + self.width and self.y_position <= bullet.y_position <= self.y_position + self.height:
                self.destroyed = True
                self.lives -= 1
                display.lives.remove()
                bullet.destroy(display)
                self.sounds['lose-health'].play()
                return

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
