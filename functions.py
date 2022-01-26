import math
from os import path, system, name


def cls():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def checkfile(fname):
    if path.exists(fname):
        return True
    else:
        return False


def time_text(s):
    d = math.floor(s/86400)
    s = s % 86400
    h = math.floor(s/3600)
    s = s % 3600
    m = math.floor(s/60)
    s = s % 60
    return "{} days {:02}:{:02}:{:02}".format(d, h, m, s)
