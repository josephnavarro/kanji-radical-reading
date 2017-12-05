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
        self.init_images()
        self.init_text()
        self.questions  = []
        
        tag       = 'none' if is_onyomi else 'full'
        words     = list(word_parts.items())
        base_keys = list(base_img.keys())

        radical_labels = [
            load_image(KANPATH),
            load_image(KENPATH),
            load_image(SEIPATH),
            ]

        for x in range(len(radical_labels)):
            radical_labels[x] = pygame.transform.scale(radical_labels[x], (128,128))

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

    def init_images(self):
        ## Initializes images
        self.background = load_image(BGPATH)
        self.dagger     = load_image(DGPATH)
        self.temp_surf  = pygame.Surface(SMALL).convert_alpha()

        ## Loads button images
        b1 = load_image(BTNPATH1[0])
        b2 = load_image(BTNPATH1[1])
        b3 = load_image(BTNPATH2[0])
        b4 = load_image(BTNPATH2[1])
        
        self.button_images = [b1, b2, b3, b4]
        self.button_sizes  = [b1.get_size(), b3.get_size()]
        

    def init_text(self):
        ## Initializes text
        self.text      = Text(size=TEXT_LG)
        self.btn_text  = Text(size=TEXT_MD)
        self.back_text = Text(size=TEXT_SM)

    def re_init(self, is_onyomi):
        ## Re-initialization routine
        self.mode = MODE_ONYOMI if is_onyomi else MODE_RADICAL
        self.current = 0
        self.strikes = 0
        random.shuffle(self.questions)
        self.is_onyomi = is_onyomi
        self.return_button = Button((32,H-128), "BACK", *self.button_images[:2], self.return_main, angle=-12)

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
        self.temp_surf.fill((0,0,0,0))
        self.questions[self.current].render(self.temp_surf)
        self.questions[self.current].render_buttons(screen)
        
        ## Render readings to screen
        for n in range(len(self.questions[self.current].readings)):
            text = self.questions[self.current].readings[n]
            if self.is_onyomi or self.questions[self.current].answer_at != n:
                self.text.render_new(text)
                self.text.render(self.temp_surf, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))
            elif not self.is_onyomi and self.questions[self.current].answer_at == n:
                self.text.render_new('★',WHITE)
                self.text.render(self.temp_surf, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))

        temp_img = smooth_rotate(self.temp_surf, -5)
        screen.blit(temp_img, (-5,-5))

        ## Render buttons on the side
        buttons = self.questions[self.current].get_button_text()
        pressed = self.questions[self.current].get_button_pressed()
        angles  = self.questions[self.current].get_button_angle()
        sizes   = self.questions[self.current].get_button_size()
        
        for n in range(len(buttons)):
            self.btn_text.render_new(buttons[n], RED)
            w1,h1 = self.btn_text.blittable.get_size()
            w2,h2 = sizes[n]
            x,y = 0,0
            if pressed[n]:
                x,y = PRESS_X, PRESS_Y
            self.btn_text.render(screen, (
                BUTTON_HORZ[n] + w2//2 + x,
                BUTTON_VERT[n] + h2//2-h1*2//3 + y),
                                 angle = angles[n])

        self.return_button.render(screen)
        w1,h1 = self.back_text.blittable.get_size()
        w2,h2 = self.button_sizes[0]
        x,y = 0,0
        if self.return_button.isPressed:
            x,y = PRESS_X, PRESS_Y
        self.back_text.render_new(self.return_button.text, color=(255,0,0))
        self.back_text.render(screen, (
            self.return_button.x+w2//2-w1//4+x,
            self.return_button.y+h2//2-h1*2//3+y),
                              angle = -12)
        
    def update(self, e, mouseClick, tick):
        ## Generic update method called by Main.main()
        if self.questions[self.current].update(e, mouseClick)():
            self.next_question()
        self.return_button.update(e, mouseClick)()
        

        
