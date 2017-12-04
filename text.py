#!usr/bin/env python
import pygame, glob, os
from   pygame.locals import *
from   constant      import *
from   utility       import *

class Text:
    def __init__(self):
        ## Blittable text object
        path      = os.path.join(DIR_ROOT, DIR_FONT)
        filename  = list(glob.glob(path + '/*.ttf'))[0]
        self.font = pygame.font.Font(filename, FONTSIZE)
        self.init_render()

    def init_render(self):
        ## Initialize default rendering constants
        self.antialias = True
        self.color     = BLACK
        self.text      = ''
        self.render_new('')

    def render_new(self,string):
        ## Render a new string
        self.blittable = self.font.render(
            self.text,
            self.antialias,
            self.color,
            )

    def render(self, screen):
        pass
