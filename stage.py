#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   question      import *
from   utility       import *
from   constant      import *

class Stage:
    def __init__(self, base_keys, base_img, word_img, word_parts, word_defs, pronunciations, is_onyomi):
        ## A single level
        self.background = load_image(os.path.join(DIR_ROOT, DIR_IMG, GAME_BACKGROUND))
        self.questions = []
        tag = 'none' if is_onyomi else 'full'
        words     = list(word_parts.items())
        base_keys = list(base_img.keys())
        
        for word in words:
            key    = word[0]
            wordp  = word_parts[key]
            images = []
            for part in wordp:
                if part in base_keys:
                    images.append(base_img[part][tag])
                else:
                    images.append(word_img[key])

            self.questions.append(Question(images, is_onyomi))

        self.current = 0

    def render(self, screen):
        ## Renders self to screen
        screen.blit(self.background, (0,0))
        self.questions[self.current].render(screen)
        
    def update(self, e, mouseClick, tick):
        ## Generic update method called by Main.main()
        pass
