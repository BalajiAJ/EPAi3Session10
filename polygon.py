


import math


class Polygon:
    def __init__(self, n: "Number of edges/ vertices", r: "Circum radius"):
        self.circumradius = r        
        self.vertices = n

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges
    
    @property
    def circumradius(self):
        return self._circumradius

    @property
    def interior_angle(self):
        return self._interior_angle

    @property
    def edge_length(self):
        return self._edge_length

    @property
    def apothem(self):
        return self._apothem

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @circumradius.setter
    def circumradius(self, value):
        if type(value) not in [float, int]:
            raise TypeError("Circumradius must be a number.")

        if value<=0:
            raise ValueError("Circumradius must be greater than 0.")

        self._circumradius = value


    @vertices.setter
    def vertices(self, value):
        if type(value) is not int:
            raise TypeError("Number of edges/ vertices must be an integer.")
        if value<3:
            raise ValueError("Number of edges/ vertices must be >= 3.")

        self._vertices = value
        self._edges = value

        self._interior_angle = (self._edges - 2) * (180 / self._edges)

        self._edge_length = 2 * self._circumradius * math.sin(math.pi/self._edges)

        self._apothem = self._circumradius * math.cos(math.pi/self._edges)

        self._area = 0.5 * self._edge_length * self._apothem

        self._perimeter = self._edges * self._edge_length


    def __repr__(self):
        return (
            f"Polygon(\
                \n\tNumber of vertices/edges = {self._edges},\
                \n\tCircumradius = {self._circumradius},\
                \n\tInterior angle = {self._interior_angle} degrees,\
                \n\tEdge length = {self._edge_length:.2f} units,\
                \n\tApothem = {self._apothem:.2f} units,\
                \n\tArea = {self._area:.2f} sq. units,\
                \n\tPerimeter = {self._perimeter:.2f} units,\
                \n\t)"
            )

    def __eq__(self, other):
        if type(other) is not Polygon:
            raise TypeError("Expected type Polygon.")
        return self.vertices == other.vertices         and self.circumradius == other.circumradius

    def __gt__(self, other):
        if type(other) is not Polygon:
            raise TypeError("Expected type Polygon.")
        return self.vertices > other.vertices


# ## Creating an instance of polygon class

# In[67]:


p = Polygon(3,4)


# ## Print the representation of the polygon class created




p


# ## Print the edges, vertices, interior angle, edge length, apothem, area, perimeter of the polygon instance



print(f'The properties of Polygon instance created are: \n\nnumber of vertices = {p._edges} \nnumber of edges = {p._edges} \nEdge Length = {p._edge_length} \ninterior angle = {p._interior_angle} \napothem = {p._apothem} \narea = {p._area} \nperimeter = {p._perimeter}')








