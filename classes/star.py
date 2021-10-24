from classes.sprite import Sprite

class Star(Sprite):
    def __init__(self, image: str = 'images/star.png', width: int = 5, height: int = 5, x_position: int = 0, y_position: int = 0):
        super().__init__(image, width, height, x_position, y_position)
        self.speed = 0.25

    def check_bound(self, display):
        if self.x_position <= 0:
            display.stars.remove(self)
        if self.x_position + self.width >= display.width:
            display.stars.remove(self)
        if self.y_position <= 0:
            display.stars.remove(self)
        if self.y_position + self.height >= display.height:
            display.stars.remove(self)

    def update(self, display):
        self.move_down()
        self.check_bound(display)