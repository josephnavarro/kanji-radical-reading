#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   constant      import *

class Stage:
    def __init__(self, root_imgs, word_imgs):
        ## A single level
        self.questions = []
        
    def update(self, tick, mouseClick):
        ## Generic update method called by Main.main()
        pass
