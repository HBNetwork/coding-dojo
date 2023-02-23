import pytest
"""Geometry"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __truediv__(self, scalar):
        return self.__class__(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class Rect:
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight

    def center(self):
        return (self.topLeft + self.botRight) / 2

    def __repr__(self):
        return f'{self.__class__.__name__}({self.topLeft!r}, {self.botRight!r})'


def test_rect():
    r = Rect(Point(1, 1), Point(3, 3))
    assert isinstance(r, Rect)
    assert r.topLeft == Point(1, 1)
    assert r.botRight == Point(3, 3)
    assert r.center() == Point(2, 2)
    assert repr(r) == 'Rect(Point(1, 1), Point(3, 3))'

def test_point():
    p = Point(2, 4)
    assert isinstance(p, Point)
    assert p.x == 2
    assert p.y == 4

    

if __name__ == "__main__":
    pytest.main(["-s", __file__])



"""
from geometry import Rect, Point

r = Rect((1,1), (3,3))
r

r.center


"""