#!usr/bin/env python
import os

## Constants
## Constant values used in other files

TITLE = "Reading Kanji with Radicals" ## Window caption
SIZE  = W,H = 800,600      ## Screen size
FPS   = 60                 ## Screen refresh rate
FONTSIZE = 108
BLACK = (0,0,0)

## GUI button placement
KANJI_VERT = [H//3 for n in range(2)]
KANJI_HORZ = [W*2//10, W*5//10]
BUTTON_HORZ = [W*6//10 for n in range(3)] ## Button y-coordinates
BUTTON_VERT = [H*(n+1)//4 for n in range(3)] ## Button x-coordinates

## Finite state machine game modes
MODE_TITLE = 'title'   ## Game title screen
MODE_STAGE = 'select'  ## Game stage selection

## Different types of game modes
MODE_ONYOMI  = 'onyomi'  ## On'yomi given (choose radical)
MODE_RADICAL = 'radical' ## Radical given (choose on'yomi)

## Vertical pixel offset when a button is pressed
OFFSET_Y = 96
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

## Files
FILE_BASE       = 'base.config'
FILE_DEFINITION = 'definition.config'
FILE_TITLE      = 'title.png'
BUTTON_IMG1A    = 'button1a.png'
BUTTON_IMG1B    = 'button1b.png'
BUTTON_IMG2A    = 'button2a.png'
BUTTON_IMG2B    = 'button2b.png'
GAME_BACKGROUND = 'game.png'

## Parser delimiters
DASH  = '-'
FILE  = '.'
SPACE = '_'
COLON = ':'
COMMA = ','
