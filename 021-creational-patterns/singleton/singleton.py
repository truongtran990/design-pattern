"""
Singleton -> A class/ component which is instantiated only once.
It's pretty easy to emplement a sloppy singleton. You just need to hide the constructor and implement the static creation method.
"""

class Database(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        dunder method is used to control creation new instance
        """
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

@singleton
class DatabaseV2(object):
    def __init__(self):
        print("Loading databases")


class A:
    x = 10
    y = 100

    def __init__(self, _x):
        print(self.x)
        print(A.x is self.x)
        self.x = _x


if __name__ == "__main__":
    # print(A.x)

    # a = A(999)
    # print(a.x)
    # print(A.x)

    d1 = Database()
    d2 = Database()
    print(d1 is d2)
