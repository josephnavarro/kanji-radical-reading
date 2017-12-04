#!usr/bin/env python
import pygame, os
from   pygame.locals import *
from   constant      import *
from   utility       import *
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

        self.init_paths()
        self.init_images()
        self.init_data()

    def init_paths(self):
        ## Initializes file paths
        self.base_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_BASE)
        self.data_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_DEFINITION)
        self.image_dir = os.path.join(DIR_ROOT, DIR_IMG)
        self.base_dir  = os.path.join(DIR_ROOT, DIR_BASE)

    def init_images(self):
        ## Gets base strings for kanji
        bases = parse(self.base_file, lambda x:int(x))
        base_strings = []
        for k,v in bases.items():
            for n in range(v):
                base_strings.append('%s%d' %(k,v))

        self.words = {}
        for base in base_strings:
            words = get_words(self.image_dir, base)
            self.words.update(words)
            
        self.bases = {}
        for base in base_strings:
            base = get_bases(self.base_dir, base)
            self.bases.update(base)

    def init_data(self):
        ## Populates string-based data members
        definitions = parse(self.data_file)
        words       = [k for k in definitions]
        onyomi      = [lambda x:split(x,DASH) for x in words]

    def init_objects(self):
        ## Initialization of general utility objects
        base_full  = []
        base_part  = []
        base_roots = []
        
        for k,v in self.bases.items():
            full = v['full']
            part = v['none']
            base_full.append(full)
            base_part.append(part)
            base_roots.append(k)
        
        self.modes = {
            MODE_TITLE:   Title(),
            MODE_ONYOMI:  Stage(base_roots, base_full),
            MODE_RADICAL: Stage(base_roots, base_part),
            }

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
            
