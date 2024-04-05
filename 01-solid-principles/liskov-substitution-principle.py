"""
Objects in a program should be replaceable with instances of theirs subtypes without altering the corectness of that program
No new exceptions can be thrown by the subtype

How to avoid violate this principles
    >>> only put the generic method into Supper class, it means method that all Subtype class has
"""
class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
    
    def __str__(self) -> str:
        return f"Width: {self.width}, Height: {self.height}"

    @property
    def area(self):
        return self._height * self._width


class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size) 

    @Rectangle.width.setter
    def width(self, width):
        self._width = self._height = width
            
    @Rectangle.height.setter
    def height(self, height):
        self._height = self._width = height


def use_it(rc):
    w = rc.width 
    rc.height = 10
    expected_area = int(w * 10)
    print(f"Expected an area of {expected_area}, got {rc.area}")

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(2)
use_it(sq)


