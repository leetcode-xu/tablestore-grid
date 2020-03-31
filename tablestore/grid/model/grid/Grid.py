#!/usr/bin/env python
""" generated source for module Grid """
# package: com.aliyun.tablestore.grid.model.grid
import ucar.ma2.Array

import ucar.ma2.DataType

import java.nio.ByteBuffer

class Grid(object):
    """ generated source for class Grid """
    buffer_ = ByteBuffer()
    dataType = DataType()
    origin = []
    shape = []

    def __init__(self, buffer_, dataType, origin, shape):
        """ generated source for method __init__ """
        self.buffer_ = buffer_
        self.dataType = dataType
        self.origin = origin
        self.shape = shape
        size = dataType.getSize()
        i = 0
        while i < shape.length:
            size *= shape[i]
            i += 1
        if buffer_.remaining() != size:
            raise IllegalArgumentException("data length and shape mismatch")
        if origin.length != shape.length:
            raise IllegalArgumentException("the length of origin and shape mismatch")

    def getDataSize(self):
        """ generated source for method getDataSize """
        return self.buffer_.remaining()

    def getDataAsByteArray(self):
        """ generated source for method getDataAsByteArray """
        data = [None]*getDataSize()
        self.buffer_.duplicate().get(data)
        return data

    def getOrigin(self):
        """ generated source for method getOrigin """
        return self.origin

    def getShape(self):
        """ generated source for method getShape """
        return self.shape

    def getDataType(self):
        """ generated source for method getDataType """
        return self.dataType

    def toArray(self):
        """ generated source for method toArray """
        array = Array.factory(self.dataType, self.shape, self.buffer_.duplicate())
        return array

