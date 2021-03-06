#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   constant      import *
from   utility       import *

class Button:
    def __init__(self, pos, text, unpressed, pressed, function, image=None, angle=0):
        ## Pressable button in game GUI
        self.image     = image
        self.pressed   = pressed   ## Image upon press
        self.unpressed = unpressed ## Image while not pressed
        self.function  = function  ## Function to execute when clicked
        self.text      = text      ## Blittable text label
        self.x, self.y = pos       ## Topleft blitting pos
        self.angle = angle
        if self.image:
            self.image = smooth_rotate(self.image,     self.angle)
        self.pressed   = smooth_rotate(self.pressed,   self.angle)
        self.unpressed = smooth_rotate(self.unpressed, self.angle)
        

        ## Initialize local member variables
        self.init_constant()

    def get_size(self):
        ## Returns image size
        return self.pressed.get_size()

    def init_constant(self):
        ## Initialize local member variables
        self.rect         = self.unpressed.get_rect() ## Make bounding box
        self.rect.topleft = self.x, self.y            ## Move rect to topleft
        self.isPressed    = False                     ## Whether it's pressed

    def render(self, screen):
        ## Draw self to screen
        if self.isPressed:
            screen.blit(self.pressed, (self.x,self.y))
        else:
            screen.blit(self.unpressed, (self.x,self.y))

        if self.image:
            w1,h1 = self.pressed.get_size()
            if self.isPressed:
                screen.blit(self.image, (
                    self.x + w1//8 + PRESS_X,
                    self.y + h1//16 + PRESS_Y))
            else:
                screen.blit(self.image, (
                    self.x + w1//8,
                    self.y + h1//16))

    def on_release(self, mouseClick):
        ## Trigger on released downclick
        clicked = bool(self.rect.collidepoint(mouseClick))
        return self.isPressed and clicked

    def on_press(self, mouseClick):
        ## Trigger on downclick
        clicked = self.rect.collidepoint(mouseClick)
        self.isPressed = bool(clicked)

    def update(self, events, mouseClick):
        ## Called during main game loop
        for e in events:
            if e.type == MOUSEBUTTONDOWN:                
                self.on_press(mouseClick)
            elif e.type == MOUSEBUTTONUP:
                if self.on_release(mouseClick):
                    self.isPressed = False
                    return self.function
                else:
                    self.isPressed = False

        ## While not pressed, return null function
        return null_function
