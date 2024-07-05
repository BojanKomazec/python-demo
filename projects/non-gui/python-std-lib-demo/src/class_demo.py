
# https://docs.python.org/3.7/library/functions.html#property
class A:
    def __init__(self, y, z):
        self._x = None
        self._y = y
        self._z = z

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

    # Although y has only gety defined, we can change it from outside, by setting _y
    # Nevertheless, by convention, variables whose names start with underscore should be used only
    # from within the class (they are considered "private").
    def gety(self):
        return self._y

    y = property(gety, "I'm the 'y' property.")

    # property decorator demo
    @property
    def z(self):
        return self._z


def _classA_demo():
    print("classA_demo()")

    a = A(123, 456)
    print(f'a.x =', a.x) # None
    print(f'a._x =', a._x) # None

    a.x = 5
    print(f'a.x =', a.x) # 5
    print(f'a._x =', a._x) # 5

    a._x = 6
    print(f'a.x =', a.x) # 6
    print(f'a._x =', a._x) # 6

    try:
        del a.x
        print(f'a.x =', a.x) # AttributeError: 'A' object has no attribute '_x'
    except:
        print("del a.x failed")

    print(f'a.y =', a.y) # 123
    print(f'a._y =', a._y) # 123

    try:
        a.y = 5 # TypeError: 'str' object is not callable
        print(f'a.y =', a.y) #
        print(f'a._y =', a._y)
    except:
        print("a.y = 5 failed")

    try:
        # Let's break the convention :)
        a._y = 5 # It is possible to change the property via underlying member (!)
        print(f'a.y =', a.y) # 5
        print(f'a._y =', a._y) # 5
    except:
        print("a._y = 5 failed")

    try:
        del a.y # AttributeError: can't delete attribute
        print(f'a.y =', a.y)
    except:
        print("del a.y failed") # this is executed

    try:
        del a._y
        print(f'a.y =', a.y)
        print(f'a._y =', a._y)
    except:
        print("del a._y failed") # this is executed

    print(f'a.z =', a.z) # 456
    print(f'a._z =', a._z) # 456

    try:
        a.z = 6 # TypeError: 'str' object is not callable
        print(f'a.z =', a.z)
        print(f'a._z =', a._z)
    except:
        print("a.z = 6 failed")  # this is executed

    try:
        a._z = 6 # It is possible to change the property via underlying member (!)
        print(f'a.z =', a.z) # 6
        print(f'a._z =', a._z) # 6
    except:
        print("a._z = 6 failed")

    try:
        del a.z # AttributeError: can't delete attribute
        print(f'a. =', a.z)
    except:
        print("del a.z failed") # this is executed

    try:
        del a._z
        print(f'a.z =', a.z)
        print(f'a._z =', a._z)
    except:
        print("del a._z failed") # this is executed


def class_demo():
    _classA_demo()

