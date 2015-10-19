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
trigger_winner = False
STATE = "intro"
player = pyglet.media.Player()


def show_winner_screen():
    global STATE
    global player
    player.pause()
    time.sleep(1)
    player = pyglet.media.Player()
    sound = pyglet.media.load('bingbingbing.m4a', streaming=False)
    player.queue(sound) 
    player.play()
    STATE = "winner"
        

def video_finished():
    global STATE
    STATE = "lottery_init"

    
def main():
    if len(sys.argv) < 3:
        print("Usage: ./chickenrun.py rows cols")
        sys.exit(-1)

    # Read command line arguments
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    names = list()
    for name in sys.argv[3:]:
        names.append(name)

    if len(names) != rows*cols:
        print("Not enough names or too many cols / rows")
        sys.exit(-1)
        
    # General settings for the game
    window_width = 838
    window_height = 480
    window = pyglet.window.Window(width=window_width, height=window_height, fullscreen=False)
    board = Board(window_width, window_height, rows, cols, names)
    chicken = Chicken()

    def chickenrun_init():
        """ Place chicken and start dead-timer """
        chicken.x = randint(0, window_width-1)
        chicken.y = randint(0, window_height-1)
        Thread(target=chicken.die, args=()).start()     # Start thread to slow down the chicken
        pyglet.clock.schedule_interval(update, 1/120.0)

    def play_movie():
        """ Prepare video and start it """
        global player
        vidPath = "chickenrun.mp4"
        source = pyglet.media.StreamingSource()
        MediaLoad = pyglet.media.load(vidPath)
        player.queue(MediaLoad)
        player.eos_action = player.EOS_STOP
        player.on_player_eos = video_finished
        player.on_eos = video_finished
        time.sleep(1)
        player.play()
        
    def update(dt):
        """ Update chicken """
        global trigger_winner
        if not chicken.dead:
            chicken.update(dt)
        elif not trigger_winner:
            Thread(target=show_winner_screen, args=()).start()
            trigger_winner = True
    
    def winner_screen():
        """ Show winner screen """
        pyglet.sprite.Sprite(img=resources.busstop, x=0, y=0).draw()    # Print busstop image
        label = pyglet.text.Label("Winner is:",
                                  font_name='Helvetica',
                                  font_size=50,
                                  x=window_width//2, y=window_height-100,
                                  anchor_x='center', anchor_y='center')
        # Get winner tile
        tile = board.get_tile(chicken.x+chicken.image.get_max_width()//2, chicken.y+chicken.image.get_max_width()//2)
        if tile:
            # Sometimes it produces an error
            tile.label = None
            tile.draw(window_width//2 - tile.width//2, window_height//2 - tile.height//2)
        label.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        global player
        global STATE
        STATE = "lottery_init"
        player.pause()
        # Create a player and queue the song
        player = pyglet.media.Player()
        sound = pyglet.media.load('jingle_loop.m4a', streaming=False)
        player.queue(sound) 
        player.play()

    @window.event
    def on_draw():
        global STATE
        window.clear()
        #print(STATE)

        if STATE is "intro":
            play_movie()
            STATE = "intro_running"
            
        elif STATE is "intro_running":
            if player.source and player.source.video_format:
                player.get_texture().blit(0,0)
                
        elif STATE is "lottery_init":
            chickenrun_init()
            STATE = "lottery"
            
        elif STATE is "lottery":
            for tile in board.tiles:
                tile.draw()
            chicken.draw()
            
        elif STATE is "winner":
            winner_screen()
            chicken.draw()
            
        else:
            print("Invalid state")


if __name__ == "__main__":
    main()
    pyglet.app.run()
