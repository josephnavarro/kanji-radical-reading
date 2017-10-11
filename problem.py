#!usr/bin/env python
import pygame
from   pygame.locals import *
from   constant      import *
from   button        import *

##　問題の画面（一問ずつインスタンス化使用するため）

class Problem:
    def __init__(self):
        ##　構築子
