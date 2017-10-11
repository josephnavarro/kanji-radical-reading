#!usr/bin/env python
import pygame
from   pygame.locals import *
from   constant      import *
from   utility       import *

## 押されることができるボタン

class Button:
    def __init__(self, pos, label, pressed, unpressed, function):
        ## 構築子
        self.label     = label     ## ビットマップに変えたテキスト
        self.pressed   = pressed   ## ボタンを押すとのイメージ
        self.unpressed = unpressed ## ボタンが押されていないイメージ
        self.function  = function  ## クリックするとの関数
        self.x, self.y = pos       ## 画面の座標的な位置

        ##　上の定数からできているほかの定数を設定する
        self.init_constant()

    def init_constant(self):
        ##　構築子で設定された定数からできているほかの定数
        self.rect         = self.pressed.get_rect() ## ボタンを押すための区域
        self.rect.topleft = self.x, self.y          ## 区域の座標的な位置
        self.isPressed    = False                   ## 今クリックされている？

        ##　テキストのレーベルをボタンの中で真ん中に位置づける
        self.xOffset = self.rect.width/2  - self.label.width/2
        self.yOffset = self.rect.height/2 - self.label.height/2

    def render(self, screen):
        ##　グラフィックを画面に全部描く
        if self.isPressed:
            screen.blit(self.pressed,   (self.x, self.y + DEPRESS))
            screen.blit(self.label,     (self.x + self.xOffset,
                                         self.y + self.yOffset + DEPRESS))
        else:
            screen.blit(self.unpressed, (self.x, self.y))
            screen.blit(self.label,     (self.x + self.xOffset,
                                         self.y + self.yOffset))

    def on_release(self, mouseClick):
        ##　マウスボタンを放した場合の実行する関数（「self.update」の関数へ戻り）
        clicked = self.rect.collidepoint(mouseClick)
        return self.isPressed and clicked

    def on_press(self, mouseClick):
        ##　本ボタンの押している変数を「True」にセットする
        clicked = self.rect.collidepoint(mouseClick)
        self.isPressed = clicked

    def update(self, events, mouseClick):
        ##　メーン関数からのイベントとマウスの座標を処理する
        for e in events:
            if e.type == MOUSEBUTTONDOWN:                
                self.on_press(mouseClick)
            elif e.type == MOUSEBUTTONUP:
                if on_release(mouseClick):
                    ##　メーン関数に戻り値用の本クラスの関数を与える
                    return self.function

        ##　入力がない場合は、「utility」からの空白関数を与える
        return null_function
