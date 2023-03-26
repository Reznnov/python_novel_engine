import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))

from pyglet.window import Window
from pyglet import app, shapes
import pyglet
from util.constant import *


window = Window(fullscreen=True)
window.set_location(2250, 150)

# Image
Eli_image = pyglet.image.load('../assets/character.png')

Eli_image.anchor_x = Eli_image.width // 4
Eli_image.anchor_y = Eli_image.height - 600
print(Eli_image.width, Eli_image.height)
@window.event
def on_draw():
    window.clear();
    Eli_image.blit(center_x, center_y);

app.run()

























