# -*- coding: utf-8 -*-
__author__ = 'imressed'

import time


def pause(t = 1):
    def wrapper(f):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return f(*args, **kwargs)
        return tmp
    return wrapper


def timer(f):
    def wrap(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print ("Func working time: %f" % (time.time() - t))
        return res
    return wrap

@timer
@pause(2)
def func(x, y):
    return x + y

print(func(2,5))