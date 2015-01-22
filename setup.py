from setuptools import setup

APP = ['main.py']
DATA_FILES = ['dialog.py', 'fonts.py', 'images.py', 'menu.py', 'rdraw.py', 'rects.py']
NAME = "Android Paint"
OPTIONS = {
    'plist': {'CFBundleShortVersionString':'1.0',}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    name=NAME,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)