from classes.sprite import Sprite




class Bullet(Sprite):
    def __init__(self, image: str = 'images/sprite.png', width: int = 100, height: int = 100, x_position: int = 0, y_position: int = 0):
        super().__init__(image=image, width=25, height=25, x_position=x_position, y_position=y_position)
        self.was_shot = False
        self.speed = 1.5

    def travel(self, direction):
        if direction == 'up':
            self.move_up()
        elif direction == 'down':
            self.move_down()
        elif direction == 'move_left':
            self.move_left()
        elif direction == 'move_right':
            self.move_right()
