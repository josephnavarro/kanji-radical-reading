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
    d = {}
    for fn in glob.glob(path + ext):
        if b in fn:
            im = load_image(fn)
            on = fn.replace('\\','/').split(SPACE)[0].split('/')[-1]
            d[on] = im

    return d

def get_bases(path, b, ext=PNGWILD):
    ## Get kanji from images and pair them with strings
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
    
def clean_line(s, j=' '):
    ## Removes in-line comments from script
    return j.join(s.split())

def extract_lines(f):
    ## Removes comments from script
    l = f.readlines()
    o = apply_vector(l, clean_line)
    return [p for p in o if len(p) != 0]

def split(s, d):
    ## Splits a string according to a delimiter
    return s.split(d)


def add_entry(d, k, v):
    ## Adds a value to a dictionary
    if k in d.keys():
        d[k] = list(d[k])
        d[k].append(v)      
    else:
        d[k] = [v]


def make_dict(p, fxn):
    ## Instantiates a new dictionary
    o = {}
    for q in p:
        add_entry(o, q[0], fxn(q[1]))
    return o

def convert_int(s):
    ## Converts a string to an int
    return int(s)
    
    
def parse(fn, fxn=lambda x:x):
    ## Parses a file and makes a dictionary
    d = {}
    with open(fn, "r", encoding='utf-8') as f:
        l = extract_lines(f)
        d = make_dict([split(m,COLON) for m in l], fxn)
        
    return d


