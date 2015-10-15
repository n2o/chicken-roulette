import pyglet
import os

working_dir = os.path.dirname(os.path.realpath(__file__))
pyglet.resource.path = [os.path.join(working_dir,'resources')]
pyglet.resource.reindex()

# Load sprites
sprites = map(lambda s: pyglet.resource.image('headless/chicken' + str(s) + '.png'), range(1, 26))
#raw = pyglet.resource.image('chicken_spritesheet.png')
#raw_seq = pyglet.image.ImageGrid(raw, 5, 5)
chicken_sprite = pyglet.image.Animation.from_image_sequence(sprites, 0.1, True)

sprites_dead = [pyglet.resource.image('headless/chicken_dead.png')]
chicken_dead = pyglet.image.Animation.from_image_sequence(sprites_dead, 0.1, True)
