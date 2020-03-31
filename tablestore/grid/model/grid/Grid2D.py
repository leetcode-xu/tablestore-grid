#!/usr/bin/env python
""" generated source for module Grid2D """
# package: com.aliyun.tablestore.grid.model.grid
import ucar.ma2.DataType

import java.nio.ByteBuffer

class Grid2D(Grid):
    """ generated source for class Grid2D """
    def __init__(self, data, dataType, origin, shape):
        """ generated source for method __init__ """
        super(Grid2D, self).__init__(shape)
        if origin.length != 2 or shape.length != 2:
            raise IllegalArgumentException("the length of origin and shape must be 2")

    def getPlane(self):
        """ generated source for method getPlane """
        return Plane(getOrigin(), getShape())

