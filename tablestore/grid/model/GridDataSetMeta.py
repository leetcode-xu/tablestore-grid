#!/usr/bin/env python
""" generated source for module GridDataSetMeta """
# package: com.aliyun.tablestore.grid.model
import ucar.ma2.DataType

import java.util.List

import java.util.Map

import java.util.concurrent.ConcurrentHashMap

class GridDataSetMeta(object):
    """ generated source for class GridDataSetMeta """
    gridDataSetId = str()
    dataType = DataType()
    variables = List()
    tSize = int()
    zSize = int()
    xSize = int()
    ySize = int()
    storeOptions = StoreOptions()
    attributes = Map()

    def __init__(self, gridDataSetId, dataType, variables, tSize, zSize, xSize, ySize, storeOptions):
        """ generated source for method __init__ """
        assert gridDataSetId != None
        assert variables != None
        assert storeOptions != None
        self.gridDataSetId = gridDataSetId
        self.dataType = dataType
        self.variables = variables
        self.tSize = tSize
        self.zSize = zSize
        self.xSize = xSize
        self.ySize = ySize
        self.storeOptions = storeOptions

    def getGridDataSetId(self):
        """ generated source for method getGridDataSetId """
        return self.gridDataSetId

    def setGridDataSetId(self, gridDataSetId):
        """ generated source for method setGridDataSetId """
        self.gridDataSetId = gridDataSetId

    def getVariables(self):
        """ generated source for method getVariables """
        return self.variables

    def setVariables(self, variables):
        """ generated source for method setVariables """
        self.variables = variables

    def gettSize(self):
        """ generated source for method gettSize """
        return self.tSize

    def settSize(self, tSize):
        """ generated source for method settSize """
        self.tSize = tSize

    def getzSize(self):
        """ generated source for method getzSize """
        return self.zSize

    def setzSize(self, zSize):
        """ generated source for method setzSize """
        self.zSize = zSize

    def getxSize(self):
        """ generated source for method getxSize """
        return self.xSize

    def setxSize(self, xSize):
        """ generated source for method setxSize """
        self.xSize = xSize

    def getySize(self):
        """ generated source for method getySize """
        return self.ySize

    def setySize(self, ySize):
        """ generated source for method setySize """
        self.ySize = ySize

    def getAttributes(self):
        """ generated source for method getAttributes """
        return self.attributes

    def setAttributes(self, attributes):
        """ generated source for method setAttributes """
        assert attributes != None
        for key in attributes.keySet():
            if key.startsWith("_"):
                raise IllegalArgumentException("attribute key can't start with \"_\"")
        self.attributes = attributes

    def addAttribute(self, key, value):
        """ generated source for method addAttribute """
        if key.startsWith("_"):
            raise IllegalArgumentException("attribute key can't start with \"_\"")
        if self.attributes == None:
            self.attributes = ConcurrentHashMap()
        self.attributes.put(key, value)

    def getStoreOptions(self):
        """ generated source for method getStoreOptions """
        return self.storeOptions

    def getDataType(self):
        """ generated source for method getDataType """
        return self.dataType

