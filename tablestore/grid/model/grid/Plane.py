#!/usr/bin/env python
""" generated source for module Plane """
# package: com.aliyun.tablestore.grid.model.grid
class Plane(object):
    """ generated source for class Plane """
    xRange = Range()
    yRange = Range()

    @overloaded
    def __init__(self, xRange, yRange):
        """ generated source for method __init__ """
        self.xRange = xRange
        self.yRange = yRange

    @__init__.register(object, int, int)
    def __init___0(self, origin, shape):
        """ generated source for method __init___0 """
        if origin.length != 2 or shape.length != 2:
            raise IllegalArgumentException("the length of origin and shape must be 2")
        self.xRange = Range(origin[0], origin[0] + shape[0])
        self.yRange = Range(origin[1], origin[1] + shape[1])

    def getOrigin(self):
        """ generated source for method getOrigin """
        #return new int[] {xRange.getStart(), yRange.getStart()};
        return [None]*

    def getShape(self):
        """ generated source for method getShape """
        #return new int[] {xRange.getSize(), yRange.getSize()};
        return [None]*

    def getxRange(self):
        """ generated source for method getxRange """
        return self.xRange

    def setxRange(self, xRange):
        """ generated source for method setxRange """
        self.xRange = xRange

    def getyRange(self):
        """ generated source for method getyRange """
        return self.yRange

    def setyRange(self, yRange):
        """ generated source for method setyRange """
        self.yRange = yRange

    def equals(self, o):
        """ generated source for method equals """
        if self == o:
            return True
        if isinstance(o, (Plane, )):
            if self.xRange == (Plane(o).getxRange()) and self.yRange == (Plane(o).getyRange()):
                return True
            return False
        return False

