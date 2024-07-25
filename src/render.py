import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math
from space import universe, body

DEBUG = True

def radius(b):
    #assuming a density of just 1 to better showcase impact of mass via radius
    return math.pow(b.m * 3/4 / math.pi, 1/3)

def plot(bodies):
    circles = []
    for bdy in bodies:
        coord = bdy.p.coord
        if DEBUG: print(f"plotting body at {coord}")
        circle = patch.Circle(bdy.p.coord, radius(bdy),color='blue', fill=True)
        circles.append(circle)
    return circles

        




