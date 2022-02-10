import random


def draw_rec(x=1, y=1):
    if x > 20:
        x = 20
    if y > 20:
        y = 20
    print('','-'*y)
    for x in range(x):
        print('|', '+'*y, '|', sep='')
    print('','-'*y)


draw_rec(4, 10)