#! /usr/bin/env python3

import functools

#create [2,3,4]
input = [i for i in range(2,5)]

product = functools.reduce(lambda x,y: x*y, input)
