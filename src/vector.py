import math
class vector:
    def __init__(self, coord):
        self._coord = coord[:]
        self._dim = len(coord)
    def __get_item__(self, idx):
        return self._coord[idx]

    #overloads add
    def __add__(self, other):
        result = [None] * self._dim
        i = 0
        while i < self._dim:
            result[i] = other._coord[i] + self._coord[i]
            i+=1
        return vector(result)

    #overloads subtraction
    def __sub__(self, other):
        result = [None] * self._dim
        for i in range(self._dim):
            result[i] = self._coord[i] - other._coord[i]
            i+=1
        return vector(result)

    #returns the multiplication of vector
    def scale(self, num):
        result = [None]*self._dim
        i = 0
        while i < self._dim:
            result[i] = self._coord[i] * num
            i+=1
        return vector(result)

    #returns the dot etween two vectors
    def dot(self, other):
        result = 0
        for i in range(self._dim):
            result += self._coord[i] * other._coord[i]
        return result

    #returns magnitude
    def mag(self):
        return math.sqrt(self.dot(self))

    # returns unit vector
    def unit_v(self):
        return self.scale(1.0 / self.mag())
    
    # returns string representation
    def __str__(self):
        return str(self._coord)
        
    # returns dimension
    def __len__(self):
        return self._n

    def __repr__(self):
        return f"coord:{self._coord}, mag:{self.mag()}"
