import pyglet, resources
from random import randint
import time


class Chicken(pyglet.sprite.Sprite):
    toggle_x = 1
    toggle_y = 1
    dir_x = 1
    dir_y = 1
    dead = False

    def __init__(self, *args, **kwargs):
        super(Chicken, self).__init__(resources.chicken_sprite, *args, **kwargs)
        self.velocity_x = 200.0
        self.velocity_y = 200.0

    def switch_toggles(self, tx, ty, dir_x, dir_y):
        self.toggle_x = tx
        self.toggly_y = ty
        self.dir_x = dir_x
        self.dir_y = dir_y

    def move(self, dt):
        self.x += self.toggle_x * self.dir_x * self.velocity_x * dt
        self.y += self.toggle_y * self.dir_y * self.velocity_y * dt
        self.check_bounds()

    def die(self):
        rand = randint(1,5)
        #rand = 1
        time.sleep(rand)
        while self.velocity_x > 0:
            dv = randint(0, 10)
            #dv = 30
            self.velocity_x -= dv
            self.velocity_y -= dv
            time.sleep(randint(0, 100)/100)
        self.dead = True
        self.image = resources.chicken_dead
        
    def update(self, dt):
        rand = randint(0, 100)
        if rand > 95:
            rand = randint(1, 12)
            if rand == 1:
                self.switch_toggles(1, 1, 1, 1)
            elif rand == 2:
                self.switch_toggles(1, 1, -1, 1)
            elif rand == 3:
                self.switch_toggles(1, 1, 1, -1)
            elif rand == 4:
                self.switch_toggles(1, 1, -1, -1)
            elif rand == 5:
                self.switch_toggles(0, 1, 1, 1)
            elif rand == 6:
                self.switch_toggles(0, 1, -1, 1)
            elif rand == 7:
                self.switch_toggles(0, 1, 1, -1)
            elif rand == 8:
                self.switch_toggles(0, 1, -1, -1)
            elif rand == 9:
                self.switch_toggles(1, 0, 1, 1)
            elif rand == 10:
                self.switch_toggles(1, 0, -1, 1)
            elif rand == 11:
                self.switch_toggles(1, 0, 1, -1)
            elif rand == 12:
                self.switch_toggles(1, 0, -1, -1)
        self.move(dt)

    def check_bounds(self):
        min_x = -self.image.get_max_width()/2
        min_y = -self.image.get_max_height()/2
        max_x = 838 - self.image.get_max_width()/2
        max_y = 500 - self.image.get_max_height()/2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
