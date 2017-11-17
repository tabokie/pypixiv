# import random
import sys

from canvas import Canvas
from scene import Scene
#from vector import Vector
#from vertex import Vertex
#from color import Color

# module author
# __author__ = 'gua'
# modified by
__author__ = 'tabokie'

class Window(object):
    def __init__(self, pixels, width, height):
        self.pixels = pixels
        self.width = width
        self.height = height

        self.canvas = Canvas(width, height, pixels)

        # fetch default scene
        self.scene=Scene(0)
        # setup key handlers
        key_esc = 27
        self.handlers = {
            key_esc: self.exit
            # key_up
            # key_zoom
        }

    def clear(self):
        self.canvas.clear()
        pass

    def update(self, dt):
        pass

    def draw(self):
        self.canvas.draw_scene(self.scene)

    def mouse_event(self, button, state, x, y):
        print('mouse event', button, state, x, y)
        # 0, left button
        # 2, right button
        # 0, state press
        # 1, state release
    def key_event(self, key, key_is_down):
        print('key event', key, key_is_down)
        # fetch command
        cmd = self.handlers.get(key, self.cmd404)
        cmd()

    def exit(self):
        sys.exit(0)

    def cmd404(self):
        pass

    