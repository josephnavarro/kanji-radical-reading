#!usr/bin/env python
import pygame
from   pygame.locals import *

## Functions used universally

def _quit():
    ## Safely quit game
    pygame.quit()
    raise SystemExit

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

    ## Default return value
    return (-1,-1)


def null_function():
    ## Do-nothing function returned by default from a button
    pass

def load_image(filename):
    ## Load image with alpha transparency
    image = pygame.image.load(filename).convert_alpha()
    return image

def clean_line(string):
    ## Removes in-line comments from script
    string = string.split(IGNORE)[0]
    string = ' '.join(string.split())
    return string

def extract_lines(_file):
    ## Removes comments from script
    lines  = _file.readlines()
    lines  = [l for l in lines if not l.startswith(IGNORE)]
    output = [clean_line(l) for l in lines]
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
        _dict[key] = value


def make_dict(pairs, func=lambda x:x):
    ## Instantiates a new dictionary
    output = {}
    for k,v in pairs:
        add_entry(output, k, func(v))
    return output

    
def parse(filename):
    ## Parses a file and makes a dictionary
    with open(filename, "r") as f:
        l = extract_lines(f)
        return make_dict([split(l,COLON) for l in lines])
        
    return {}


