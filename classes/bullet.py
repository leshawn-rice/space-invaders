from classes.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, image: str = 'images/sprite.png', width: int = 10, height: int = 15, x_position: int = 0, y_position: int = 0, shooter=None):
        super().__init__(image=image, width=width, height=height, x_position=x_position, y_position=y_position)
        self.speed = 1.5
        self.direction = 'up'
        self.shooter = shooter

    def travel(self):
        if self.direction == 'up':
            self.move_up()
        elif self.direction == 'down':
            self.move_down()
        elif self.direction == 'move_left':
            self.move_left()
        elif self.direction == 'move_right':
            self.move_right()

    def check_bound(self, display):
        if self.x_position <= 0:
            display.sprites.remove(self)
            self.shooter.bullets.remove(self)
        if self.x_position + self.width >= display.width:
            display.sprites.remove(self)
            self.shooter.bullets.remove(self)
        if self.y_position <= 0:
            display.sprites.remove(self)
            self.shooter.bullets.remove(self)
        if self.y_position + self.height >= display.height:
            display.sprites.remove(self)
            self.shooter.bullets.remove(self)

    def update(self, display):
        self.travel()
        self.check_bound(display)
