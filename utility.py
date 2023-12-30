"""
Universal functions
"""
import pygame
import glob
from pygame.locals import *
from pygame.transform import scale as sc
from pygame.transform import rotate as rot
from constant import *


def _quit():
    """
    Safely quits pygame.
    """
    pygame.quit()
    raise SystemExit


def apply_vector(vector, *fxns):
    """
    Mutates an input iterable by applying one or more functions over each
    of its elements.

    Returns a copy of the input iterable, as modified in this way.
    """
    for fxn in fxns:
        vector = [fxn(v) for v in vector[:]]

    return vector


def smooth_rotate(img, angle, scale=MINISCALE):
    """
    Rotates and scales an image. Returns the image.
    """
    # Calculate new integer dimensions
    size = apply_vector(
        img.get_size(),
        lambda x: x * scale,
        round,
        int,
    )
    
    # Scale
    img = sc(img, size)
    
    # Rotate
    img = rot(img, angle)
    
    return img


def get_words(path, b, ext=PNGWILD) -> dict:
    ## Get kanji from images and pair them with strings
    d: dict = {}
    for fn in glob.glob(path + ext):
        if b in fn:
            im = load_image(fn)
            on = fn.replace('\\','/').split(SPACE)[0].split('/')[-1]
            d[on] = im

    return d


def get_bases(path, b, ext=PNGWILD) -> dict:
    ## Get kanji from images and pair them with strings
    full = None
    none = None
    for fn in glob.glob(path + ext):
        if b in fn:
            if KEY_NONE in fn:
                none = load_image(fn)
            else:
                full = load_image(fn)

    return {
        KEY_NONE: none,
        KEY_FULL: full
    }


def get_scaling():
    """
    Calculates ratio between true window size and internal screen dimensions
    """
    w1, h1 = pygame.display.get_surface().get_size()
    return W / w1, H / h1


def get_input(events):
    ## Get mouse input
    x, y = -1, -1
    for e in events:
        if e.type == QUIT:
            ## Click [x] to exit window
            _quit()

        elif e.type == KEYDOWN:
            ## Keypress processing
            if e.key == K_ESCAPE:
                ## Press ESC to exit window
                pass
                # _quit()
        
        elif e.type == MOUSEBUTTONDOWN:
            ## Get mouse pos on click
            x, y = pygame.mouse.get_pos()
        
        elif e.type == MOUSEBUTTONUP:
            ## Get mouse pos on click
            x, y = pygame.mouse.get_pos()

    sx, sy = get_scaling()

    return x * sx, y * sy


def null_function():
    """
    Do-nothing function returned by default from a button
    """
    pass


def load_image(filename: str) -> pygame.Surface:
    """
    Loads an image with alpha transparency.
    """
    return pygame.image.load(filename).convert_alpha()

    
def clean_line(s: str, j: str = ' ') -> str:
    """
    Normalizes whitespace within the contents of a string,
    """
    return j.join(s.split())


def extract_lines(f):
    """
    Removes comments from the contents of a script file
    """
    l = f.readlines()
    o = apply_vector(l, clean_line)
    return [p for p in o if bool(p)]


def split(string: str, delim: str) -> list:
    """
    Splits a string according to a delimiter
    """
    return string.split(delim)


def add_entry(d: dict, key, val):
    """
    Adds a value to a dictionary, ensuring it's stored in a list
    """
    if key not in d.keys():
        d[key] = [val]
    else:
        d[key] = list(d[key])
        d[key].append(val)


def make_dict(p, fxn) -> dict:
    """
    Instantiates a new dictionary, ensuring each of its values are lists
    """
    o: dict = {}
    for q in p:
        add_entry(o, q[0], fxn(q[1]))
    return o


def convert_int(s: str) -> int:
    """
    Converts a string to an integer.
    """
    return int(s)
    
    
def parse(filename, fxn=lambda x: x) -> dict:
    """
    Parses a script file and makes a dictionary mapping out of it.
    
    Default function to apply is the identity function.
    """
    ## Parses a file and makes a dictionary
    d: dict = {}
    with open(filename, "r", encoding='utf-8') as f:
        l = extract_lines(f)
        d = make_dict([split(m, COLON) for m in l], fxn)
        
    return d
