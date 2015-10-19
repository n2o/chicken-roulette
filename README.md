# chicken-roulette
Small adaption to the roulette from South Park - American Economics.

Sounds and video are adapted from the original South Park series. All credits belong to them.

## Description
This little game shows a video from [YouTube](https://www.youtube.com/watch?v=wz-PtEJEaqY). Pressing any key stops the
video and starts the game. The game shows a headless chicken running spawning and running randomly on the board.

Yes, you have to press any key. The awesome pyglet documentation does not describe how to stop a video and keep
the app running.

## Usage
The tool expects many command-line arguments:

1. rows: number of rows on the board
2. cols: number of columns on the board
3. names*: place any number of names / numbers, which should appear on the board

rows*cols must match the number of names.

Example:
```bash
$ python chickenrun.py 2 2 Alice Bob Charly Trudy
```

![Chicken](http://i.imgur.com/vpTEFDW.png)
