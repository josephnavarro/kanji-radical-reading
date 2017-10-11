#!usr/bin/env python
import pygame
from   pygame.locals import *
from   constant      import *
from   utility       import *
from   level         import *
from   stage         import *

## Primary entrypoint for application

class Main:
    def __init__(self):
        ## Constructor
        pygame.init()

        pygame.display.set_caption(TITLE)           ## Set window caption
        self.window = pygame.display.set_mode(SIZE) ## Create window
        self.screen = pygame.Surface(SIZE)          ## Create blitting surface
        self.clock  = pygame.time.Clock()           ## FPS throttler
        self.mode   = MODE_TITLE                    ## Current game state

    def init_objects(self):
        ## Initialization of general utility objects
        self.modes = {Level(), Stage(),}
        pass

    def run_title(self):
        ## Entry into title screen loop
        pass

    def run_stage_select(self):
        ## Entry into stage selection loop
        pass

    def run_diff_select(self):
        ## Entry into difficulty selection loop
        pass

    def main(self):
        ## Main game loop
        while True:
            tick = self.clock.tick(FPS) / 1000.0 ## Time increment
            e = pygame.event.get() ## Poll for user input
            
            mouseClick = get_input(e) ## Get mouse coords on click
            
