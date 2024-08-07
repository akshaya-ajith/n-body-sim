import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math
import random as rd
from space import universe, body

DEBUG = False

def radius(b):
    #assuming a density of just 1 to better showcase impact of mass via radius
    radius = math.pow(b.m * 3/4 / math.pi, 1/3)
    return radius

def plot(bodies,ax):
    circles = []
    for bdy in bodies:
        coord = bdy.p.coord
        if DEBUG: print(f"plotting body at {coord}")
        circle = ax.add_patch(plt.Circle(bdy.p.coord, radius(bdy),color='blue', fill=True))
        circles.append(circle)
    return circles

        




