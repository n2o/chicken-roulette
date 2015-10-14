import pyglet
from random import randint, shuffle


class Board(object):
    """ Initialize board, which creates the tiles """
    tiles = list()

    def __init__(self, window_width, window_height, rows, cols):
        self.window_width = window_width
        self.window_height = window_height
        self.rows = rows
        self.cols = cols
        self.lots = list(range(rows * cols))
        shuffle(self.lots)
        self.calc_tilesize()
        self.create_tiles()
        self.batch = pyglet.graphics.Batch()
        
        
    def calc_tilesize(self):
        self.tile_width = self.window_width / self.cols
        self.tile_height = self.window_height / self.rows

    def create_tiles(self):        
        for col in range(self.cols):
            for row in range(self.rows):
                # Choose random color
                c1 = randint(0, 255)
                c2 = randint(0, 255)
                c3 = randint(0, 255)
                color = (c1,c2,c3, c1,c2,c3, c1,c2,c3, c1,c2,c3)

                # Pick random lot
                lot_index = randint(0, len(self.lots)-1)
                lot = self.lots[lot_index]
                self.lots.remove(lot)
                
                x = (col % self.cols) * self.tile_width
                y = (row % self.rows) * self.tile_height
                self.tiles.append(Tile(x, y, self.tile_width, self.tile_height, color, lot))
    

class Tile(object):
    """ Class for tiles """
    def __init__(self, x, y, width, height, color, lot):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.lot = lot
        self.label = None
        self.image = None
    
    def draw_rect(self, color):
        if not self.image:
            width = int(round(self.width))
            height = int(round(self.height))
            image_pattern = pyglet.image.SolidColorImagePattern(color=color)
            self.image = image_pattern.create_image(width, height)
        self.image.blit(self.x, self.y)

    def draw(self):
        x = int(round(self.x))
        y = int(round(self.y))
        dx = int(round(self.width))
        dy = int(round(self.height))
        if not self.label:
            self.label = pyglet.text.Label(str(self.lot),
                                           font_name='Helvetica',
                                           font_size=100,
                                           x=x+dx//2, y=y+dy//2,
                                           anchor_x='center', anchor_y='center')
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', [x, y, x+dx, y, x+dx, y+dy, x, y+dy]),
                             ('c3B', self.color))
        self.label.draw()
                          

