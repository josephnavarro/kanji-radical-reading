#! /usr/bin/env python
import asyncio
import pygame, os
from   pygame.locals import *
from   constant      import *
from   utility       import *
from   stage         import *
from   button        import *
from   text          import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.mixer.pre_init(44100, -16, 2, 4096)
## Primary entrypoint for application

class Intermediate:
    def __init__(self):
        ## Intermediate state
        self.mode = MODE_INTERMEDIATE

    def get_mode(self):
        return MODE_TITLE

    def render(self, screen):
        pass

    def update(self, a, b, c):
        pass

class Wrapper:
    def __init__(self):
        ## Wrapper to handle finite state machine changes
        self.mode = MODE_TITLE
        self.init_images()

    def re_init(self):
        ## Re-initializes things when out of focus
        self.onyomi_button.isPressed = False
        self.radical_button.isPressed = False
        self.mode = MODE_TITLE

    def init_images(self):
        ## Initialize images for title screen
        self.background = load_image(os.path.join(DIR_ROOT, DIR_IMG, FILE_TITLE))
        self.button_img = [
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG1A)),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG1B)),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG2A)),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG2B)),
            ]     
        
        pos1 = MAIN_BUTTON_HORZ[0], MAIN_BUTTON_VERT[0]
        pos2 = MAIN_BUTTON_HORZ[1], MAIN_BUTTON_VERT[1]

        def toggle_onyomi():
            self.mode = MODE_ONYOMI

        def toggle_radical():
            self.mode = MODE_RADICAL

        text_blank = Text()

        self.onyomi_button  = Button(pos1, text_blank, self.button_img[0], self.button_img[1],  toggle_radical)
        self.radical_button = Button(pos2, text_blank, self.button_img[2], self.button_img[3], toggle_onyomi)

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
    def __init__(self, scale=SCALE):
        ## Constructor
        pygame.init()
        
        self.scale = scale
        self.size  = int(round(W*scale)), int(round(H*scale))

        pygame.display.set_caption(TITLE)           ## Set window caption
        pygame.mouse.set_visible(False)
        self.window = pygame.display.set_mode(self.size) ## Create window
        pygame.display.set_icon(load_image(ICONPATH))
        self.screen = pygame.Surface(SIZE)          ## Create blitting surface
        self.clock  = pygame.time.Clock()           ## FPS throttler
        self.mode   = MODE_TITLE                    ## Current game state

        self.init_paths()
        self.init_sound()
        self.init_data()
        self.init_objects()

    def init_paths(self):
        self.base_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_BASE)
        self.data_file = os.path.join(DIR_ROOT, DIR_DATA, FILE_DEFINITION)
        self.image_dir = os.path.join(DIR_ROOT, DIR_IMG)
        self.base_dir  = os.path.join(DIR_ROOT, DIR_BASE)
        self.kanji_dir = os.path.join(DIR_ROOT, DIR_KANJI)

    def init_sound(self):
        ## Initializes BGM, among other things
        self.click_sound = pygame.mixer.Sound(SFX1_PATH)
        self.click_sound.set_volume(0.2)
        pygame.mixer.music.load(BGM_PATH)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play()

    def init_mouse(self):
        ## Initializes mouse images
        self.mouse_img = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'cursor.png'))
        self.mouse_click_img = [
            load_image(os.path.join(DIR_ROOT, DIR_IMG, 'cursor-1.png')),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, 'cursor-2.png')),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, 'cursor-3.png')),
            load_image(os.path.join(DIR_ROOT, DIR_IMG, 'cursor-4.png')),
            ]
        self.mouse_counter = 0
        self.mouse_animating = False

    def init_data(self):
        ## Populates string-based data members
        self.init_mouse()
        
        definitions    = parse(self.data_file, lambda x:split(x,COMMA)[0])
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

        readings = parse(self.data_file, lambda x:[''.join(a.split()) for a in split(x,COMMA)[1].split(DASH)])
        for k,v in readings.items():
            v = v[0]
            s = split(k, DASH)
            newDict = {}
            if s[0] in base_strings:
                newDict['base']  = v[0]
                newDict['other'] = v[1]
                newDict['order'] = ['base','other']
            else:
                newDict['base']  = v[1]
                newDict['other'] = v[0]
                newDict['order'] = ['other','base']
            readings[k] = newDict

        self.readings = readings

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
                self.readings,
                is_onyomi=True
                ),
            MODE_RADICAL: Stage(
                base_keys,
                self.base_img,
                self.word_img,
                self.word_onyomi,
                self.word_defs,
                self.readings,
                is_onyomi=False
                ),
            MODE_INTERMEDIATE: Intermediate(),
            
            }

    def update(self, e, mouseClick, tick):
        ## Update method
        self.modes[self.mode].update(e, mouseClick, tick)
        self.mode = self.modes[self.mode].get_mode()

        if self.mode == MODE_INTERMEDIATE:
            self.modes[MODE_TITLE].re_init()
            self.modes[MODE_ONYOMI].re_init(True)
            self.modes[MODE_RADICAL].re_init(False)

    def render(self):
        ## Render whole screen
        self.modes[self.mode].render(self.screen)

        x,y = pygame.mouse.get_pos()
        sx,sy = get_scaling()
        pos = x*sx, y*sy

        if self.mouse_animating:
            click_img  = self.mouse_click_img[int(round(self.mouse_counter))]
            click_rect = click_img.get_rect(center=pos) 
            self.screen.blit(click_img, click_rect)
        
        rect = self.mouse_img.get_rect(midtop=pos)
        self.screen.blit(self.mouse_img, rect)
        pygame.transform.scale(self.screen, self.size, self.window) 
        #self.window.blit(self.screen, (0,0))
        pygame.display.flip()

    def main(self):
        ## Main game loop
        while True:
            tick = self.clock.tick(FPS) / 1000.0
            e    = pygame.event.get()
            
            for ev in e:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.click_sound.play()
                    self.mouse_animating = True
                elif ev.type == pygame.MOUSEBUTTONUP:
                    self.mouse_animating = False

            if self.mouse_animating:
                self.mouse_counter += tick * 16
                if int(round(self.mouse_counter)) >= 3:
                    self.mouse_animating = False
                    self.mouse_counter = 0
            
            mouseClick = get_input(e) ## Get mouse coords on click
            
            self.update(e, mouseClick, tick)
            #print(self.mode)
            self.render()

    async def asyncmain(self):
        ## Main game loop
        clock = self.clock
        click_sound = self.click_sound
        update = self.update
        render = self.render

        while True:
            tick = clock.tick(FPS) / 1000.0
            e    = pygame.event.get()
            
            for ev in e:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    self.mouse_animating = True
                elif ev.type == pygame.MOUSEBUTTONUP:
                    self.mouse_animating = False

            if self.mouse_animating:
                self.mouse_counter += tick * 16
                if int(round(self.mouse_counter)) >= 3:
                    self.mouse_animating = False
                    self.mouse_counter = 0
            
            mouseClick = get_input(e) ## Get mouse coords on click
            
            update(e, mouseClick, tick)
            #print(self.mode)
            render()
            await asyncio.sleep(0)


if __name__ == "__main__":
    main = Main(1)
    asyncio.run(main.asyncmain())
