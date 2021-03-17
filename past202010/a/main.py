#!/usr/bin/env python3

import numpy as np

ABC = list(map(int,(input().split())))
ABC_sort = np.argsort(ABC)
sec = ABC_sort[1]

if sec == 0:
    print('A')
elif sec == 1:
    print('B')
else:
    print('C')