#!usr/bin/env python
import pygame
from   pygame.locals import *
from   utility       import *
from   constant      import *
from   button        import *
from   text          import *

## A single stage's question instance

class Question:
    def __init__(self, images, kana, is_onyomi):
        self.images = images
        self.base   = kana['base']
        self.other  = kana['other']
        
        a = kana['order'][0]
        b = kana['order'][1]
        self.readings = kana[a], kana[b]

    def render(self, screen):
        for n in range(len(self.images)):
            image = self.images[n]
            screen.blit(image, image.get_rect(center=( KANJI_HORZ[n], KANJI_VERT[n])))

    
