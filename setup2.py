from distutils.core import setup
import py2exe, os, glob

dfiles = []

rootdir = 'C:/Users/Joey Schamoley/Desktop/games/'

def get_files(dfiles, directory):
    d1 = rootdir + directory
    for files in os.listdir(d1):
        f1 = d1 + files
        if os.path.isfile(f1):
            f2 = directory, [f1]
            dfiles.append(f2)
        else:
            get_files(dfiles, directory + files + '/')

get_files(dfiles, 'res/')

setup(
    version = "0.0001",
    description = "Final project for JPNS401 at Purdue University",
    name = "Kanji by Radical",
    url = "web.ics.purdue.edu/~navarro0/jpns401.html",
    author = "Joey Navarro",
    author_email = "navarro0@purdue.edu",
    license = "MIT License",

    # targets to build
    windows = [{
        'script': "main.py",
        'icon_resources': [(0, 'res/img/favicon.ico')],
        'copyright': "Copyright (c) 2017 Joey Navarro"
    }],
    options = {'py2exe': {
        'optimize': 2,
        'bundle_files': 1,
        'compressed': True,
        'excludes': [],
        'packages': [],
        'dll_excludes': [''],
        'includes': [
        'button',
        'constant',
        'question',
        'stage',
        'text',
        'utility',],
        'excludes':[
            'setup2',
            ],
        'dist_dir': 'outputs'}
               },
    zipfile = None,
    data_files = [
        ('res/base', glob.glob('res/base/*.png')),
        ('res/data', glob.glob('res/data/*.config')),
        ('res/font', glob.glob('res/font/*.ttf')),
        ('res/img', glob.glob('res/img/*.png') + glob.glob('res/img/*.ico')),
        ('res/kanji', glob.glob('res/kanji/*.png')),
        ('res/radical', glob.glob('res/radical/*.png')),
        ('res/snd', glob.glob('res/snd/*.ogg')),],
    )
