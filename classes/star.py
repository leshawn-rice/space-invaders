from classes.sprite import Sprite
import datetime
import random


class Star(Sprite):
    MAX_STARS = 15
    
    def __init__(self, image: str = 'images/star.png', width: int = 5, height: int = 5, x_position: int = 0, y_position: int = 0):
        super().__init__(image, width, height, x_position, y_position)
        self.speed = 0.25


    @classmethod
    def create(cls, display=None, last_recorded_time=None, is_initial=False):
        current_time = datetime.datetime.now()
        time_diff_ms = (current_time -  last_recorded_time).total_seconds() * 1000
        if time_diff_ms >= 250 or is_initial:
            last_recorded_time = current_time
            for i in range(cls.MAX_STARS):
                x = random.randint(0, display.width)
                y = random.randint(0 - display.height / 2, 0)
                star = cls(x_position=x, y_position=y)
                display.sprites.add(star)
        return last_recorded_time


    def check_bound(self, display):
        try:
            if self.x_position < 0:
                display.sprites.remove(self)
            if self.x_position + self.width >= display.width:
                display.sprites.remove(self)
            if self.y_position < 0 - display.height / 2:
                display.sprites.remove(self)
            if self.y_position + self.height >= display.height:
                display.sprites.remove(self)
        except:
            # If the player goes from fullscreen to small screen issues will happen, so just clear display.stars
            sprites_copy = display.sprites.copy()
            for sprite in sprites_copy:
                if isinstance(sprite, Star):
                    display.sprites.remove(sprite)

    def update(self, display):
        self.move_down()
        self.check_bound(display)