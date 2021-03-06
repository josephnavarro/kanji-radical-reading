#!usr/bin/env python
import pygame
from   pygame.locals import *
from   random        import shuffle as shffl
from   math          import sin, cos, degrees
from   question      import *
from   utility       import *
from   text          import *
from   constant      import *

class Stage:
    def __init__(self, bkey, base_img, word_img, word_parts, word_defs, kana, is_onyomi):
        ## A single level
        self.init_images(is_onyomi)
        self.init_text()
        self.questions  = []
        
        tag   = KEY_NONE if is_onyomi else KEY_FULL
        wlist = list(word_parts.items())
        bkey  = list(base_img.keys())
        
        others = []
        for w in wlist:
            k = w[0]
            r = kana[k][KEY_OTHER]
            if r not in others:
                others.append(r)
                
        for w in wlist:
            k   = w[0]
            p   = word_parts[k]
            full_ims = []
            part_ims = []
            for q in p:
                if q in bkey:
                    full_ims.append(base_img[q][KEY_FULL])
                    part_ims.append(base_img[q][KEY_NONE])
                else:
                    full_ims.append(word_img[k])
                    part_ims.append(word_img[k])

            shffl(others)
            b = self.button_images[2:]
            if not is_onyomi:
                bimg = self.button_images[:2]
                
            new = Question(b, self.labels, full_ims, part_ims, kana[k], others[:2], word_defs[k], is_onyomi)
            self.questions.append(new)

        self.re_init(is_onyomi)

    def return_main(self):
        ## Signals to return to home screen
        self.mode = MODE_INTERMEDIATE

    def init_images(self, is_onyomi):
        ## Initializes images
        self.background = load_image(BGPATH1 if is_onyomi else BGPATH2)
        self.dagger     = load_image(DGPATH)
        self.temp_surf  = pygame.Surface(SMALL).convert_alpha()

        ## Loads button images
        b1 = load_image(BTNPATH1[0])
        b2 = load_image(BTNPATH1[1])
        b3 = load_image(BTNPATH2[0])
        b4 = load_image(BTNPATH2[1])
        
        self.button_images = [b1, b2, b3, b4]
        self.button_sizes  = [b1.get_size(), b3.get_size()]

        self.labels = apply_vector([
            load_image(KANPATH),
            load_image(KENPATH),
            load_image(SEIPATH),
            ], lambda x:sc(x,KANJISIZE))
        

    def init_text(self):
        ## Initializes text
        self.text      = Text(size=TEXT_LG)
        self.btn_text  = Text(size=TEXT_MD)
        self.back_text = Text(size=TEXT_SM)
        self.def_text  = Text(size=TEXT_DF)

    def re_init(self, is_onyomi):
        ## Re-initialization routine
        self.mode = MODE_ONYOMI if is_onyomi else MODE_RADICAL
        self.current = 0
        self.strikes = 0
        shffl(self.questions)
        self.is_onyomi = is_onyomi
        self.return_button = Button((32,H-128), "BACK", self.button_images[0], self.button_images[1], self.return_main, angle=-12)
        self.next_button = Button((240,H-100), "NEXT", self.button_images[0], self.button_images[1], self.next_question, angle=1)

        for q in self.questions:
            q.do_continue = False

    def get_mode(self):
        return self.mode
          
    def next_question(self):
        ## Go to the next question
        if self.questions[self.current].do_continue:
            self.questions[self.current].do_continue = False
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
            if self.is_onyomi:
                self.text.render_new(text)
                self.text.render(self.temp_surf, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))
            else:
                if self.questions[self.current].answer_at != n or self.questions[self.current].do_continue:
                    self.text.render_new(text)
                    self.text.render(self.temp_surf, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))
                elif self.questions[self.current].answer_at == n:
                    self.text.render_new('★',WHITE)
                    self.text.render(self.temp_surf, (KANJI_HORZ[n], KANJI_VERT[n] + OFFSET_Y))

        temp_img = smooth_rotate(self.temp_surf, -5)
        screen.blit(temp_img, (-5,-5))

        ## Render buttons on the side
        buttons = self.questions[self.current].get_button_text()
        pressed = self.questions[self.current].get_button_pressed()
        angles  = self.questions[self.current].get_button_angle()
        sizes   = self.questions[self.current].get_button_size()
        defs    = self.questions[self.current].get_definition()
        
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

        if self.questions[self.current].do_continue:
            self.next_button.render(screen)
            w1,h1 = self.back_text.blittable.get_size()
            w2,h2 = self.button_sizes[0]
            x,y = 0,0
            if self.next_button.isPressed:
                x,y = PRESS_X, PRESS_Y
            self.back_text.render_new(self.next_button.text, color=(255,0,0))
            self.back_text.render(screen, (
                self.next_button.x+w2//2-w1//4+x,
                self.next_button.y+h2//2-h1*2//3+y),
                                  angle = 1)

        for n in range(len(defs)):
            self.def_text.render_new(defs[n], color=BLACK)

            vsin = sin(DEF_ANGLE)
            vcos = cos(DEF_ANGLE)
            vy = n*(vsin*TEXT_DD + vcos*TEXT_DD)
            vx = n*(-vsin*TEXT_DD + vcos*TEXT_DD)
            
            self.def_text.render(screen, (240+vx,340+vy), angle=DEF_ANGLE)
        
    def update(self, e, mouseClick, tick):              
        ## Generic update method called by Main.main()
        self.questions[self.current].update(e, mouseClick)()
                
        self.return_button.update(e, mouseClick)()
        self.next_button.update(e, mouseClick)()
        

        
