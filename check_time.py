# -*- coding: utf-8 -*-
__author__ = 'imressed'

import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print ("Func working time: %f" % (time.time() - t))
        return res
    return tmp

@timer
def func(x, y):
    return x + y

print(func(2,5))