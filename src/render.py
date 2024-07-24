import matplotlib.pyplot as plt
import math
from space import universe, body

DEBUG = True

def radius(b):
    #assuming a density of just 1 to better showcase impact of mass via radius
    return math.pow(b.m * 3/4 / math.pi, 1/3)

def plot(bodies, img):
    for bdy in bodies:
        rad = radius(bdy)
        coord = bdy.p.coord
        if DEBUG: print(f"plotting body with radius {rad} at {coord}")
        img.add_patch(plt.Circle(bdy.p.coord, rad,color='blue', fill=True))
    img.set_xlim(-1, 1000)  # Ensure the limits are set every time
    img.set_ylim(-1, 1000)
    img.set_aspect('equal')  # Ensure aspect ratio is equal
    print("Axis limits set and plot updated")

        




