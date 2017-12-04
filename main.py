#!usr/bin/env python
import pygame, os
from   pygame.locals import *
from   constant      import *
from   utility       import *
from   stage         import *
from   button        import *

## Primary entrypoint for application

class Wrapper:
    def __init__(self):
        ## Wrapper to handle finite state machine changes
        self.mode = MODE_TITLE
        self.init_images()

    def init_images(self):
        ## Initialize images for title screen
        self.background = load_image(os.path.join(DIR_ROOT, DIR_IMG, FILE_TITLE))
        self.button_img = [
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG1A)),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG1B)),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG2A)),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG2B)),
            ]
        
        
            
        pos1 = W//16,   H//2
        pos2 = W*8//16, H//2

        def toggle_onyomi():
            self.mode = MODE_ONYOMI

        def toggle_radical():
            self.mode = MODE_RADICAL

        self.onyomi_button  = Button(pos1, *self.button_img[:2],  toggle_onyomi)
        self.radical_button = Button(pos2, *self.button_img[2:4], toggle_radical)

    def render(self, screen):
        ## Render buttons
        screen.blit(self.background,(0,0))
        self.onyomi_button.render(screen)
        self.radical_button.render(screen)

    def get_mode(self):
        ## Gets returned mode
        return self.mode

    def update(self, e, mouseClick, tick):
        ## Update all buttons
        function1 = self.onyomi_button.update(e,  mouseClick)
        function2 = self.radical_button.update(e, mouseClick)
        function1()
        function2()

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
        self.init_data()
        self.init_objects()

    def init_paths(self):
        self.base_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_BASE)
        self.data_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_DEFINITION)
        self.image_dir = os.path.join(DIR_ROOT, DIR_IMG)
        self.base_dir  = os.path.join(DIR_ROOT, DIR_BASE)
        self.kanji_dir = os.path.join(DIR_ROOT, DIR_KANJI)

    def init_data(self):
        ## Populates string-based data members
        
        definitions = parse(self.data_file)
        words       = [k for k in definitions]
        onyomi      = [split(x,DASH) for x in words]

        self.word_onyomi = {words[n]:onyomi[n] for n in range(len(words))}
        self.word_defs   = definitions

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

    def init_objects(self):
        ## Initialization of general utility objects
        base_keys = []
        
        for k,v in self.base_img.items():
            base_keys.append(k)

        self.modes = {
            MODE_TITLE:   Wrapper(),
            MODE_ONYOMI:  Stage(
                base_keys,
                self.base_img,
                self.word_img,
                self.word_onyomi,
                self.word_defs,
                is_onyomi=True
                ),
            MODE_RADICAL: Stage(
                base_keys,
                self.base_img,
                self.word_img,
                self.word_onyomi,
                self.word_defs,
                is_onyomi=False
                ),
            }

    def update(self, e, mouseClick, tick):
        ## Update method
        self.modes[self.mode].update(e, mouseClick, tick)
        self.mode = self.modes[MODE_TITLE].get_mode()

    def render(self):
        ## Render whole screen
        self.window.blit(self.screen, (0,0))
        self.modes[self.mode].render(self.screen)
        pygame.display.flip()

    def main(self):
        ## Main game loop
        while True:
            tick = self.clock.tick(FPS) / 1000.0
            e    = pygame.event.get()
            
            mouseClick = get_input(e) ## Get mouse coords on click
            self.update(e, mouseClick, tick)            
            self.render()
            

main = Main()
main.main()
