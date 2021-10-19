import sys
import pygame
from classes.display import Display
from classes.player import Player


class Game:
    def __init__(self):
        self.display = Display(width = 600, height = 600, caption = 'Space Invaders')
        self.player = Player(image='images/player.png', width=200, height=200)
        self.display.sprites.append(self.player)
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


    def handle_keys(self, key):
        if not self.paused:
            self.handle_movement(key)

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.pause()

        keys = pygame.key.get_pressed()
        self.handle_keys(keys)


    def loop(self):
        while self.playing:
            self.check_input()
            self.display.update()