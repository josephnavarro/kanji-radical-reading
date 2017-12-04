#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   constant      import *

class Stage:
    def __init__(self, words, bases):
        ## A single level
        self.problems = []
        

    def update_list(self, questions):
        ## Initializes randomized pool of questions
        self.questions = questions[:]  ## Copy list of strings
        random.shuffle(self.questions) ## Randomize order of sentences

    def update(self, tick, mouseClick):
        ## Generic update method called by Main.main()
        pass
