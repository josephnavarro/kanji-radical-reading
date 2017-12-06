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
    def __init__(self, button_images, radical_labels, kanji_images, kana, other_kana, definition, is_onyomi):
        self.images = kanji_images
        self.base  = kana['base']
        self.other = kana['other']
        definition = definition[0].strip()

        defs = definition.split(' ')
        output = []
        string = ''
        for d in defs:            
            string += d+' '
            if len(string) >= WORD_LONG:
                output.append(string)
                string = ''

        if len(string) != 0:
            output.append(string)

        self.definition = output[:]
        
        
        a = kana['order'][0]
        b = kana['order'][1]
        self.answer_at = kana['order'].index('base')
        radical_order = ['かん','けん','せい']
        self.readings = kana[a], kana[b]
        self.buttons  = []
        angles = [-ANGLE, ANGLE, -ANGLE]

        if not is_onyomi:
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
                newButton = Button(pos, text, btn1, btn2, fxn, None, angle=angles[n])
                self.buttons.append(newButton)

        else:
            for n in range(3):
                pos  = BUTTON_HORZ[n], BUTTON_VERT[n]
                if radical_order[n] == self.base:
                    fxn = correct
                else:
                    fxn = incorrect            
                btn1      = button_images[0]
                btn2      = button_images[1]
                newButton = Button(pos, '', btn1, btn2, fxn, radical_labels[n], angle=angles[n])
                self.buttons.append(newButton)

    def get_button_text(self):
        out_text = []
        for b in self.buttons:
            out_text.append(b.text)
        return out_text

    def get_definition(self):
        return self.definition

    def get_button_angle(self):
        out_angle = []
        for b in self.buttons:
            out_angle.append(b.angle)
        return out_angle

    def get_button_size(self):
        out_size = []
        for b in self.buttons:
            out_size.append(b.get_size())
        return out_size

    def get_button_pressed(self):
        return [b.isPressed for b in self.buttons]

    def render(self, screen):
        for n in range(len(self.images)):
            image = self.images[n]
            screen.blit(image, image.get_rect(center=(KANJI_HORZ[n], KANJI_VERT[n])))

    def render_buttons(self, screen):
        for b in self.buttons:
            b.render(screen)

    def update(self, e, mouseClick):
        fxn = incorrect
        
        for b in self.buttons:
            result = b.update(e, mouseClick)
            if result():
                fxn = correct

        return fxn

    
