#!usr/bin/env python
import os

## Constants
## Constant values used in other files

TITLE = "漢字の部首で読もう" ## Window caption
SIZE  = W,H = 800,600      ## Screen size
FPS   = 60                 ## Screen refresh rate


## GUI button placement
BTNVERT = [480     for n in range(3)] ## Button y-coordinates
BTNHORZ = [W/(3-n) for n in range(3)] ## Button x-coordinates


## Finite state machine game modes
MODE_TITLE = 'title'   ## Game title screen
MODE_STAGE = 'select'  ## Game stage selection
MODE_GAME  = 'game'    ## In-game level


## Different types of game modes
MODE_ONYOMI  = 'onyomi'  ## On'yomi given (choose radical)
MODE_RADICAL = 'radical' ## Radical given (choose on'yomi)


## Vertical pixel offset when a button is pressed
DEPRESS = 0


## Folder hierarchy
DIR_ROOT  = 'res'
DIR_FONT  = 'font'
DIR_IMG   = 'img'
DIR_KANJI = 'kanji'
DIR_SND   = 'snd'
DIR_DATA  = 'data'


## Directory listings
FONT_DIR  = os.path.join(DIR_ROOT, DIR_FONT)
IMG_DIR   = os.path.join(DIR_ROOT, DIR_IMG)
SND_DIR   = os.path.join(DIR_ROOT, DIR_SND)
DATA_DIR  = os.path.join(DIR_ROOT, DIR_DATA)
KANJI_DIR = os.path.join(DIR_ROOT, DIR_KANJI)


## Recognized file extensions
DATA_FILETYPE = 'config'  ## Level definition

## Parser delimiters
DASH  = '-'
FILE  = '.'
SPACE = '_'
