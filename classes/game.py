import sys
import pygame
import random
from classes.display import Display
from classes.player import Player
from classes.enemy import Enemy


class Game:
    def __init__(self):
        self.display = Display(caption='Space Invaders')
        self.player = Player()
        self.enemies = set()
        self.display.sprites.add(self.player)
        self.playing = True
        self.paused = False
        self.loop()

    def quit(self):
        self.playing = False
        pygame.quit()
        sys.exit(0)

    def pause(self):
        self.paused = not self.paused
        while self.paused:
            self.check_input()

    def handle_movement(self, keys):
        if keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()

    def handle_shot(self, keys):
        # get time of last shot bullet, if X ms have elapsed, then shoot buller
        if keys[pygame.K_SPACE]:
            self.player.shoot_bullet()

    def handle_keys(self, key):
        if not self.paused:
            self.handle_movement(key)
            self.handle_shot(key)

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.pause()

        keys = pygame.key.get_pressed()
        self.handle_keys(keys)

    def create_enemies(self):
        self.enemies = set(
            [sprite for sprite in self.display.sprites if isinstance(sprite, Enemy)])
        if len(self.enemies) < 5:
            for i in range(5 - len(self.enemies)):
                x = random.randint(0, self.display.width - 100)
                y = 0
                enemy = Enemy(x_position=x, y_position=y)
                self.enemies.add(enemy)
                self.display.sprites.add(enemy)

    def check_collisions(self):
        for enemy in self.enemies:
            enemy.check_collision_bullet(self.player)

    def loop(self):
        while self.playing:
            self.check_input()
            self.check_collisions()
            self.create_enemies()
            self.display.update()
