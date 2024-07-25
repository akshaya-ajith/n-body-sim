import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from space import universe, body
from render import plot


u = universe([], 0)
circles = []
time = 0


def run(u, img):
    count = rd.randint(3,10)
    sim_length = 10


    ax = plt.gca()
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 500)
    u.init_body(count)
    circles = plot(u.bodies)
    for circle in circles: 
        ax.add_patch(circle)

    ani = animation.FuncAnimation(img, update, frames=sim_length, interval=1, blit=True)
    plt.show()
    """
    while time < sim_length:
        img.clear()
        u.timelapse()
        for obj in u.bodies:
            print(obj)
        time+=u.dt
        
        ax = plt.gca()
        circles = plot(u.bodies,ax)
        plt.draw()  # Update the figure
        print("Plotted timelapse")
        plt.show()
    """

def update(frame):
    global time
    time+=u.dt
    u.timelapse()
    for obj in u.bodies:
        print(obj)
    for i, circle in enumerate(circles):
        circle.center = u.bodies[i].pos.coord

    return circles

def main():
    
    plt.style.use('dark_background')
    img = plt.figure(figsize=(10,10))
    
    run(u,img)

if __name__ == "__main__":
    main()