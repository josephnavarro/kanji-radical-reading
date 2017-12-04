#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   utility       import *
from   constant      import *

class Stage:
    def __init__(self, base_keys, word_imgs, word_parts, word_defs):
        ## A single level
        #print(word_parts.items())
        #print(word_defs.items())
        pass

    def render(self, screen):
        ## Renders self to screen
        
        pass
        
    def update(self, tick, mouseClick):
        ## Generic update method called by Main.main()
        pass
