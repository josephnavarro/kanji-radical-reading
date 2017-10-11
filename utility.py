#!usr/bin/env python
import pygame
from   pygame.locals import *

## どこでも使われている関数

def _quit():
    ## ゲームを閉める
    pygame.quit()
    raise SystemExit


def get_input(events):
    ## ゲーム中でマウスとキーボードの入力を使う
    for e in events:
        if e.type == QUIT:
            ## 右上のボタンを押てウィンドウを消したい場合
            _quit()

        elif e.type == KEYDOWN:
            ## キーボードで入力した場合
            if e.key == K_ESCAPE:
                ## キーでゲームを閉める場合
                _quit()
        
        elif e.type == MOUSEBUTTONDOWN:
            ## クリックしたマウスの位置を戻す
            return pygame.mouse.get_pos()

    ## ディフォルトに戻すもの
    return (-1,-1)


def null_function():
    ## 何も書いていないので、おかしそうですが、実はこれは大切な関数である
    pass


def load_image(filename):
    ## Loads a bitmap image
    image = pygame.image.load(filename).convert_alpha()
    return image
