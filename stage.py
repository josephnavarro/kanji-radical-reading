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
        self.questions  = []
        
        self.text     = Text(size=108)
        self.btn_text = Text(size=68)
        tag       = 'none' if is_onyomi else 'full'
        words     = list(word_parts.items())
        base_keys = list(base_img.keys())

        button_up     = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'button3a.png'))
        button_down   = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'button3b.png'))
        button_images = [button_up, button_down]
        self.button_size = button_up.get_size()

        others = []
        for word in words:
            r = readings[word[0]]['other']
            if r not in others:
                others.append(r)
                
        for word in words:
            key    = word[0]
            wordp  = word_parts[key]
            kanji_images = []
            for part in wordp:
                if part in base_keys:
                    kanji_images.append(base_img[part][tag])
                else:
                    kanji_images.append(word_img[key])

            kana = readings[key]

            random.shuffle(others)
            other_kana = others[:2]

            newQuestion = Question(button_images, kanji_images, kana, other_kana, is_onyomi)
            self.questions.append(newQuestion)

        self.current = 0
        random.shuffle(self.questions)

    def next_question(self):
        ## Go to the next question
        self.current += 1
        if self.current == len(self.questions):
            self.current = 0

    def render(self, screen):
        ## Renders self to screen
        screen.blit(self.background, (0,0))
        self.questions[self.current].render(screen)
        
        ## Render readings to screen
        for n in range(len(self.questions[self.current].readings)):
            self.text.render_new(self.questions[self.current].readings[n])
            self.text.render(screen, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))

        ## Render buttons on the side
        buttons = self.questions[self.current].get_button_text()
        pressed = self.questions[self.current].get_button_pressed()
        for n in range(len(buttons)):
            self.btn_text.render_new(buttons[n])
            w1,h1 = self.btn_text.blittable.get_size()
            w2,h2 = self.button_size
            x,y = 0,0
            if pressed[n]:
                x,y = PRESS_X, PRESS_Y
            self.btn_text.render(screen, (
                BUTTON_HORZ[n]+w1*3//4+x,
                BUTTON_VERT[n]+h1//8+y))
        
    def update(self, e, mouseClick, tick):
        ## Generic update method called by Main.main()
        if self.questions[self.current].update(e, mouseClick)():
            print("A")
            self.next_question()
        

        
