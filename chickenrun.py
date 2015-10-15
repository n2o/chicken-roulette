#!/usr/bin/env python3
import pyglet
from random import shuffle, randint
import sys
import chicken, resources, board
import math
import time
from threading import Thread


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

board = board.Board(window_width, window_height, rows, cols)
chicken = chicken.Chicken()
chicken.x = randint(0, window_width)
chicken.y = randint(0, window_height)

# Start thread to slow down the chicken
t = Thread(target=chicken.die, args=())
t.start()


def update(dt):
    if not chicken.dead:
        chicken.update(dt)

    
@window.event
def on_draw():
    window.clear()
    red = (255,0,0, 255,0,0, 255,0,0, 255,0,0)
    for tile in board.tiles:
        tile.draw()
    chicken.draw()
    #if player.source and player.source.video_format:
    #    player.get_texture().blit(0,0)
    #    if player.time > 9 and player.time < 19:
    #        label.draw()
    #    if player.time >= 19:
    #        label.x = window.width//2
    #        label.y = window.height//2
    #        label.draw()

    
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
