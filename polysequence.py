#!/usr/bin/env python
# coding: utf-8

# In[133]:


from polygon import Polygon
from functools import lru_cache
import math


# In[114]:


class PolySeq:
    def __init__(self, n: "number of vertices for largest polygon", r: "common circumradius"):
        self.n = n
        self.circumradius = r


    @property
    def n(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, value):
        if type(value) not in [float, int]:
            raise TypeError("Circumradius must be a number.")

        if value<=0:
            raise ValueError("Circumradius must be greater than 0.")

        self._circumradius = value


    @n.setter
    def n(self, value):
        if type(value) is not int:
            raise TypeError("Number of edges/ vertices must be an integer.")
        if value<3:
            raise ValueError("Number of edges/ vertices must be >= 3.")

        self._n = value

    def __len__(self):
        return self.n - 2

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n - 2 + s
            if s < 0 or s >=(self.n-2):
                raise IndexError
            else:
                return self._poly(s)
        else:
            start, stop, step = s.indices(self.n-2)
            rng = range(start, stop, step)
            return [self._poly(i) for i in rng]
        
    def __repr__(self):
        return (
            f"Represents a Polygon with \nNumber of vertices/edges = {self.n}, \
            \nCircumradius = {self._circumradius}, \
            \nand also returns a polygon with highest area perimeter ratio \
            "
            )

    @property
    @lru_cache()
    def max_eff_polygon(self):
        return sorted(self, key = lambda x: x.area/x.perimeter)[-1]

    @lru_cache() 
    def _poly(self, n):
        return Polygon(n+3, self.circumradius)


# In[127]:


polyseqobj = PolySeq(25,10)


# In[128]:


print(polyseqobj)


# In[129]:


len(polyseqobj)


# In[130]:


polyseqobj[0]


# In[131]:


polyseqobj.max_eff_polygon


# In[132]:


polyseqobj[:3]


# In[ ]:




