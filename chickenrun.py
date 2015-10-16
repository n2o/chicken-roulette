#!/usr/bin/env python3
import pyglet
from random import shuffle, randint
import sys
import math
import time
from threading import Thread

import resources
from board import Board
from chicken import Chicken


# Prepare winner screen
show_winner = False
trigger_winner = False
video_running = True


def show_winner_screen():
    global show_winner
    time.sleep(1)
    show_winner = True
    

def video_finished():
    video_running = False
    
    
def main():
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
    #player.eos_action = player.EOS_STOP
    #player.on_player_eos = video_finished()
    #player.on_eos = video_finished()
    #player.play()

    board = Board(window_width, window_height, rows, cols)
    chicken = Chicken()
    chicken.x = randint(0, window_width-1)
    chicken.y = randint(0, window_height-1)

    # Start thread to slow down the chicken
    Thread(target=chicken.die, args=()).start()


    def update(dt):
        global trigger_winner
        if not chicken.dead:
            chicken.update(dt)
        elif not trigger_winner:
            Thread(target=show_winner_screen, args=()).start()
            trigger_winner = True
    

    def winner_screen():
        label = pyglet.text.Label("Gewonnen hat:",
                                  font_name='Helvetica',
                                  font_size=50,
                                  x=window_width//2, y=window_height-100,
                                  anchor_x='center', anchor_y='center')
        label.draw()
        tile = board.get_tile(chicken.x+chicken.image.get_max_width()//2, chicken.y+chicken.image.get_max_width()//2)

        tile.label = None
        tile.draw(window_width//2 - tile.width//2, window_height//2 - tile.height//2)
    

    @window.event
    def on_draw():
        global show_winner
        #global video_running
        window.clear()

        #if video_running:
        #    if player.source and player.source.video_format:
        #        player.get_texture().blit(0,0)
        #else:
        if not show_winner:
            for tile in board.tiles:
                tile.draw()
            chicken.draw()
        else:
            winner_screen()
            chicken.draw()

    #
    #    if player.time > 9 and player.time < 19:
    #        label.draw()
    #    if player.time >= 19:
    #        label.x = window.width//2
    #        label.y = window.height//2
    #        label.draw()

    
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()



if __name__ == "__main__":
    main()
