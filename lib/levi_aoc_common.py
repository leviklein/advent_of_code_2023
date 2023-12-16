from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def all_equal(iterable, value):
    return iterable[0] == value and all_equal(iterable)

import datetime as dt
def print_every_n_seconds(t, seconds, line):
    delta = dt.datetime.now()-t
    if delta.seconds >= seconds:
        print(line)
    return delta.seconds >= seconds
