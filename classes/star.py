from classes.sprite import Sprite

class Star(Sprite):
    def __init__(self, image: str = 'images/star.png', width: int = 25, height: int = 25, x_position: int = 0, y_position: int = 0):
        super().__init__(image, width, height, x_position, y_position)