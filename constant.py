#!usr/bin/env python
import os

## 定数集
## 他のファイルで使われている定数

TITLE = '漢字の部首で読もう'
SIZE  = W,H = 800,600  ## 外面サイズ
FPS   = 60             ## リフレッシュレート


## GUIの要素を画面に整えるための定数
BTNVERT = [480     for n in range(3)] ## 三つのボタンを縦に位置合わせする
BTNHORZ = [W/(3-n) for n in range(3)] ## 三つのボタンを横にいち合わせする


## 状態マシンのいろいろなステート
MODE_TITLE = 0  ## タイトル（アプリのはじめの画面）
MODE_STAGE = 1  ## ゲームモードを選ぶ所
MODE_GAME  = 2  ## ゲーム内の状態


## 上に書いてある「MODE_STAGE」の中では、別々のゲームモードの状態マシン
GKS_ONKR_BS1  = 0  ## 一つの部首がない漢字を一つ完成する(音読みあり)
GKS_ONKR_BS2  = 1  ## 一つの部首がない漢字を三つ完成する(それらの同じ音読みあり)
GON_KYOCH     = 2  ## 一つの漢字の音読みを選ぶ（中心した部首を強調する）
GON_TEIGI     = 3  ## 一つの漢字の音読みを選ぶ（定義あり）
GON_KUHAK     = 4  ## 一つの漢字の音読みを選ぶ（ほかにもない）
GON_TEIGI_JKG = 5  ## 熟語の音読みを選ぶ（定義あり）
GON_KUHAK_JKG = 6  ## 熟語の音読みを選ぶ（ほかにもない）
GON_BNMYK_JKG = 7  ## 熟語の音読みを選ぶ（文での使い方の文脈あり）


## 引用仕用の定数
DOWN_CLICK = 0  ## GUIのボタンを押すとの動く距離(px)


## フォルダーヒエラルキーの定数
DIR_ROOT = 'res'
DIR_FONT = 'font'
DIR_IMG  = 'img'
DIR_SND  = 'snd'
DIR_DATA = 'data'


## フォントについての定数
FONT_DIR = os.path.join(DIR_ROOT, DIR_FONT)
IMG_DIR  = os.path.join(DIR_ROOT, DIR_IMG)
SND_DIR  = os.path.join(DIR_ROOT, DIR_SND)
DATA_DIR = os.path.join(DIR_ROOT, DIR_DATA)


## 特別なファイルネームと拡張子の定数
F_EXT = '.lmao'  ## レベルや一般的なコンフィグレーションなどの拡張子
F_CFG = 'config' ## コンフィグレーションのファイルネーム

## パーサーの定数
COLON  = ':'
COMMA  = ','
IGNORE = '#'


## パーサーからの変数
VAR_FONT = 'font'
