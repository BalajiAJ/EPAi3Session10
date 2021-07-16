# Sequence Types

#### In this session, we try to understand sequence types in python such as lists, tuples, sets, string etc. and also understand custorm sequence stypes
#### All sequences are iterables but not all iterables are not sequences in python, for example we cannot access elements by index for a set in python
#### Sequence types support operators like in, not in, range etc. and also support comcatenate operations.

## Assignment

A regular strictly convex polygon is a polygon that has the following characteristics:

1. all interior angles are less than 180
2. all sides have equal length

**Objective 1:**

1. Create a Polygon Class:
   1. where initializer takes in:
      1. number of edges/vertices
      2. circumradius
   2. that can provide these properties:
      1. \# edges
      2. \# vertices
      3. interior angle
      4. edge length
      5. apothem
      6. area
      7. perimeter
   3. that has these functionalities:
      1. a proper `__repr__` function
      2. implements equality (==) based on # vertices and circumradius (`__eq__`)
      3. implements > based on number of vertices only (`__gt__`)

**Objective 2:**

1. Implement a Custom Polygon sequence type:
   1. where initializer takes in:
      1. number of vertices for largest polygon in the sequence
      2. common circumradius for all polygons
   2. that can provide these properties:
      1. max efficiency polygon: returns the Polygon with the highest **area: perimeter** ratio for edges(n) = 25
   3. that has these functionalities:
      1. functions as a sequence type (`__getitem__`)
      2. supports the len() function (`__len__`)
      3. has a proper representation (`__repr__`)

### Polygon Class

The class is the implementation of the required polygon class. The usage is demonstrated below.

```python
from polygon import Polygon

p1 = Polygon(12, 20) # No. of vertices/edges: 12, circumradius: 20
p2 = Polygon(12, 20) # No. of vertices/edges: 12, circumradius: 20
p3 = Polygon(15, 25) # No. of vertices/edges: 15, circumradius: 25
```

### PolySequence

The class is the implementation of a custom polygon sequence according to what is described in the objective. The usage is as follows:

```python
from polysequence import PolySeq

seq = PolySeq(25, 10) # Max edge count: 25, common circumradius: 10
```

The proper demonstration of the working and features can be found in the jupyter notebook. 