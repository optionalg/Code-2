#!/usr/bin/env python
"""
Code Copyright (C) 2012-2014 Liam Stanley
isup.py - Code Isup Module
http://code.liamstanley.io/
"""

import re
from urllib import urlopen
from util.hook import *

def isup(code,input):
    """isup <url> - Is it down for everyone, or just you?"""
    if empty(code, input): return
    if len(input.group(2).split()) != 1: return error(code)
    try:
        data = urlopen('http://isup.me/%s' % input.group(2)).read()
        if 'not just you' in data:
            return code.say('{red}%s is down! It\'s not just you!' % input.group(2))
        elif 'It\'s just you.' in data:
            return code.say('{green}%s is up! Must just be you!' % input.group(2))
        else:
            return error(code)
    except:
        return error(code)
isup.commands = ['isup', 'isdown', 'check', 'up', 'down']
isup.example = 'isup http://google.com'

if __name__ == '__main__':
    print __doc__.strip()
