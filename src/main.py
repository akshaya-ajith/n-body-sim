import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from space import universe, body
from render import plot


u = universe([], 0)
circles = []
time = 0

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('k')
ax.set_xlim(0, 1500)
ax.set_ylim(0, 1500)


def run(u):
    count = rd.randint(50,75)
    sim_length = 10

    u.init_body(count)
    circles = plot(u.bodies, ax)
    for circle in circles: 
        ax.add_patch(circle)
    
    for patch in ax.patches:
        patch.remove()

    ani = animation.FuncAnimation(fig, update, init_func=init, frames=sim_length, interval=1, blit=True)
    plt.show()

def init():
    # initialize an empty list of cirlces
    return []

def update(frame):
    global time
    time+=u.dt
    u.timelapse()
    for obj in u.bodies:
        print(obj)

    return plot(u.bodies, ax)

def main():
    run(u)

if __name__ == "__main__":
    main()