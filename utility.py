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
    ## ビットマップファイルを開けて戻す
    image = pygame.image.load(filename).convert_alpha()
    return image


def clean_line(string):
    ## パーサーのために不要な文字を消して戻す
    string = string.split(IGNORE)[0]
    string = ' '.join(string.split())
    return string
    

def extract_lines(_file):
    ## ファイル算体から空白でないラインを戻す
    lines  = _file.readlines()
    lines  = [l for l in lines if not l.startswith(IGNORE)]
    output = [clean_line(l) for l in lines]
    return output


def split(string, delim):
    ## 簡単に部分を分ける
    return string.split(delim)


def dictionary(_input, func=lambda x:x):
    ## _inputからのラインを「：」で分けて、dictを戻す
    return {k:func(v) for k,v in [split(l,COLON) for l in _input]}

    
def parse(filename):
    ## テキストファイルを開けて内容を読んで、その中に書いてあったデータを戻す
    with open(filename, "r") as f:
        return dictionary(extract_lines(f))
        
    return {}


