#!usr/bin/env python
import pygame, os
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

    def init_paths(self):
        ## Initializes file paths
        self.base_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_BASE)
        self.image_dir = os.path.join(DIR_ROOT, DIR_IMG)

    def init_objects(self):
        ## Initialization of general utility objects
        self.modes = {Level(), Stage(),}
        pass

    def init_images(self):
        ## Gets base strings for kanji
        bases = parse(self.base_file, convert_int)
        base_strings = []
        for k,v in bases.items():
            for n in range(v):
                base_strings.append('%s%d' %(k,v))

        words = []
        for base in base_strings:
            get_kanji(self.image_dir, base)
        self.base = get_kanji(BASE_DIR,

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
            tick = self.clock.tick(FPS) / 1000.0
            e = pygame.event.get()
            
            mouseClick = get_input(e) ## Get mouse coords on click
            
