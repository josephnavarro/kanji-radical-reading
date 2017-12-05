#!usr/bin/env python
import pygame, glob, os
from   pygame.locals    import *
from   pygame.transform import scale  as sc
from   pygame.transform import rotate as rot
from   constant         import *

## Functions used universally

def _quit():
    ## Safely quit game
    pygame.quit()
    raise SystemExit

def apply_vector(vector, *fxns):
    ## Applies a function over all elements
    for fxn in fxns:
        vector = [fxn(v) for v in vector[:]]

    return vector

def smooth_rotate(img, angle, scale=MINISCALE):
    ## Rotates and scales
    size = apply_vector(img.get_size(), lambda x:x*scale, round, int)
    img  = sc(img, size)
    img  = rot(img, angle)
    return img

def get_words(path, b, ext=PNGWILD):
    ## Get kanji from images and pair them with strings
    _dict = {}
    for fn in glob.glob(path + ext):
        if b in fn:
            im = load_image(fn)
            on = filename.replace('\\','/').split(SPACE)[0].split('/')[-1]
            _dict[on] = im

    return _dict

def get_bases(path, b, ext=PNGWILD):
    ## Get kanji from images and pair them with strings
    _dict = {}
    full  = None
    none  = None
    for fn in glob.glob(path + ext):
        if b in fn:
            if KEY_NONE in fn:
                none = load_image(fn)
            else:
                full = load_image(fn)

    return {KEY_NONE:none, KEY_FULL:full}

def get_scaling():
    ## Gets ratio between window size and interal screen
    w1, h1 = pygame.display.get_surface().get_size()
    return W/w1, H/h1

def get_input(events):
    ## Get mouse input
    x,y = -1,-1
    for e in events:
        if e.type == QUIT:
            ## Click [x] to exit window
            _quit()

        elif e.type == KEYDOWN:
            ## Keypress processing
            if e.key == K_ESCAPE:
                ## Press ESC to exit window
                _quit()
        
        elif e.type == MOUSEBUTTONDOWN:
            ## Get mouse pos on click
            x,y = pygame.mouse.get_pos()
        
        elif e.type == MOUSEBUTTONUP:
            ## Get mouse pos on click
            x,y = pygame.mouse.get_pos()

    sx,sy = get_scaling()

    return x*sx, y*sy


def null_function():
    ## Do-nothing function returned by default from a button
    pass

def load_image(fn):
    ## Load image with alpha transparency
    return pygame.image.load(fn).convert_alpha()
    
def clean_line(string, joiner=' '):
    ## Removes in-line comments from script
    string = ' '.join(string.split())
    return string

def extract_lines(_file):
    ## Removes comments from script
    lines  = _file.readlines()
    output = [clean_line(l) for l in lines]
    output = [l for l in output if len(l) != 0]
    return output

def split(string, delim):
    ## Splits a string according to a delimiter
    return string.split(delim)


def add_entry(_dict, key, value):
    ## Adds a value to a dictionary
    if key in _dict.keys():
        _dict[key] = list(_dict[key])
        _dict[key].append(value)      
    else:
        _dict[key] = [value]


def make_dict(pairs, func):
    ## Instantiates a new dictionary
    output = {}
    for p in pairs:
        add_entry(output, p[0], func(p[1]))
    return output

def convert_int(string):
    ## Converts a string to an int
    return int(string)
    
    
def parse(filename, func=lambda x:x):
    ## Parses a file and makes a dictionary
    with open(filename, "r", encoding='utf-8') as f:
        lines = extract_lines(f)
        return make_dict([split(line,COLON) for line in lines], func)
        
    return {}


