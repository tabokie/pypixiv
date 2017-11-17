from __future__ import division

from OpenGL.GLUT import *
from OpenGL.GL import *

import numpy as np

from window import Window

# module author
# __author__ = 'gua'
# modified by
__author__ = 'tabokie'

class GlutWindow(object):
    def __init__(self, width, height, title):
        super(GlutWindow, self).__init__()
        self.width = width
        self.height = height
        self.title = title

        self.texture_id = 0
        self.vertices = None

        self.pixels = np.zeros(self.width * self.height, np.uint32)
        self.window = Window(self.pixels, self.width, self.height)

        self.setup()

    def mouse_event(self, button, state, x, y):
        self.window.mouse_event(button, state, x, y)

    def key_event(self, key, key_is_down, x, y):
    	# convert to anscii
        key = ord(key)
        self.window.key_event(key, key_is_down)

    def key_down(self, key, x, y):
        self.key_event(key, True, x, y)

    def key_up(self, key, x, y):
        self.key_event(key, False, x, y)

    def setup(self):
        self.setup_glut()
        self.setup_gl()

    def setup_glut(self):
        # glutInit(sys.argv)

        # initial glut window
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)

        # create window and register events
        glutCreateWindow(self.title)
        glutDisplayFunc(self.show)

        glutMouseFunc(self.mouse_event)

        glutKeyboardFunc(self.key_down)
        glutKeyboardUpFunc(self.key_up)
        # glutSetKeyRepeat(GLUT_KEY_REPEAT_ON)

    def setup_gl(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glClearColor(0, 0, 0, 1)# all white
        glViewport(0, 0, self.width, self.height)

        #new texture
        self.texture_id = glGenTextures(1)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        # nearest filter method for both zoom oprations
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.width, self.height,
                     0, GL_RGBA, GL_UNSIGNED_INT_8_8_8_8, self.pixels)

        self.vertices = [
            # (u, v), (x, y, z)
            (0, 0), (-1, -1, 0),
            (1, 0), (1, -1, 0),
            (1, 1), (1, 1, 0),
            (0, 1), (-1, 1, 0),
        ]

    def update(self, dt=100000):
        # clear
        self.clear()

        # update
        delta = dt / 1000.0
        self.window.update(delta)

        # draw
        self.window.draw()

        # show
        glutPostRedisplay()
        glutTimerFunc(dt, self.update, dt)

    def run(self):
        self.update()
        glutMainLoop()

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.window.clear()

    def show(self):
        # update texture and render
        # modify initial texture
        glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, self.width, self.height,
                        GL_RGBA, GL_UNSIGNED_INT_8_8_8_8, self.pixels)

        vertices = self.vertices
        # draw quadrangle
        glBegin(GL_QUADS)
        # load vertices
        for i in range(0, 4 * 2, 2):
        	# specify texture's local coordinates
            glTexCoord2f(*vertices[i])
            # and correponding global coordinates
            glVertex3f(*vertices[i+1])
        glEnd()

        glutSwapBuffers()