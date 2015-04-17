# -*- coding: utf-8 -*-
__author__ = 'imressed'
from decorator import decorator

@decorator
def cool(f, *args, **kwargs):
    print('more simple decorator')
    return f(*args, **kwargs)

@cool
def example(st):
    print('do cool %s'% st)


example('things')