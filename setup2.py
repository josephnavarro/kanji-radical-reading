from distutils.core import setup
import py2exe
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
        'optimize': 2, 'bundle_files': 1, 'compressed': True, \
        'excludes': [], 'packages': [], \
        'dll_excludes': [''],
        'includes': [
        'button',
        'constant',
        'question',
        'stage',
        'text',
        'utility',],
        'dist_dir': 'outputs'}
               },
    zipfile = None,
    data_files = ['res'],
    )
