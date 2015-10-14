import pyglet


class Board(object):
    tiles = list()
    
    """ Initialize board, which creates the tiles """
    def __init__(self, window_width, window_height, rows, cols):
        self.window_width = window_width
        self.window_height = window_height
        self.rows = rows
        self.cols = cols
        self.calc_tilesize()
        self.create_tiles()

    def calc_tilesize(self):
        self.tile_width = self.window_width / self.cols
        self.tile_height = self.window_height / self.rows

    def create_tiles(self):
        for num in range(self.rows * self.cols):
            x = (num % self.cols) * self.tile_width
            y = (num % self.rows) * self.tile_height
            self.tiles.append(Tile(x, y, self.tile_width, self.tile_height))
        for tile in self.tiles:
            print(str(tile.x) + ", " + str(tile.y))    
    

class Tile(object):
    """ Class for tiles """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_rect(self, color):
        width = int(round(self.width))
        height = int(round(self.height))
        image_pattern = pyglet.image.SolidColorImagePattern(color=color)
        image = image_pattern.create_image(width, height)
        image.blit(self.x, self.y)
