#!/usr/bin/env python
""" generated source for module QueryGridDataSetResult """
# package: com.aliyun.tablestore.grid.model
import java.util.List

class QueryGridDataSetResult(object):
    """ generated source for class QueryGridDataSetResult """
    gridDataSetMetas = List()
    totalCount = long()
    isAllSuccess = bool()
    nextToken = []

    def getGridDataSetMetas(self):
        """ generated source for method getGridDataSetMetas """
        return self.gridDataSetMetas

    def setGridDataSetMetas(self, gridDataSetMetas):
        """ generated source for method setGridDataSetMetas """
        self.gridDataSetMetas = gridDataSetMetas

    def getTotalCount(self):
        """ generated source for method getTotalCount """
        return self.totalCount

    def setTotalCount(self, totalCount):
        """ generated source for method setTotalCount """
        self.totalCount = totalCount

    def isAllSuccess(self):
        """ generated source for method isAllSuccess """
        return self.isAllSuccess

    def setAllSuccess(self, allSuccess):
        """ generated source for method setAllSuccess """
        self.isAllSuccess = allSuccess

    def getNextToken(self):
        """ generated source for method getNextToken """
        return self.nextToken

    def setNextToken(self, nextToken):
        """ generated source for method setNextToken """
        self.nextToken = nextToken

