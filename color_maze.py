#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 16:54:40 2017

@author: wolfiedieterich
"""
import numpy as np
from PIL import Image

sequence = "R O Y P O"

field = """R R B R R R B P Y G P B B B G P B P P R
B G Y P R P Y Y O R Y P P Y Y R R R P P
B P G R O P Y G R Y Y G P O R Y P B O O
R B B O R P Y O O Y R P B R G R B G P G
R P Y G G G P Y P Y O G B O R Y P B Y O
O R B G B Y B P G R P Y R O G Y G Y R P
B G O O O G B B R O Y Y Y Y P B Y Y G G
P P G B O P Y G B R O G B G R O Y R B R
Y Y P P R B Y B P O O G P Y R P P Y R Y
P O O B B B G O Y G O P B G Y R R Y R B
P P Y R B O O R O R Y B G B G O O P B Y
B B R G Y G P Y G P R R P Y G O O Y R R
O G R Y B P Y O P B R Y B G P G O O B P
R Y G P G G O R Y O O G R G P P Y P B G
P Y P R O O R O Y R P O R Y P Y B B Y R
O Y P G R P R G P O B B R B O B Y Y B P
B Y Y P O Y O Y O R B R G G Y G R G Y G
Y B Y Y G B R R O B O P P O B O R R R P
P O O O P Y G G Y P O G P O B G P R P B
R B B R R R R B B B Y O B G P G G O O Y"""

f = np.array([list(i) for i in field.replace(' ','').splitlines()])
seq = (list(sequence.replace(' ','')))
directions = {'up':   [0, -1],
              'down': [0, 1],
              'left': [-1, 0],
              'right':[1, 0]}

def get_starts(f):
    """looks for starting opportunities at the bottom of the matrix (or length of matrix - 1)
    returns an array of starting opportunities that match the first char in sequence """
    start = seq[0]
    startops = np.argwhere(f[f.shape[1]-1]== start)
    return startops


def get_ops(x, y, count, f, next_c, directions):
    ops = []
    for key in directions:
        try:
            xy = np.add([x,y],directions[key])
            dx, dy = xy.item(0), xy.item(1)
            if f[dy, dx] == next_c:
                ops.append([dx,dy,count])
        except IndexError:
            pass
    return ops


def next_step(x, y, path, seq, f, count, directions, hist):
    if y == 0:
        return (x,y), True
    n = seq[count]
    count = (count+1)%len(seq)
    ops = get_ops(x, y, count, f, n, directions)
    for op in ops:
        if not op in hist:
            hist.append(op)
            p, end = next_step(op[0], op[1], path, seq, f, count, directions, hist)
            if end:
                path.append(p)
                return (x, y), True
    return None, False

def run(f, seq, directions):
    starts = get_starts(f)
    count = 1
    for i in starts:
        path =[]
        hist = []
        hist.append([i.item(0),f.shape[1]-1,1])
        # p not used???
        p, end = next_step(i.item(0), f.shape[1]-1, path, seq, f, count, directions, hist)
        if end:
            path.append((i.item(0),f.shape[1]-1))
            return path

result = run(f, seq, directions)
#print(result[::-1])
for line_num, line in enumerate(f):
    out = [x if (col, line_num) in result else '/' for col, x in enumerate(line)]
    print(' '.join(out))

