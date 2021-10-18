import pygame

class Sprite:
    def __init__(self, image: str = 'images/sprite.png', width: int = 100, height: int = 100, x_position: int = 0, y_position: int = 0):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.size = (self.width, self.height)
        self.sprite = pygame.transform.scale(self.image, self.size)
        self.x_position = x_position
        self.y_position = y_position
        self.position = (self.x_position, self.y_position)

    def move(self, x, y):
        self.x_position = x 
        self.y_position = y 