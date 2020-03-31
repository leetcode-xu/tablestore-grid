#!/usr/bin/env python
""" generated source for module GetDataParam """
# package: com.aliyun.tablestore.grid.model
import java.util.List

class GetDataParam(object):
    """ generated source for class GetDataParam """
    dataTableName = str()
    dataSetId = str()
    variable = str()
    t = int()
    z = int()
    columnsToGet = List()

    def __init__(self, dataTableName, dataSetId, variable, t, z, columnsToGet):
        """ generated source for method __init__ """
        self.dataTableName = dataTableName
        self.dataSetId = dataSetId
        self.variable = variable
        self.t = t
        self.z = z
        self.columnsToGet = columnsToGet

    def getDataTableName(self):
        """ generated source for method getDataTableName """
        return self.dataTableName

    def setDataTableName(self, dataTableName):
        """ generated source for method setDataTableName """
        self.dataTableName = dataTableName

    def getDataSetId(self):
        """ generated source for method getDataSetId """
        return self.dataSetId

    def setDataSetId(self, dataSetId):
        """ generated source for method setDataSetId """
        self.dataSetId = dataSetId

    def getVariable(self):
        """ generated source for method getVariable """
        return self.variable

    def setVariable(self, variable):
        """ generated source for method setVariable """
        self.variable = variable

    def getT(self):
        """ generated source for method getT """
        return self.t

    def setT(self, t):
        """ generated source for method setT """
        self.t = t

    def getZ(self):
        """ generated source for method getZ """
        return self.z

    def setZ(self, z):
        """ generated source for method setZ """
        self.z = z

    def getColumnsToGet(self):
        """ generated source for method getColumnsToGet """
        return self.columnsToGet

    def setColumnsToGet(self, columnsToGet):
        """ generated source for method setColumnsToGet """
        self.columnsToGet = columnsToGet

