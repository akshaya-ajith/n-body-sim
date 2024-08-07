import math
import random as rd
from vector import vector

G_CONSTANT = 6.673*(10**-11)
DEBUG = True

#################### Celestial Bodies (objects in universe)
class body:
    def __init__(self, mass, pos, vel, acc):
        self.m = mass
        self.p = pos
        #self.prev_pos = prev_pos (for Verlet, but without user input)
        self._v = vel
        self._a = acc #for Verlet
        self.r = math.pow(self.m * 3/4 / math.pi, 1/3)
        #self.prev_acc = prev_acc (for Verlet, but without user input)

    # In order to find rad from Body 1 to Body 2
    def distance(self, other):
        d = self.p - other.p
        return d

    def update_acc(self, other):
        self._prev_a = self._a
        a_net = vector([0,0])
        
        if not isinstance(other, list):
            other = [other]
        
        for body in other:
            r12 = self.distance(body)
            if r12.mag() == 0: #skips itself
                continue
            f_mag = G_CONSTANT * (self.m * body.m) / (r12.mag()*r12.mag())
            a_mag = f_mag / self.m
            #derive next a from F = ma
            a_net += (r12.unit_v()).scale(a_mag)

        self._a = a_net

    def update_pos(self, other, dt):
        self._prev_p = self.p

        self.update_acc(other)
        self._v += (self._a).scale(dt)

        self.p+= (self._v.scale(dt) + self._a.scale(0.5*dt*dt))
        

    def __repr__(self):
        return f"Body(mass={self.m}, pos={self.p}, acc={self._a})"

    def check_coll(self, other):
        distance = self.distance(other).mag()
        center2center = self.r + other.r
        if(center2center >= distance): 
            #derived from elastic collisions, where momentum (mv) is conserved:
            total_mass = self.m + other.m
            vf1 = self._v.scale((self.m-other.m) / total_mass) + other._v.scale(2 * other.m / total_mass)
            
            vf2 = other._v.scale((other.m-self.m) / total_mass) + self._v.scale(2 * self.m / total_mass)
            
            self._v = vf1
            other._v = vf2

####################### Universe: collection of multiple bodies
class universe:
    def __init__(self, bodies, total_e):
        #constant timelapse val
        self.dt = 0.01
        self.bodies = bodies[:]
        
        
    def init_body(self, count):
        for cbody in range(count):
            rand_x = rd.randint(100,850)
            rand_y = rd.randint(100,850)
            rand_velx = rd.randint(-5,5)
            rand_vely = rd.randint(-5,5)
            rand_mass = rd.randint(5, 1000)
            b = body(rand_mass, vector([rand_x, rand_y]), vector([rand_velx, rand_vely]), vector([0.0,0.0]))
            self.bodies.append(b)

    def timelapse(self):
        for body1 in self.bodies:
            for body2 in self.bodies:
                if body2==body1:
                    continue
                body1.update_pos(body2, self.dt)
            for body2 in self.bodies:
                if body2==body1:
                    continue
                body1.check_coll(body2)


