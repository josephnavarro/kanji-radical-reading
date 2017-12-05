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
        self.back_text = Text(size=48)
        tag       = 'none' if is_onyomi else 'full'
        words     = list(word_parts.items())
        base_keys = list(base_img.keys())

        button_up1     = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'button3a.png'))
        button_down1   = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'button3b.png'))
        button_up2     = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'button4a.png'))
        button_down2   = load_image(os.path.join(DIR_ROOT, DIR_IMG, 'button4b.png'))
        
        self.button_images = [button_up1, button_down1, button_up2, button_down2]
        self.button_sizes  = [button_up1.get_size(), button_up2.get_size()]

        kan_img = load_image(os.path.join(DIR_ROOT, DIR_RADICAL, 'kan.png'))
        ken_img = load_image(os.path.join(DIR_ROOT, DIR_RADICAL, 'ken.png'))
        sei_img = load_image(os.path.join(DIR_ROOT, DIR_RADICAL, 'sei.png'))

        radical_labels = [kan_img, ken_img, sei_img]

        for x in range(len(radical_labels)):
            radical_labels[x] = pygame.transform.smoothscale(radical_labels[x], (128,128))

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

            if not is_onyomi:
                bimg = self.button_images[:2]
            else:
                bimg = self.button_images[2:]

            newQuestion = Question(bimg, radical_labels, kanji_images, kana, other_kana, is_onyomi)
            self.questions.append(newQuestion)

        self.re_init(is_onyomi)

    def return_main(self):
        ## Signals to return to home screen
        self.mode = MODE_INTERMEDIATE

    def re_init(self, is_onyomi):
        ## Re-initialization routine
        self.mode = MODE_ONYOMI if is_onyomi else MODE_RADICAL
        self.current = 0
        random.shuffle(self.questions)
        self.is_onyomi = is_onyomi
        self.return_button = Button((32,H-128), "Back", *self.button_images[:2], self.return_main)

    def get_mode(self):
        return self.mode
    
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
            text = self.questions[self.current].readings[n]
            if self.is_onyomi or self.questions[self.current].answer_at != n:
                self.text.render_new(text)
                self.text.render(screen, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))
            elif not self.is_onyomi and self.questions[self.current].answer_at == n:
                self.text.render_new('★',RED)
                self.text.render(screen, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))

        ## Render buttons on the side
        buttons = self.questions[self.current].get_button_text()
        pressed = self.questions[self.current].get_button_pressed()
        for n in range(len(buttons)):
            self.btn_text.render_new(buttons[n], RED)
            w1,h1 = self.btn_text.blittable.get_size()
            w2,h2 = self.button_sizes[1 if self.is_onyomi else 0]
            x,y = 0,0
            if pressed[n]:
                x,y = PRESS_X, PRESS_Y
            self.btn_text.render(screen, (
                BUTTON_HORZ[n] + w2//2 + x,
                BUTTON_VERT[n] + h2//2-h1*2//3 + y))

        self.return_button.render(screen)
        self.back_text.render_new(self.return_button.text)
        w1,h1 = self.back_text.blittable.get_size()
        w2,h2 = self.button_sizes[0]
        x,y = 0,0
        if self.return_button.isPressed:
            x,y = PRESS_X, PRESS_Y
        self.back_text.render(screen, (
            self.return_button.x+w2//2-w1//4+x,
            self.return_button.y+h2//2-h1*2//3+y))
        
    def update(self, e, mouseClick, tick):
        ## Generic update method called by Main.main()
        if self.questions[self.current].update(e, mouseClick)():
            self.next_question()
        self.return_button.update(e, mouseClick)()
        

        
