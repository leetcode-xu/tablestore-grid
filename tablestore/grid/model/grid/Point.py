#!/usr/bin/env python
""" generated source for module Point """
# package: com.aliyun.tablestore.grid.model.grid
class Point(object):
    """ generated source for class Point """
    x = int()
    y = int()

    def __init__(self, x, y):
        """ generated source for method __init__ """
        self.x = x
        self.y = y

    def getX(self):
        """ generated source for method getX """
        return self.x

    def setX(self, x):
        """ generated source for method setX """
        self.x = x

    def getY(self):
        """ generated source for method getY """
        return self.y

    def setY(self, y):
        """ generated source for method setY """
        self.y = y

    def equals(self, o):
        """ generated source for method equals """
        if self == o:
            return True
        if isinstance(o, (Point, )):
            if self.x == (Point(o)).x and self.y == (Point(o)).y:
                return True
            return False
        return False

