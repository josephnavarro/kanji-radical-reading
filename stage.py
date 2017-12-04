#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   utility       import *
from   constant      import *

class Stage:
    def __init__(self, base_keys, base_img, word_img, word_parts, word_defs):
        ## A single level
        '''
        print("BASE IMG")
        print(base_img.keys())
        print("WORD_PARTS")
        print(word_parts.keys())
        print("WORD_IMG")'''
        print(word_img)
        words = list(word_parts.items())
        return
        for word in words:
            print(word)
            print(word_defs[word[0]])
            print(word_parts[word[0]])

    def render(self, screen):
        ## Renders self to screen
        
        pass
        
    def update(self, tick, mouseClick):
        ## Generic update method called by Main.main()
        pass
