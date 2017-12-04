#!usr/bin/env python
import pygame, glob, os
from   pygame.locals import *
from   constant      import *
from   utility       import *

class Text:
    def __init__(self, text='', size=FONTSIZE):
        ## Blittable text object
        path      = os.path.join(DIR_ROOT, DIR_FONT)
        filename  = list(glob.glob(path + '/*.ttf'))[0]
        self.font = pygame.font.Font(filename, size)
        self.init_render(text)

    def init_render(self, text):
        ## Initialize default rendering constants
        self.antialias = True
        self.color     = BLACK
        self.text      = None
        self.render_new(text)

    def render_new(self, string):
        ## Render a new string
        if string != self.text:
            self.text = string
            self.blittable = self.font.render(
                self.text,
                self.antialias,
                self.color,
                )

    def get_rect(self, **kwargs):
        return self.blittable.get_rect(**kwargs)

    def render(self, screen, pos):
        ## Render self to screen at pos
        screen.blit(self.blittable, self.blittable.get_rect(midtop=pos))
