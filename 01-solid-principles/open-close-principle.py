"""
Open to extension, but close to modification
"""
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size) -> None:
        self.size = size
        self.color = color
        self.name = name

class ProductFilter:
    """
    Filter product by some criterias
    """
    def filter_by_color(self, items, color):
        for item in items:
            if item.color == color:
                yield item

    def filter_by_size(self, items, size):
        for item in items:
            if item.size == size:
                yield item

    def filter_by_size_and_color(self, items, size, color):
        for item in items:
            if item.size == size and item.color == color:
                yield item
    
    def filter_by_x_or_y(self, *args):
        pass
    # when client want to add more filter functionalities? how do you handle its?
    # add more function into this class
    # this way violate the Open/Close principles
    ### LET REFACTOR ITS 


class Specification:
    """
    Base class for specification,
    When you need to add more filter functionality, you need to inherit from this class
    """
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        """
        Overload operator `and`
        """
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return  item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return  item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args 

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
            )) 


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    # initialize products
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    #### work with old approach ####
    pf = ProductFilter()
    print("Green products filter (old)")
    for item in pf.filter_by_color(products, Color.GREEN):
        print(f" - {item.name} is green")

    #### work with new approach ####
    bf = BetterFilter()

    green_spec = ColorSpecification(Color.GREEN)
    print("Green products filter (new)")
    for item in bf.filter(products, green_spec):
        print(f" - {item.name} is green")

    large_spec = SizeSpecification(Size.LARGE)
    print("Large products filter (new)")
    for item in bf.filter(products, large_spec):
        print(f" - {item.name} is large")

    large_blue_spec = large_spec & ColorSpecification(Color.BLUE)
    print("Large-Blue products filter (new)")
    for item in bf.filter(products, large_blue_spec):
        print(f" - {item.name} is large and blue")

