import time
import pygame
from classes.screen import Display
from classes.player import Player


class Game:
    def __init__(self):
        self.display = Display(width = 600, height = 600, caption = 'Space Invaders')
        self.player = Player(image='images/player.png', width=200, height=200)

        self.display.sprites.append(self.player)
        self.loop()

    def loop(self):
        for i in range(1000):
            self.display.fill()
            self.display.update()