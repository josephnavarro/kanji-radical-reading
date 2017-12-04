#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   utility       import *
from   constant      import *

class Stage:
    def __init__(self, base_keys, base_img, word_img, word_parts, word_defs, onyomi):
        ## A single level
        '''
        print("BASE IMG")
        print(base_img.keys())
        print("WORD_PARTS")
        print(word_parts.keys())
        print("WORD_IMG")'''
        tag = 'full' if not onyomi else 'none'
        
        words     = list(word_parts.items())
        base_keys = list(base_img.keys())
        for word in words:
            key = word[0]
            wordp = word_parts[key]
            for part in wordp:
                if part in base_keys:
                    print(base_img[part][tag])
                    
                else:
                    print(word_img[key])

    def render(self, screen):
        ## Renders self to screen
        
        pass
        
    def update(self, tick, mouseClick):
        ## Generic update method called by Main.main()
        pass
