import math


def f (y,x, n):
    if (n<300):
        print ((x-y*y*y)/(20+n))
        print (n+1,(x-y*y*y)/(20+n) - y)
        f ((x-y*y*y)/(20+n), x, n+1)

f (4, 100, 0)