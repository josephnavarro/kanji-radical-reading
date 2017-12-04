#!usr/bin/env python
import pygame,os
from   pygame.locals import *
from   utility       import *
from   constant      import *
from   button        import *
from   text          import *

## A single stage's question instance

class Question:
    def __init__(self, button_images, kanji_images, kana, is_onyomi):
        self.images = kanji_images
        self.base   = kana['base']
        self.other  = kana['other']
        b1, b2      = button_images
        
        a = kana['order'][0]
        b = kana['order'][1]
        self.readings = kana[a], kana[b]

        self.buttons = [Button((BUTTON_HORZ[n], BUTTON_VERT[n]),'test',b1,b2,null_function) for n in range(3)]

    def get_button_text(self):
        out_text = []
        for b in self.buttons:
            out_text.append(b.text)
        return out_text

    def get_button_pressed(self):
        return [b.isPressed for b in self.buttons]

    def render(self, screen):
        for n in range(len(self.images)):
            image = self.images[n]
            screen.blit(image, image.get_rect(center=(KANJI_HORZ[n], KANJI_VERT[n])))

        for b in self.buttons:
            b.render(screen)

    def update(self, e, mouseClick):
        for b in self.buttons:
            b.update(e, mouseClick)

    
