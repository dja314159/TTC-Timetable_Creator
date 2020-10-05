import os

import sys

x = sys.maxsize


G = [[  0, 1, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 2, x, 2, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#101
    [1, 0, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        5, 5, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#102
    [  1, x, 0, 1, x, x, x, 2, x, x, 1, x, x, x, x, x, x, 2, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#103
    [  x, x, 1, 0, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#104
    [  x, x, x, x, 0, 3, x, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        3, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#105    
    [  x, x, x, x, 3, 0, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, 8, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#106
    [  x, x, x, x, x, 1, 0, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, 2, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, 2, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#107
    [  x, x, 2, x, 1, x, x, 0, 1, x, 1, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#108
    [  x, x, x, x, x, x, x, 1, 0, 1, 1, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#109
    [  x, x, x, x, x, x, x, x, 1, 0, x, 1, x, 1, 1, 1, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        2, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#110
    [  x, x, 1, x, x, x, x, 1, 1, x, 0, x, x, x, x, 1, x, 1, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#111
    [  x, x, x, x, x, x, x, x, x, 1, x, 0, 1, 1, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#112
    [  x, x, x, x, x, x, x, x, x, x, x, 1, 0, 1, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, 1, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#113
    [  x, x, x, x, x, x, x, x, x, 1, x, 1, 1, 0, 1, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#114
    [  x, x, x, x, x, x, x, x, x, 1, x, x, x, 1, 0, 1, 1, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#115
    [  x, x, x, x, x, x, x, x, x, 1, 1, x, x, x, 1, 0, 1, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#116
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 1, 0, x, 2, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#117
    [  2, x, 2, x, x, x, x, x, x, x, 1, x, x, x, x, x, x, 0, 1, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#118
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 2, 1, 0, 1, 1, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#119
    [  2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 0, 1, x, 2,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#120
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 1, 0, 1, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#121
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 0, 1,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#122
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 2, x, 1, 0,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#123
    [  x, 5, x, 1, 3, 2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        0, 1, 1, 1, x, x, 2, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#201
    [  x, 5, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, 0, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#202
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, 1, 0, 1, 1, 1, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#203
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, x, 1, 0, x, 1, x, 1, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#204
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, 1, x, 0, 1, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#205
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, 1, 1, 1, 0, x, x, 1, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#206
    [  x, x, x, x, x, x, 2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        2, x, x, x, x, x, 0, 1, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, 3, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#207
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, 1, x, x, 1, 0, 1, 1, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#208
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 1, x, 1, 0, 1, 1, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#209
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, 1, 1, 0, 1, 1, x, 2, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, 3, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#210
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, 1, 1, 0, 1, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#211
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, 1, 1, 0, 1, 2, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#212
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, 1, 0, 2, 1, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#213
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, 2, x, 2, 2, 0, 2, 1, 1, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, 2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#214
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, 1, 2, 0, 2, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#215
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 2, 0, 1, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#216
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x, 1, 0, 1,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#217
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 0,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, 1, 1, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#218
    [  x, x, x, x, x, x, x, x, x, 2, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        0, 1, 1, 1, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#301
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, 0, x, 1, 1, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#302
    [  x, x, x, x, x, x, x, x, x, x, x, 1, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, x, 0, x, x, x, 1, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#303
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, 1, x, 0, 1, x, 1, 1, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#304
    [  x, x, x, x, x, x, 8, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, 1, x, 1, 0, 1, x, 1, x, 1, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#305
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, 1, 0, x, x, x, x, 1,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 3, x, x, 4,
        x, x, x, x, x, x, x, x, x, x, x],#306
    [  x, x, x, x, x, x, x, x, x, x, x, x, 1, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, 1, 1, x, x, 0, 1, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#307
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, 1, 1, x, 1, 0, 1, 1, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#308
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, 1, 0, 1, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#309
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, 1, x, x, 1, 1, 0, 1,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#310
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 1, x, x, x, 1, 0,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 4,
        x, x, x, x, x, x, x, x, x, x, x],#311
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        0, 1, 1, 1, x, x, x, 2, 1, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#401 
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, 3, x, x, x, 2, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        1, 0, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#402
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        1, 1, 0, 1, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#403
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        1, x, 1, 0, 1, 1, x, x, 1, 1, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#404
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, 1, 1, 0, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#405
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, 1, 1, 0, 1, x, x, 1, x, x, x, x, x, x, x, x, x, x, x,
        1, x, x, 1, x, x, x, x, x, x, x],#406
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 1, 0, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, x, x, 1, x, x, 1, 1, x, x, x],#407
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, 3, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        2, x, x, x, x, x, x, 0, 1, x, x, x, 1, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#408
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        1, x, x, 1, x, x, x, 1, 0, 1, 1, 1, 1, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#409
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, 1, x, 1, x, x, 1, 0, 1, 1, x, x, x, x, x, x, x, x, x,
        1, 1, x, x, x, x, x, x, x, x, x],#410
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, 1, 1, 0, 1, x, x, x, 1, x, x, x, x, x,
        x, 1, 1, x, x, x, x, x, x, x, x],#411
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, 1, 1, 1, 0, 1, 1, 1, 1, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#412
    [  x, x, x, x, x, x, 2, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, 1, 1, x, x, 1, 0, 1, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#413
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, 1, 1, 0, 1, 1, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#414
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, 1, x, 1, 0, 1, 1, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#415
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, 1, 1, x, 1, 1, 0, 1, 1, 1, x, x,
        x, x, 1, x, x, x, x, x, x, x, x],#416
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 1, 0, 1, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x],#417
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 3, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 1, 0, x, 1, x,
        x, x, x, x, x, x, x, x, x, x, x],#418
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x, x, 0, x, x,
        x, x, 1, x, x, 1, x, x, x, 1, x],#419
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x, 0, 1,
        x, x, x, x, x, x, x, x, x, x, 1],#420
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 4, x, x, x, x, 4,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, 0,
        x, x, x, x, x, x, x, x, x, x, x],#421
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 1, 1, x, x, 1, x, x, x, x, x, x, x, x, x, x, x,
        0, 1, x, 1, 1, x, x, x, x, x, x],#501
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, 1, 1, x, x, x, x, x, x, x, x, x, x,
        1, 0, 1, 1, 1, x, x, x, x, x, x],#502
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, 1, x, x, x, x, 1, x, x, 1, x, x,
        x, 1, 0, x, 1, x, x, x, x, x, x],#503
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, 1, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        1, 1, x, 0, 1, x, 1, 1, x, x, x],#504
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, 1, 1, 1, 0, 1, x, x, x, x, x],#505
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x, x,
        x, x, x, x, 1, 0, x, x, x, 1, x],#506
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, 1, x, x, 0, 1, 1, x, x],#507
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, 1, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, 1, x, x, 1, 0, 1, x, x],#508
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, 1, 1, 0, x, x],#509
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x, x,
        x, x, x, x, x, 1, x, x, x, 0, 1],#510
    [  x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x,
        x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1, x,
        x, x, x, x, x, x, x, x, x, 1, 0]#511
    ]

def printGraph(G):
    for row in G:
        print (row)

def BadAPSP(G, show=0):
    assert len(G) == len(G[0])
    M = G
    n = len(M[0])
    for l in range(n-1):
        if show:
            print ('l=%d' % (l))
            printGraph(M)
            print ('-'*10)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    M[i][j] = min([M[i][j], M[i][k]+M[k][j]])
    print ("APSP:")
    printGraph(M)
    return M

def FloydWarshall(G, show=0):
    assert len(G) == len(G[0])
    M = G
    n = len(M[0])
    for k in range(n):
        if show:
            print ('k=%d' % (k-1))
            printGraph(M)
            print ('-'*10)
        for i in range(n):
            for j in range(n):
                M[i][j] = min([M[i][j], M[i][k]+M[k][j]])
    print ("APSP (k=%d):" % k)
    printGraph(M)
    return M

#BadAPSP(G, 1)
FloydWarshall(G, 1)
