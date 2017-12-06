#!usr/bin/env python
import os

## Constants
## Constant values used in other files

TITLE     = "Kanji by Radical" ## Window caption
SIZE      = W,H = 800,600              ## Screen size
SMALL     = W*2//3, H*2//3             ## Small screen
FPS       = 60                         ## Screen refresh rate
FONTSIZE  = 108
BLACK     = (0,0,0)
RED       = (255,0,0)
WHITE     = (255,255,255)
ANGLE     = 3.75
SCALE     = 1.5
MINISCALE = 0.8
KANJISIZE = 128,128
WORD_LONG = 8

## Font sizes
TEXT_LG = 90
TEXT_MD = 40
TEXT_DF = 40
TEXT_DD = 35
TEXT_SM = 36
DEF_ANGLE = -6

## GUI button placement
KANJI_VERT       = [H//4 for n in range(2)]
KANJI_HORZ       = [32+W*3//18, 32+W*8//18]
MAIN_BUTTON_HORZ = [64, W//2 + 64]
MAIN_BUTTON_VERT = [H//2 + 64 for n in range(2)]
BUTTON_HORZ      = [480 for n in range(3)]      ## Button y-coordinates
BUTTON_VERT      = [32 + 176 * n for n in range(3)] ## Button x-coordinates

## Finite state machine game modes
MODE_TITLE        = 'title'        ## Game title screen
MODE_STAGE        = 'select'       ## Game stage selection
MODE_INTERMEDIATE = 'intermediate'

## Different types of game modes
MODE_ONYOMI  = 'onyomi'  ## On'yomi given (choose radical)
MODE_RADICAL = 'radical' ## Radical given (choose on'yomi)

## Vertical pixel offset when a button is pressed
OFFSET_Y = 120
PRESS_X  = 8
PRESS_Y  = 8

## Folder hierarchy
DIR_ROOT    = 'res'
DIR_FONT    = 'font'
DIR_IMG     = 'img'
DIR_KANJI   = 'kanji'
DIR_RADICAL = 'radical'
DIR_BASE    = 'base'
DIR_DATA    = 'data'
DIR_SOUND   = 'snd'

## Files
FILE_BASE       = 'base.config'
FILE_DEFINITION = 'definition.config'
FILE_TITLE      = 'title.png'
BUTTON_IMG1A    = 'button1a.png'
BUTTON_IMG1B    = 'button1b.png'
BUTTON_IMG2A    = 'button2a.png'
BUTTON_IMG2B    = 'button2b.png'
BUTTON_IMG3A    = 'button3a.png'
BUTTON_IMG3B    = 'button3b.png'
BUTTON_IMG4A    = 'button4a.png'
BUTTON_IMG4B    = 'button4b.png'
DAGGER_IMG      = 'dagger.png'
CHAR_KAN        = 'kan.png'
CHAR_KEN        = 'ken.png'
CHAR_SEI        = 'sei.png'
GAME_BACKGROUND1 = 'game1.png'
GAME_BACKGROUND2 = 'game2.png'
ICONFILE         = 'icon.png'
BGM_FILE         = 'bgm.ogg'

## Parser delimiters
DASH    = '-'
FILE    = '.'
SPACE   = '_'
COLON   = ':'
COMMA   = ','
PNGWILD = '/*.png'

## Image paths
BGPATH1  = os.path.join(DIR_ROOT, DIR_IMG,   GAME_BACKGROUND1)
BGPATH2  = os.path.join(DIR_ROOT, DIR_IMG,   GAME_BACKGROUND2)
BGM_PATH = os.path.join(DIR_ROOT, DIR_SOUND, BGM_FILE)
ICONPATH = os.path.join(DIR_ROOT, DIR_IMG,   ICONFILE)
DGPATH   = os.path.join(DIR_ROOT, DIR_IMG,   DAGGER_IMG)
BTNPATH1 = [
    os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG3A),
    os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG3B),
    ]
BTNPATH2 = [
    os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG4A),
    os.path.join(DIR_ROOT, DIR_IMG, BUTTON_IMG4B),
    ]

KANPATH = os.path.join(DIR_ROOT, DIR_RADICAL, CHAR_KAN)
KENPATH = os.path.join(DIR_ROOT, DIR_RADICAL, CHAR_KEN)
SEIPATH = os.path.join(DIR_ROOT, DIR_RADICAL, CHAR_SEI)

## Dagger animation constants
START_POS = [
    
    ]

## Dictionary keys
KEY_NONE  = 'none'
KEY_FULL  = 'full'
KEY_OTHER = 'other'
