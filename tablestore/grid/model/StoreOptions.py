#!/usr/bin/env python
""" generated source for module StoreOptions """
# package: com.aliyun.tablestore.grid.model
class StoreOptions(object):
    """ generated source for class StoreOptions """
    class StoreType:
        """ generated source for enum StoreType """
        SLICE = u'SLICE'

    storeType = StoreType()
    xSplitCount = 10
    ySplitCount = 10

    def __init__(self, storeType):
        """ generated source for method __init__ """
        self.storeType = storeType

    def getStoreType(self):
        """ generated source for method getStoreType """
        return self.storeType

    def setStoreType(self, storeType):
        """ generated source for method setStoreType """
        self.storeType = storeType

    def getxSplitCount(self):
        """ generated source for method getxSplitCount """
        return self.xSplitCount

    def setxSplitCount(self, xSplitCount):
        """ generated source for method setxSplitCount """
        self.xSplitCount = xSplitCount

    def getySplitCount(self):
        """ generated source for method getySplitCount """
        return self.ySplitCount

    def setySplitCount(self, ySplitCount):
        """ generated source for method setySplitCount """
        self.ySplitCount = ySplitCount

