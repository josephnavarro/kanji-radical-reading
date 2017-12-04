#!usr/bin/env python
import pygame, os, random
from   pygame.locals import *
from   utility       import *
from   constant      import *
from   button        import *
from   text          import *

## A single stage's question instance

def correct():
    ## A correct answer
    return True

def incorrect():
    ## An incorrect answer
    return False

class Question:
    def __init__(self, button_images, kanji_images, kana, other_kana, is_onyomi):
        self.images = kanji_images
        self.base   = kana['base']
        self.other  = kana['other']
        
        a = kana['order'][0]
        b = kana['order'][1]
        self.readings = kana[a], kana[b]
        self.buttons  = []

        c = [self.base, *other_kana]
        random.shuffle(c)

        for n in range(3):
            pos  = BUTTON_HORZ[n], BUTTON_VERT[n]
            text      = c[n]
            if text == self.base:
                fxn = correct
            else:
                fxn = incorrect
            btn1      = button_images[0]
            btn2      = button_images[1]
            newButton = Button(pos, 'test', btn1, btn2, fxn)
            self.buttons.append(newButton)

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

    
