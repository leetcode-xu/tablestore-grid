#!/usr/bin/env python
""" generated source for module Range """
# package: com.aliyun.tablestore.grid.model.grid
class Range(object):
    """ generated source for class Range """
    start = int()
    end = int()

    @overloaded
    def __init__(self, end):
        """ generated source for method __init__ """
        self.start = 0
        self.end = end

    @__init__.register(object, int, int)
    def __init___0(self, start, end):
        """ generated source for method __init___0 """
        self.start = start
        self.end = end

    def getStart(self):
        """ generated source for method getStart """
        return self.start

    def setStart(self, start):
        """ generated source for method setStart """
        self.start = start

    def getEnd(self):
        """ generated source for method getEnd """
        return self.end

    def setEnd(self, end):
        """ generated source for method setEnd """
        self.end = end

    def getSize(self):
        """ generated source for method getSize """
        return self.end - self.start

    def equals(self, o):
        """ generated source for method equals """
        if self == o:
            return True
        if isinstance(o, (Range, )):
            if self.start == (Range(o)).start and self.end == (Range(o)).end:
                return True
            return False
        return False

    def __str__(self):
        """ generated source for method toString """
        return ("[" + self.start + ", " + self.end + ")")

