#!usr/bin/env python
import pygame, glob, os
from   pygame.locals import *
from   constant      import *

## Functions used universally

def _quit():
    ## Safely quit game
    pygame.quit()
    raise SystemExit

def smooth_rotate(img, angle):
    ## Rotates with antialiasing
    img = pygame.transform.rotate(img, angle)
    x,y = img.get_size()
    img = pygame.transform.scale(img, (x-4,y-4))
    return img

def get_words(path, base, ext='*.png'):
    ## Get kanji from images and pair them with strings
    _dict = {}
    for filename in glob.glob(path + '/*.png'):
        if base in filename:
            image  = load_image(filename)
            onyomi = filename.replace('\\','/').split(SPACE)[0].split('/')[-1]
            _dict[onyomi] = image

    return _dict

def get_bases(path, base, ext='*.png'):
    ## Get kanji from images and pair them with strings
    _dict = {}
    full  = None
    none  = None
    for filename in glob.glob(path + '/*.png'):
        if base in filename:
            if 'none' in filename:
                none = load_image(filename)
            else:
                full = load_image(filename)

    return {'none':none, 'full':full}

def get_input(events):
    ## Get mouse input
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
            return pygame.mouse.get_pos()
        
        elif e.type == MOUSEBUTTONUP:
            ## Get mouse pos on click
            return pygame.mouse.get_pos()

    ## Default return value
    return (-1,-1)


def null_function():
    ## Do-nothing function returned by default from a button
    pass

def load_image(filename):
    ## Load image with alpha transparency
    image = pygame.image.load(filename).convert_alpha()
    return image

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


