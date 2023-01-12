version 0.1 for Windows

import os

def search(text):
    os.startfile('https://www.google.com/search?q={}'.format(text))
