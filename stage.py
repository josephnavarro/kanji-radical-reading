#!usr/bin/env python
import pygame, random
from   pygame.locals import *
from   constant      import *

##　小テストみたいなレベルのクラス（問題とボタンの位置を含めている一般的な設計）

class Stage:
    def __init__(self, questions=[]):
        ##　構築子
        self.update_list(questions) ##　

    def update_list(self, sentences):
        ## Initializes randomized pool of questions
        self.questions = questions[:]  ## Copy list of strings
        random.shuffle(self.questions) ## Randomize order of sentences

    def update(self, tick, mouseClick):
        ## Generic update method called by Main.main()
        pass
