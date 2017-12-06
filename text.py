#!usr/bin/env python
import pygame, glob, os
from   pygame.locals import *
from   constant      import *
from   utility       import *

class Text:
    def __init__(self, text='', size=FONTSIZE):
        ## Blittable text object
        path      = os.path.join(DIR_ROOT, DIR_FONT)
        filename  = path + '/font.ttf' #list(glob.glob(path + '/*.ttf'))[0]
        self.font = pygame.font.Font(filename, size)
        self.init_render(text)

    def init_render(self, text):
        ## Initialize default rendering constants
        self.antialias = False
        self.color     = BLACK
        self.text      = None
        self.render_new(text)

    def render_new(self, string, color=None):
        ## Render a new string
        if string != self.text:
            color = color if color else self.color
            self.text = string
            self.blittable = self.font.render(
                self.text,
                self.antialias,
                color,
                )

    def get_rect(self, **kwargs):
        return self.blittable.get_rect(**kwargs)

    def render(self, screen, pos, angle=0):
        ## Render self to screen at pos
        blits = pygame.transform.rotate(self.blittable, angle)
        screen.blit(blits, blits.get_rect(midtop=pos))
