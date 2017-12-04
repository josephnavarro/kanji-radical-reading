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

## Different types of game modes
MODE_ONYOMI  = 'onyomi'  ## On'yomi given (choose radical)
MODE_RADICAL = 'radical' ## Radical given (choose on'yomi)

## Vertical pixel offset when a button is pressed
DEPRESS = 0

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

## Parser delimiters
DASH  = '-'
FILE  = '.'
SPACE = '_'
COLON = ':'
