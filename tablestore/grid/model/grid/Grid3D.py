#!/usr/bin/env python
""" generated source for module Grid3D """
# package: com.aliyun.tablestore.grid.model.grid
import ucar.ma2.DataType

import java.nio.ByteBuffer

import java.util.Arrays

class Grid3D(Grid):
    """ generated source for class Grid3D """
    def __init__(self, data, dataType, origin, shape):
        """ generated source for method __init__ """
        super(Grid3D, self).__init__(shape)
        if origin.length != 3 or shape.length != 3:
            raise IllegalArgumentException("the length of origin and shape must be 2")

    def getGrid2D(self, idx):
        """ generated source for method getGrid2D """
        if idx < 0 or idx >= shape[0]:
            raise IllegalArgumentException("index out of range")
        itemSize = shape[1] * shape[2] * dataType.getSize()
        pos = idx * itemSize
        newBuffer = buffer_.slice_()
        newBuffer.position(pos)
        newBuffer.limit(pos + itemSize)
        newBuffer = newBuffer.slice_()
        return Grid2D(newBuffer, dataType, Arrays.copyOfRange(origin, 1, origin.length), Arrays.copyOfRange(shape, 1, shape.length))

