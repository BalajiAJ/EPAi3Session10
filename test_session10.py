import pytest
import re
import inspect
import random
import os
import math
from decimal import *

from polygon import Polygon
from polysequence import PolySeq

README_CONTENT_CHECK_FOR = [
    "repr",
    "getitem",
    "len",
    "edges"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    print(len(readme_words))
    assert len(readme_words) >= 50, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_indentations_session10():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        break
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_indentations_custompolygon():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(PolySeq)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        break
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter_session10():
    functions = inspect.getmembers(Polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_custompolygon():
    functions = inspect.getmembers(PolySeq, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_cuspolygon_repr():
    q = PolySeq(4,8)
    assert q.__repr__().__contains__("returns a polygon with highest area perimeter ratio"), 'The representation of the Custom Polygon object does not meet expectations' 

def test_cuspolygon_len():
    q = PolySeq(4,4)
    #print(str(q.number))
    assert len(q) == 2, 'Length should be 2 less than number of edges'

def test_polygon_edgelen():
    p = Polygon(3,4)
    assert math.isclose(p._edge_length,6.93,abs_tol=1) == True, 'Test case failed'

def test_polygon_apothem():
    p = Polygon(3,4)
    assert math.isclose(p._apothem,  2, abs_tol=1) == True, 'Test case failed'

def test_polygon_area():
    p = Polygon(3,4)
    assert math.isclose(p._area, 6.9,abs_tol=1) == True, 'Test case failed'

def test_polygon_perimeter():
    p = Polygon(3,4)
    assert math.isclose(p._perimeter, 20,abs_tol=1) == True, 'Test case failed'

def test_equal():
    p1 = Polygon(5,9)
    p2 = Polygon(7,8)

    assert (p1.__eq__(p2)) == False, "Test case failed"

def test_gt():
    p1 = Polygon(5,9)
    p2 = Polygon(7,8)

    assert (p1>p2) == False, "Test case failed"
    assert (p2>p1) == True, "Test case failed"