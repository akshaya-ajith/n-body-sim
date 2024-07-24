import random as rd
import matplotlib.pyplot as plt

from space import universe, body
from render import plot

def run(u, img):
    count = rd.randint(3,10)
    time = 0
    sim_length = 1
    u.init_body(count)

    with plt.ion():

        while time < sim_length:
            img.clear()
            u.timelapse()
            for obj in u.bodies:
                print(obj)
            time+=u.dt
            img.clear()
            plot(u.bodies,img)
            plt.draw()  # Update the figure
            plt.pause(0.01)  # Pause to allow the plot to update
            print("Plotted timelapse")
    
    plt.ioff()  # Disable interactive mode
    plt.show()

def main():
    bodies = []
    total_e = 0
    u = universe(bodies, total_e)
    
    plt.style.use('dark_background')
    img = plt.figure(figsize=(10,10))
    
    run(u,img)

if __name__ == "__main__":
    main()