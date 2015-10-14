#!/usr/bin/env python3
import pyglet
from random import shuffle, randint
import sys
import chicken, resources, board
import math

if len(sys.argv) < 3:
    print("Usage: ./chickenrun.py rows cols")
    sys.exit(-1)

rows = int(sys.argv[1])
cols = int(sys.argv[2])
    
vidPath="chickenrun.mp4"
window_width = 838
window_height = 480
window = pyglet.window.Window(width=window_width, height=window_height, fullscreen=False)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

#player.queue(MediaLoad)
#player.play()

label = pyglet.text.Label('-1',
                          font_name='Helvetica',
                          font_size=100,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

chicken = chicken.Chicken(resources.chicken_sprite)
board = board.Board(window_width, window_height, rows, cols)
chicken.x = window_width//2
chicken.y = window_height//2


def update(dt):
    chicken.update(dt)

    
@window.event
def on_draw():
    window.clear()
    red = (255,0,0, 255,0,0, 255,0,0, 255,0,0)
    #pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
    #                     ('v2i', [10, 10, 100, 10, 100, 100, 10, 100]),
    #                     ('c3B', red))
    #board.tiles[0].draw()
    for tile in board.tiles:
        tile.draw()
    chicken.draw()
    #makeCircle(200, (chicken.x + chicken.image.get_max_width()/2), (chicken.y + chicken.image.get_max_height()/2 - 20))
    #circle.draw(pyglet.gl.GL_LINE_LOOP)
    #if player.source and player.source.video_format:
    #    player.get_texture().blit(0,0)
    #    if player.time > 9 and player.time < 19:
    #        label.draw()
    #    if player.time >= 19:
    #        label.x = window.width//2
    #        label.y = window.height//2
    #        label.draw()

def makeCircle(numPoints, cx, cy):
    global circle
    verts = []
    for i in range(numPoints):
        angle = math.radians(float(i)/numPoints * 360.0)
        x = 10 * math.cos(angle) + int(cx)
        y = 10 * math.sin(angle) + int(cy)
        verts += [x, y]
    circle = pyglet.graphics.vertex_list(numPoints, ('v2f', verts))

    
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
