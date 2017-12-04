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
        self.init_objects()

    def init_paths(self):
        ## Initializes file paths
        self.base_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_BASE)
        self.data_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_DEFINITION)
        self.image_dir = os.path.join(DIR_ROOT, DIR_IMG)
        self.base_dir  = os.path.join(DIR_ROOT, DIR_BASE)
        self.kanji_dir  = os.path.join(DIR_ROOT, DIR_KANJI)

    def init_images(self):
        ## Gets base strings for kanji
        bases = parse(self.base_file, lambda x:int(x))
        base_strings = []
        for k,v in bases.items():
            for n in range(v[0]):
                base_strings.append('%s%d' %(k,(n+1)))
                
        self.word_img = {}
        for base in base_strings:
            words = get_words(self.kanji_dir, base)
            self.word_img.update(words)
            
        self.base_img = {}
        for base in base_strings:
            base_dict = get_bases(self.base_dir, base)
            self.base_img.update({base:base_dict})

    def init_data(self):
        ## Populates string-based data members
        definitions = parse(self.data_file)
        words       = [k for k in definitions]
        onyomi      = [split(x,DASH) for x in words]

        self.word_onyomi = {words[n]:onyomi[n] for n in range(len(words))}
        self.word_defs  = definitions

    def init_objects(self):
        ## Initialization of general utility objects
        base_keys = []
        
        for k,v in self.base_img.items():
            base_keys.append(k)

        self.modes = {
            MODE_TITLE:   None,
            MODE_ONYOMI:  Stage(
                base_keys,
                self.base_img,
                self.word_img,
                self.word_onyomi,
                self.word_defs,
                ),
            MODE_RADICAL: Stage(
                base_keys,
                self.base_img,
                self.word_img,
                self.word_onyomi,
                self.word_defs,
                ),
            }

    def main(self):
        ## Main game loop
        while True:
            tick = self.clock.tick(FPS) / 1000.0
            e = pygame.event.get()
            
            mouseClick = get_input(e) ## Get mouse coords on click
            

main = Main()
