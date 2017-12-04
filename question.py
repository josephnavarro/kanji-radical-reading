#!usr/bin/env python
import pygame
from   pygame.locals import *
from   constant      import *
from   button        import *
from   text          import *

## A single stage's question instance

class Question:
    def __init__(self, word, base, answer):
        self.word = word
