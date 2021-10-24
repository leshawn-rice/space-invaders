import pygame
import datetime

class Sprite:
    def __init__(self, image: str = 'images/sprite.png', width: int = 100, height: int = 100, x_position: int = 0, y_position: int = 0):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.size = (self.width, self.height)
        self.speed = 0.5
        self.sprite = pygame.transform.scale(self.image, self.size)
        self.x_position = x_position
        self.y_position = y_position
        self.position = (self.x_position, self.y_position)
        self.last_recorded_time = datetime.datetime.now()

    def get_time_diff(self):
        self.current_time = datetime.datetime.now()
        return (self.current_time - self.last_recorded_time).total_seconds() * 1000


    def move(self, x: int = 0, y: int = 0):
        self.x_position = x 
        self.y_position = y 
        self.position = (self.x_position, self.y_position)
    
    def move_left(self):
        self.move(x = self.x_position - self.speed, y = self.y_position)

    def move_right(self):
        self.move(x = self.x_position + self.speed, y = self.y_position)

    def move_up(self):
        self.move(x = self.x_position, y = self.y_position - self.speed)

    def move_down(self):
        self.move(x = self.x_position, y = self.y_position + self.speed)

    def update(self, display):
        pass