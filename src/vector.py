import math
class vector:
    def __init__(self, coord):
        self.coord = coord[:]
        self._dim = len(coord)
    def __get_item__(self, idx):
        return self.coord[idx]

    #overloads add
    def __add__(self, other):
        result = [None] * self._dim
        i = 0
        while i < self._dim:
            result[i] = other.coord[i] + self.coord[i]
            i+=1
        return vector(result)

    #overloads subtraction
    def __sub__(self, other):
        result = [None] * self._dim
        for i in range(self._dim):
            result[i] = self.coord[i] - other.coord[i]
            i+=1
        return vector(result)
    #returns the multiplication of vector
    def scale(self, num):
        result = [None]*self._dim
        i = 0
        while i < self._dim:
            result[i] = self.coord[i] * num
            i+=1
        return vector(result)

    #returns the dot etween two vectors
    def dot(self, other):
        result = 0
        for i in range(self._dim):
            result += self.coord[i] * other.coord[i]
        return result

    #returns magnitude
    def mag(self):
        return math.sqrt(self.dot(self))

    # returns unit vector
    def unit_v(self):
        return self.scale(1.0 / self.mag())
    
    # returns string representation
    def __str__(self):
        return str(self.coord)
        
    # returns dimension
    def __len__(self):
        return self._n

    def __repr__(self):
        return f"coord:{self.coord}, mag:{self.mag()}"
