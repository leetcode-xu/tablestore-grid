#!/usr/bin/env python
""" generated source for module Grid4D """
# package: com.aliyun.tablestore.grid.model.grid
import ucar.ma2.DataType

import java.nio.ByteBuffer

import java.util.Arrays

class Grid4D(Grid):
    """ generated source for class Grid4D """
    def __init__(self, data, dataType, origin, shape):
        """ generated source for method __init__ """
        super(Grid4D, self).__init__(shape)
        if origin.length != 4 or shape.length != 4:
            raise IllegalArgumentException("the length of origin and shape must be 2")

    def getGrid3D(self, idx):
        """ generated source for method getGrid3D """
        if idx < 0 or idx >= shape[0]:
            raise IllegalArgumentException("index out of range")
        itemSize = shape[1] * shape[2] * shape[3] * dataType.getSize()
        pos = idx * itemSize
        newBuffer = buffer_.slice_()
        newBuffer.position(pos)
        newBuffer.limit(pos + itemSize)
        newBuffer = newBuffer.slice_()
        return Grid3D(newBuffer, dataType, Arrays.copyOfRange(origin, 1, origin.length), Arrays.copyOfRange(shape, 1, shape.length))

