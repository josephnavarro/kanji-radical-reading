#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   utility       import *
from   text          import *
from   constant      import *

class Stage:
    def __init__(self, base_keys, base_img, word_img, word_parts, word_defs, readings, is_onyomi):
        ## A single level
        self.background = load_image(os.path.join(DIR_ROOT, DIR_IMG, GAME_BACKGROUND))
        self.questions = []
        tag = 'none' if is_onyomi else 'full'
        words     = list(word_parts.items())
        base_keys = list(base_img.keys())
        self.text = Text()
        
        for word in words:
            key    = word[0]
            wordp  = word_parts[key]
            images = []
            for part in wordp:
                if part in base_keys:
                    images.append(base_img[part][tag])
                else:
                    images.append(word_img[key])

            kana = readings[key]

            newQuestion = Question(images, kana, is_onyomi)
            self.questions.append(newQuestion)

        self.current = 0

    def render(self, screen):
        ## Renders self to screen
        screen.blit(self.background, (0,0))
        self.questions[self.current].render(screen)
        
        ## Render readings to screen
        for n in range(len(self.questions[self.current].readings)):
            self.text.render_new(self.questions[self.current].readings[n])
            self.text.render(screen, (W*n*3//8,H*2//3))
        
    def update(self, e, mouseClick, tick):
        ## Generic update method called by Main.main()
        pass
        
