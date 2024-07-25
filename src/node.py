"""
from copy import deepcopy
from vector import vector
import numpy as np

class node:
    def __init__(self, pos, vel, m):
        self.m = m
        self.pos = pos.coord
        self.mom = pos.coord.scale(m)
        self.child = None
"""
